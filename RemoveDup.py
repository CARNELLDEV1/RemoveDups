import arcpy
import os

# Configuration

CONFIG = {
    'SDE':r'Database Connections\Connection to carnell99 (3).sde',
    'newJobName':'Points_Version',
    'LocalPath':r'C:\Users\haoye\OneDrive - Carnell Support Services Ltd\Desktop\Projects\RemoveDup\Data'
    }

# Configure the workspace for SDE
arcpy.env.workspace = CONFIG['SDE']
jobName = CONFIG['newJobName']
outfile = CCONFIG['LocalPath']

# Configure the names
ly_names = arcpy.ListFeatureClasses()
matching = [fc for fc in ly_names if jobName in fc]

for ly in matching:
    infile = arcpy.env.workspace +"\\" + ly
    arcpy.CopyFeatures_management(infile,outfile)