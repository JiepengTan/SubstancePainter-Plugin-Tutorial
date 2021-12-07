import AlgWidgets 2.0
import QtQuick.Dialogs 1.0
import "logic.js" as LogicJS

AlgToolBarButton {
  id: root
  iconName: "icons/gamestan.png"
  onClicked: {
    LogicJS.doExportMaps();
  }
}
