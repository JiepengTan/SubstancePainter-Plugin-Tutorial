import AlgWidgets 2.0
import QtQuick.Dialogs 1.0
import "logic.js" as LogicJS

AlgToolBarButton {
  id: root
  iconName: "icons/gamestan.png" // 插件图标的路径
  onClicked: {
    LogicJS.doExportMaps();      // 插件按钮点击后 调用logic.js 的doExportMaps 函数
  }
}
