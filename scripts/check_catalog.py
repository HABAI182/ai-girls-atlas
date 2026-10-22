"""Check core JSON schemas, duplicate source URLs, portable paths and package rights."""
import json
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, urlunsplit

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / 'data' / f'{name}.json').read_text(encoding='utf-8'))


def source_key(url):
    parsed = urlsplit(url)
    # A reply anchor identifies a specific public comment; preserve it and queries.
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip('/'), parsed.query, parsed.fragment))


def path_error(path):
    parts = PurePosixPath(path).parts
    if '\\' in path or ':' in path or not parts or parts[0] != 'assets' or '..' in parts:
        return f'Asset path must stay under assets/ using portable forward slashes: {path}'
    if any(part.rstrip(' .') != part for part in parts):
        return f'Nonportable asset path: {path}'
    return None


def check():
    errors = []
    schema = json.loads((ROOT / 'schemas' / 'catalog.schema.json').read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)
    for name in ['characters', 'assets', 'sources', 'videos', 'ready-packages', 'package-rights']:
        scoped = {'$schema': schema['$schema'], '$defs': schema['$defs'], '$ref': f'#/$defs/{name}'}
        validator = Draft202012Validator(scoped, format_checker=FormatChecker())
        for error in validator.iter_errors(read(name)):
            location = '/'.join(str(p) for p in error.absolute_path)
            errors.append(f'{name}.json/{location}: {error.message}')
    seen = {}
    for source in read('sources')['sources']:
        key = source_key(source['url'])
        if key in seen:
            errors.append(f'Duplicate source URL: {seen[key]} / {source["id"]}: {source["url"]}')
        seen[key] = source['id']
    asset_paths = set()
    for asset in read('assets')['assets']:
        for path in [asset['path']] + ([asset['preview']] if asset.get('preview') else []):
            issue = path_error(path)
            if issue:
                errors.append(issue)
            key = path.casefold()
            if key in asset_paths:
                errors.append(f'Duplicate asset path (case insensitive): {path}')
            asset_paths.add(key)
    packages = {p['id'] for p in read('ready-packages')['packages']}
    audit = read('package-rights')
    audit_ids = [p['package_id'] for p in audit['packages']]
    if len(audit_ids) != len(set(audit_ids)) or set(audit_ids) != packages:
        errors.append('Every downloadable package needs exactly one package-rights record.')
    for record in audit['packages']:
        if record['license_id'] == 'CC-BY-NC' and record['review_status'] != 'version_unspecified':
            errors.append(f'Unversioned CC declaration needs an explicit gap: {record["package_id"]}')
    return errors


if __name__ == '__main__':
    issues = check()
    if issues:
        raise SystemExit('\n'.join(issues))
    print('Core schemas, source deduplication, asset paths and package rights passed.')
