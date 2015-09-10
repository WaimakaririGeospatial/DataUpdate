import sys
import GISDataProcess

maintainFeatureClass = sys.argv[1]
publishFeatureClass = sys.argv[2]

updateFeatureClass = GISDataProcess.UpdateFeatureClass(maintainFeatureClass, publishFeatureClass)
updateFeatureClass.delete_publish_features()
updateFeatureClass.append_maintain_features()
