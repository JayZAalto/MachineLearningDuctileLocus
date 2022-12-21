# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022.HF5 replay file
# Internal Version: 2022_09_26-18.03.59 176852
# Run by giridhs1 on Sat Nov 26 00:20:47 2022
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
o2 = session.openOdb(name='G1_Damage_P.odb')
#: Model: Z:/Project/odb test/G1/G1_Damage_P.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['G1_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodeSets=("FORCE_DISP", ))
xy1 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172079']
xy2 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172093']
xy3 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172094']
xy4 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172095']
xy5 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172096']
xy6 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172097']
xy7 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172098']
xy8 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172099']
xy9 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172100']
xy10 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172101']
xy11 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172102']
xy12 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172103']
xy13 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172104']
xy14 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172105']
xy15 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172106']
xy16 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172107']
xy17 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172108']
xy18 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172109']
xy19 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172110']
xy20 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172111']
xy21 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172112']
xy22 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172113']
xy23 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172114']
xy24 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172115']
xy25 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172116']
xy26 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172796']
xy27 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172797']
xy28 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172798']
xy29 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172799']
xy30 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172800']
xy31 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172801']
xy32 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172802']
xy33 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172803']
xy34 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172804']
xy35 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172805']
xy36 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172806']
xy37 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172807']
xy38 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172808']
xy39 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172809']
xy40 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172810']
xy41 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172811']
xy42 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172812']
xy43 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172813']
xy44 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172814']
xy45 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172815']
xy46 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172816']
xy47 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172817']
xy48 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172818']
xy49 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 172819']
xy50 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173234']
xy51 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173242']
xy52 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173243']
xy53 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173245']
xy54 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173263']
xy55 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173341']
xy56 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173343']
xy57 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173344']
xy58 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173346']
xy59 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173351']
xy60 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173352']
xy61 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173353']
xy62 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173364']
xy63 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173372']
xy64 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173375']
xy65 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173376']
xy66 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173377']
xy67 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173400']
xy68 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173406']
xy69 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173427']
xy70 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173430']
xy71 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173433']
xy72 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173439']
xy73 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173440']
xy74 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173441']
xy75 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173443']
xy76 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173454']
xy77 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173458']
xy78 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 173459']
xy79 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75, xy76, xy77, xy78))*2/1000
xy79.setValues(
    sourceDescription='sum ( ( "RF:RF2 PI: PART-1-1 N: 172079", "RF:RF2 PI: PART-1-1 N: 172093", "RF:RF2 PI: PART-1-1 N: 172094", "RF:RF2 PI: PART-1-1 N: 172095", "RF:RF2 PI: PART-1-1 N: 172096", "RF:RF2 PI: PART-1-1 N: 172097", "RF:RF2 PI: PART-1-1 N: 172098", "RF:RF2 PI: PART-1-1 N: 172099", "RF:RF2 PI: PART-1-1 N: 172100", "RF:RF2 PI: PART-1-1 N: 172101", "RF:RF2 PI: PART-1-1 N: 172102", "RF:RF2 PI: PART-1-1 N: 172103", "RF:RF2 PI: PART-1-1 N: 172104", "RF:RF2 PI: PART-1-1 N: 172105", "RF:RF2 PI: PART-1-1 N: 172106", "RF:RF2 PI: PART-1-1 N: 172107", "RF:RF2 PI: PART-1-1 N: 172108", "RF:RF2 PI: PART-1-1 N: 172109", "RF:RF2 PI: PART-1-1 N: 172110", "RF:RF2 PI: PART-1-1 N: 172111", "RF:RF2 PI: PART-1-1 N: 172112", "RF:RF2 PI: PART-1-1 N: 172113", "RF:RF2 PI: PART-1-1 N: 172114", "RF:RF2 PI: PART-1-1 N: 172115", "RF:RF2 PI: PART-1-1 N: 172116", "RF:RF2 PI: PART-1-1 N: 172796", "RF:RF2 PI: PART-1-1 N: 172797", "RF:RF2 PI: PART-1-1 N: 172798", "RF:RF2 PI: PART-1-1 N: 172799", "RF:RF2 PI: PART-1-1 N: 172800", "RF:RF2 PI: PART-1-1 N: 172801", "RF:RF2 PI: PART-1-1 N: 172802", "RF:RF2 PI: PART-1-1 N: 172803", "RF:RF2 PI: PART-1-1 N: 172804", "RF:RF2 PI: PART-1-1 N: 172805", "RF:RF2 PI: PART-1-1 N: 172806", "RF:RF2 PI: PART-1-1 N: 172807", "RF:RF2 PI: PART-1-1 N: 172808", "RF:RF2 PI: PART-1-1 N: 172809", "RF:RF2 PI: PART-1-1 N: 172810", "RF:RF2 PI: PART-1-1 N: 172811", "RF:RF2 PI: PART-1-1 N: 172812", "RF:RF2 PI: PART-1-1 N: 172813", "RF:RF2 PI: PART-1-1 N: 172814", "RF:RF2 PI: PART-1-1 N: 172815", "RF:RF2 PI: PART-1-1 N: 172816", "RF:RF2 PI: PART-1-1 N: 172817", "RF:RF2 PI: PART-1-1 N: 172818", "RF:RF2 PI: PART-1-1 N: 172819", "RF:RF2 PI: PART-1-1 N: 173234", "RF:RF2 PI: PART-1-1 N: 173242", "RF:RF2 PI: PART-1-1 N: 173243", "RF:RF2 PI: PART-1-1 N: 173245", "RF:RF2 PI: PART-1-1 N: 173263", "RF:RF2 PI: PART-1-1 N: 173341", "RF:RF2 PI: PART-1-1 N: 173343", "RF:RF2 PI: PART-1-1 N: 173344", "RF:RF2 PI: PART-1-1 N: 173346", "RF:RF2 PI: PART-1-1 N: 173351", "RF:RF2 PI: PART-1-1 N: 173352", "RF:RF2 PI: PART-1-1 N: 173353", "RF:RF2 PI: PART-1-1 N: 173364", "RF:RF2 PI: PART-1-1 N: 173372", "RF:RF2 PI: PART-1-1 N: 173375", "RF:RF2 PI: PART-1-1 N: 173376", "RF:RF2 PI: PART-1-1 N: 173377", "RF:RF2 PI: PART-1-1 N: 173400", "RF:RF2 PI: PART-1-1 N: 173406", "RF:RF2 PI: PART-1-1 N: 173427", "RF:RF2 PI: PART-1-1 N: 173430", "RF:RF2 PI: PART-1-1 N: 173433", "RF:RF2 PI: PART-1-1 N: 173439", "RF:RF2 PI: PART-1-1 N: 173440", "RF:RF2 PI: PART-1-1 N: 173441", "RF:RF2 PI: PART-1-1 N: 173443", "RF:RF2 PI: PART-1-1 N: 173454", "RF:RF2 PI: PART-1-1 N: 173458", "RF:RF2 PI: PART-1-1 N: 173459" ) )*2/1000')
tmpName = xy79.name
session.xyDataObjects.changeKey(tmpName, 'Force')
xy1 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172079']
xy2 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172093']
xy3 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172094']
xy4 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172095']
xy5 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172096']
xy6 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172097']
xy7 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172098']
xy8 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172099']
xy9 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172100']
xy10 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172101']
xy11 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172102']
xy12 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172103']
xy13 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172104']
xy14 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172105']
xy15 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172106']
xy16 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172107']
xy17 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172108']
xy18 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172109']
xy19 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172110']
xy20 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172111']
xy21 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172112']
xy22 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172113']
xy23 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172114']
xy24 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172115']
xy25 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172116']
xy26 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172796']
xy27 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172797']
xy28 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172798']
xy29 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172799']
xy30 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172800']
xy31 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172801']
xy32 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172802']
xy33 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172803']
xy34 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172804']
xy35 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172805']
xy36 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172806']
xy37 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172807']
xy38 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172808']
xy39 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172809']
xy40 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172810']
xy41 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172811']
xy42 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172812']
xy43 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172813']
xy44 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172814']
xy45 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172815']
xy46 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172816']
xy47 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172817']
xy48 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172818']
xy49 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 172819']
xy50 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173234']
xy51 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173242']
xy52 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173243']
xy53 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173245']
xy54 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173263']
xy55 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173341']
xy56 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173343']
xy57 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173344']
xy58 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173346']
xy59 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173351']
xy60 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173352']
xy61 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173353']
xy62 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173364']
xy63 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173372']
xy64 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173375']
xy65 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173376']
xy66 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173377']
xy67 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173400']
xy68 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173406']
xy69 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173427']
xy70 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173430']
xy71 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173433']
xy72 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173439']
xy73 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173440']
xy74 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173441']
xy75 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173443']
xy76 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173454']
xy77 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173458']
xy78 = session.xyDataObjects['U:U2 PI: PART-1-1 N: 173459']
xy79 = avg((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75, xy76, xy77, xy78))
xy79.setValues(
    sourceDescription='avg ( ( "U:U2 PI: PART-1-1 N: 172079", "U:U2 PI: PART-1-1 N: 172093", "U:U2 PI: PART-1-1 N: 172094", "U:U2 PI: PART-1-1 N: 172095", "U:U2 PI: PART-1-1 N: 172096", "U:U2 PI: PART-1-1 N: 172097", "U:U2 PI: PART-1-1 N: 172098", "U:U2 PI: PART-1-1 N: 172099", "U:U2 PI: PART-1-1 N: 172100", "U:U2 PI: PART-1-1 N: 172101", "U:U2 PI: PART-1-1 N: 172102", "U:U2 PI: PART-1-1 N: 172103", "U:U2 PI: PART-1-1 N: 172104", "U:U2 PI: PART-1-1 N: 172105", "U:U2 PI: PART-1-1 N: 172106", "U:U2 PI: PART-1-1 N: 172107", "U:U2 PI: PART-1-1 N: 172108", "U:U2 PI: PART-1-1 N: 172109", "U:U2 PI: PART-1-1 N: 172110", "U:U2 PI: PART-1-1 N: 172111", "U:U2 PI: PART-1-1 N: 172112", "U:U2 PI: PART-1-1 N: 172113", "U:U2 PI: PART-1-1 N: 172114", "U:U2 PI: PART-1-1 N: 172115", "U:U2 PI: PART-1-1 N: 172116", "U:U2 PI: PART-1-1 N: 172796", "U:U2 PI: PART-1-1 N: 172797", "U:U2 PI: PART-1-1 N: 172798", "U:U2 PI: PART-1-1 N: 172799", "U:U2 PI: PART-1-1 N: 172800", "U:U2 PI: PART-1-1 N: 172801", "U:U2 PI: PART-1-1 N: 172802", "U:U2 PI: PART-1-1 N: 172803", "U:U2 PI: PART-1-1 N: 172804", "U:U2 PI: PART-1-1 N: 172805", "U:U2 PI: PART-1-1 N: 172806", "U:U2 PI: PART-1-1 N: 172807", "U:U2 PI: PART-1-1 N: 172808", "U:U2 PI: PART-1-1 N: 172809", "U:U2 PI: PART-1-1 N: 172810", "U:U2 PI: PART-1-1 N: 172811", "U:U2 PI: PART-1-1 N: 172812", "U:U2 PI: PART-1-1 N: 172813", "U:U2 PI: PART-1-1 N: 172814", "U:U2 PI: PART-1-1 N: 172815", "U:U2 PI: PART-1-1 N: 172816", "U:U2 PI: PART-1-1 N: 172817", "U:U2 PI: PART-1-1 N: 172818", "U:U2 PI: PART-1-1 N: 172819", "U:U2 PI: PART-1-1 N: 173234", "U:U2 PI: PART-1-1 N: 173242", "U:U2 PI: PART-1-1 N: 173243", "U:U2 PI: PART-1-1 N: 173245", "U:U2 PI: PART-1-1 N: 173263", "U:U2 PI: PART-1-1 N: 173341", "U:U2 PI: PART-1-1 N: 173343", "U:U2 PI: PART-1-1 N: 173344", "U:U2 PI: PART-1-1 N: 173346", "U:U2 PI: PART-1-1 N: 173351", "U:U2 PI: PART-1-1 N: 173352", "U:U2 PI: PART-1-1 N: 173353", "U:U2 PI: PART-1-1 N: 173364", "U:U2 PI: PART-1-1 N: 173372", "U:U2 PI: PART-1-1 N: 173375", "U:U2 PI: PART-1-1 N: 173376", "U:U2 PI: PART-1-1 N: 173377", "U:U2 PI: PART-1-1 N: 173400", "U:U2 PI: PART-1-1 N: 173406", "U:U2 PI: PART-1-1 N: 173427", "U:U2 PI: PART-1-1 N: 173430", "U:U2 PI: PART-1-1 N: 173433", "U:U2 PI: PART-1-1 N: 173439", "U:U2 PI: PART-1-1 N: 173440", "U:U2 PI: PART-1-1 N: 173441", "U:U2 PI: PART-1-1 N: 173443", "U:U2 PI: PART-1-1 N: 173454", "U:U2 PI: PART-1-1 N: 173458", "U:U2 PI: PART-1-1 N: 173459" ) )')
tmpName = xy79.name
session.xyDataObjects.changeKey(tmpName, 'Disp')
odb = session.odbs['G1_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Max. Principal'), (
    INVARIANT, 'Mid. Principal'), (INVARIANT, 'Min. Principal'), )), ('SDV1', 
    INTEGRATION_POINT), ('SDV16', INTEGRATION_POINT), ('SDV17', 
    INTEGRATION_POINT), ('SDV18', INTEGRATION_POINT), ('SDV20', 
    INTEGRATION_POINT), ('SDV22', INTEGRATION_POINT), ('TRIAX', 
    INTEGRATION_POINT), ), elementSets=("CR-2", ))
x0 = session.xyDataObjects['Disp']
x1 = session.xyDataObjects['Force']
session.writeXYReport(fileName='G1_P_FD.rpt', xyData=(x0, x1))
x0 = session.xyDataObjects['S:Max Principal PI: PART-1-1 E: 33600 IP: 1']
x1 = session.xyDataObjects['S:Mid Principal PI: PART-1-1 E: 33600 IP: 1']
x2 = session.xyDataObjects['S:Min Principal PI: PART-1-1 E: 33600 IP: 1']
x3 = session.xyDataObjects['SDV1 PI: PART-1-1 E: 33600 IP: 1']
x4 = session.xyDataObjects['SDV16 PI: PART-1-1 E: 33600 IP: 1']
x5 = session.xyDataObjects['SDV17 PI: PART-1-1 E: 33600 IP: 1']
x6 = session.xyDataObjects['SDV18 PI: PART-1-1 E: 33600 IP: 1']
x7 = session.xyDataObjects['SDV20 PI: PART-1-1 E: 33600 IP: 1']
x8 = session.xyDataObjects['SDV22 PI: PART-1-1 E: 33600 IP: 1']
x9 = session.xyDataObjects['TRIAX PI: PART-1-1 E: 33600 IP: 1']
session.writeXYReport(fileName='G1_P_LS_Cr2.rpt', xyData=(x0, x1, x2, x3, x4, 
    x5, x6, x7, x8, x9))
