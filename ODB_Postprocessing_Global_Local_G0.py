# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-20.57.30 176069
# Run by liz11 on Wed Oct 19 11:18:17 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
#: Warning: Permission was denied for "abaqus.rpy"; "abaqus.rpy.4" will be used for this session's replay file.
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=410.437469482422, 
    height=256.899993896484)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
import os
os.chdir(r"W:\Zinan\Post\eMBW\Fine_IJP_EP")
o1 = session.openOdb(name='W:/Zinan/Post/eMBW/Fine_IJP_EP/G0_P100_erald.odb', 
    readOnly=False)
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: W:/Zinan/Post/eMBW/Fine_IJP_EP/G0_P100_erald.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       7
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.0701, 
    farPlane=84.7195, width=45.668, height=29.5585, viewOffsetX=-1.33364, 
    viewOffsetY=-0.261936)
odb = session.odbs['W:/Zinan/Post/eMBW/Fine_IJP_EP/G0_P100_erald.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodeSets=("FORCE_DISP", ))
xy1 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21421']
xy2 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21422']
xy3 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21423']
xy4 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21426']
xy5 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21427']
xy6 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21428']
xy7 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21431']
xy8 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21432']
xy9 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21436']
xy10 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21437']
xy11 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21439']
xy12 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21440']
xy13 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21444']
xy14 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21445']
xy15 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21446']
xy16 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21449']
xy17 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21452']
xy18 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21455']
xy19 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21457']
xy20 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21458']
xy21 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21459']
xy22 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21460']
xy23 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21461']
xy24 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21465']
xy25 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21469']
xy26 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21470']
xy27 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21515']
xy28 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21516']
xy29 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21517']
xy30 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21518']
xy31 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21519']
xy32 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21520']
xy33 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21521']
xy34 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21522']
xy35 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21523']
xy36 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21524']
xy37 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21525']
xy38 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21526']
xy39 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21527']
xy40 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21528']
xy41 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21529']
xy42 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21530']
xy43 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21531']
xy44 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21532']
xy45 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21533']
xy46 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21534']
xy47 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21535']
xy48 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21536']
xy49 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21537']
xy50 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21538']
xy51 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21539']
xy52 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21540']
xy53 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21541']
xy54 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21542']
xy55 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21543']
xy56 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21544']
xy57 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21545']
xy58 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21546']
xy59 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21547']
xy60 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21548']
xy61 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21549']
xy62 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21550']
xy63 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21551']
xy64 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21552']
xy65 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21553']
xy66 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21587']
xy67 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21589']
xy68 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21590']
xy69 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21591']
xy70 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21594']
xy71 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21596']
xy72 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21597']
xy73 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21598']
xy74 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21600']
xy75 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 21601']
xy76 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75))*2/1000
xy76.setValues(
    sourceDescription='sum ( ( "RF:RF2 PI: PART-1-1 N: 21421", "RF:RF2 PI: PART-1-1 N: 21422", "RF:RF2 PI: PART-1-1 N: 21423", "RF:RF2 PI: PART-1-1 N: 21426", "RF:RF2 PI: PART-1-1 N: 21427", "RF:RF2 PI: PART-1-1 N: 21428", "RF:RF2 PI: PART-1-1 N: 21431", "RF:RF2 PI: PART-1-1 N: 21432", "RF:RF2 PI: PART-1-1 N: 21436", "RF:RF2 PI: PART-1-1 N: 21437", "RF:RF2 PI: PART-1-1 N: 21439", "RF:RF2 PI: PART-1-1 N: 21440", "RF:RF2 PI: PART-1-1 N: 21444", "RF:RF2 PI: PART-1-1 N: 21445", "RF:RF2 PI: PART-1-1 N: 21446", "RF:RF2 PI: PART-1-1 N: 21449", "RF:RF2 PI: PART-1-1 N: 21452", "RF:RF2 PI: PART-1-1 N: 21455", "RF:RF2 PI: PART-1-1 N: 21457", "RF:RF2 PI: PART-1-1 N: 21458", "RF:RF2 PI: PART-1-1 N: 21459", "RF:RF2 PI: PART-1-1 N: 21460", "RF:RF2 PI: PART-1-1 N: 21461", "RF:RF2 PI: PART-1-1 N: 21465", "RF:RF2 PI: PART-1-1 N: 21469", "RF:RF2 PI: PART-1-1 N: 21470", "RF:RF2 PI: PART-1-1 N: 21515", "RF:RF2 PI: PART-1-1 N: 21516", "RF:RF2 PI: PART-1-1 N: 21517", "RF:RF2 PI: PART-1-1 N: 21518", "RF:RF2 PI: PART-1-1 N: 21519", "RF:RF2 PI: PART-1-1 N: 21520", "RF:RF2 PI: PART-1-1 N: 21521", "RF:RF2 PI: PART-1-1 N: 21522", "RF:RF2 PI: PART-1-1 N: 21523", "RF:RF2 PI: PART-1-1 N: 21524", "RF:RF2 PI: PART-1-1 N: 21525", "RF:RF2 PI: PART-1-1 N: 21526", "RF:RF2 PI: PART-1-1 N: 21527", "RF:RF2 PI: PART-1-1 N: 21528", "RF:RF2 PI: PART-1-1 N: 21529", "RF:RF2 PI: PART-1-1 N: 21530", "RF:RF2 PI: PART-1-1 N: 21531", "RF:RF2 PI: PART-1-1 N: 21532", "RF:RF2 PI: PART-1-1 N: 21533", "RF:RF2 PI: PART-1-1 N: 21534", "RF:RF2 PI: PART-1-1 N: 21535", "RF:RF2 PI: PART-1-1 N: 21536", "RF:RF2 PI: PART-1-1 N: 21537", "RF:RF2 PI: PART-1-1 N: 21538", "RF:RF2 PI: PART-1-1 N: 21539", "RF:RF2 PI: PART-1-1 N: 21540", "RF:RF2 PI: PART-1-1 N: 21541", "RF:RF2 PI: PART-1-1 N: 21542", "RF:RF2 PI: PART-1-1 N: 21543", "RF:RF2 PI: PART-1-1 N: 21544", "RF:RF2 PI: PART-1-1 N: 21545", "RF:RF2 PI: PART-1-1 N: 21546", "RF:RF2 PI: PART-1-1 N: 21547", "RF:RF2 PI: PART-1-1 N: 21548", "RF:RF2 PI: PART-1-1 N: 21549", "RF:RF2 PI: PART-1-1 N: 21550", "RF:RF2 PI: PART-1-1 N: 21551", "RF:RF2 PI: PART-1-1 N: 21552", "RF:RF2 PI: PART-1-1 N: 21553", "RF:RF2 PI: PART-1-1 N: 21587", "RF:RF2 PI: PART-1-1 N: 21589", "RF:RF2 PI: PART-1-1 N: 21590", "RF:RF2 PI: PART-1-1 N: 21591", "RF:RF2 PI: PART-1-1 N: 21594", "RF:RF2 PI: PART-1-1 N: 21596", "RF:RF2 PI: PART-1-1 N: 21597", "RF:RF2 PI: PART-1-1 N: 21598", "RF:RF2 PI: PART-1-1 N: 21600", "RF:RF2 PI: PART-1-1 N: 21601" ) )*2/1000')
tmpName = xy76.name
session.xyDataObjects.changeKey(tmpName, 'Force')
xy1 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21421']
xy2 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21422']
xy3 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21423']
xy4 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21426']
xy5 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21427']
xy6 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21428']
xy7 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21431']
xy8 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21432']
xy9 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21436']
xy10 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21437']
xy11 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21439']
xy12 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21440']
xy13 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21444']
xy14 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21445']
xy15 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21446']
xy16 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21449']
xy17 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21452']
xy18 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21455']
xy19 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21457']
xy20 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21458']
xy21 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21459']
xy22 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21460']
xy23 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21461']
xy24 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21465']
xy25 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21469']
xy26 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21470']
xy27 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21515']
xy28 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21516']
xy29 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21517']
xy30 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21518']
xy31 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21519']
xy32 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21520']
xy33 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21521']
xy34 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21522']
xy35 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21523']
xy36 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21524']
xy37 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21525']
xy38 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21526']
xy39 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21527']
xy40 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21528']
xy41 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21529']
xy42 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21530']
xy43 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21531']
xy44 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21532']
xy45 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21533']
xy46 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21534']
xy47 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21535']
xy48 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21536']
xy49 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21537']
xy50 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21538']
xy51 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21539']
xy52 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21540']
xy53 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21541']
xy54 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21542']
xy55 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21543']
xy56 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21544']
xy57 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21545']
xy58 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21546']
xy59 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21547']
xy60 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21548']
xy61 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21549']
xy62 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21550']
xy63 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21551']
xy64 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21552']
xy65 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21553']
xy66 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21587']
xy67 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21589']
xy68 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21590']
xy69 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21591']
xy70 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21594']
xy71 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21596']
xy72 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21597']
xy73 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21598']
xy74 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21600']
xy75 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 21601']
xy76 = avg((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75))
xy76.setValues(
    sourceDescription='avg ( ( "U:U2 PI: PART-1-1 N: 21421", "U:U2 PI: PART-1-1 N: 21422", "U:U2 PI: PART-1-1 N: 21423", "U:U2 PI: PART-1-1 N: 21426", "U:U2 PI: PART-1-1 N: 21427", "U:U2 PI: PART-1-1 N: 21428", "U:U2 PI: PART-1-1 N: 21431", "U:U2 PI: PART-1-1 N: 21432", "U:U2 PI: PART-1-1 N: 21436", "U:U2 PI: PART-1-1 N: 21437", "U:U2 PI: PART-1-1 N: 21439", "U:U2 PI: PART-1-1 N: 21440", "U:U2 PI: PART-1-1 N: 21444", "U:U2 PI: PART-1-1 N: 21445", "U:U2 PI: PART-1-1 N: 21446", "U:U2 PI: PART-1-1 N: 21449", "U:U2 PI: PART-1-1 N: 21452", "U:U2 PI: PART-1-1 N: 21455", "U:U2 PI: PART-1-1 N: 21457", "U:U2 PI: PART-1-1 N: 21458", "U:U2 PI: PART-1-1 N: 21459", "U:U2 PI: PART-1-1 N: 21460", "U:U2 PI: PART-1-1 N: 21461", "U:U2 PI: PART-1-1 N: 21465", "U:U2 PI: PART-1-1 N: 21469", "U:U2 PI: PART-1-1 N: 21470", "U:U2 PI: PART-1-1 N: 21515", "U:U2 PI: PART-1-1 N: 21516", "U:U2 PI: PART-1-1 N: 21517", "U:U2 PI: PART-1-1 N: 21518", "U:U2 PI: PART-1-1 N: 21519", "U:U2 PI: PART-1-1 N: 21520", "U:U2 PI: PART-1-1 N: 21521", "U:U2 PI: PART-1-1 N: 21522", "U:U2 PI: PART-1-1 N: 21523", "U:U2 PI: PART-1-1 N: 21524", "U:U2 PI: PART-1-1 N: 21525", "U:U2 PI: PART-1-1 N: 21526", "U:U2 PI: PART-1-1 N: 21527", "U:U2 PI: PART-1-1 N: 21528", "U:U2 PI: PART-1-1 N: 21529", "U:U2 PI: PART-1-1 N: 21530", "U:U2 PI: PART-1-1 N: 21531", "U:U2 PI: PART-1-1 N: 21532", "U:U2 PI: PART-1-1 N: 21533", "U:U2 PI: PART-1-1 N: 21534", "U:U2 PI: PART-1-1 N: 21535", "U:U2 PI: PART-1-1 N: 21536", "U:U2 PI: PART-1-1 N: 21537", "U:U2 PI: PART-1-1 N: 21538", "U:U2 PI: PART-1-1 N: 21539", "U:U2 PI: PART-1-1 N: 21540", "U:U2 PI: PART-1-1 N: 21541", "U:U2 PI: PART-1-1 N: 21542", "U:U2 PI: PART-1-1 N: 21543", "U:U2 PI: PART-1-1 N: 21544", "U:U2 PI: PART-1-1 N: 21545", "U:U2 PI: PART-1-1 N: 21546", "U:U2 PI: PART-1-1 N: 21547", "U:U2 PI: PART-1-1 N: 21548", "U:U2 PI: PART-1-1 N: 21549", "U:U2 PI: PART-1-1 N: 21550", "U:U2 PI: PART-1-1 N: 21551", "U:U2 PI: PART-1-1 N: 21552", "U:U2 PI: PART-1-1 N: 21553", "U:U2 PI: PART-1-1 N: 21587", "U:U2 PI: PART-1-1 N: 21589", "U:U2 PI: PART-1-1 N: 21590", "U:U2 PI: PART-1-1 N: 21591", "U:U2 PI: PART-1-1 N: 21594", "U:U2 PI: PART-1-1 N: 21596", "U:U2 PI: PART-1-1 N: 21597", "U:U2 PI: PART-1-1 N: 21598", "U:U2 PI: PART-1-1 N: 21600", "U:U2 PI: PART-1-1 N: 21601" ) )')
tmpName = xy76.name
session.xyDataObjects.changeKey(tmpName, 'Disp')
x0 = session.xyDataObjects['Disp']
x1 = session.xyDataObjects['Force']
session.writeXYReport(fileName='W:/Zinan/Post/eMBW/Fine_IJP_EP/G0_FD.rpt', 
    xyData=(x0, x1))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.2684, 
    farPlane=70.9974, width=10.0419, height=6.32249, viewOffsetX=0.304584, 
    viewOffsetY=-0.232315)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PEEQ', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TRIAX', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PEEQ', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TRIAX', outputPosition=INTEGRATION_POINT, )
odb = session.odbs['W:/Zinan/Post/eMBW/Fine_IJP_EP/G0_P100_erald.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('PEEQ', INTEGRATION_POINT), ('S', INTEGRATION_POINT, ((
    INVARIANT, 'Max. Principal'), (INVARIANT, 'Mid. Principal'), (INVARIANT, 
    'Min. Principal'), )), ('TRIAX', INTEGRATION_POINT), ), elementSets=(
    "CR-ELE_2", ))
x0 = session.xyDataObjects['PEEQ PI: PART-1-1 E: 26597 IP: 1']
x1 = session.xyDataObjects['S:Max Principal PI: PART-1-1 E: 26597 IP: 1']
x2 = session.xyDataObjects['S:Mid Principal PI: PART-1-1 E: 26597 IP: 1']
x3 = session.xyDataObjects['S:Min Principal PI: PART-1-1 E: 26597 IP: 1']
x4 = session.xyDataObjects['TRIAX PI: PART-1-1 E: 26597 IP: 1']
session.writeXYReport(fileName='W:/Zinan/Post/eMBW/Fine_IJP_EP/G0_LS_Cr2.rpt', 
    xyData=(x0, x1, x2, x3, x4))
