"""
Lego Digital Designer C4D Importer
Copyright: Gerhard Messer
Written for CINEMA 4D R16+

Modified Date: 25.09.2014
"""

import c4d
from c4d import gui, plugins, utils, bitmaps, storage

import collections, os

#1033677    LDDImport --  registered 25.09.2014
PLUGIN_ID = 1033677

class LDDImporter(c4d.plugins.ObjectData:
    pass
    
    
    

"""
def EnhanceMainMenu():
    mainMenu = gui.GetMenuResource("M_EDITOR")                    # Get main menu resource
    pluginsMenu = gui.SearchPluginMenuResource()                  # Get 'Plugins' main menu resource

    menu = c4d.BaseContainer()                                    # Create a container to hold a new menu information
    menu.InsData(c4d.MENURESOURCE_SUBTITLE, "LDDImport")            # Set the name of the menu
    menu.InsData(c4d.MENURESOURCE_COMMAND, "IDM_NEU")             # Add registered default command 'New Scene' to the menu
    menu.InsData(c4d.MENURESOURCE_SEPERATOR, True);               # Add a separator
    menu.InsData(c4d.MENURESOURCE_COMMAND, "PLUGIN_CMD_5159")     # Add command 'Cube' with ID 5159 to the menu

    submenu = c4d.BaseContainer()                                 # Create a new submenu container
    submenu.InsData(c4d.MENURESOURCE_SUBTITLE, "Submenu")         # This is a submenu
    submenu.InsData(c4d.MENURESOURCE_COMMAND, "IDM_SPEICHERN")    # Add registered default command 'Save' to the menu

    menu.InsData(c4d.MENURESOURCE_SUBMENU, submenu)               # Add the submenu

    if pluginsMenu:
        # Insert menu after 'Plugins' menu
        mainMenu.InsDataAfter(c4d.MENURESOURCE_STRING, menu, pluginsMenu)
    else:
        # Insert menu after the last existing menu ('Plugins' menu was not found)
        mainMenu.InsData(c4d.MENURESOURCE_STRING, menu)

def PluginMessage(id, data):
    if id==c4d.C4DPL_BUILDMENU:
        EnhanceMainMenu()

class Test(gui.GeDialog):
    
    mem_info = MemoryInfo()
    cur_mem_info = None
    
    def __init__(self):
        self.AddGadget(c4d.DIALOG_NOMENUBAR, 0)#disable menubar
    
    def CreateLayout(self):
        
        bc = c4d.GetMachineFeatures()
        self.SetTitle(bc[c4d.MACHINEINFO_COMPUTERNAME])
        self.GroupBegin(id=0, flags=c4d.BFH_SCALEFIT, rows=1, title="", cols=2, groupflags=c4d.BORDER_GROUP_IN)
        self.AddGadget(c4d.DIALOG_PIN, 0)#enable WindowPin
        self.cur_mem_info = self.AddStaticText(id=0, initw=0, inith=0, name="", borderstyle=0, flags=c4d.BFH_SCALEFIT)
        self.GroupEnd()
        
        self.AddSeparatorH(inith=0)
        
        self.GroupBegin(id=0, flags=c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, title="", rows=1, cols=1, groupflags=c4d.BORDER_GROUP_IN)
        self.GroupBorderSpace(5, 5, 5, 5)
        
        #give really unique ID to userarea, otherwise the update process will fail!
        area = self.AddUserArea(id=1001, flags=c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT)
        self.AttachUserArea(self.mem_info, area)
        self.GroupEnd()
        return True
    
    def InitValues(self):
        self.SetTimer(500)
        return True
    
    def Timer(self, msg):
        bc = self.mem_info.Update()
        self.SetString(self.cur_mem_info, ("Current: %.3f MB" % (CalcValueToMB(bc[c4d.C4D_MEMORY_STAT_MEMORY_INUSE]))))

"""
class LDDImportCommandData(c4d.plugins.CommandData):
    dialog = None

    def Execute(self, doc):
        """Just create the dialog when the user clicked on the entry
        in the plugins menu to open it."""
        if self.dialog is None:
           self.dialog = Test()

        return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID, defaulth=400, defaultw=400)

    def RestoreLayout(self, sec_ref):
        """Same for this method. Just allocate it when the dialog
        is needed"""
        if self.dialog is None:
           self.dialog = Test()

        return self.dialog.Restore(pluginid=PLUGIN_ID, secret=sec_ref)

if __name__ == "__main__":
     bmp = bitmaps.BaseBitmap()
     dir, f = os.path.split(__file__)
     fn = os.path.join(dir, "res", "LDDimport.png")
     bmp.InitWith(fn)
     c4d.plugins.RegisterCommandPlugin(id=PLUGIN_ID, str="LDD Importer",
                                      help="Imports Lego Digital Designer Models",info=0,
                                        dat=LDDImportCommandData(), icon=bmp)
                                        
                                        
    c4d.plugins.RegisterObject