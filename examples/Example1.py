import GISDataProcess

maintainFeatureClass = 'c:\Users\samdrum\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\PROD_GIS_PUBLISH_giscreator.sde\GIS_PUBLISH.GISCREATOR.TEST_UPDATES'
publishFeatureClass = 'c:\Users\samdrum\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\PROD_GIS_PUBLISH_giscreator.sde\GIS_PUBLISH.GISCREATOR.TEST_PUBLISH'

updateFeatureClass = GISDataProcess.UpdateFeatureClass(maintainFeatureClass, publishFeatureClass)
updateFeatureClass.delete_publish_features()
updateFeatureClass.append_maintain_features()
