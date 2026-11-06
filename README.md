# 个人网站（单文件 · BuyCart 电商风）

一个按 **BuyCart**（WooCommerce 子主题 `buycart 1.0.26`）的视觉语言重做的个人介绍站：
深蓝信息条 + 白色头部（logo / 搜索 / 电话 / CTA）+ 主蓝粘性导航 + 大字号渐变 Hero + 深蓝数据条，
内容区用白卡片承载。整套站点仍然是**一个 `index.html`**，双击即可打开。

- **一个文件就能跑**：CSS、JavaScript 和 7 张界面截图（base64 webp）全部内嵌，不依赖框架、CDN 或网络。
- **三档响应式**：宽屏（≥1080）、平板（920–1080）、手机（<920 汉堡菜单，<640 进一步收窄）。
- **含三个可运行的实战项目**：博客「技术周刊」、问答社区「问渠」、在线商城「蚂蚁严选」，
  卡片里的界面截图悬停会切换成详情页，点击可打开灯箱看大图。

```
personal-website/
├─ index.html            ← 最终成品（392 KB，双击打开）
├─ index.template.html   ← 可编辑的源码（图片用 @@IMG:key@@ 占位）
├─ build.py              ← 把占位替换成 base64，生成 index.html
├─ assets/               ← 7 张 webp（6 张项目界面 + 1 张本站首屏，共 242 KB）
└─ screenshots/          ← 验证脚本自动拍的成品截图（可删）
```

## 打开

双击 `index.html`。Chrome / Edge / Safari / Firefox 均可，无需启动服务器。

## 页面结构

| 区块 | 内容 |
| --- | --- |
| 顶部信息条 | 武汉理工大学 · 数字经济 · 在读 / 开放实习与项目合作 / 邮箱 / 电话 |
| 头部 | 「杨」logo + 杨诚铭 + Full-Stack Developer / 站内搜索 / 电话块 / 「联系我」蓝色 CTA |
| 蓝色导航 | 关于 · 成果 · 能力 · 经历 · 爱好 · 联系（粘性，滚动高亮当前区块） |
| Hero | 「把想法做成**能跑起来**的产品」+ 一句话自述 + 两个 CTA + 「现在在做什么」玻璃卡 |
| 数据条 | 3 个全栈项目 · 16 张数据表 · 282 项自动化验证 · 99 条端到端用例 |
| 成果 `#works` | 分类筛选（全部/博客/社区/商城/本站）+ 关键词搜索 + 4 张项目卡 + 灯箱 |
| 关于 `#about` | 姓名名片（杨诚铭 · 学校专业 · 三个标签）+ 两栏白卡：左边一段自述，右边基本信息表 |
| 能力 `#skills` | 5 条技能条（熟练/熟悉）+ 16 个技术标签 + 3 门语言 |
| 经历 `#timeline` | 4 条倒序时间轴（2026.10 → 2025.09 入学） |
| 爱好 `#hobbies` | 6 条（内联 SVG 图标 + 一句短语） |
| 联系 `#contact` | 深蓝渐变大圆角面板：邮箱 / 电话 / 位置 |
| 页脚 | 站点简介 + 页面导航 + 联系方式 + 版权 |

## 交互

- **粘性导航**：`IntersectionObserver`（`rootMargin:-45% 0px -50% 0px`）跟随滚动高亮当前区块，点击平滑跳转并抵消导航高度；
- **项目筛选与搜索**：5 个分类 chip 与搜索框叠加生效（匹配卡片标题、描述与 `data-keywords`），无结果显示空状态；
- **灯箱**：每张项目卡内有两张图（首页 / 详情页），点击打开后可 ← → 切换、Esc 关闭、点遮罩关闭，打开时锁定页面滚动；
- **汉堡菜单**：<920px 出现，抽屉带 01–06 编号，点导航项后自动收起；
- **滚动淡入**：`.reveal` 进入视口后加 `.in`；`prefers-reduced-motion: reduce` 下全部直出；
- **回到顶部**：滚过一屏后右下角浮现；
- **键盘可达**：首个可聚焦元素是「跳到主内容」，焦点态有 2px 主蓝描边。

## 设计规范

| 项 | 值 |
| --- | --- |
| 主蓝（导航 / 按钮） | `#157DF7`（BuyCart `--wf-main-rgb` 21,125,247） |
| 深蓝（信息条 / 数据条 / 页脚） | `#0B32B5`（`--wf-secondary-color`）、页脚 `#081B3F` |
| 强调黄（Hero 关键词） | `#FFC94A`，对应 BuyCart 促销卡的黄色 |
| 墨色 / 正文 / 次要 | `#0F1B2E` / `#3D4C63` / `#6B7A90`，底色 `#F4F7FB`、分割线 `#E3E9F2` |
| 字体 | `Inter, Segoe UI, system-ui, Noto Sans SC, Microsoft YaHei, sans-serif` |
| 圆角 | 卡片 14px、面板 20px、按钮 10–13px（父主题按钮 `border-radius:1.2rem` 的近似） |
| 断点 | 1080（Hero 单列、爱好 2 列）、920（汉堡菜单、项目/技能单列）、640（信息条右侧与头部按钮隐藏） |
| 动效 | 淡入 0.6s、悬停 0.2–0.45s |

排版细节：中文段落做了「源码换行不产生空格」的处理（`build.py` 里的 `CJK_LINEBREAK`），
短句用 `text-wrap: balance / pretty`（新浏览器生效，旧浏览器自动忽略）。

## 构建

`@@IMG:key@@` 是图片占位符，构建时替换成 `data:image/webp;base64,...`：

```bash
python build.py
# [OK] output: ...\index.html
#      inlined images (7): blog-detail, blog-home, community-detail, community-home, mall-home, mall-order, site-hero
#      single-file size: 392 KB
```

换图片的步骤：

1. 截图转成宽 1100px 的 webp（`Image.open(p).convert('RGB').resize((1100, h)).save(p, 'WEBP', quality=76)`）；
2. 存为 `assets/名字.webp`；
3. 模板里写 `@@IMG:名字@@`；
4. 跑 `python build.py`。

> 项目截图是用**干净的种子数据**重新拍的（三个项目各自 `scripts/init-db.js` 重置后，
> 用 `_tools/make-shots.js` 以 demo 账号登录截图 1440×900），不是 E2E 测试留下的脏数据。

## 验证

`_tools/verify-site.js` 用无头 Edge 在 1440 / 834 / 390 三个宽度上跑 **37 项断言**：

```
cd _tools
node verify-site.js
# 合计 37 / 37 通过
```

覆盖：横向溢出、导航/信息条色值、Hero 字号与字重、结构计数（4 数据项 / 4 项目卡 / 6 爱好 / 4 时间轴 / 5 技能条）、
按钮圆角、图片加载与 alt、淡入是否全部触发、技能条宽度、回到顶部、粘性导航 `top=0`、区块高亮切换、
分类筛选、搜索命中与空状态、灯箱开关/切换/Esc/滚动锁定、跳转链接、平板汉堡与单列、手机抽屉展开收起、控制台零报错。

截图写到 `screenshots/`（`desktop-hero|works|about|skills|timeline|hobbies|contact|full`、`lightbox`、`tablet-full`、`mobile-hero|full|menu`）。

## 还需要你补的一处

| 位置 | 现状 | 说明 |
| --- | --- | --- |
| 学习经历中间 2 条 | 带 `示例` 虚线小标 | 「React 19 + TypeScript 系统学习」「Web 基础与工程化」，按真实情况改写后删掉 `<span class="sample">示例</span>` |

照片区（原 4:5 人像位）已按要求删除，「关于我」现在是一张横向姓名名片 + 两栏正文卡，
不再需要提供头像图片。其余信息都已是真实内容：武汉理工大学 · 数字经济 · 2025.09 入学（在读）、
`2891812082@qq.com`、`13677391257`、武汉；荣誉奖项区块此前也已整块删除。

## 已知取舍

- 图片内联成 base64 让单文件变成 392 KB（图片 242 KB），换来「双击即开、零依赖」；想更小就把图片改成外链文件。
- Hero 的强调黄只出现在一处（「能跑起来」），其余强调仍靠主蓝，避免电商配色被滥用。
- 首屏数字（3 / 16 / 282 / 99）来自三个项目的真实验证结果：183 条接口断言 + 99 条 E2E，加总 282。