# AI Girls Atlas · AI 娘形象与二创资料库

围绕主流AI产品、模型家族与创作工具，整理**角色长什么样、谁设计的、有哪些版本、去哪里找原图，以及能怎样继续创作**。

本库是非官方同人研究与素材参考档案。以用户指定的两条B站视频、知乎问题、GenderSwapAI专题及两个GitHub素材仓为重点，附原作者动态和社区项目。资料核验日期：**2026-10-20（北京时间）**。

## 先看哪里

- **[六个重点来源的详细研究与提炼](docs/01-focus-sources.md)**：逐项解释内容、价值、证据与落地。
- **[角色体系与版本规则](docs/02-character-system.md)**：解决同名不同图、模型与产品混淆。
- **[视频、表情包、网站与项目导航](docs/03-resource-library.md)**：按用途找作品。
- **[来源比较](docs/04-source-comparison.md)** · **[原创创作模板](docs/05-creation-playbook.md)**。
- **[来源与使用状态](docs/06-rights-and-provenance.md)** · **[缺口与后续清单](docs/07-gaps-and-roadmap.md)** · **[核验方法](docs/08-research-method.md)**。

## 本次覆盖

| 记录 | 数量 | 准确含义 |
| --- | ---: | --- |
| 产品/模型/工具/平台条目 | 38 | 按类型标注，包含历史产品；不等于独立模型数 |
| 已有形象资料或作品线索 | 29 | 含17个较完整的文字角色档案与其他线索 |
| 待补条目 | 9 | 未确认可靠形象，不冒充已完成 |
| 有本地图片的角色 | 9 | 八位早期主角、Seed及部分独立作者版本 |
| 本地原作/参考图片文件 | 32 | 18份作者立绘/变体/Q版截帧 + 14份独立项目立绘/表情 |
| 轻量预览 | 9 | 上游生成，单独计数 |
| 外部图库参考 | 44 | 作者原帖和图片入口；未打包镜像 |
| 视频记录 | 29 | 两条重点视频抽帧，其余元数据与简介 |
| 表情包/形象作品导航 | 28 | 来自站点元数据，未镜像整站图片 |
| 来源入口 | 131 | 每项带证据层级，详见sources.json |

**已有文字档案、已有作品线索、已有本地图片，是不同的完成状态。** 本次覆盖核心聊天模型及部分绘图、音频与编程工具；未做市场份额统计，不宣称“所有主流AI已齐全”。

## 八位主角的早期版本

以下缩略图来自 shuaizenge/ai-girls 的公开预览；原设计为 ZipZipPipe，DeepSeek 另保留上善无形原角色署名。预览只是入口，完整署名与使用状态见各角色页及 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

| DeepSeek | GPT | Claude | Gemini |
| --- | --- | --- | --- |
| [<img src="assets/previews/deepseek.jpg" width="150" alt="DeepSeek鲸鱼娘">](characters/deepseek/README.md) | [<img src="assets/previews/gpt.jpg" width="150" alt="GPT龙娘">](characters/gpt/README.md) | [<img src="assets/previews/claude.jpg" width="150" alt="Claude橙发花饰版本">](characters/claude/README.md) | [<img src="assets/previews/gemini.jpg" width="150" alt="Gemini猫娘">](characters/gemini/README.md) |
| [Grok](characters/grok/README.md) | [Kimi](characters/kimi/README.md) | [GLM](characters/glm/README.md) | [Qwen](characters/qwen/README.md) |
| [<img src="assets/previews/grok.jpg" width="150" alt="Grok早期版本">](characters/grok/README.md) | [<img src="assets/previews/kimi.jpg" width="150" alt="Kimi早期版本">](characters/kimi/README.md) | [<img src="assets/previews/glm.jpg" width="150" alt="GLM狐娘">](characters/glm/README.md) | [<img src="assets/previews/qwen.jpg" width="150" alt="Qwen中式衣裙版本">](characters/qwen/README.md) |

另有 [Seed娘立绘](characters/seed/README.md)：本次从原图SEED工牌与豆包玩偶确认身份，纠正了上游将其归入Gemini变体的分类，原字节保留；见[data/corrections.json](data/corrections.json)。

还有 JAdpp 的六张独立角色立绘和八种鲸鱼娘表情，放在各角色页中。它们有自己的设计、署名与文件许可，不冒充上图早期原版。

## 角色总览

状态说明：**本地图片**有可核对的文件；**档案与外链**有外观资料与参考原帖；**作品线索**需要继续补细节；**待补**尚未确认可采用形象。

| 条目 | 类型 | 状态 | 识别点或缺口 |
| --- | --- | --- | --- |
| [DeepSeek / 深度求索](characters/deepseek/README.md) | `model-family` | 本地图片 | 蓝色长发；鲸鱼鳍状耳饰与鲸尾；深蓝白女仆裙 |
| [ChatGPT / GPT](characters/gpt/README.md) | `product-and-model-family` | 本地图片 | 白色长发；龙角、龙翼与长尾；浅色礼服 |
| [Claude](characters/claude/README.md) | `model-family` | 本地图片 | 橙色长发；花形发饰；米白橙黑层叠长裙与书本 |
| [Gemini](characters/gemini/README.md) | `model-family` | 本地图片 | 蓝紫渐变长发；猫耳猫尾；异色瞳与星形元素 |
| [Grok](characters/grok/README.md) | `model-family` | 本地图片 | 金发；黑红或黑色裙装；蝙蝠翼、尖角与斧形道具 |
| [Kimi](characters/kimi/README.md) | `product-and-model-family` | 本地图片 | 白至银紫色长发；月亮和K元素；黑白深蓝非对称服装 |
| [GLM / 智谱](characters/glm/README.md) | `model-family` | 本地图片 | 黑色长发；狐耳和蓬松尾部；黑白服装及书本/Z元素 |
| [Qwen / 通义千问](characters/qwen/README.md) | `model-family` | 本地图片 | 蓝紫长发；圆形发饰；中式衣裙与折扇 |
| [Seed 娘（豆包相关同人）](characters/seed/README.md) | `model-family` | 本地图片 | 紫蓝单马尾；蓝白服装；豆包挂件 |
| [MiniMax](characters/minimax/README.md) | `model-family` | 档案与外链 | 橙色短发；粉色贝雷帽；场记板、照片与创作道具 |
| [Llama](characters/llama/README.md) | `model-family` | 档案与外链 | 白色长卷发；白色猫耳；宽松白色外套 |
| [Mistral](characters/mistral/README.md) | `model-family` | 档案与外链 | 金色长发；红色宽檐帽；红白法师裙 |
| [Perplexity](characters/perplexity/README.md) | `product` | 档案与外链 | 墨绿色长发；绿系长袍；星形法杖 |
| [文心 / ERNIE](characters/wenxin/README.md) | `model-family` | 档案与外链 | 蓝色方块发夹；蓝色系头发；中式衣裙 |
| [RWKV](characters/rwkv/README.md) | `model-family` | 档案与外链 | 深紫长发；放射状王冠；紫色羽翼与羽毛服饰 |
| [腾讯混元 / Hunyuan](characters/hunyuan/README.md) | `model-family` | 档案与外链 | 深色长发；中式长裙；算盘 |
| [JEV 裁判者](characters/jev/README.md) | `community-model-reference` | 档案与外链 | 黑粉配色；天平；嘴部荆棘 |
| [OpenCode](characters/opencode/README.md) | `coding-tool` | 作品线索 | 黑色长发；机械感尖角；灰黑服装 |
| [Zcode](characters/zcode/README.md) | `coding-tool` | 作品线索 | 浅色长发；蒙眼元素；浅蓝白工程少女轮廓 |
| [Codex 龙娘分支](characters/codex/README.md) | `coding-tool` | 作品线索 | 龙娘分支；细节以作者发布的三视图为准 |
| [Image 2 黑龙娘](characters/image2/README.md) | `image-model-reference` | 作品线索 | 黑龙娘分支；已有三视图入口 |
| [NovelAI](characters/novelai/README.md) | `creative-product` | 作品线索 | 本次仅确认生成式模型合照中的形象线索 |
| [Midjourney](characters/midjourney/README.md) | `image-product` | 作品线索 | 本次仅确认生成式模型合照中的形象线索 |
| [Suno](characters/suno/README.md) | `music-product` | 作品线索 | 本次仅确认生成式模型合照中的形象线索 |
| [ElevenLabs](characters/elevenlabs/README.md) | `audio-product` | 作品线索 | 本次仅确认生成式模型合照中的形象线索 |
| [豆包官方头像及其他版本](characters/doubao/README.md) | `product` | 作品线索 | 官方短发头像有来源；同人造型存在多个分支 |
| [StepFun / 阶跃星辰](characters/stepfun/README.md) | `model-family` | 作品线索 | 找到三项站点记录；精确外貌和原作许可待原帖逐图核对 |
| [MiMo / 小米](characters/mimo/README.md) | `model-family` | 作品线索 | 至少存在不同作者版本；站点有立绘和设定稿线索 |
| [Hugging Face](characters/huggingface/README.md) | `platform` | 作品线索 | 站点条目描述黄色笑脸玩偶与海军蓝外套 |
| [Microsoft Copilot](characters/copilot/README.md) | `product` | 待补 | 与GitHub Copilot分开；本次未确认采用哪一套社区形象。 |
| [腾讯元宝](characters/yuanbao/README.md) | `product` | 待补 | 产品条目与混元模型角色分开，未指定同人作者。 |
| [讯飞星火](characters/spark/README.md) | `model-family` | 待补 | 找到产品入口；未取得可核验的成套角色设计。 |
| [Cohere / Command](characters/cohere/README.md) | `model-family` | 待补 | 保留模型家族入口，未找到本次可核验的娘化资产。 |
| [可灵 / Kling](characters/kling/README.md) | `video-product` | 待补 | 官方入口本次读取受限；没有补造角色图或厂商许可。 |
| [Runway](characters/runway/README.md) | `video-product` | 待补 | 产品有官方入口，未指定成熟社区形象。 |
| [Sora（历史产品）](characters/sora/README.md) | `historical-video-product` | 待补 | 原入口当前转到官方停用说明；作为历史产品待补档，不列为当前可用服务。 |
| [Stable Diffusion](characters/stable-diffusion/README.md) | `image-model-family` | 待补 | 模型家族与各WebUI/服务不混同，拟人设计待补。 |
| [FLUX](characters/flux/README.md) | `image-model-family` | 待补 | 模型家族与厂商分开登记；未找到本次可核验角色档案。 |

## 六个重点入口

1. [《各AI娘形象盘点》](https://www.bilibili.com/video/BV14phK66Ejw/)：认人和描述来源链。
2. [《各个ai刻板印象》](https://www.bilibili.com/video/BV1pLn36sEJq/)：社区笑话、使用语境与外形差异。
3. [知乎：在哪里找这些角色的提示词](https://www.zhihu.com/question/2078891449882514701)：参考图与动作描述的分工。
4. [GenderSwapAI AI娘化专题](https://genderswapai.com/zh-CN/ai-gijinka)：成套角色、三视图、视频及项目索引。
5. [lmy414/ai-girl-stickers](https://github.com/lmy414/ai-girl-stickers)：表情包与形象作品的公开图片档案。
6. [shuaizenge/ai-girls](https://github.com/shuaizenge/ai-girls)：早期原图、Q版展示与逐文件来源核验。

## 对创作者最有用的几条提炼

- 同一产品可以拥有多个作者版本，先选版本再谈“角色应该长什么样”。
- 参考图固定人物身份，提示词描述本次动作、情绪、构图与场景；反推描述不叫原始提示词。
- 立绘、Q版原图、视频截帧、三视图、表情包与桌宠精灵图分别管理。
- 角色原型、二次设计、具体图片作者、投稿者和整理者分别署名。
- 社区刻板印象留在作品语境里，不变成模型能力、真实情感或当前厂商政策。
- 图片可公开查看、可非商业分享、可改编、可商用是不同状态，逐项保留证据。

## 数据和文件

```text
characters/<id>/README.md    38个条目的识别点、版本规则与来源
assets/zipzippipe/           早期立绘、变体和作者视频Q版展示截帧
assets/jadpp/               独立项目的角色立绘与鲸鱼娘表情
assets/previews/            九份轻量预览
data/                       JSON主记录与CSV导出
docs/                       八篇专题研究与维护说明
licenses/upstream/          随素材保留的上游声明
scripts/verify.py           本地完整性与引用校验
```

从 [data/README.md](data/README.md) 选择JSON或CSV。CSV包含Unicode列值，适合用UTF-8方式导入表格工具。仓库中的程序不需要网络，也不调用模型API。

下载或克隆后，在仓库目录运行：

```powershell
python scripts/verify.py
```

验证会检查文件哈希、大小、关系引用、相对链接和统计。它不证明角色审美、三视图结构正确，也不等于逐作品授权复核。

## 使用与贡献

DeepSeek相关指定图片及JAdpp指定图片保留已有CC BY-NC-SA 4.0条款；其他早期图片依据作者开放分享/再创作声明记录，未统一宣称MIT、CC0或可商用。官方头像、来源不明三视图和禁止转载的纯人声未复制。详情见[来源与使用状态](docs/06-rights-and-provenance.md)。

欢迎补作者原帖、缺失Q版原文件、三视图和明确许可，见[贡献说明](CONTRIBUTING.md)。这不是任何厂商官方形象库，也没有把参考项目安装到用户系统。

本库新写的说明与模板为CC BY 4.0，原创维护脚本为MIT；第三方图片各保留原有状态，见[许可边界](LICENSE.md)。
