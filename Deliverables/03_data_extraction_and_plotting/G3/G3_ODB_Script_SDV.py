# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022.HF5 replay file
# Internal Version: 2022_09_26-18.03.59 176852
# Run by giridhs1 on Wed Nov  2 10:33:43 2022
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
o2 = session.openOdb(name='G3_Damage_P.odb')
#: Model: Z:/Project/odb test/Plasticity/G3/G3_P.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['G3_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodeSets=("FORCE_DISP", ))
xy1 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117047']
xy2 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117048']
xy3 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117049']
xy4 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117050']
xy5 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117051']
xy6 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117052']
xy7 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117053']
xy8 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117054']
xy9 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117055']
xy10 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117056']
xy11 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117057']
xy12 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117058']
xy13 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117059']
xy14 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117060']
xy15 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117061']
xy16 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117062']
xy17 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117063']
xy18 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117064']
xy19 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117065']
xy20 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117066']
xy21 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117067']
xy22 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117068']
xy23 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117069']
xy24 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117070']
xy25 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117224']
xy26 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117263']
xy27 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117283']
xy28 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117284']
xy29 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117285']
xy30 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117286']
xy31 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117287']
xy32 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117288']
xy33 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117289']
xy34 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117290']
xy35 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117291']
xy36 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117292']
xy37 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117293']
xy38 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117294']
xy39 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117295']
xy40 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117296']
xy41 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117297']
xy42 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117298']
xy43 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117299']
xy44 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117300']
xy45 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117301']
xy46 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117302']
xy47 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117303']
xy48 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117304']
xy49 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117305']
xy50 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117306']
xy51 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117307']
xy52 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117308']
xy53 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117309']
xy54 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117310']
xy55 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117311']
xy56 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117312']
xy57 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117313']
xy58 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117314']
xy59 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117315']
xy60 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117316']
xy61 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117317']
xy62 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117318']
xy63 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117319']
xy64 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117320']
xy65 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117321']
xy66 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117322']
xy67 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117323']
xy68 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117324']
xy69 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117325']
xy70 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117326']
xy71 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117327']
xy72 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117328']
xy73 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117329']
xy74 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117330']
xy75 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117347']
xy76 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117348']
xy77 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117349']
xy78 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 117350']
xy79 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75, xy76, xy77, xy78))*2/1000
xy79.setValues(
    sourceDescription='sum ( ( "RF:RF2 PI: PART-1-1 N: 117047", "RF:RF2 PI: PART-1-1 N: 117048", "RF:RF2 PI: PART-1-1 N: 117049", "RF:RF2 PI: PART-1-1 N: 117050", "RF:RF2 PI: PART-1-1 N: 117051", "RF:RF2 PI: PART-1-1 N: 117052", "RF:RF2 PI: PART-1-1 N: 117053", "RF:RF2 PI: PART-1-1 N: 117054", "RF:RF2 PI: PART-1-1 N: 117055", "RF:RF2 PI: PART-1-1 N: 117056", "RF:RF2 PI: PART-1-1 N: 117057", "RF:RF2 PI: PART-1-1 N: 117058", "RF:RF2 PI: PART-1-1 N: 117059", "RF:RF2 PI: PART-1-1 N: 117060", "RF:RF2 PI: PART-1-1 N: 117061", "RF:RF2 PI: PART-1-1 N: 117062", "RF:RF2 PI: PART-1-1 N: 117063", "RF:RF2 PI: PART-1-1 N: 117064", "RF:RF2 PI: PART-1-1 N: 117065", "RF:RF2 PI: PART-1-1 N: 117066", "RF:RF2 PI: PART-1-1 N: 117067", "RF:RF2 PI: PART-1-1 N: 117068", "RF:RF2 PI: PART-1-1 N: 117069", "RF:RF2 PI: PART-1-1 N: 117070", "RF:RF2 PI: PART-1-1 N: 117224", "RF:RF2 PI: PART-1-1 N: 117263", "RF:RF2 PI: PART-1-1 N: 117283", "RF:RF2 PI: PART-1-1 N: 117284", "RF:RF2 PI: PART-1-1 N: 117285", "RF:RF2 PI: PART-1-1 N: 117286", "RF:RF2 PI: PART-1-1 N: 117287", "RF:RF2 PI: PART-1-1 N: 117288", "RF:RF2 PI: PART-1-1 N: 117289", "RF:RF2 PI: PART-1-1 N: 117290", "RF:RF2 PI: PART-1-1 N: 117291", "RF:RF2 PI: PART-1-1 N: 117292", "RF:RF2 PI: PART-1-1 N: 117293", "RF:RF2 PI: PART-1-1 N: 117294", "RF:RF2 PI: PART-1-1 N: 117295", "RF:RF2 PI: PART-1-1 N: 117296", "RF:RF2 PI: PART-1-1 N: 117297", "RF:RF2 PI: PART-1-1 N: 117298", "RF:RF2 PI: PART-1-1 N: 117299", "RF:RF2 PI: PART-1-1 N: 117300", "RF:RF2 PI: PART-1-1 N: 117301", "RF:RF2 PI: PART-1-1 N: 117302", "RF:RF2 PI: PART-1-1 N: 117303", "RF:RF2 PI: PART-1-1 N: 117304", "RF:RF2 PI: PART-1-1 N: 117305", "RF:RF2 PI: PART-1-1 N: 117306", "RF:RF2 PI: PART-1-1 N: 117307", "RF:RF2 PI: PART-1-1 N: 117308", "RF:RF2 PI: PART-1-1 N: 117309", "RF:RF2 PI: PART-1-1 N: 117310", "RF:RF2 PI: PART-1-1 N: 117311", "RF:RF2 PI: PART-1-1 N: 117312", "RF:RF2 PI: PART-1-1 N: 117313", "RF:RF2 PI: PART-1-1 N: 117314", "RF:RF2 PI: PART-1-1 N: 117315", "RF:RF2 PI: PART-1-1 N: 117316", "RF:RF2 PI: PART-1-1 N: 117317", "RF:RF2 PI: PART-1-1 N: 117318", "RF:RF2 PI: PART-1-1 N: 117319", "RF:RF2 PI: PART-1-1 N: 117320", "RF:RF2 PI: PART-1-1 N: 117321", "RF:RF2 PI: PART-1-1 N: 117322", "RF:RF2 PI: PART-1-1 N: 117323", "RF:RF2 PI: PART-1-1 N: 117324", "RF:RF2 PI: PART-1-1 N: 117325", "RF:RF2 PI: PART-1-1 N: 117326", "RF:RF2 PI: PART-1-1 N: 117327", "RF:RF2 PI: PART-1-1 N: 117328", "RF:RF2 PI: PART-1-1 N: 117329", "RF:RF2 PI: PART-1-1 N: 117330", "RF:RF2 PI: PART-1-1 N: 117347", "RF:RF2 PI: PART-1-1 N: 117348", "RF:RF2 PI: PART-1-1 N: 117349", "RF:RF2 PI: PART-1-1 N: 117350" ) )*2/1000')
tmpName = xy79.name
session.xyDataObjects.changeKey(tmpName, 'Force')
xy1 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117047']
xy2 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117048']
xy3 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117049']
xy4 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117050']
xy5 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117051']
xy6 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117052']
xy7 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117053']
xy8 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117054']
xy9 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117055']
xy10 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117056']
xy11 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117057']
xy12 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117058']
xy13 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117059']
xy14 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117060']
xy15 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117061']
xy16 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117062']
xy17 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117063']
xy18 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117064']
xy19 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117065']
xy20 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117066']
xy21 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117067']
xy22 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117068']
xy23 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117069']
xy24 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117070']
xy25 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117224']
xy26 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117263']
xy27 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117283']
xy28 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117284']
xy29 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117285']
xy30 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117286']
xy31 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117287']
xy32 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117288']
xy33 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117289']
xy34 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117290']
xy35 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117291']
xy36 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117292']
xy37 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117293']
xy38 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117294']
xy39 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117295']
xy40 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117296']
xy41 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117297']
xy42 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117298']
xy43 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117299']
xy44 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117300']
xy45 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117301']
xy46 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117302']
xy47 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117303']
xy48 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117304']
xy49 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117305']
xy50 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117306']
xy51 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117307']
xy52 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117308']
xy53 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117309']
xy54 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117310']
xy55 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117311']
xy56 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117312']
xy57 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117313']
xy58 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117314']
xy59 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117315']
xy60 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117316']
xy61 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117317']
xy62 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117318']
xy63 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117319']
xy64 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117320']
xy65 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117321']
xy66 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117322']
xy67 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117323']
xy68 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117324']
xy69 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117325']
xy70 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117326']
xy71 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117327']
xy72 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117328']
xy73 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117329']
xy74 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117330']
xy75 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117347']
xy76 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117348']
xy77 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117349']
xy78 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 117350']
xy79 = avg((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75, xy76, xy77, xy78))
xy79.setValues(
    sourceDescription='avg ( ( "U:U2 PI: PART-1-1 N: 117047", "U:U2 PI: PART-1-1 N: 117048", "U:U2 PI: PART-1-1 N: 117049", "U:U2 PI: PART-1-1 N: 117050", "U:U2 PI: PART-1-1 N: 117051", "U:U2 PI: PART-1-1 N: 117052", "U:U2 PI: PART-1-1 N: 117053", "U:U2 PI: PART-1-1 N: 117054", "U:U2 PI: PART-1-1 N: 117055", "U:U2 PI: PART-1-1 N: 117056", "U:U2 PI: PART-1-1 N: 117057", "U:U2 PI: PART-1-1 N: 117058", "U:U2 PI: PART-1-1 N: 117059", "U:U2 PI: PART-1-1 N: 117060", "U:U2 PI: PART-1-1 N: 117061", "U:U2 PI: PART-1-1 N: 117062", "U:U2 PI: PART-1-1 N: 117063", "U:U2 PI: PART-1-1 N: 117064", "U:U2 PI: PART-1-1 N: 117065", "U:U2 PI: PART-1-1 N: 117066", "U:U2 PI: PART-1-1 N: 117067", "U:U2 PI: PART-1-1 N: 117068", "U:U2 PI: PART-1-1 N: 117069", "U:U2 PI: PART-1-1 N: 117070", "U:U2 PI: PART-1-1 N: 117224", "U:U2 PI: PART-1-1 N: 117263", "U:U2 PI: PART-1-1 N: 117283", "U:U2 PI: PART-1-1 N: 117284", "U:U2 PI: PART-1-1 N: 117285", "U:U2 PI: PART-1-1 N: 117286", "U:U2 PI: PART-1-1 N: 117287", "U:U2 PI: PART-1-1 N: 117288", "U:U2 PI: PART-1-1 N: 117289", "U:U2 PI: PART-1-1 N: 117290", "U:U2 PI: PART-1-1 N: 117291", "U:U2 PI: PART-1-1 N: 117292", "U:U2 PI: PART-1-1 N: 117293", "U:U2 PI: PART-1-1 N: 117294", "U:U2 PI: PART-1-1 N: 117295", "U:U2 PI: PART-1-1 N: 117296", "U:U2 PI: PART-1-1 N: 117297", "U:U2 PI: PART-1-1 N: 117298", "U:U2 PI: PART-1-1 N: 117299", "U:U2 PI: PART-1-1 N: 117300", "U:U2 PI: PART-1-1 N: 117301", "U:U2 PI: PART-1-1 N: 117302", "U:U2 PI: PART-1-1 N: 117303", "U:U2 PI: PART-1-1 N: 117304", "U:U2 PI: PART-1-1 N: 117305", "U:U2 PI: PART-1-1 N: 117306", "U:U2 PI: PART-1-1 N: 117307", "U:U2 PI: PART-1-1 N: 117308", "U:U2 PI: PART-1-1 N: 117309", "U:U2 PI: PART-1-1 N: 117310", "U:U2 PI: PART-1-1 N: 117311", "U:U2 PI: PART-1-1 N: 117312", "U:U2 PI: PART-1-1 N: 117313", "U:U2 PI: PART-1-1 N: 117314", "U:U2 PI: PART-1-1 N: 117315", "U:U2 PI: PART-1-1 N: 117316", "U:U2 PI: PART-1-1 N: 117317", "U:U2 PI: PART-1-1 N: 117318", "U:U2 PI: PART-1-1 N: 117319", "U:U2 PI: PART-1-1 N: 117320", "U:U2 PI: PART-1-1 N: 117321", "U:U2 PI: PART-1-1 N: 117322", "U:U2 PI: PART-1-1 N: 117323", "U:U2 PI: PART-1-1 N: 117324", "U:U2 PI: PART-1-1 N: 117325", "U:U2 PI: PART-1-1 N: 117326", "U:U2 PI: PART-1-1 N: 117327", "U:U2 PI: PART-1-1 N: 117328", "U:U2 PI: PART-1-1 N: 117329", "U:U2 PI: PART-1-1 N: 117330", "U:U2 PI: PART-1-1 N: 117347", "U:U2 PI: PART-1-1 N: 117348", "U:U2 PI: PART-1-1 N: 117349", "U:U2 PI: PART-1-1 N: 117350" ) )')
tmpName = xy79.name
session.xyDataObjects.changeKey(tmpName, 'Disp')
x0 = session.xyDataObjects['Disp']
x1 = session.xyDataObjects['Force']
session.writeXYReport(fileName='G3_P_FD.rpt', xyData=(x0, x1))
odb = session.odbs['G3_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Max. Principal'), (
    INVARIANT, 'Mid. Principal'), (INVARIANT, 'Min. Principal'), )), ('SDV1', 
    INTEGRATION_POINT), ('SDV16', INTEGRATION_POINT), ('SDV17', INTEGRATION_POINT), ('SDV18', INTEGRATION_POINT), ('SDV20', INTEGRATION_POINT), ('SDV22', INTEGRATION_POINT),('TRIAX', INTEGRATION_POINT), ), elementSets=("CR-2", 
    ))
x0 = session.xyDataObjects['S:Max Principal PI: PART-1-1 E: 267 IP: 1']
x1 = session.xyDataObjects['S:Mid Principal PI: PART-1-1 E: 267 IP: 1']
x2 = session.xyDataObjects['S:Min Principal PI: PART-1-1 E: 267 IP: 1']
x3 = session.xyDataObjects['SDV1 PI: PART-1-1 E: 267 IP: 1']
x4 = session.xyDataObjects['SDV16 PI: PART-1-1 E: 267 IP: 1']
x5 = session.xyDataObjects['SDV17 PI: PART-1-1 E: 267 IP: 1']
x6 = session.xyDataObjects['SDV18 PI: PART-1-1 E: 267 IP: 1']
x7 = session.xyDataObjects['SDV20 PI: PART-1-1 E: 267 IP: 1']
x8 = session.xyDataObjects['SDV22 PI: PART-1-1 E: 267 IP: 1']
x9 = session.xyDataObjects['TRIAX PI: PART-1-1 E: 267 IP: 1']
session.writeXYReport(fileName='G3_P_LS_Cr2.rpt', xyData=(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9))