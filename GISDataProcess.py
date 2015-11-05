import arcpy


class UpdateFeatureClass(object):

    def __init__(self, maintain_feature_class, publish_feature_class):

        is_maintain_feature_class = arcpy.Exists(maintain_feature_class)
        is_publish_feature_class = arcpy.Exists(publish_feature_class)

        print maintain_feature_class
        print publish_feature_class

        if (not is_maintain_feature_class) and (not is_publish_feature_class):

            raise ValueError("Neither publish or maintain feature class can be found")

        elif not is_publish_feature_class:

            raise ValueError("The publish feature class cannot be found")

        elif not is_maintain_feature_class:

            raise ValueError("The maintain feature class cannot be found")

        else:
            self.maintain_feature_class = maintain_feature_class
            self.publish_feature_class = publish_feature_class

    def delete_publish_features(self):

        try:
            arcpy.DeleteFeatures_management(self.publish_feature_class)
        except:
            raise arcpy.GetMessages()

    def append_maintain_features(self):

        try:

            schema_type = "NO_TEST"
            field_mappings = ""
            subtype = ""
            arcpy.Append_management(self.maintain_feature_class, self.publish_feature_class,
                                         schema_type, field_mappings, subtype)

        except:

           print arcpy.GetMessages()
           raise ValueError('An error occurred')


class UpdatePointFeatureClass(UpdateFeatureClass):

    def append_maintain_feature_points(self):

        try:

            in_memory_feature_class = 'in_memory\point_feature_class'
            arcpy.FeatureToPoint_management(self.maintain_feature_class, in_memory_feature_class, "INSIDE")

            self.maintain_feature_class = in_memory_feature_class
            self.append_maintain_features()

        except:

            print  arcpy.GetMessages()
            raise ValueError('An error occurred')

        finally:

            del in_memory_feature_class

class RebuildGeocoder(object):

    def __init__(self, geocoder):

        try:
            arcpy.RebuildAddressLocator_geocoding(geocoder)

        except:

            print  arcpy.GetMessages()
            raise ValueError('An error occurred')