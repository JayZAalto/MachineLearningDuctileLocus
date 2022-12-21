# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022.HF5 replay file
# Internal Version: 2022_09_26-18.03.59 176852
# Run by giridhs1 on Fri Dec  2 16:16:36 2022
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
o2 = session.openOdb(name='G4_Damage_P.odb')
#: Model: Z:/Project/odb test/G4/G4_Damage_P.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.683, 
    farPlane=90.3542, width=20.4146, height=9.16718, viewOffsetX=-0.5895, 
    viewOffsetY=-0.0198908)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.7988, 
    farPlane=89.2385, width=6.25264, height=2.80774, viewOffsetX=-0.708121, 
    viewOffsetY=-0.301389)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.8967, 
    farPlane=87.7787, width=6.36939, height=2.86017, cameraPosition=(60.814, 
    -35.1497, -50.2562), cameraUpVector=(-0.449388, 0.57735, 0.681702), 
    cameraTarget=(27.551, -77.8843, 0.202482), viewOffsetX=-0.721344, 
    viewOffsetY=-0.307017)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.8825, 
    farPlane=87.7929, width=6.03489, height=2.70996, viewOffsetX=-0.613315, 
    viewOffsetY=-0.224429)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.9161, 
    farPlane=87.7593, width=6.03827, height=2.71148, viewOffsetX=-0.54297, 
    viewOffsetY=-0.881996)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-0.409034, 
    viewOffsetY=-0.607133)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV1', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV20', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.6192, 
    farPlane=105.39, width=3.28732, height=1.47617, viewOffsetX=-0.180149, 
    viewOffsetY=0.0860308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.5579, 
    farPlane=105.452, width=4.20256, height=1.88716, viewOffsetX=-0.111273, 
    viewOffsetY=0.0634799)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV22', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV1', outputPosition=INTEGRATION_POINT, )
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=300)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=300)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.5104, 
    farPlane=105.499, width=4.76866, height=2.14137, viewOffsetX=-0.0269113, 
    viewOffsetY=0.123063)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.3091, 
    farPlane=109.044, width=6.49932, height=2.91852, cameraPosition=(13.5084, 
    -35.1497, -57.1604), cameraUpVector=(0.234221, 0.57735, 0.782181), 
    cameraTarget=(30.8452, -77.8843, 0.735525), viewOffsetX=-0.0366781, 
    viewOffsetY=0.167726)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.1572, 
    farPlane=109.196, width=6.47705, height=2.90852, viewOffsetX=2.18632, 
    viewOffsetY=0.222931)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(13.4743, 
    -35.2496, -57.2239), cameraUpVector=(0.263307, 0.576949, 0.773175), 
    cameraTarget=(30.8111, -77.9842, 0.671981))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.8678, 
    farPlane=104.436, width=6.58129, height=2.95532, cameraPosition=(14.2397, 
    -47.2714, -64.3962), cameraUpVector=(0.225324, 0.712513, 0.664496), 
    cameraTarget=(30.8849, -78.5258, 0.602657), viewOffsetX=2.2215, 
    viewOffsetY=0.226518)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0869, 
    farPlane=95.0012, width=7.05347, height=3.16735, cameraPosition=(16.184, 
    -68.2669, -70.8896), cameraUpVector=(0.162779, 0.883047, 0.440148), 
    cameraTarget=(30.9715, -78.8179, 0.865269), viewOffsetX=2.38088, 
    viewOffsetY=0.24277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0456, 
    farPlane=95.0426, width=7.04741, height=3.16463, viewOffsetX=2.30067, 
    viewOffsetY=0.858147)
session.viewports['Viewport: 1'].view.setValues(farPlane=95.0426, width=7.0474, 
    height=3.16463, viewOffsetX=2.1704, viewOffsetY=0.407294)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0831, 
    farPlane=95.0051, width=6.23194, height=2.79845, viewOffsetX=2.03072, 
    viewOffsetY=0.326031)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.1179, 
    farPlane=94.9702, width=6.23646, height=2.80048, viewOffsetX=2.35112, 
    viewOffsetY=0.801965)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.1175, 
    farPlane=94.9706, width=6.23641, height=2.80046, viewOffsetX=2.03601, 
    viewOffsetY=0.272557)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4367, 
    farPlane=94.6515, width=2.48156, height=1.11434, viewOffsetX=1.42712, 
    viewOffsetY=-0.0731508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4506, 
    farPlane=94.6375, width=2.48227, height=1.11466, viewOffsetX=1.37094, 
    viewOffsetY=-0.187692)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4506, 
    farPlane=94.6375, width=2.48227, height=1.11466, viewOffsetX=1.78695, 
    viewOffsetY=0.128383)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4762, 
    farPlane=94.612, width=2.06282, height=0.926309, viewOffsetX=1.7902, 
    viewOffsetY=0.131724)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=11.1235, minValue=0, showMaxLocation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4365, 
    farPlane=94.6516, width=2.80845, height=1.26113, viewOffsetX=1.83783, 
    viewOffsetY=0.173708)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.171, 
    farPlane=94.2095, width=2.56113, height=1.15007, cameraPosition=(14.5731, 
    -93.4523, -69.5642), cameraUpVector=(0.219563, 0.971445, 0.0899287), 
    cameraTarget=(30.9804, -78.2951, 1.00364), viewOffsetX=1.67598, 
    viewOffsetY=0.15841)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.3923, 
    farPlane=95.5606, width=2.57396, height=1.15584, cameraPosition=(34.1667, 
    -48.7172, -65.319), cameraUpVector=(-0.267726, 0.687095, 0.675443), 
    cameraTarget=(29.7244, -80.2325, 1.50772), viewOffsetX=1.68438, 
    viewOffsetY=0.159204)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.1185, 
    farPlane=86.65, width=8.75076, height=3.92952, viewOffsetX=0.39304, 
    viewOffsetY=-0.028595)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=156)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=153)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV16', outputPosition=INTEGRATION_POINT, )
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=84)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74.9688, 
    farPlane=78.1802, width=14.973, height=6.72361, viewOffsetX=0.869934, 
    viewOffsetY=-0.0806074)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=44)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=117)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV17', outputPosition=INTEGRATION_POINT, )
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=221)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=155)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV18', outputPosition=INTEGRATION_POINT, )
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=174)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV16', outputPosition=INTEGRATION_POINT, )
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=161)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=160)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=128)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=115)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=167)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=166)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=165)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=164)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=163)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=162)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=159)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=156)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=155)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=154)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.3326, 
    farPlane=92.0176, width=12.4493, height=5.59034, cameraPosition=(13.3937, 
    -21.6707, -50.5028), cameraUpVector=(-0.306011, 0.600413, 0.738824), 
    cameraTarget=(28.5949, -76.7659, 0.566948), viewOffsetX=0.723305, 
    viewOffsetY=-0.0670209)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.8283, 
    farPlane=84.0842, width=13.9464, height=6.2626, cameraPosition=(18.8727, 
    -56.111, -72.8366), cameraUpVector=(0.170259, 0.9519, 0.254752), 
    cameraTarget=(28.7125, -77.3996, 0.133572), viewOffsetX=0.810284, 
    viewOffsetY=-0.0750803)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=54)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=35)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV1', outputPosition=INTEGRATION_POINT, )
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=71)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=174)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=171)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=170)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=145)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=153)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=158)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=144)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=156)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=148)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=149)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=150)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=151)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=152)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=153)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=160)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=159)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=158)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=157)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=156)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=155)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=154)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=153)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=152)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=153)
session.viewports[session.currentViewportName].odbDisplay.setFrame(step='move', 
    frame=152)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69.2535, 
    farPlane=84.6626, width=20.214, height=9.07706, viewOffsetX=1.86031, 
    viewOffsetY=-3.28401)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV16', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV18', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV16', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SDV1', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.2868, 
    farPlane=83.6293, width=7.84406, height=3.52237, viewOffsetX=1.6147, 
    viewOffsetY=-1.99961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.2461, 
    farPlane=83.6699, width=7.83952, height=3.52033, viewOffsetX=1.02447, 
    viewOffsetY=-0.30098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6476, 
    farPlane=83.2685, width=3.11661, height=1.39951, viewOffsetX=0.340953, 
    viewOffsetY=0.519563)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6652, 
    farPlane=83.2509, width=3.11738, height=1.39986, viewOffsetX=0.354483, 
    viewOffsetY=0.442987)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6651, 
    farPlane=83.251, width=3.11738, height=1.39986, viewOffsetX=0.173932, 
    viewOffsetY=-0.155309)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6651, 
    farPlane=83.251, width=3.11738, height=1.39986, viewOffsetX=0.0260342, 
    viewOffsetY=-0.931943)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6651, 
    farPlane=83.251, width=3.11738, height=1.39986, viewOffsetX=-0.0796071, 
    viewOffsetY=-1.48805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6651, 
    farPlane=83.251, width=3.11738, height=1.39986, viewOffsetX=-0.263999, 
    viewOffsetY=-1.92718)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6651, 
    farPlane=83.251, width=3.11738, height=1.39986, viewOffsetX=-0.196773, 
    viewOffsetY=-1.77185)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.6972, 
    farPlane=83.2188, width=2.59043, height=1.16323, viewOffsetX=-0.204513, 
    viewOffsetY=-1.69368)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.7118, 
    farPlane=83.2043, width=2.59096, height=1.16347, viewOffsetX=0.065237, 
    viewOffsetY=-1.17285)
session.viewports['Viewport: 1'].view.setValues(farPlane=83.2043, 
    viewOffsetX=0.331836, viewOffsetY=-0.731369)
session.viewports['Viewport: 1'].view.setValues(farPlane=83.2043, 
    viewOffsetX=0.414849, viewOffsetY=-0.395078)
session.viewports['Viewport: 1'].view.setValues(farPlane=83.2043, 
    viewOffsetX=0.580875, viewOffsetY=0.0942169)
session.viewports['Viewport: 1'].view.setValues(farPlane=83.2043, 
    viewOffsetX=0.555332, viewOffsetY=0.376318)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.7729, 
    farPlane=83.1432, width=1.78897, height=0.803336, viewOffsetX=0.422723, 
    viewOffsetY=0.351053)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.783, 
    farPlane=83.1331, width=1.78923, height=0.803451, viewOffsetX=0.420579, 
    viewOffsetY=-0.0748357)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.7368, 
    farPlane=83.1793, width=2.45635, height=1.10302, viewOffsetX=0.510234, 
    viewOffsetY=-0.00496283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.7237, 
    farPlane=83.1923, width=2.45589, height=1.10282, viewOffsetX=0.425402, 
    viewOffsetY=-0.562413)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.7238, 
    farPlane=83.1923, width=2.45589, height=1.10282, viewOffsetX=0.245334, 
    viewOffsetY=-1.11836)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70.7238, 
    farPlane=83.1923, width=2.45589, height=1.10282, viewOffsetX=0.364875, 
    viewOffsetY=-1.23922)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.5908, 
    farPlane=86.3916, width=2.38183, height=1.06956, cameraPosition=(44.5008, 
    -108.454, -68.929), cameraUpVector=(0.262448, 0.901085, -0.345205), 
    cameraTarget=(28.9268, -77.6936, -0.475273), viewOffsetX=0.353871, 
    viewOffsetY=-1.20185)
odb = session.odbs['G4_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Max. Principal'), (
    INVARIANT, 'Mid. Principal'), (INVARIANT, 'Min. Principal'), )), ('SDV1', 
    INTEGRATION_POINT), ('SDV16', INTEGRATION_POINT), ('SDV17', 
    INTEGRATION_POINT), ('SDV18', INTEGRATION_POINT), ('SDV20', 
    INTEGRATION_POINT), ('SDV22', INTEGRATION_POINT), ('TRIAX', 
    INTEGRATION_POINT), ), elementPick=(('SH-1', 1, ('[#0:1528 #200 ]', )), ), )
odb = session.odbs['G4_Damage_P.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodeSets=("FORCE_DISP", ))
xy1 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105451']
xy2 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105453']
xy3 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105456']
xy4 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105459']
xy5 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105483']
xy6 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105484']
xy7 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105485']
xy8 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105973']
xy9 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105974']
xy10 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 105981']
xy11 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106095']
xy12 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106162']
xy13 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106163']
xy14 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106164']
xy15 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106165']
xy16 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106166']
xy17 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106167']
xy18 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106168']
xy19 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106169']
xy20 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106170']
xy21 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106171']
xy22 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106172']
xy23 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106173']
xy24 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106174']
xy25 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106175']
xy26 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106214']
xy27 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106215']
xy28 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106216']
xy29 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106217']
xy30 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106218']
xy31 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106219']
xy32 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106220']
xy33 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106221']
xy34 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106222']
xy35 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106223']
xy36 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106224']
xy37 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106225']
xy38 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106226']
xy39 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106227']
xy40 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106228']
xy41 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106229']
xy42 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106230']
xy43 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106231']
xy44 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106232']
xy45 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106266']
xy46 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106267']
xy47 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106268']
xy48 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106269']
xy49 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106270']
xy50 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106271']
xy51 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106272']
xy52 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106273']
xy53 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106274']
xy54 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106275']
xy55 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106276']
xy56 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106277']
xy57 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106278']
xy58 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106279']
xy59 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106280']
xy60 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106281']
xy61 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106282']
xy62 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106283']
xy63 = session.xyDataObjects['RF:RF2 PI: SH-1 N: 106284']
xy64 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63))*2/1000
xy64.setValues(
    sourceDescription='sum ( ( "RF:RF2 PI: SH-1 N: 105451", "RF:RF2 PI: SH-1 N: 105453", "RF:RF2 PI: SH-1 N: 105456", "RF:RF2 PI: SH-1 N: 105459", "RF:RF2 PI: SH-1 N: 105483", "RF:RF2 PI: SH-1 N: 105484", "RF:RF2 PI: SH-1 N: 105485", "RF:RF2 PI: SH-1 N: 105973", "RF:RF2 PI: SH-1 N: 105974", "RF:RF2 PI: SH-1 N: 105981", "RF:RF2 PI: SH-1 N: 106095", "RF:RF2 PI: SH-1 N: 106162", "RF:RF2 PI: SH-1 N: 106163", "RF:RF2 PI: SH-1 N: 106164", "RF:RF2 PI: SH-1 N: 106165", "RF:RF2 PI: SH-1 N: 106166", "RF:RF2 PI: SH-1 N: 106167", "RF:RF2 PI: SH-1 N: 106168", "RF:RF2 PI: SH-1 N: 106169", "RF:RF2 PI: SH-1 N: 106170", "RF:RF2 PI: SH-1 N: 106171", "RF:RF2 PI: SH-1 N: 106172", "RF:RF2 PI: SH-1 N: 106173", "RF:RF2 PI: SH-1 N: 106174", "RF:RF2 PI: SH-1 N: 106175", "RF:RF2 PI: SH-1 N: 106214", "RF:RF2 PI: SH-1 N: 106215", "RF:RF2 PI: SH-1 N: 106216", "RF:RF2 PI: SH-1 N: 106217", "RF:RF2 PI: SH-1 N: 106218", "RF:RF2 PI: SH-1 N: 106219", "RF:RF2 PI: SH-1 N: 106220", "RF:RF2 PI: SH-1 N: 106221", "RF:RF2 PI: SH-1 N: 106222", "RF:RF2 PI: SH-1 N: 106223", "RF:RF2 PI: SH-1 N: 106224", "RF:RF2 PI: SH-1 N: 106225", "RF:RF2 PI: SH-1 N: 106226", "RF:RF2 PI: SH-1 N: 106227", "RF:RF2 PI: SH-1 N: 106228", "RF:RF2 PI: SH-1 N: 106229", "RF:RF2 PI: SH-1 N: 106230", "RF:RF2 PI: SH-1 N: 106231", "RF:RF2 PI: SH-1 N: 106232", "RF:RF2 PI: SH-1 N: 106266", "RF:RF2 PI: SH-1 N: 106267", "RF:RF2 PI: SH-1 N: 106268", "RF:RF2 PI: SH-1 N: 106269", "RF:RF2 PI: SH-1 N: 106270", "RF:RF2 PI: SH-1 N: 106271", "RF:RF2 PI: SH-1 N: 106272", "RF:RF2 PI: SH-1 N: 106273", "RF:RF2 PI: SH-1 N: 106274", "RF:RF2 PI: SH-1 N: 106275", "RF:RF2 PI: SH-1 N: 106276", "RF:RF2 PI: SH-1 N: 106277", "RF:RF2 PI: SH-1 N: 106278", "RF:RF2 PI: SH-1 N: 106279", "RF:RF2 PI: SH-1 N: 106280", "RF:RF2 PI: SH-1 N: 106281", "RF:RF2 PI: SH-1 N: 106282", "RF:RF2 PI: SH-1 N: 106283", "RF:RF2 PI: SH-1 N: 106284" ) )*2/1000')
tmpName = xy64.name
session.xyDataObjects.changeKey(tmpName, 'Force')
xy1 = session.xyDataObjects['U:U2 PI: SH-1 N: 105451']
xy2 = session.xyDataObjects['U:U2 PI: SH-1 N: 105453']
xy3 = session.xyDataObjects['U:U2 PI: SH-1 N: 105456']
xy4 = session.xyDataObjects['U:U2 PI: SH-1 N: 105459']
xy5 = session.xyDataObjects['U:U2 PI: SH-1 N: 105483']
xy6 = session.xyDataObjects['U:U2 PI: SH-1 N: 105484']
xy7 = session.xyDataObjects['U:U2 PI: SH-1 N: 105485']
xy8 = session.xyDataObjects['U:U2 PI: SH-1 N: 105973']
xy9 = session.xyDataObjects['U:U2 PI: SH-1 N: 105974']
xy10 = session.xyDataObjects['U:U2 PI: SH-1 N: 105981']
xy11 = session.xyDataObjects['U:U2 PI: SH-1 N: 106095']
xy12 = session.xyDataObjects['U:U2 PI: SH-1 N: 106162']
xy13 = session.xyDataObjects['U:U2 PI: SH-1 N: 106163']
xy14 = session.xyDataObjects['U:U2 PI: SH-1 N: 106164']
xy15 = session.xyDataObjects['U:U2 PI: SH-1 N: 106165']
xy16 = session.xyDataObjects['U:U2 PI: SH-1 N: 106166']
xy17 = session.xyDataObjects['U:U2 PI: SH-1 N: 106167']
xy18 = session.xyDataObjects['U:U2 PI: SH-1 N: 106168']
xy19 = session.xyDataObjects['U:U2 PI: SH-1 N: 106169']
xy20 = session.xyDataObjects['U:U2 PI: SH-1 N: 106170']
xy21 = session.xyDataObjects['U:U2 PI: SH-1 N: 106171']
xy22 = session.xyDataObjects['U:U2 PI: SH-1 N: 106172']
xy23 = session.xyDataObjects['U:U2 PI: SH-1 N: 106173']
xy24 = session.xyDataObjects['U:U2 PI: SH-1 N: 106174']
xy25 = session.xyDataObjects['U:U2 PI: SH-1 N: 106175']
xy26 = session.xyDataObjects['U:U2 PI: SH-1 N: 106214']
xy27 = session.xyDataObjects['U:U2 PI: SH-1 N: 106215']
xy28 = session.xyDataObjects['U:U2 PI: SH-1 N: 106216']
xy29 = session.xyDataObjects['U:U2 PI: SH-1 N: 106217']
xy30 = session.xyDataObjects['U:U2 PI: SH-1 N: 106218']
xy31 = session.xyDataObjects['U:U2 PI: SH-1 N: 106219']
xy32 = session.xyDataObjects['U:U2 PI: SH-1 N: 106220']
xy33 = session.xyDataObjects['U:U2 PI: SH-1 N: 106221']
xy34 = session.xyDataObjects['U:U2 PI: SH-1 N: 106222']
xy35 = session.xyDataObjects['U:U2 PI: SH-1 N: 106223']
xy36 = session.xyDataObjects['U:U2 PI: SH-1 N: 106224']
xy37 = session.xyDataObjects['U:U2 PI: SH-1 N: 106225']
xy38 = session.xyDataObjects['U:U2 PI: SH-1 N: 106226']
xy39 = session.xyDataObjects['U:U2 PI: SH-1 N: 106227']
xy40 = session.xyDataObjects['U:U2 PI: SH-1 N: 106228']
xy41 = session.xyDataObjects['U:U2 PI: SH-1 N: 106229']
xy42 = session.xyDataObjects['U:U2 PI: SH-1 N: 106230']
xy43 = session.xyDataObjects['U:U2 PI: SH-1 N: 106231']
xy44 = session.xyDataObjects['U:U2 PI: SH-1 N: 106232']
xy45 = session.xyDataObjects['U:U2 PI: SH-1 N: 106266']
xy46 = session.xyDataObjects['U:U2 PI: SH-1 N: 106267']
xy47 = session.xyDataObjects['U:U2 PI: SH-1 N: 106268']
xy48 = session.xyDataObjects['U:U2 PI: SH-1 N: 106269']
xy49 = session.xyDataObjects['U:U2 PI: SH-1 N: 106270']
xy50 = session.xyDataObjects['U:U2 PI: SH-1 N: 106271']
xy51 = session.xyDataObjects['U:U2 PI: SH-1 N: 106272']
xy52 = session.xyDataObjects['U:U2 PI: SH-1 N: 106273']
xy53 = session.xyDataObjects['U:U2 PI: SH-1 N: 106274']
xy54 = session.xyDataObjects['U:U2 PI: SH-1 N: 106275']
xy55 = session.xyDataObjects['U:U2 PI: SH-1 N: 106276']
xy56 = session.xyDataObjects['U:U2 PI: SH-1 N: 106277']
xy57 = session.xyDataObjects['U:U2 PI: SH-1 N: 106278']
xy58 = session.xyDataObjects['U:U2 PI: SH-1 N: 106279']
xy59 = session.xyDataObjects['U:U2 PI: SH-1 N: 106280']
xy60 = session.xyDataObjects['U:U2 PI: SH-1 N: 106281']
xy61 = session.xyDataObjects['U:U2 PI: SH-1 N: 106282']
xy62 = session.xyDataObjects['U:U2 PI: SH-1 N: 106283']
xy63 = session.xyDataObjects['U:U2 PI: SH-1 N: 106284']
xy64 = avg((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63))
xy64.setValues(
    sourceDescription='avg ( ( "U:U2 PI: SH-1 N: 105451", "U:U2 PI: SH-1 N: 105453", "U:U2 PI: SH-1 N: 105456", "U:U2 PI: SH-1 N: 105459", "U:U2 PI: SH-1 N: 105483", "U:U2 PI: SH-1 N: 105484", "U:U2 PI: SH-1 N: 105485", "U:U2 PI: SH-1 N: 105973", "U:U2 PI: SH-1 N: 105974", "U:U2 PI: SH-1 N: 105981", "U:U2 PI: SH-1 N: 106095", "U:U2 PI: SH-1 N: 106162", "U:U2 PI: SH-1 N: 106163", "U:U2 PI: SH-1 N: 106164", "U:U2 PI: SH-1 N: 106165", "U:U2 PI: SH-1 N: 106166", "U:U2 PI: SH-1 N: 106167", "U:U2 PI: SH-1 N: 106168", "U:U2 PI: SH-1 N: 106169", "U:U2 PI: SH-1 N: 106170", "U:U2 PI: SH-1 N: 106171", "U:U2 PI: SH-1 N: 106172", "U:U2 PI: SH-1 N: 106173", "U:U2 PI: SH-1 N: 106174", "U:U2 PI: SH-1 N: 106175", "U:U2 PI: SH-1 N: 106214", "U:U2 PI: SH-1 N: 106215", "U:U2 PI: SH-1 N: 106216", "U:U2 PI: SH-1 N: 106217", "U:U2 PI: SH-1 N: 106218", "U:U2 PI: SH-1 N: 106219", "U:U2 PI: SH-1 N: 106220", "U:U2 PI: SH-1 N: 106221", "U:U2 PI: SH-1 N: 106222", "U:U2 PI: SH-1 N: 106223", "U:U2 PI: SH-1 N: 106224", "U:U2 PI: SH-1 N: 106225", "U:U2 PI: SH-1 N: 106226", "U:U2 PI: SH-1 N: 106227", "U:U2 PI: SH-1 N: 106228", "U:U2 PI: SH-1 N: 106229", "U:U2 PI: SH-1 N: 106230", "U:U2 PI: SH-1 N: 106231", "U:U2 PI: SH-1 N: 106232", "U:U2 PI: SH-1 N: 106266", "U:U2 PI: SH-1 N: 106267", "U:U2 PI: SH-1 N: 106268", "U:U2 PI: SH-1 N: 106269", "U:U2 PI: SH-1 N: 106270", "U:U2 PI: SH-1 N: 106271", "U:U2 PI: SH-1 N: 106272", "U:U2 PI: SH-1 N: 106273", "U:U2 PI: SH-1 N: 106274", "U:U2 PI: SH-1 N: 106275", "U:U2 PI: SH-1 N: 106276", "U:U2 PI: SH-1 N: 106277", "U:U2 PI: SH-1 N: 106278", "U:U2 PI: SH-1 N: 106279", "U:U2 PI: SH-1 N: 106280", "U:U2 PI: SH-1 N: 106281", "U:U2 PI: SH-1 N: 106282", "U:U2 PI: SH-1 N: 106283", "U:U2 PI: SH-1 N: 106284" ) )')
tmpName = xy64.name
session.xyDataObjects.changeKey(tmpName, 'Disp')
x0 = session.xyDataObjects['Disp']
x1 = session.xyDataObjects['Force']
session.writeXYReport(fileName='G4_P_FD.rpt', xyData=(x0, x1))
x0 = session.xyDataObjects['S:Max Principal PI: SH-1 E: 52905 IP: 1']
x1 = session.xyDataObjects['S:Mid Principal PI: SH-1 E: 52905 IP: 1']
x2 = session.xyDataObjects['S:Min Principal PI: SH-1 E: 52905 IP: 1']
x3 = session.xyDataObjects['SDV1 PI: SH-1 E: 52905 IP: 1']
x4 = session.xyDataObjects['SDV16 PI: SH-1 E: 52905 IP: 1']
x5 = session.xyDataObjects['SDV17 PI: SH-1 E: 52905 IP: 1']
x6 = session.xyDataObjects['SDV18 PI: SH-1 E: 52905 IP: 1']
x7 = session.xyDataObjects['SDV20 PI: SH-1 E: 52905 IP: 1']
x8 = session.xyDataObjects['SDV22 PI: SH-1 E: 52905 IP: 1']
x9 = session.xyDataObjects['TRIAX PI: SH-1 E: 52905 IP: 1']
session.writeXYReport(fileName='G4_P_LS_Cr2.rpt', xyData=(x0, x1, x2, x3, x4, 
    x5, x6, x7, x8, x9))
