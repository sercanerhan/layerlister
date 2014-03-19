import arcpy
import pythonaddins
import os

class ButtonClass5(object):
    """Implementation for layerlister_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("CURRENT")
        layers = arcpy.mapping.ListLayers(mxd,"*")
        text_file = open(r"D:\liste.txt", "w")
        for lyr in layers:
			print>>text_file, lyr
        text_file.close()