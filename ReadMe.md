# Data Update #
A simple update for deleting and appending data from one geodatabase to another assuming no change to table schema

## Requirements ##
- arcpy 10.2

## Installation ##
No specific setup file has been created for this module. Rather users can simply copy the module itself to the site-packages folder or create a .pth file while references the directory where GISProcess.py is located. This will give python access to the module.

## Example Usage ##

###From a Script###
The user can create a script which calls the module as follows:

```PYTHON

import GISDataProcess

maintainFeatureClass = 'PATH TO MAINTAIN FEATURE CLASS'
publishFeatureClass = 'PATH TO PUBLISH FEATURE CLASS'

updateFeatureClass = GISDataProcess.UpdateFeatureClass(maintainFeatureClass, publishFeatureClass)
updateFeatureClass.delete_publish_features()
updateFeatureClass.append_maintain_features()
```

Alternatively the following script could be run from a scheduled update passing in arguments

```python RunGISDataProcess.py [PATH TO MAINTAIN FEATURE CLASS] [PATH TO PUBLISH FEATURE CLASS]```

```PYTHON
### RunGISDataProcess.py

import sys
import GISDataProcess

maintainFeatureClass = sys.argv[1]
publishFeatureClass = sys.argv[2]

updateFeatureClass = GISDataProcess.UpdateFeatureClass(maintainFeatureClass, publishFeatureClass)
updateFeatureClass.delete_publish_features()
updateFeatureClass.append_maintain_features()

```

## Author ##
Sam Drummond (Sam Drummond Consulting)