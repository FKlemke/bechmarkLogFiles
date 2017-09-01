import toolBox

##run this file for generation of csv and image files

def visualizeBuild ():
    plotVal1 = []
    plotVal2 = []
    plotVal1 = toolBox.parseBuildTimes(sourcefile1, plotVal1, targetfile)
    plotVal1 = toolBox.parseBuildTimes(sourcefile2, plotVal1, targetfile)
    plotVal1 = toolBox.parseBuildTimes(sourcefile3, plotVal1, targetfile)
    plotVal2 = toolBox.parseBuildTimes(sourcefile4, plotVal2, targetfile)
    plotVal2 = toolBox.parseBuildTimes(sourcefile5, plotVal2, targetfile)
    plotVal2 = toolBox.parseBuildTimes(sourcefile6, plotVal2, targetfile)
    toolBox.visusalizeBuildTimes(titelName, plotVal1, plotVal2, testcase)

def visualizeBenchmarks3Groups():
    plotVal1 = []
    plotVal2 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    toolBox.setHeaderLatRegSec(targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile1, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile2, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile3, plotVal1, plotVal2, targetfile)
    toolBox.visusalizeValueSets(titelName, plotVal1, plotVal2, testcase)

def visualizeBenchmarks4Groups():
    plotVal1 = []
    plotVal2 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    toolBox.setHeaderLatRegSec(targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile1, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile2, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile3, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk2(sourcefile4, plotVal1, plotVal2, targetfile)
    toolBox.visusalizeValueSetsVaporTools(titelName, plotVal1, plotVal2, testcase)

def visualizeThreadUsage():
    plotVal1 = []
    plotVal2 = []
    plotVal3 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    toolBox.setHeaderTop(targetfile)
    plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile1, plotVal1, plotVal2, plotVal3, targetfile)
    plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile2, plotVal1, plotVal2, plotVal3, targetfile)
    plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile3, plotVal1, plotVal2, plotVal3, targetfile)

# BUILD TIMES V1
testcase = "BUILDSbenchmarkingV1"
titelName = "Build times"
sourcefile1 = './RawLogFiles/btDebugPerfectServerV1.txt'
sourcefile2 = './RawLogFiles/btDebugVaporServerV1.txt'
sourcefile3 = './RawLogFiles/btDebugKituraServerV1.txt'
sourcefile4 = './RawLogFiles/btReleasePerfectServerV1.txt'
sourcefile5 = './RawLogFiles/btReleaseVaporServerV1.txt'
sourcefile6 = './RawLogFiles/btReleaseKituraServerV1.txt'
targetfile = 'datalyzed/csv/' + testcase + '.csv'
visualizeBuild ()

# BUILD TIMES V1
testcase = "BUILDSbenchmarkingV1"
titelName = "Build times"
sourcefile1 = './RawLogFiles/btDebugPerfectServerV1.txt'
sourcefile2 = './RawLogFiles/btDebugVaporServerV1.txt'
sourcefile3 = './RawLogFiles/btDebugKituraServerV1.txt'
sourcefile4 = './RawLogFiles/btReleasePerfectServerV1.txt'
sourcefile5 = './RawLogFiles/btReleaseVaporServerV1.txt'
sourcefile6 = './RawLogFiles/btReleaseKituraServerV1.txt'
targetfile = 'datalyzed/csv/' + testcase + '.csv'
visualizeBuild ()


# JSON V1
testcase = "JSONbenchmarkingV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
visualizeBenchmarks3Groups()

# JSON V1 Vapor Tools
testcase = "JSONbenchmarkingVaporToolsV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/jsonVaporClientWrk2V3.txt'
sourcefile4 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
visualizeBenchmarks4Groups()

# JSON V2
testcase = "JSONbenchmarkingV2"
titelName = "JSON benchmarking / Non generated"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
visualizeBenchmarks3Groups()

# JSON V2 Vapor Tools
testcase = "JSONbenchmarkingVaporToolsV2"
titelName = "JSON benchmarking / Non generated"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/jsonVaporClientWrk2V3.txt'
sourcefile4 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
visualizeBenchmarks4Groups()

# HTML V1
testcase = "HTMLbenchmarkingV1"
titelName = "HTML benchmarking"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
visualizeBenchmarks3Groups()

# HTML V1 Vapor Tools
testcase = "HTMLbenchmarkingVaporToolsV1"
titelName = "HTML benchmarking"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/htmlVaporClientWrk2V3.txt'
sourcefile4 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
visualizeBenchmarks4Groups()

# HTML V2
testcase = "HTMLbenchmarkingV2"
titelName = "HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
visualizeBenchmarks3Groups()

# HTML V2 Vapor Tools
testcase = "HTMLbenchmarkingVaporToolsV2"
titelName = "HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/htmlVaporClientWrk2V4.txt'
sourcefile4 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
visualizeBenchmarks4Groups()

# STRESS V1
testcase = "STRESSbenchmarkingV1"
titelName = "Stress Test benchmarking"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V1.txt'
visualizeBenchmarks3Groups()

# STRESS V1 Vapor Tools
testcase = "STRESSbenchmarkingVaporToolsV1"
titelName = "Stress Test benchmarking"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1C.txt'
sourcefile3 = './RawLogFiles/stressVaporClientWrk2V1.txt'
sourcefile4 = './RawLogFiles/stressKituraClientWrk2V1.txt'
visualizeBenchmarks4Groups()

# STRESS V2
testcase = "STRESSbenchmarkingV2"
titelName = "Stress Test benchmarking / High Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V2.txt'
visualizeBenchmarks3Groups()

# STRESS V2 Vapor Tools
testcase = "STRESSbenchmarkingVaporToolsV2"
titelName = "Stress Test benchmarking / High Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2C.txt'
sourcefile3 = './RawLogFiles/stressVaporClientWrk2V2.txt'
sourcefile4 = './RawLogFiles/stressKituraClientWrk2V2.txt'
visualizeBenchmarks4Groups()

# STRESS V3
testcase = "STRESSbenchmarkingV3"
titelName = "Stress Test benchmarking / Spike Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V3.txt'
visualizeBenchmarks3Groups()

# STRESS V3 Vapor Tools
testcase = "STRESSbenchmarkingV3"
titelName = "Stress Test benchmarking / Spike Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3C.txt'
sourcefile3 = './RawLogFiles/stressVaporClientWrk2V3.txt'
sourcefile4 = './RawLogFiles/stressKituraClientWrk2V3.txt'
visualizeBenchmarks4Groups()

# Thread usage
testcase = "THREADbenchmarkingV1"
titelName = "Thread usage"
sourcefile1 = './RawLogFiles/stressPerfectServerTopV1.txt'
sourcefile2 = './RawLogFiles/stressVaporServerTopV1.txt'
sourcefile3 = './RawLogFiles/stressKituraServerTopV1.txt'
visualizeThreadUsage()




