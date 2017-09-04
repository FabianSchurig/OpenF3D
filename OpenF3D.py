#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface   

        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent
        
        doc = app.activeDocument
        
        #Create FileDialog
        dialog = ui.createFileDialog()
        dialog.filter = 'Fusion Archive (*.f3d)'
        dialog.initialDirectory = os.path.expanduser('~/Documents/')
        if dialog.showOpen() != adsk.core.DialogResults.DialogOK:
            return
        
        # Get import manager
        importManager = app.importManager
        
        # Get archive import options
        archiveFileName = dialog.filename #'C:\\Users\\Fabi\\Documents\\test.f3d'
        archiveOptions = importManager.createFusionArchiveImportOptions(archiveFileName)
        
        # Import archive file to root component
        importManager.importToTarget(archiveOptions, root)
        
        importedComponent = design.allComponents.item(design.allComponents.count-1)
        importedBodies = importedComponent.bRepBodies
        
        
        ui.messageBox('Bodies in active document {}, imported bodies {} \n center of mass {}'.format(root.bRepBodies.count, importedBodies.count, importedBodies.item(0).physicalProperties.centerOfMass.asArray()))
        
                
        #doc.close(False)
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))