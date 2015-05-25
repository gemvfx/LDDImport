"""
Lego Digital Designer C4D Importer
Copyright: Gerhard Messer
Written for CINEMA 4D R16+

Version History
0.1 - 2015-05-18 - initial plugin 

"""

import c4d
from c4d import gui, plugins, utils, bitmaps, storage

import os, sys

#1033677    LDDImport --  registered 25.09.2014
PLUGIN_ID = 1033677

class Olddimporter(c4d.plugins.ObjectData):
    print "hihi"
    pass
  
        
def main():
    bmp = bitmaps.BaseBitmap()
    dir, f = os.path.split(__file__)
    fn = os.path.join(dir, "res", "LDDimport.png")
    bmp.InitWith(fn)
    c4d.plugins.RegisterObjectPlugin(id=PLUGIN_ID, str="LDD Importer", g=Olddimporter, 
                                        description="LDDImporter", info=c4d.OBJECT_GENERATOR, icon=None)
    
        
if __name__ == "__main__":
    main()
                                        
