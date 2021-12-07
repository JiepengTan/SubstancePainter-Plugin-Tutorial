import QtQuick 2.2
import Painter 1.0

PainterPlugin {

    Component.onCompleted: {
		// 使用 export.qml 文件在左边的插件栏中创建一个按钮 
        alg.ui.addWidgetToPluginToolBar("export.qml");
    }
}