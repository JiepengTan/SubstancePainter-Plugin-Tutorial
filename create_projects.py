# author : jiepengtan
# https://github.com/JiepengTan/SubstancePainter-Plugin-Tutorial

from PySide2 import QtWidgets, QtCore
import substance_painter.project
import substance_painter.ui
import os

from enum import Enum
class EPluginState(Enum):
    Idle = 1
    WaitReplaceMesh = 2  # 等待 relaod mesh 完成 
    WaitSaveProject = 3  # 等待 save as  完成

def Log(info):
     substance_painter.logging.info(info)



class CreateProjectByReloadMesh:
    def __init__(self):
        self.btn = QtWidgets.QPushButton('remesh');
        self.btn.setFixedSize(50,50)
        self.btn.clicked.connect(self.create_projects)
        substance_painter.ui.add_plugins_toolbar_widget(self.btn)

        # 状态设置
        self.status = EPluginState.Idle
        connections = {
            # 如需监听 其他事件，添加即可，具体事件名 请查看API 文档
            substance_painter.event.BusyStatusChanged: self.on_busy_status_changed,
        }
        # 注册事件监听函数
        for event, callback in connections.items():
            substance_painter.event.DISPATCHER.connect(event, callback)

    def __del__(self):
        substance_painter.ui.delete_ui_element(self.btn)


    def on_busy_status_changed(self, e):
        #Log("Changed status" + str(isBusy) + " status " + str(self.status) )
        # 判定SP 是否正在执行 任务
        isBusy = substance_painter.project.is_busy()
        if(not isBusy):
            if(self.status == EPluginState.WaitReplaceMesh):
                self.save_project()
            if(self.status == EPluginState.WaitSaveProject):
                self.reload_next_mesh()

    def save_project(self):
        self.status = EPluginState.WaitSaveProject
        substance_painter.project.save_as(self.targetProjectFile)

    def create_projects(self,targetMeshName):
        # 从约定好的文件中读取数据
        dstFile ="d://_fishman_sp_tutorial_input_dir.data"
        if(not os.path.exists(dstFile)):
            return
        fo = open(dstFile, "r+")
        self.targetDir = fo.readline();
        fo.close()
        Log(self.targetDir)

        # self.targetDir = "D:/temp/TestFbxs/input"

        rootdir = self.targetDir
        files = os.listdir(rootdir) 
        # 得到所有需要处理的 低模路径
        allFiles = list()
        for i in range(0,len(files)):
            path = os.path.join(rootdir,files[i])
            if os.path.isfile(path):
                if(path.endswith("_low.fbx")):
                    allFiles.append(path)
        self.allFiles = allFiles
        self.curIdx = 0
        self.reload_next_mesh()

    def set_output_dir(self):
        filePath = self.allFiles[self.curIdx]
        self.curIdx = self.curIdx + 1
        filePath = filePath.replace("\\","/")
        fileName = os.path.split(filePath)[1]
        self.targetProjectFile = os.path.join(self.targetDir,"../spp_files",os.path.splitext(fileName)[0] + ".spp").replace("\\","/")
        self.targetProjectFile = os.path.abspath(self.targetProjectFile).replace("\\","/")
        targetMeshName = filePath
        Log("create_projects start " + targetMeshName)
        return targetMeshName

    def reload_next_mesh(self):
        self.status = EPluginState.Idle
        if(self.curIdx is None):
            return
        if(self.curIdx >= len(self.allFiles)):
            Log("----- Reload meshes done!!! -----")
            self.curIdx = None
            return
        self.status = EPluginState.WaitReplaceMesh
        # 计算输出路径
        targetMeshName = self.set_output_dir()

        # 替换 低模
        mesh_reloading_settings = substance_painter.project.MeshReloadingSettings(
        import_cameras=True,
        preserve_strokes=True)
        substance_painter.project.reload_mesh(
            targetMeshName,
            mesh_reloading_settings,
            self.on_reload_result
        )

    def on_reload_result(self,value):
        pass
    
CREATE_PROJECT_RELOAD_MESH_PLUGIN = None

def start_plugin():
    global CREATE_PROJECT_RELOAD_MESH_PLUGIN
    CREATE_PROJECT_RELOAD_MESH_PLUGIN = CreateProjectByReloadMesh()

def close_plugin():
    global CREATE_PROJECT_RELOAD_MESH_PLUGIN
    del CREATE_PROJECT_RELOAD_MESH_PLUGIN
