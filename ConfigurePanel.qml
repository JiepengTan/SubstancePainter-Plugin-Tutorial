import QtQuick 2.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import AlgWidgets 2.0
import "logic.js" as LogicJS

AlgDialog {
  id: configureDialog
  visible: false
  title: "configure"
  width: 500
  height: 220
  minimumWidth: 400
  minimumHeight: 220

  function reload() {
    content.reload()
  }

  onAccepted: {
    // 判定用户是否有设置输出路径
    if (exportPath.text != "...") {
      // 将用户设置的输出路径保存到 setting.ini 文件中方便读取
		  alg.settings.setValue("exportPath", exportPath.text);
	  }
  }

  Rectangle {
    id: content
    parent: contentItem
    anchors.fill: parent
    anchors.margins: 12
    color: "transparent"
    clip: true

    function reload() {
      exportPath.reload()
    }

    AlgScrollView {
      id: scrollView
      anchors.fill: parent

      ColumnLayout {
        spacing: 18
        Layout.maximumWidth: scrollView.viewportWidth
        Layout.minimumWidth: scrollView.viewportWidth

      // 增加一栏
        ColumnLayout {
          spacing: 6
          Layout.fillWidth: true

          AlgLabel {
            text: qsTr("Path to Output")
            Layout.fillWidth: true
          }

          RowLayout {
            spacing: 6
            Layout.fillWidth: true

            AlgTextEdit {
              id: exportPath
              borderActivated: true
              wrapMode: TextEdit.Wrap
              readOnly: true
              Layout.fillWidth: true

              function reload() {
                text = alg.settings.value("exportPath", "...")
              }

              Component.onCompleted: {
                // 加载的时候刷新
                reload()
              }
            }

            AlgButton {
              id: outputDirButton
              text: qsTr("Set path")
              onClicked: {
                // 打开文件选择对话框
                outputDirDialog.setVisible(true)
              }
            }
          }
        }
      }
    }
  }
  // 文件选择对话框
  FileDialog {
    id: outputDirDialog
    title: "Please select export path..."
    selectFolder: true
    onAccepted: { // 玩家确定后回调
      // 将url 转为路径
      exportPath.text = alg.fileIO.urlToLocalFile(fileUrl.toString())
      alg.log.info("fileUrl.toString() " + fileUrl.toString() + "exportPath "+exportPath.text)
      alg.settings.setValue("exportPath", exportPath.text);
    }
    onVisibleChanged: {
      if (!visible) {
        //文件对话框 不可见后 重新显示配置界面
        configureDialog.requestActivate();
      }
    }
  }
}
