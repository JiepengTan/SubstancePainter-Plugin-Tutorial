// author : jiepengtan
// https://github.com/JiepengTan/SubstancePainter-Plugin-Tutorial

import QtQuick 2.2
import Painter 1.0

PainterPlugin {

    Component.onCompleted: {
		// 使用 export.qml 文件在左边的插件栏中创建一个按钮 
        alg.ui.addWidgetToPluginToolBar("export.qml");
    }
	// 实例化
	ConfigurePanel {
        id: configurePanel
    }
	// 当用户点击 插件的 configure 按钮时候，调用 ConfigurePanel.qml 显示
    onConfigure: {
        configurePanel.open();
    }
}