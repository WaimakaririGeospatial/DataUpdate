import GISDataProcess

maintainFeatureClass = 'C:\Users\samdrum\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\PROD_GIS_VIEWS_giscreator.sde' \
                       '\GIS_VIEWS.giscreator.SV_LINZ_PARCEL_CORE'
publishFeatureClass = 'C:\Users\samdrum\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\PROD_GIS_PUBLISH_giscreator.sde' \
                      '\GIS_PUBLISH.GISCREATOR.LINZ_PARCEL_CORE_TEST'

#Update polygons
updateFeatureClass = GISDataProcess.UpdateFeatureClass(maintainFeatureClass, publishFeatureClass)
updateFeatureClass.delete_publish_features()
updateFeatureClass.append_maintain_features()

publishFeatureClass = 'C:\Users\samdrum\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\PROD_GIS_PUBLISH_giscreator.sde' \
                      '\GIS_PUBLISH.GISCREATOR.LINZ_PARCEL_CORE_POINT_TEST'

#Update points
updateFeatureClass = GISDataProcess.UpdatePointFeatureClass(maintainFeatureClass, publishFeatureClass)
updateFeatureClass.delete_publish_features()
updateFeatureClass.append_maintain_feature_points()
