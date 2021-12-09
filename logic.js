// author : jiepengtan
// https://github.com/JiepengTan/SubstancePainter-Plugin-Tutorial

function Log(infos) {
  alg.log.info(infos);
}

function checkDir(dir) {
  dir = dir.replace("\\", "/");
  if (!dir.endsWith("/")) {
      dir = dir + "/"
  }
  return dir
}

function getAllLowMeshes(dir) {
  var files = alg.fileIO.listDir(dir)
  var lowFiles = []
  for (var fileIdx in files) {
      var file = files[fileIdx]
      if (file.endsWith("_low.fbx")) {
          lowFiles.push(file);
      }
  }
  return lowFiles
}


function checkAndSetHighPolyMesh(pathToLow) {
  var pathToHigh = [pathToLow.replace("_low", "_high")]
  // 这里我们只用到了 高模信息绑定，如需要设置其他属性 ，可以参考该格式进行类似的设定
  var params = alg.baking.commonBakingParameters()
  params.detailParameters.High_Definition_Meshes = pathToHigh
  alg.baking.setCommonBakingParameters(params)
}

function bakeAllDocs() {
  // 遍历所有的材质球 对每一个材质球都进行贴图烘焙
  alg.mapexport.documentStructure().materials.forEach(function (material) {
      alg.baking.bake(material.name);
  });
}

function exportMaps(outPath,textureSize) {
  // 从配置中读取 导出的贴图模板
  var presetName = alg.settings.value("presetName", "");
  // 导出 贴图
  alg.mapexport.exportDocumentMaps(
      presetName,
      outPath,
      "png",
      { resolution: [textureSize, textureSize] });
}

function loadProject(dir,fileName){
  // 根据低模名字计算项目文件名字
  var projectDir = dir.slice(0, dir.slice(0,dir.length-1).lastIndexOf('/')) + '/spp_files/';
  var projectPath = projectDir +fileName.replace(".fbx",".spp");
  // 打开项目 （如果项目已经打开，确保关闭）
  if (alg.project.isOpen()) {
    alg.project.close()
  }
  alg.project.open("file:///"+ projectPath)
}

function doExportMaps() {
  var dir = alg.settings.value("inputPath", "");
  dir = checkDir(dir)
  // 1.获取所有的低模名字
  var allMeshes = getAllLowMeshes(dir);
  var textureSize = 1024 ;// 输出贴图的大小
  var saveDir = alg.settings.value("exportPath", "");
  var curIdx = 0;
  allMeshes.forEach(fileName => {
      Log((++curIdx)+"/" + allMeshes.length + " :"+ fileName)
      // 2.加载项目文件
      loadProject(dir,fileName);
      // 3.绑定高模
      checkAndSetHighPolyMesh(dir + fileName);
      // 4.烘焙贴图 id AO 等
      bakeAllDocs();
      // 5.导出最终贴图
      exportMaps(saveDir,textureSize); 
  });
  Log("Output all texture done!")
}