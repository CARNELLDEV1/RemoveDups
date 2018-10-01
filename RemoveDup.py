###############################################################
#
#
#
###############################################################

import arcpy
import os

###############################################################
# Configuration for database server and local filedatabase
###############################################################

CONFIG = {
    'SDE':r'Database Connections\Connection to carnell99 (3).sde',
    'newJobName':'Points_Version',
    'LocalPath':r'C:\Users\haoye\OneDrive - Carnell Support Services Ltd\Desktop\Projects\RemoveDup\Data\Data.shp'
    }

################################################################
# Configure the workspace for SDE
################################################################
arcpy.env.workspace = CONFIG['SDE']
jobName = CONFIG['newJobName']
outfile = CONFIG['LocalPath']

################################################################
# Configure the name matching comparison
################################################################

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
for lyr in arcpy.mapping.ListLayers(mxd, "", df):
    if lyr.name == "Data":
        arcpy.mapping.MoveLayer(df,lyr)
mxd.saveACopy(r"C:\Project\Project2.mxd")
del mxd

ly_names = arcpy.ListFeatureClasses()
matching = [fc for fc in ly_names if jobName in fc]

if os.path.isfile(outfile):
    os.remove(outfile)

for ly in matching:
    infile = os.path.join(arcpy.env.workspace,ly)
    arcpy.CopyFeatures_management(infile,outfile)

#################################################################
#
#################################################################

