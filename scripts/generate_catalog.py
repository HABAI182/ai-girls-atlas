"""Generate current catalog summaries and CSV exports; --check never writes files."""
import argparse
import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(name, key=None):
    data = json.loads((ROOT / 'data' / f'{name}.json').read_text(encoding='utf-8'))
    return data[key] if key else data


def cell(value):
    if value is None:
        return ''
    if isinstance(value, list):
        return ' | '.join(str(v) for v in value)
    return str(value)


def csv_text(fields, records):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields.split(','), lineterminator='\n')
    writer.writeheader()
    for record in records:
        writer.writerow({k: cell(record.get(k)) for k in writer.fieldnames})
    return out.getvalue()


def block(text, name, body):
    start, end = f'<!-- generated:{name}:start -->', f'<!-- generated:{name}:end -->'
    pattern = re.escape(start) + r'.*?' + re.escape(end)
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f'Missing or duplicate generated block: {name}')
    return re.sub(pattern, lambda _: f'{start}\n{body.rstrip()}\n{end}', text, flags=re.S)


def outputs():
    coverage = read('coverage')
    chars = read('characters', 'characters')
    videos = read('videos', 'videos')
    categories = read('video-categories', 'categories')
    studies = {s['video_id']: s for s in read('video-studies', 'studies')}
    supplementary = {s['video_id']: s for s in read('video-observations', 'observations')}
    category_names = {c['id']: c['title'] for c in categories}
    indexed_genres = {vid: c['id'] for c in categories for vid in c['indexed_video_ids']}
    classified = sum(bool(v.get('primary_genre', indexed_genres.get(v['id']))) for v in videos)
    unclassified = len(videos) - classified
    result = {}
    for name, fields, records in [
        ('characters', 'id,name,entity_kind,status,creators,observed_traits,identity_rules', chars),
        ('assets', 'id,character_id,path,kind,bytes,sha256,source_url,supplier', read('assets', 'assets')),
        ('videos', 'id,title,author,published_at,duration_seconds,category,review_scope,url', videos),
        ('variants', 'id,character_id,collection,title,creators,observed_traits,difference_from_other_versions,asset_ids,prompt_url', read('variants', 'variants')),
        ('audio', 'id,title,kind,publisher,duration_seconds,source_url,review_scope', read('audio', 'audio')),
        ('memes', 'id,title,character_ids,detail_url,license_type_as_recorded,review_scope', read('memes', 'memes')),
        ('expressions', 'id,asset_id,label,emotion_tags_editorial,suggested_context_editorial', read('expressions', 'expressions')),
    ]:
        result[f'data/{name}.csv'] = csv_text(fields, records)
    all_rows = []
    for video in videos:
        study = studies.get(video['id'], {})
        supplement = supplementary.get(video['id'], {})
        genre = video.get('primary_genre', indexed_genres.get(video['id'], ''))
        popularity = video.get('popularity_snapshot') or {}
        part = next((p for p in [study.get('part'), study.get('reviewed_part'),
                                supplement.get('reviewed_part')] if isinstance(p, dict)), {})
        all_rows.append({
            'video_id': video['id'], 'title': video['title'], 'author': video['author'],
            'url': video['url'], 'primary_genre': genre,
            'genre_title': category_names.get(genre, '社区印象语境（未作画面品类分析）'),
            'classification_basis': video.get('classification_basis', video['review_scope']),
            'visual_styles_observed': study.get('visual_styles', video.get('visual_styles', [])),
            'duration_seconds': video.get('duration_seconds'),
            'reviewed_part_seconds': part.get('duration_seconds', part.get('part_duration_seconds')),
            'view_snapshot': popularity.get('view'),
            'snapshot_date': popularity.get('checked_on', popularity.get('date')),
            'study_path': study.get('case_path', supplement.get('page_path', video.get('supplementary_review_path', ''))),
            'relation_to_ai_girls': video.get('relation_to_ai_girls', 'community_impression_context'),
        })
    result['videos/all-videos.csv'] = csv_text(
        'video_id,title,author,url,primary_genre,genre_title,classification_basis,visual_styles_observed,duration_seconds,reviewed_part_seconds,view_snapshot,snapshot_date,study_path,relation_to_ai_girls',
        all_rows)
    stats = (
        f"**{coverage['entity_records']} 个角色及关联条目 · {coverage['artwork_files']} 份本地参考文件 · "
        f"{coverage['video_records']} 条视频 · {coverage['source_records']} 个来源入口 · "
        f"{coverage['ready_material_packages']} 组下载素材**\n\n"
        f"社区印象：{coverage['community_impression_characters']} 个角色、{coverage['community_impression_records']} 条记录；"
        f"另有 {coverage['original_persona_dialogues']} 句本库原创对白。数量口径见[收录统计](docs/collection-status.md)。")
    result['README.md'] = block((ROOT / 'README.md').read_text(encoding='utf-8'), 'stats', stats)
    video_stats = (
        f"当前 **{coverage['video_records']} 条视频记录**：{classified} 条进入现有主品类索引，"
        f"另 {unclassified} 条仅用于社区印象语境，尚未归入画面品类；"
        f"**{coverage['video_study_cases']} 篇抽帧案例**覆盖 {coverage['video_content_categories']} 个内容品类。"
        "其中21篇是AI娘作品、2篇是关联制作方法参考。观察范围以每条记录为准。")
    result['videos/README.md'] = block((ROOT / 'videos/README.md').read_text(encoding='utf-8'), 'video-stats', video_stats)
    gap_stats = (
        f"以[data/coverage.json](../data/coverage.json)为准。当前 {coverage['entity_records']} 个条目，"
        f"{coverage['entities_with_local_assets']} 个有本地图片，{coverage['artwork_files']} 份原图/派生/参考文件，"
        f"另有 {coverage['preview_files']} 张预览；{coverage['wanted_entities']} 个条目仍待补。"
        f"现有 {coverage['production_kits']} 组素材关联包；"
        f"实际下载目录为 {coverage['ready_material_packages']} 组，二者口径不同。")
    result['docs/07-gaps-and-roadmap.md'] = block((ROOT / 'docs/07-gaps-and-roadmap.md').read_text(encoding='utf-8'), 'gap-stats', gap_stats)
    persona_stats = (
        f"当前共 **{coverage['persona_profiles']} 份人设资料**："
        f"{coverage['editorial_persona_profiles']} 份本库原创工作草案、"
        f"{coverage['source_summary_persona_profiles']} 份作者原设摘要；"
        f"**{coverage['original_persona_dialogues']} 句同题原创对白**。"
        f"{coverage['written_persona_branch_entities']} 个条目有作者文字分支，"
        f"{coverage['persona_official_context_entities']} 个条目接入产品资料语境。"
        "来源摘要不强制增写原创台词；这些证据不等于全社区公认性格。")
    result['encyclopedia/personas/README.md'] = block(
        (ROOT / 'encyclopedia/personas/README.md').read_text(encoding='utf-8'), 'persona-stats', persona_stats)
    status_names = {'local_assets': '本地图片', 'profile_and_references': '档案与外链',
                    'visual_lead': '作品线索', 'external_work_lead': '作品线索', 'wanted': '待补'}
    index = ['# 角色与作者版本索引', '', '[看图与快速入口](../README.md) · [社区印象](../encyclopedia/personas/community-impressions.md) · [版本比较](../docs/10-variant-guide.md)', '',
             '由 `data/characters.json` 生成；同产品的不同作者版本在各角色页分别列出。', '',
             '| 角色 | 类型 | 当前状态 | 识别点/缺口 |', '| --- | --- | --- | --- |']
    for char in chars:
        traits = '；'.join(char['observed_traits'][:3]) or char['identity_rules']
        index.append(f"| [{char['name']}]({char['id']}/README.md) | {char['entity_kind']} | {status_names[char['status']]} | {traits.replace('|', '／')} |")
    result['characters/README.md'] = '\n'.join(index) + '\n'
    labels = {
        'entity_records': '角色及关联条目', 'entities_with_visual_evidence_or_leads': '有形象资料或线索',
        'wanted_entities': '仍待补形象的条目', 'entities_with_local_assets': '有本地图片的条目',
        'artwork_files': '本地原图/派生/参考文件', 'preview_files': '轻量预览（另计）',
        'external_gallery_references': '外部参考', 'video_records': '视频记录',
        'video_study_cases': '抽帧视频案例', 'video_content_categories': '视频品类',
        'source_records': '来源入口', 'expanded_design_variants': '扩展作者版本',
        'reviewed_reference_projects': '参考项目', 'audio_source_records': '声音来源',
        'meme_navigation_records': '表情/作品导航', 'expression_index_records': '本地表情语境',
        'ready_material_packages': '实际下载素材目录', 'production_kits': '素材关联包',
        'creator_records': '贡献者/作者记录', 'community_impression_records': '社区印象记录',
        'community_impression_characters': '社区印象涉及角色', 'community_pending_leads': '社区印象待核线索',
        'public_comment_samples': '公开评论样本', 'persona_profiles': '人设资料档案（含来源摘要）',
        'editorial_persona_profiles': '本库原创工作人设', 'source_summary_persona_profiles': '作者原设摘要',
        'original_persona_dialogues': '原创对白', 'real_product_dialogue_samples': '真实产品对话采样',
        'model_branch_collection_records': '模型与工具分支专题记录',
        'model_branch_image_reviews': '本轮分支原图实际查看',
        'model_branch_text_only_records': '本轮仅文字分支',
    }
    rows = [f'| {label} | {coverage[key]} |' for key, label in labels.items()]
    result['docs/collection-status.md'] = (
        '# 当前收录统计\n\n[首页](../README.md) · [数据](../data/README.md) · [待补](07-gaps-and-roadmap.md)\n\n'
        f"目录整理日期：{coverage['checked_on']}；来源采集日期各自保留，不能把目录更新理解为全部来源当天重查。\n\n"
        '由 `data/coverage.json` 生成，`verify.py` 再与主记录逐项对照。\n\n'
        '| 项目 | 数量 |\n| --- | ---: |\n' + '\n'.join(rows) + '\n\n'
        f'视频的 {classified} 条已有主品类，{unclassified} 条仅作社区印象语境；抽帧不等于完整观看或试听。'
        '角色单位含模型、产品、工具、平台与历史项目，不能当作市场覆盖率。'
        '原创人设与对白不等于社区共识或真实模型输出。\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for name, expected in outputs().items():
        path = ROOT / name
        actual = path.read_text(encoding='utf-8-sig') if path.exists() else None
        if actual == expected:
            continue
        if args.check:
            stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding='utf-8', newline='\n')
            print(f'Updated {name}')
    if stale:
        raise SystemExit('Generated catalog is stale; run python scripts/generate_catalog.py:\n' + '\n'.join(stale))
    if args.check:
        print('Catalog summaries and CSV exports are current.')


if __name__ == '__main__':
    main()
