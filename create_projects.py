from PySide2 import QtWidgets, QtCore
import substance_painter


def Log(info):
     substance_painter.logging.info(info)

class ProjectCreator:
    def __init__(self):
        # 1. 创建一个 名为 remesh 按钮
        self.btn = QtWidgets.QPushButton('remesh');
        # 2. 注册按钮点击回调函数
        self.btn.clicked.connect(self.replace_mesh)
        # 3. 将按钮添加到 侧边栏中
        substance_painter.ui.add_plugins_toolbar_widget(self.btn)

    def __del__(self):
        # 销毁创建的按钮 
        substance_painter.ui.delete_ui_element(self.btn)

    def replace_mesh(self):
        Log("on click replace_mesh")
    
CREATE_PROJECT_RELOAD_MESH_PLUGIN = None

def start_plugin():
    global CREATE_PROJECT_RELOAD_MESH_PLUGIN
    CREATE_PROJECT_RELOAD_MESH_PLUGIN = ProjectCreator()

def close_plugin():
    global CREATE_PROJECT_RELOAD_MESH_PLUGIN
    del CREATE_PROJECT_RELOAD_MESH_PLUGIN
