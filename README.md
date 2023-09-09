# SplaPainter-depe_nxbt
> Splatoon3 Painter - dependency_nxbt

### 这个工具可以帮助你便捷的在 `Splatoon3` 中绘制名片
###### 本工具基于 [NXBT](https://github.com/Brikwerk/nxbt) ，即：使用本工具生成 `NXBT` 可用的宏程序。

### 使用方法
- 安装依赖
```text
pip install -r requirements.txt
```

- 将要绘制的图片放置于 `main.py` 同级目录，并命名为 `input.png`，请使用分辨率为320x120的图片  
- 运行 `main.py`
- 程序将创建文件 `result.png` 与 `result.txt`
> `result.png` 可以预览生成的效果  
> `result.txt` 为 `NXBT` 可使用的宏程序

### 已知问题
- 绘制所需时间较长，通常需要30-45分钟。
- 有时会丢失指令，即绘制可能错位，经过测试，单次绘画错误率约为10%，程序经过优化，绘制错误通常只存在于某一行。