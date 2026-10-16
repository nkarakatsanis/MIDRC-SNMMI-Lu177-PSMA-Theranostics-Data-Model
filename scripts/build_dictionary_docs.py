"""Generate human-readable MIDRC-style node/property documentation from JSON.

Run from any directory. Use --check to detect documentation drift without writing.
No schemas, examples, or terminology assertions are modified.
"""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = json.loads((ROOT / 'release.json').read_text())
MODEL = ROOT / META['model_directory']
SCHEMAS = {p.stem: json.loads(p.read_text()) for p in sorted((MODEL / 'schemas').glob('*.json'))}
CATALOG = {x['id']: x for x in json.loads((MODEL / 'node_catalog.json').read_text())}
VERSION = META['release_version']


def cell(value):
    return html.escape(' '.join(str(value).split()), quote=False).replace('|', '&#124;')


def literal(value):
    return '<code>' + cell(json.dumps(value, ensure_ascii=False)) + '</code>'


def describe(prop):
    return prop.get('description') or prop.get('term', {}).get('description') or 'No description supplied in the schema.'


def datatype(prop):
    if 'type' in prop:
        value = prop['type']
        result = ' or '.join(value) if isinstance(value, list) else value
        if value == 'array':
            result += ' of ' + datatype(prop.get('items', {}))
        return result
    for key, label in [('oneOf', 'exactly one of'), ('anyOf', 'one or more of')]:
        if key in prop:
            return label + ': ' + '; '.join(datatype(x) for x in prop[key])
    if 'enum' in prop:
        kinds = []
        for x in prop['enum']:
            kind = ('null' if x is None else 'boolean' if isinstance(x, bool) else
                    'string' if isinstance(x, str) else 'integer' if isinstance(x, int) else
                    'number' if isinstance(x, float) else 'object' if isinstance(x, dict) else 'array')
            if kind not in kinds:
                kinds.append(kind)
        return ' or '.join(kinds) + ' (enumerated)'
    return 'Not explicitly typed; see schema constraints'


def constraints(prop):
    result = []
    if 'enum' in prop:
        result.append('Allowed values: ' + ', '.join(literal(v) for v in prop['enum']))
    labels = {'format': 'Format', 'minimum': 'Minimum', 'maximum': 'Maximum',
              'minLength': 'Minimum length', 'minItems': 'Minimum items',
              'maxItems': 'Maximum items', 'uniqueItems': 'Unique items',
              'pattern': 'Pattern', 'default': 'Default', 'systemAlias': 'System alias'}
    for key, label in labels.items():
        if key in prop:
            result.append(label + ': ' + literal(prop[key]))
    if isinstance(prop.get('items'), dict):
        item = constraints(prop['items'])
        if item:
            result.append('Each item: (' + '; '.join(item) + ')')
    for key, label in [('oneOf', 'Exactly one alternative'), ('anyOf', 'One or more alternatives')]:
        if key in prop:
            branches = []
            for i, p in enumerate(prop[key], 1):
                detail = constraints(p)
                if p.get('required'):
                    detail.append('required keys: ' + ', '.join(literal(k) for k in p['required']))
                branches.append(str(i) + '. ' + cell(datatype(p)) + (': ' + '; '.join(detail) if detail else ''))
            result.append(label + ': [' + ' / '.join(branches) + ']')
    term = prop.get('term', {}).get('termDef')
    if term:
        terms = term if isinstance(term, list) else [term]
        for t in terms:
            if isinstance(t, dict):
                result.append('Source term: ' + cell('; '.join(str(t[k]) for k in ['source', 'cde_id', 'term', 'cde_version'] if t.get(k) is not None)))
    return result


def links(schema):
    return [link for entry in schema.get('links', []) for link in entry.get('subgroup', [entry])]


def node_page(name, schema):
    cat = CATALOG[name]
    rel = '../../' + META['model_directory']
    lines = [f'# {schema.get("title", name)} (`{name}`)', '',
             f'Release **{VERSION}** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)', '',
             cell(schema.get('description', '')), '',
             '| Attribute | Value |', '| --- | --- |',
             f'| Record grain | {cell(cat.get("record_grain", "See description"))} |',
             f'| Category | `{schema.get("category", "")}` |',
             f'| Navigation group | {cell(cat.get("group", ""))} |',
             f'| MIDRC relationship | `{cat.get("midrc_relation", "")}` |',
             f'| Submittable | {literal(schema.get("submittable"))} |',
             f'| Additional properties permitted | {literal(schema.get("additionalProperties"))} |',
             f'| Unique keys | {literal(schema.get("uniqueKeys", []))} |',
             '', f'[JSON schema]({rel}/schemas/{name}.json) · [YAML schema]({rel}/integration/yaml/{name}.yaml) · [Submission template]({rel}/templates/submission_{name}_template.json)', '',
             '## Relationships', '',
             'Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.', '']
    flattened = links(schema)
    required = set(schema.get('required', []))
    groups = {}
    group_notes = []
    for entry in schema.get('links', []):
        if 'subgroup' in entry:
            number = len(group_notes) + 1
            for link in entry['subgroup']:
                groups[link['name']] = number
            rule = ('exactly one populated member' if entry.get('exclusive') else 'at least one populated member') if entry.get('required') else ('at most one populated member' if entry.get('exclusive') else 'optional members')
            group_notes.append(f'Group {number}: **{rule}** among ' + ', '.join('`' + l['name'] + '`' for l in entry['subgroup']) + '.')
    if flattened:
        lines += ['| Link property | Target | Multiplicity | Required | Back-reference | Label |', '| --- | --- | --- | --- | --- | --- |']
        for link in flattened:
            req = 'Yes' if link.get('required') or link['name'] in required else 'No'
            if link['name'] in groups:
                req += f'; group {groups[link["name"]]}'
            lines.append(f'| `{link["name"]}` | [{link["target_type"]}]({link["target_type"]}.md) | `{link["multiplicity"]}` | {req} | `{link["backref"]}` | `{link.get("label", "")}` |')
        lines += [''] + [x + '\n' for x in group_notes]
    else:
        lines += ['No outgoing links are declared.', '']
    lines += ['## Properties', '',
              '“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.', '',
              'The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.', '']
    sys = set(schema.get('systemProperties', []))
    link_names = {x['name'] for x in flattened}
    categories = [('Data and identification properties', [k for k in schema['properties'] if k not in sys and k not in link_names]),
                  ('Relationship properties', [k for k in schema['properties'] if k in link_names]),
                  ('System-managed properties', [k for k in schema['properties'] if k in sys and k not in link_names])]
    for heading, names in categories:
        if not names:
            continue
        lines += ['### ' + heading, '', '| Property | Required | Type | Definition | Allowed values and constraints |', '| --- | --- | --- | --- | --- |']
        for key in names:
            prop = schema['properties'][key]
            lines.append(f'| `{key}` | {"Yes" if key in required else "No"} | {cell(datatype(prop))} | {cell(describe(prop))} | {"; ".join(constraints(prop)) or "—"} |')
        lines += ['']
    if schema.get('constraints'):
        lines += ['## Additional node constraints', '', '```json', json.dumps(schema['constraints'], indent=2, ensure_ascii=False), '```', '']
    example = MODEL / 'examples/by_node' / (name + '.json')
    if example.exists():
        lines += ['## Synthetic examples', '', f'[Read the synthetic {name} records]({rel}/examples/by_node/{name}.json). These are structural demonstrations, not patient data or treatment recommendations.', '']
    lines += ['Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.', '']
    return '\n'.join(lines)


def outputs():
    pages = {ROOT / 'docs/dictionary' / (n + '.md'): node_page(n, s) for n, s in SCHEMAS.items()}
    count = sum(len(s['properties']) for s in SCHEMAS.values())
    nlinks = sum(len(links(s)) for s in SCHEMAS.values())
    index = [f'# Human-readable data dictionary — {VERSION}', '',
             f'**{len(SCHEMAS)} node types · {count:,} node/property entries · {nlinks} relationships.** Shared properties are counted once per node, not as distinct clinical concepts.', '',
             '[Architecture and use cases](../DATA_MODEL.md) · [Domain index](../DOMAINS.md) · [Repository guide](../REPOSITORY_GUIDE.md)', '',
             'Each page follows the MIDRC dictionary structure: node identity and category, record grain, links and back-references, multiplicity and required link groups, then property definitions, types, allowed values and constraints. The source JSON schemas remain authoritative.', '',
             'The dictionary describes the complete v0.3.0 proposal under `extensions/lu177_psma/v0.3.0/`. The inherited `gdcdictionary/` source is a separate preserved baseline. This documentation does not indicate a deployed MIDRC release or completed clinical/terminology review.', '',
             '| Node | Group | MIDRC relationship | Properties | Links |', '| --- | --- | --- | ---: | ---: |']
    for n, s in SCHEMAS.items():
        c = CATALOG[n]
        index.append(f'| [{n}]({n}.md) | {cell(c.get("group", ""))} | `{c.get("midrc_relation", "")}` | {len(s["properties"])} | {len(links(s))} |')
    index += ['', 'Regenerate with `python scripts/build_dictionary_docs.py`; use `--check` to verify that the pages match the schemas.', '']
    pages[ROOT / 'docs/dictionary/README.md'] = '\n'.join(index)
    return pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = outputs()
    stale = [str(p.relative_to(ROOT)) for p, content in expected.items() if not p.exists() or p.read_text() != content]
    if args.check:
        if stale:
            raise SystemExit('Missing or stale dictionary documentation: ' + ', '.join(stale))
        print(f'PASS: {len(expected) - 1} node documentation pages match the schemas.')
    else:
        for path, content in expected.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        print(f'Generated {len(expected) - 1} node pages and the dictionary index.')


if __name__ == '__main__':
    main()
