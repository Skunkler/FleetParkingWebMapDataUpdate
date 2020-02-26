#This script was written by Warren Kunkler in support of the Fleet Parking Webmap update from Facility View to Sip. Currently this script takes a copy of the old FV_COMMON fleet parking data provided by Jeff Ferdinand
#and appends it to a newly created feature class called LVVWDGIS.PARKING_FLEET. This script was debugged and successfully launched in Development as LVVWDGIS schema owner

#Things to add to this script: the ability to grant permission to the data


import arcpy, sys, traceback, datetime, os
from arcpy import env


dBaseConnection = r"C:\Users\kunklerw\AppData\Roaming\ESRI\Desktop10.7\ArcCatalog\LVVWDGIS_DEV.sde"
env.workspace = dBaseConnection
env.overwriteOutput = True
AppendData = r"U:\GISAdmin\PARKING_FLEET\parking.gdb\PARKING_FLEET"

outpath = dBaseConnection
print "Creating roads feature class now"

try:

    arcpy.CreateFeatureclass_management(outpath, "LVVWDGIS.PARKING_FLEET", "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_StatePlane_Nevada_East_FIPS_2701_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',656166.6666666665],PARAMETER['False_Northing',26246666.66666666],PARAMETER['Central_Meridian',-115.5833333333333],PARAMETER['Scale_Factor',0.9999],PARAMETER['Latitude_Of_Origin',34.75],UNIT['Foot_US',0.3048006096012192]];-17790500 -19184900 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", config_keyword="ST_GEOMETRY", spatial_grid_1="0", spatial_grid_2="0", spatial_grid_3="0")
    arcpy.MakeFeatureLayer_management(outpath+"\\PARKING_FLEET", "ParkingLyr")
    arcpy.AddField_management('ParkingLyr',"LOT", "TEXT", "", "", 10, "LOT", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management('ParkingLyr',"TYPE", "TEXT", "", "", 20, "TYPE", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management('ParkingLyr',"THEME", "TEXT", "", "", 20, "THEME", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management('ParkingLyr',"LASTUPDT", "DATE")
    #arcpy.AddField_management('ParkingLyr',"SHAPE", "GEOMETRY", "", "", size, "VEHICLE", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management('ParkingLyr',"VEHICLE", "TEXT", "", "", 10, "VEHICLE", "NULLABLE", "NON_REQUIRED")
except:
    print arcpy.GetMessages(2)


try:
    print "now appending data to feature class"

    arcpy.MakeFeatureLayer_management(AppendData, 'OrigFacFleet_Parking')
    arcpy.Append_management('OrigFacFleet_Parking', 'ParkingLyr', 'NO_TEST')
    print "process done!"
except:
    print arcpy.GetMessages(2)


