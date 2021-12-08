## FishMan Substance Painter Plugin Tutorial

这是Substance Painter 插件 教程，内容是制作一个
- 1.批量替换mesh 生成 ssp项目文件
- 2.批量根据ssp 项目文件导出贴图的功能

对应的是下面这个gif的第2，3 步 效果

![](https://pic2.zhimg.com/80/v2-e54c13417a4c9dd5f36db0fcec531c4e_1440w.gif)

对应的教程：
[Substance Painter 插件开发教程 01](https://zhuanlan.zhihu.com/p/442473363)


## 使用本插件
1. [下载本工程(TODO 当前没有完成)](https://codeload.github.com/JiepengTan/SubstancePainter-Plugin-Tutorial/zip/refs/heads/main)
2. 点击 Substance Painter，点击菜单栏``JavaScript/Plugins folder`` 将本工程解压到项目中并拷贝create_projects.py文件
3. 点击 Substance Painter，点击菜单栏``Python/Plugins folder`` 打开插件目录，将create_projects.py文件黏贴到 plugins 目录下
4. 点击菜单栏``JavaScript/Reload Plugins folder`` 重新加载插件
5. 点击菜单栏``Python/Reload Plugins folder`` 重新加载插件
6. 点击菜单栏``JavaScript/hello plugin/configure`` 配置 高低模路径和 贴图输出路径
7. 如需 批量生成 ssp 项目文件 ，点击侧边栏的 ``remesh`` 按钮 （需要先打开目录）
8. 如需 批量生成 导出贴图 ，点击侧边栏的 我的头像的按钮


## License
Distributed under the MIT license. 