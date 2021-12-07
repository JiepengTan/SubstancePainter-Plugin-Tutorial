function exportMaps(outPath,textureSize) {
  // 获取当前的 Preset 的名字
  var presetName = alg.mapexport.getProjectExportPreset();
  // 导出 贴图
  alg.mapexport.exportDocumentMaps(
      presetName,
      outPath,
      "png",
      { resolution: [textureSize, textureSize] });
}


function doExportMaps() {
  var saveDir = "D:/FishMan_SPTutorial/output"; // 输出贴图的目标路径 
  var textureSize = 1024 ;// 输出贴图的大小
  alg.log.info(saveDir)
  exportMaps(saveDir, textureSize); //
}