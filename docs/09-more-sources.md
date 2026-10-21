# 更多网站与GitHub项目：本轮补充了什么

更新于2026-10-21。本轮读取14个GitHub项目的公开说明与目录，选取可回溯的图片；新增50张本地图片。项目里有好用的文字规范、素材、动画和创作流程，分别记录其价值。

## 按需求选择入口

| 参考项目 | 主要用途 | 给本库带来的补充 | 使用说明 |
| --- | --- | --- | --- |
| [SelinLee/ai-moe-atlas](https://github.com/SelinLee/ai-moe-atlas) | 多语图鉴与素材工坊 | 补全MiniMax/Llama原图，借鉴逐作品来源与文件处理记录。 | 逐图条件；生成参考与作者原图分开。 |
| [Apprentice-Geo/AI-Fanworks](https://github.com/Apprentice-Geo/AI-Fanworks) | 按投稿作者归档 | 补入ApprenTice常规与Q版；另有风格、海报与提示词。 | 仅选有目录许可的ApprenTice图；两位海报作者保留权利，外链即可。 |
| [lshhhhhhh/ai-school-op](https://github.com/lshhhhhhh/ai-school-op) | 校园形象与分镜制作 | 18位统一服装的人设及逐角色提示词，补星火/Cohere。 | 人设图CC BY-NC 4.0；原作动画和音乐不随本库复制。 |
| [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | 角色皮肤与表情 | 新增三个透明表情，并保留上游抠图及署名链记录。 | 代码与美术分别声明；本次仅取maid-atelier明确覆盖的图片。 |
| [TreapGoGo/deepseek-whale-girl](https://github.com/TreapGoGo/deepseek-whale-girl) | 二创资源与工作流 | 从单一角色入口继续发现服装、绘画和社区项目。 | 网站MIT不覆盖所有角色图；工作流为参考链接。 |
| [AATINF/deepseek-whale-girl-assets](https://github.com/AATINF/deepseek-whale-girl-assets) | 细节拆解与Prompt清单 | 93张扩展包提供服装、鲸尾、配色、姿势等检索思路。 | README把上游图片称MIT，原维护者已在Issue37纠正；本轮留链接。 |
| [Neko3000/deepseek-whalechan](https://github.com/Neko3000/deepseek-whalechan) | 角色一致性规范 | 已有角色可继续补比例、服装、动作和参考图用途。 | 文档与图片范围不同；没有逐图授权映射的参考图留外链。 |
| [EDMOK/blue-fish-archive](https://github.com/EDMOK/blue-fish-archive) | 表情包原始档案 | 补上lmy414部分早期档案的上游来源关系。 | 图像仍按具体作者条件；不把站点图库整批再授权。 |
| [the-beating-light-of-the-nail/deepseek-chan-meme-pack](https://github.com/the-beating-light-of-the-nail/deepseek-chan-meme-pack) | 表情与语境导航 | 结合梗鲸详情页，增加情绪和对话场景索引。 | README数量与在线目录可能不同；不以整理站代替图片作者。 |
| [tqlearning/ai-girl-chatgpt-pets](https://github.com/tqlearning/ai-girl-chatgpt-pets) | 透明精灵图结构参考 | 两套角色动作与方向布局，可供理解动画素材组织。 | 其美术开放授权尚未确认；本库只索引，不打包。 |
| [legeling/awesome-codex-pet](https://github.com/legeling/awesome-codex-pet) | 多作者宠物版本目录 | 同一请求下区分GPT两作者与Codex居家版本。 | 逐submission保留非商业与署名待核内容；未安装运行。 |
| [AwesomeHou/openpet-ai-girls](https://github.com/AwesomeHou/openpet-ai-girls) | 另一套多角色宠物设计 | 与常见ZipZipPipe系列对照，避免产品同名就合并角色。 | 声明偏向仓库内查看与欣赏，本轮只链接。 |
| [lokicorvus/crosspet](https://github.com/lokicorvus/crosspet) | 任务状态与角色动作 | 可参考多模型角色、服装和工作动作的分工。 | 单独美术CC BY-NC-SA声明；本轮读取文档，不运行桌宠。 |
| [glt258/anime-character-director](https://github.com/glt258/anime-character-director) | 通用角色设计方法 | 借鉴参考图分工、约束与改稿记录，属于制作工具。 | 不作为AI娘原设定或现成角色素材统计。 |

完整固定提交在[projects.json](../data/projects.json)，图片供应关系见[assets.json](../data/assets.json)。这14个是本轮深入读取的项目，其中包括已有来源的扩写，不把它们全部宣称为首次发现。

## 跨角色素材：从“有图”走向“有版本”

[AI-Fanworks](https://github.com/Apprentice-Geo/AI-Fanworks)的价值在于按投稿作者和作品目录组织资料。本次取ApprenTice目录20张图：九个AI主题，加一组GLM狐耳分支，各有常规和Q版。两张总合照没有重复算作新的角色图。海报作者的目录采用另一套条件，继续保留外链；同一GitHub仓库中的作品并不共享一个图片许可。

[校园AI娘项目](https://github.com/lshhhhhhh/ai-school-op)则解决“同一主题怎样让一群角色同框”的问题。本库补入18张人设，每人都有作者发布的提示词入口。共用校服让角色主要靠发型、配饰与领结区分。GPT、GLM、Grok等与常见早期版本差别很大，应按这个项目独立选角，不能把它们混成同一套人物的随机换装。

[AI Moe Atlas](https://selinlee.github.io/ai-moe-atlas/zh/)提供另一个完整图鉴实例，本轮由其固定快照补到MiniMax与Llama的原始大图和轻量预览。其生成主页参考、采集原图和静态3D模型分别保留制作记录，适合借鉴原图与处理结果的对应方式。

## 单角色扩展：鲸鱼娘还有哪些方向

[深海女仆工坊](https://github.com/Small-tailqwq/dsh-deep-whale)的三个透明表情能直接作为表情素材参考。本库保留上善无形、ZipZipPipe、Small-tailqwq的创作链，并区分全身立绘与经过抠图的头像。

[TreapGoGo资源库](https://treapgogo.github.io/deepseek-whale-girl/)适合继续找社区作品和工作流；它提供投稿入口，并区分原始设定与社区演绎。[AATINF扩展包](https://github.com/AATINF/deepseek-whale-girl-assets)可按衣服、鲸尾、表情、姿势、色卡与壁纸寻找参考，Prompt清单有助于了解“一个角色还能补哪些素材”。本轮保存入口，未把93张扩展图整包重复搬来。

[Neko3000规范](https://github.com/Neko3000/deepseek-whalechan)帮助回答已有角色的细节问题：身份、服装、画风、动作与身体比例应怎样分别描述。其比例预设是项目内部约定，不能写成全社区唯一标准。可以借鉴方法，再以实际选用的作者版本作为依据。

## 表情与动画：继续深入的入口

[梗鲸](https://aigengtu.com/archive)和[EDMOK档案馆](https://fisharchive.cc/)增加了编号、台词与作品分类的检索路径。前者在线目录数量与旧README宣传数字不同，故不使用旧数字作为实时规模；页面的介绍文作者也不自动当作图片作者。

动画方面，OpenPet、CrossPet、tqlearning和awesome-codex-pet提供不同粒度的材料：独立角色设计、工作状态立绘、整张动画精灵图，以及同角色不同制作者的版本。对形象仓库最有用的是保留“谁做的哪套动作”，并回链到那套文件及元数据。本次只收录项目和版本导航，没有把软件安装或运行结果写进素材完成度。

## 怎样继续取材

先从角色页挑一个作者版本，再到该系列原帖找三视图、服装和声音；发现新文件时先比对已有图像与版本，避免把不同压缩文件当成新设计。需要二创流程可看通用设计工具，需要角色原作则回原作者。两种入口都保留，但在库里各自明确用途。


## 站点导航补记

从GenderSwapAI英文首页实际进入[社区项目页](https://genderswapai.com/ai-gijinka/projects)，可见OpenPet、c-dom桌宠、skylar-fei女仆和JAdpp故事四个方向。它们与本库原有入口关联，未重复下载。History为首页沿革段落；此前猜测中文/history路由的404不代表该站没有沿革内容。视频部分已扩成[独立品类与案例栏目](../videos/README.md)。

## 用户补充：鲸鱼娘开源资产库导览

[TreapGoGo视频与站点专题](../encyclopedia/focus-treap.md)已补齐作者录屏、参考图/提示词、社区画廊、六份工作流和网页投稿之间的关系。固定提交与先前相同，已有项目材料继续使用，没有重抓整库。

## 继续补充的三个GitHub项目

| 项目 | 具体所得 |
| --- | --- |
| larcgpt/ai-model-musume | 22个作者设定方向和三语角色卡；本轮重点查看SD与MiMo。无标准根许可，图片只留外链。 |
| Andersen216/dsh-whale-girl-live2d | 取得氵六青运行模型、8组动作和44个表情。补注册表情的model3入口后用官方SDK检查。 |
| 7l-ui/whalegirl-pet | 取得PSD、15层PNG、CMO3、MOC3和四组动作；模型实际SDK加载，未宣称测试Android真机。 |

累计深入评述17个项目。两套新Live2D已经实际加载；不把安卓、聊天接口或DSH宿主安装当素材工作的一部分。
