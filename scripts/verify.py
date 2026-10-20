"""Validate the public atlas without downloading or executing third-party code."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(ok, message):
    if not ok:
        errors.append(message)

def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

def unique(records, label):
    ids = [r['id'] for r in records]
    require(len(ids) == len(set(ids)), f'Duplicate {label} ID')
    return set(ids)

def check_file(record):
    path = ROOT / record['path']
    require(path.is_file(), f'Missing asset: {record["path"]}')
    if not path.is_file():
        return
    b = path.read_bytes()
    require(len(b) == record['bytes'], f'Asset size mismatch: {record["path"]}')
    require(hashlib.sha256(b).hexdigest() == record['sha256'], f'Asset digest mismatch: {record["path"]}')

chars = read('characters.json')['characters']
assets = read('assets.json')['assets']
sources = read('sources.json')['sources']
videos = read('videos.json')['videos']
refs = read('references.json')['references']
memes = read('memes.json')['memes']
coverage = read('coverage.json')
char_ids = unique(chars, 'character')
asset_ids = unique(assets, 'asset')
source_ids = unique(sources, 'source')
unique(videos, 'video')
unique(refs, 'reference')
unique(memes, 'meme')
expected_files = set()
for a in assets:
    require(a['character_id'] in char_ids, f'Unknown asset character: {a["id"]}')
    require(bool(a['creators']), f'Missing asset attribution: {a["id"]}')
    require(bool(a['license'].get('evidence_url')), f'Missing license evidence: {a["id"]}')
    require(a['license']['status'] in ('author_declared', 'author_sharing_statement', 'maintainer_declared'), f'Unexpected local license status: {a["id"]}')
    check_file(a)
    expected_files.add(a['path'])
    if a.get('preview_receipt'):
        check_file(a['preview_receipt'])
        expected_files.add(a['preview_receipt']['path'])
    for key in ('source_url', 'retrieved_url'):
        require(a[key].startswith('https://'), f'Invalid asset URL: {a["id"]}/{key}')
for c in chars:
    require(set(c['sources']).issubset(source_ids), f'Dangling character source: {c["id"]}')
    require(set(c['local_asset_ids']).issubset(asset_ids), f'Dangling asset relation: {c["id"]}')
    require((ROOT / 'characters' / c['id'] / 'README.md').is_file(), f'Missing character page: {c["id"]}')
    if c['status'] == 'wanted':
        require(not c['local_asset_ids'] and not c['observed_traits'], f'Wanted entry pretends completion: {c["id"]}')
    for aid in c['local_asset_ids']:
        require(any(a['id'] == aid and a['character_id'] == c['id'] for a in assets), f'Asset assigned to wrong character: {aid}')
for v in videos:
    require(v['source_id'] in source_ids, f'Dangling video source: {v["id"]}')
for fix in read('corrections.json')['corrections']:
    require(fix['asset_id'] in asset_ids, f'Correction references absent asset: {fix["asset_id"]}')
    require(any(a['id'] == fix['asset_id'] and a['character_id'] == fix['corrected_character_id'] for a in assets), f'Correction not applied: {fix["asset_id"]}')
for s in sources:
    parsed = urlsplit(s['url'])
    require(parsed.scheme in ('http', 'https') and parsed.hostname, f'Invalid source URL: {s["id"]}')
    require(not parsed.username and not parsed.password, f'Credential-bearing URL: {s["id"]}')
actual_files = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'assets').rglob('*') if p.is_file()}
require(actual_files == expected_files, 'Uncatalogued or absent asset files')
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:
        continue
    text = p.read_text(encoding='utf-8')
    # Preserved upstream notices refer to files outside this selected asset subset.
    if 'licenses' in p.relative_to(ROOT).parts:
        continue
    for raw in re.findall(r'\]\(([^)]+)\)', text):
        target = raw.strip('<>').split('#')[0]
        if not target or urlsplit(target).scheme or target.startswith('//'):
            continue
        local = (p.parent / unquote(target)).resolve()
        require(local.is_relative_to(ROOT), f'Link escapes repository: {p.name}: {target}')
        require(local.exists(), f'Broken relative link: {p.relative_to(ROOT)}: {target}')
    for raw in re.findall(r'<img[^>]+src="([^"]+)"', text):
        if not raw.startswith('https://'):
            require((p.parent / raw).is_file(), f'Missing HTML preview: {raw}')
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts:
        continue
    require(p.suffix.lower() not in ('.mp3', '.mp4', '.wav', '.exe', '.dll', '.env'), f'Unexpected binary or private config: {p.relative_to(ROOT)}')
checks = {
    'entity_records': len(chars),
    'entities_with_visual_evidence_or_leads': sum(c['status'] != 'wanted' for c in chars),
    'wanted_entities': sum(c['status'] == 'wanted' for c in chars),
    'entities_with_local_assets': sum(bool(c['local_asset_ids']) for c in chars),
    'artwork_files': len(assets),
    'preview_files': sum('preview' in a for a in assets),
    'external_gallery_references': len(refs),
    'video_records': len(videos),
    'meme_navigation_records': len(memes),
    'source_records': len(sources),
}
for key, value in checks.items():
    require(coverage[key] == value, f'Coverage mismatch: {key}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(json.dumps({'ok': True, 'checks': checks, 'asset_files_verified': len(expected_files)}, ensure_ascii=False, indent=2))
