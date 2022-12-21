# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022.HF5 replay file
# Internal Version: 2022_09_26-18.03.59 176852
# Run by giridhs1 on Tue Nov 29 15:51:24 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=317.764556884766, 
    height=185.698120117188)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='G0_Damage_P.odb')
#: Model: Z:/Project/odb test/G0/G0_Damage_P.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['G0_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodeSets=("FORCE_DISP", ))
xy1 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165659']
xy2 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165660']
xy3 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165661']
xy4 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165662']
xy5 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165706']
xy6 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165707']
xy7 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165708']
xy8 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165709']
xy9 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165775']
xy10 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165776']
xy11 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165777']
xy12 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165778']
xy13 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165779']
xy14 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165784']
xy15 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165785']
xy16 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165786']
xy17 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165787']
xy18 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165788']
xy19 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165789']
xy20 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165790']
xy21 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165816']
xy22 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165817']
xy23 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165818']
xy24 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165819']
xy25 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165820']
xy26 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165821']
xy27 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165822']
xy28 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165823']
xy29 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165824']
xy30 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165825']
xy31 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165826']
xy32 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165827']
xy33 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165828']
xy34 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165829']
xy35 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165830']
xy36 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165831']
xy37 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165832']
xy38 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165833']
xy39 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 165834']
xy40 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39))*2/1000
xy40.setValues(
    sourceDescription='sum ( ( "RF:RF2 PI: PART-1-1 N: 165659", "RF:RF2 PI: PART-1-1 N: 165660", "RF:RF2 PI: PART-1-1 N: 165661", "RF:RF2 PI: PART-1-1 N: 165662", "RF:RF2 PI: PART-1-1 N: 165706", "RF:RF2 PI: PART-1-1 N: 165707", "RF:RF2 PI: PART-1-1 N: 165708", "RF:RF2 PI: PART-1-1 N: 165709", "RF:RF2 PI: PART-1-1 N: 165775", "RF:RF2 PI: PART-1-1 N: 165776", "RF:RF2 PI: PART-1-1 N: 165777", "RF:RF2 PI: PART-1-1 N: 165778", "RF:RF2 PI: PART-1-1 N: 165779", "RF:RF2 PI: PART-1-1 N: 165784", "RF:RF2 PI: PART-1-1 N: 165785", "RF:RF2 PI: PART-1-1 N: 165786", "RF:RF2 PI: PART-1-1 N: 165787", "RF:RF2 PI: PART-1-1 N: 165788", "RF:RF2 PI: PART-1-1 N: 165789", "RF:RF2 PI: PART-1-1 N: 165790", "RF:RF2 PI: PART-1-1 N: 165816", "RF:RF2 PI: PART-1-1 N: 165817", "RF:RF2 PI: PART-1-1 N: 165818", "RF:RF2 PI: PART-1-1 N: 165819", "RF:RF2 PI: PART-1-1 N: 165820", "RF:RF2 PI: PART-1-1 N: 165821", "RF:RF2 PI: PART-1-1 N: 165822", "RF:RF2 PI: PART-1-1 N: 165823", "RF:RF2 PI: PART-1-1 N: 165824", "RF:RF2 PI: PART-1-1 N: 165825", "RF:RF2 PI: PART-1-1 N: 165826", "RF:RF2 PI: PART-1-1 N: 165827", "RF:RF2 PI: PART-1-1 N: 165828", "RF:RF2 PI: PART-1-1 N: 165829", "RF:RF2 PI: PART-1-1 N: 165830", "RF:RF2 PI: PART-1-1 N: 165831", "RF:RF2 PI: PART-1-1 N: 165832", "RF:RF2 PI: PART-1-1 N: 165833", "RF:RF2 PI: PART-1-1 N: 165834" ) )*2/1000')
tmpName = xy40.name
session.xyDataObjects.changeKey(tmpName, 'Force')
xy1 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165659']
xy2 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165660']
xy3 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165661']
xy4 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165662']
xy5 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165706']
xy6 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165707']
xy7 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165708']
xy8 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165709']
xy9 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165775']
xy10 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165776']
xy11 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165777']
xy12 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165778']
xy13 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165779']
xy14 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165784']
xy15 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165785']
xy16 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165786']
xy17 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165787']
xy18 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165788']
xy19 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165789']
xy20 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165790']
xy21 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165816']
xy22 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165817']
xy23 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165818']
xy24 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165819']
xy25 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165820']
xy26 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165821']
xy27 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165822']
xy28 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165823']
xy29 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165824']
xy30 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165825']
xy31 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165826']
xy32 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165827']
xy33 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165828']
xy34 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165829']
xy35 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165830']
xy36 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165831']
xy37 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165832']
xy38 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165833']
xy39 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 165834']
xy40 = avg((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39))
xy40.setValues(
    sourceDescription='avg ( ( "U:U2 PI: PART-1-1 N: 165659", "U:U2 PI: PART-1-1 N: 165660", "U:U2 PI: PART-1-1 N: 165661", "U:U2 PI: PART-1-1 N: 165662", "U:U2 PI: PART-1-1 N: 165706", "U:U2 PI: PART-1-1 N: 165707", "U:U2 PI: PART-1-1 N: 165708", "U:U2 PI: PART-1-1 N: 165709", "U:U2 PI: PART-1-1 N: 165775", "U:U2 PI: PART-1-1 N: 165776", "U:U2 PI: PART-1-1 N: 165777", "U:U2 PI: PART-1-1 N: 165778", "U:U2 PI: PART-1-1 N: 165779", "U:U2 PI: PART-1-1 N: 165784", "U:U2 PI: PART-1-1 N: 165785", "U:U2 PI: PART-1-1 N: 165786", "U:U2 PI: PART-1-1 N: 165787", "U:U2 PI: PART-1-1 N: 165788", "U:U2 PI: PART-1-1 N: 165789", "U:U2 PI: PART-1-1 N: 165790", "U:U2 PI: PART-1-1 N: 165816", "U:U2 PI: PART-1-1 N: 165817", "U:U2 PI: PART-1-1 N: 165818", "U:U2 PI: PART-1-1 N: 165819", "U:U2 PI: PART-1-1 N: 165820", "U:U2 PI: PART-1-1 N: 165821", "U:U2 PI: PART-1-1 N: 165822", "U:U2 PI: PART-1-1 N: 165823", "U:U2 PI: PART-1-1 N: 165824", "U:U2 PI: PART-1-1 N: 165825", "U:U2 PI: PART-1-1 N: 165826", "U:U2 PI: PART-1-1 N: 165827", "U:U2 PI: PART-1-1 N: 165828", "U:U2 PI: PART-1-1 N: 165829", "U:U2 PI: PART-1-1 N: 165830", "U:U2 PI: PART-1-1 N: 165831", "U:U2 PI: PART-1-1 N: 165832", "U:U2 PI: PART-1-1 N: 165833", "U:U2 PI: PART-1-1 N: 165834" ) )')
tmpName = xy40.name
session.xyDataObjects.changeKey(tmpName, 'Disp')
odb = session.odbs['G0_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Max. Principal'), (
    INVARIANT, 'Mid. Principal'), (INVARIANT, 'Min. Principal'), )), ('SDV1', 
    INTEGRATION_POINT), ('SDV16', INTEGRATION_POINT), ('SDV17', 
    INTEGRATION_POINT), ('SDV18', INTEGRATION_POINT), ('SDV20', 
    INTEGRATION_POINT), ('SDV22', INTEGRATION_POINT), ('TRIAX', 
    INTEGRATION_POINT), ), elementSets=("CR-2", ))
x0 = session.xyDataObjects['Disp']
x1 = session.xyDataObjects['Force']
session.writeXYReport(fileName='G0_P_FD.rpt', xyData=(x0, x1))
x0 = session.xyDataObjects['S:Max Principal PI: PART-1-1 E: 100241 IP: 1']
x1 = session.xyDataObjects['S:Mid Principal PI: PART-1-1 E: 100241 IP: 1']
x2 = session.xyDataObjects['S:Min Principal PI: PART-1-1 E: 100241 IP: 1']
x3 = session.xyDataObjects['SDV1 PI: PART-1-1 E: 100241 IP: 1']
x4 = session.xyDataObjects['SDV16 PI: PART-1-1 E: 100241 IP: 1']
x5 = session.xyDataObjects['SDV17 PI: PART-1-1 E: 100241 IP: 1']
x6 = session.xyDataObjects['SDV18 PI: PART-1-1 E: 100241 IP: 1']
x7 = session.xyDataObjects['SDV20 PI: PART-1-1 E: 100241 IP: 1']
x8 = session.xyDataObjects['SDV22 PI: PART-1-1 E: 100241 IP: 1']
x9 = session.xyDataObjects['TRIAX PI: PART-1-1 E: 100241 IP: 1']
session.writeXYReport(fileName='G0_P_LS_Cr2.rpt', xyData=(x0, x1, x2, x3, x4, 
    x5, x6, x7, x8, x9))
