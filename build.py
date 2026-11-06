"""把 index.template.html 里的 @@IMG:key@@ 占位替换成内联 base64，产出单文件 index.html。

用法：python build.py
依赖：Pillow（生成 webp）、标准库 base64
"""
import base64
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
SRC = os.path.join(HERE, "index.template.html")
DST = os.path.join(HERE, "index.html")

TOKEN = re.compile(r"@@IMG:([a-z0-9\-]+)@@")

# 中文排版：源码里的换行在浏览器里会渲染成一个空格（「接口实现， 到前端」这种）。
# 只消除「中日韩字符之间」的换行空白，不动 Latin 词间空格与标签。
CJK = "\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef"
CJK_LINEBREAK = re.compile(f"(?<=[{CJK}])[ \t]*\n[ \t]*(?=[{CJK}])")


def data_uri(key: str) -> str:
    path = os.path.join(ASSETS, key + ".webp")
    if not os.path.exists(path):
        sys.exit(f"缺少图片：{path}（先运行 assets 生成步骤）")
    with open(path, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    return f"data:image/webp;base64,{b64}"


def main() -> None:
    with open(SRC, encoding="utf-8") as fh:
        html = fh.read()

    keys = sorted(set(TOKEN.findall(html)))
    if not keys:
        sys.exit("模板里没有找到 @@IMG:key@@ 占位")

    cache = {}
    for key in keys:
        cache[key] = data_uri(key)

    html = TOKEN.sub(lambda m: cache[m.group(1)], html)

    html = CJK_LINEBREAK.sub("", html)

    with open(DST, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)

    size = os.path.getsize(DST) / 1024
    print(f"[OK] output: {DST}")
    print(f"     inlined images ({len(keys)}): {', '.join(keys)}")
    print(f"     single-file size: {size:.0f} KB")


if __name__ == "__main__":
    main()