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


def visualizeTop():
    plotVal1 = []
    plotVal2 = []
    plotVal3 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    plotVal1, plotVal2, plotVal3 = toolBox.parseTopServer(sourcefile1, plotVal1, plotVal2, plotVal3,targetfile)
    toolBox.visusalizeTopServer(titelName, plotVal1, plotVal2, plotVal3, testcase)

def visualizeWrk2Throuput():
    plotVal1 = []
    plotVal2 = []
    plotVal3 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    plotVal1, plotVal2, plotVal3 = toolBox.parseErrorsWrk2(sourcefile1, plotVal1, plotVal2, plotVal3, targetfile)
    plotVal1, plotVal2, plotVal3 = toolBox.parseErrorsWrk2(sourcefile2, plotVal1, plotVal2, plotVal3, targetfile)
    plotVal1, plotVal2, plotVal3 = toolBox.parseErrorsWrk2(sourcefile3, plotVal1, plotVal2, plotVal3, targetfile)
    toolBox.visusalize3ValueSets(titelName,plotVal1,plotVal2,plotVal3,testcase)

# def visualize1Group():
#     plotVal1 = []
#     targetfile = 'datalyzed/csv/' + testcase + '.csv'
#     plotVal1 = toolBox.parseThreadServer(sourcefile1,plotVal1,targetfile)
#     plotVal1 = toolBox.parseThreadServer(sourcefile2, plotVal1, targetfile)
#     plotVal1 = toolBox.parseThreadServer(sourcefile3, plotVal1, targetfile)
#     toolBox.visusalize1ValueSet(titelName,plotVal1,testcase)

#
# # BUILD TIMES V1
# testcase = "BUILDSbenchmarkingV1"
# titelName = "Build times"
# sourcefile1 = './RawLogFiles/btDebugPerfectServerV1.txt'
# sourcefile2 = './RawLogFiles/btDebugVaporServerV1.txt'
# sourcefile3 = './RawLogFiles/btDebugKituraServerV1.txt'
# sourcefile4 = './RawLogFiles/btReleasePerfectServerV1.txt'
# sourcefile5 = './RawLogFiles/btReleaseVaporServerV1.txt'
# sourcefile6 = './RawLogFiles/btReleaseKituraServerV1.txt'
# targetfile = 'datalyzed/csv/' + testcase + '.csv'
# visualizeBuild ()
#
# # BUILD TIMES V1
# testcase = "BUILDSbenchmarkingV1"
# titelName = "Build times"
# sourcefile1 = './RawLogFiles/btDebugPerfectServerV1.txt'
# sourcefile2 = './RawLogFiles/btDebugVaporServerV1.txt'
# sourcefile3 = './RawLogFiles/btDebugKituraServerV1.txt'
# sourcefile4 = './RawLogFiles/btReleasePerfectServerV1.txt'
# sourcefile5 = './RawLogFiles/btReleaseVaporServerV1.txt'
# sourcefile6 = './RawLogFiles/btReleaseKituraServerV1.txt'
# targetfile = 'datalyzed/csv/' + testcase + '.csv'
# visualizeBuild ()
#
# ############################################################
#
# # JSON V1
# testcase = "JSONbenchmarkingV1"
# titelName = "JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
# sourcefile2= './RawLogFiles/jsonVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
# visualizeBenchmarks3Groups()
#
# # JSON V1 Vapor Tools
# testcase = "JSONbenchmarkingVaporToolsV1"
# titelName = "JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
# sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
# sourcefile4 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
# visualizeBenchmarks4Groups()
#
# # JSON V1 PERFECT
# testcase = "JSONbenchmarkingV1Perfect"
# titelName = "Perfect JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonPerfectServerTopV1.txt'
# visualizeTop()
#
# # JSON V1 Vapor
# testcase = "JSONbenchmarkingV1VaporManual"
# titelName = "Vapor Manual JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonVaporServerTopV1.txt'
# visualizeTop()
#
# # JSON V1 Vapor Tools
# testcase = "JSONbenchmarkingV1Vapor"
# titelName = "Vapor JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonVaporServerTopV3.txt'
# visualizeTop()
#
# # JSON V1 Kitura
# testcase = "JSONbenchmarkingV1Kitura"
# titelName = "Kitura JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonKituraServerTopV1.txt'
# visualizeTop()
#
# ############################################################
#
# # JSON V2
# testcase = "JSONbenchmarkingV2"
# titelName = "JSON benchmarking / Non generated"
# sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
# sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
# visualizeBenchmarks3Groups()
#
# # JSON V2 Vapor Tools
# testcase = "JSONbenchmarkingVaporToolsV2"
# titelName = "JSON benchmarking / Non generated"
# sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
# sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V4.txt'
# sourcefile3 = './RawLogFiles/jsonVaporClientWrk2V2.txt'
# sourcefile4 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
# visualizeBenchmarks4Groups()
#
# # JSON V2 PERFECT
# testcase = "JSONbenchmarkingV2Perfect"
# titelName = "Perfect JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonPerfectServerTopV2.txt'
# visualizeTop()
#
# # JSON V2 Vapor
# testcase = "JSONbenchmarkingV2VaporMan"
# titelName = "Vapor Manual JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonVaporServerTopV2.txt'
# visualizeTop()
#
# # JSON V2 Vapor
# testcase = "JSONbenchmarkingV2Vapor"
# titelName = "Vapor JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonVaporServerTopV4.txt'
# visualizeTop()
#
# # JSON V2 Kitura
# testcase = "JSONbenchmarkingV2Kitura"
# titelName = "Kitura JSON benchmarking"
# sourcefile1 = './RawLogFiles/jsonKituraServerTopV2.txt'
# visualizeTop()
#
# ############################################################
#
# # HTML V1
# testcase = "HTMLbenchmarkingV1"
# titelName = "HTML benchmarking"
# sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
# sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
# visualizeBenchmarks3Groups()
#
# # HTML V1 Vapor Tools
# testcase = "HTMLbenchmarkingVaporToolsV1"
# titelName = "HTML benchmarking"
# sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
# sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/htmlVaporClientWrk2V1.txt'
# sourcefile4 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
# visualizeBenchmarks4Groups()
#
# testcase = "HTMLbenchmarkingV1Perfect"
# titelName = "Perfect HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlPerfectServerTopV2.txt'
# visualizeTop()
#
# testcase = "HTMLbenchmarkingV1Vapor"
# titelName = "Vapor HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlVaporServerTopV4.txt'
# visualizeTop()
#
# testcase = "HTMLbenchmarkingV1VaporMan"
# titelName = "Vapor Manual HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlVaporServerTopV1.txt'
# visualizeTop()
#
# testcase = "HTMLbenchmarkingV1Kitura"
# titelName = "Kitura HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlKituraServerTopV2.txt'
# visualizeTop()
#
# ############################################################
#
# # HTML V2
# testcase = "HTMLbenchmarkingV2"
# titelName = "HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
# sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V4.txt'
# sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
# visualizeBenchmarks3Groups()
#
# # HTML V2 Vapor Tools
# testcase = "HTMLbenchmarkingVaporToolsV2"
# titelName = "HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
# sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V4.txt'
# sourcefile3 = './RawLogFiles/htmlVaporClientWrk2V2.txt'
# sourcefile4 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
# visualizeBenchmarks4Groups()
#
# testcase = "HTMLbenchmarkingV2Perfect"
# titelName = "Perfect HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlPerfectServerTopV2.txt'
# visualizeTop()
#
# testcase = "HTMLbenchmarkingV2Vapor"
# titelName = "Vapor HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlVaporServerTopV4.txt'
# visualizeTop()
#
# testcase = "HTMLbenchmarkingV2VaporMan"
# titelName = "Vapor Manual HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlVaporServerTopV1.txt'
# visualizeTop()
#
# testcase = "HTMLbenchmarkingV2Kitura"
# titelName = "Kitura HTML benchmarking / Large HTML"
# sourcefile1 = './RawLogFiles/htmlKituraServerTopV2.txt'
# visualizeTop()
# ############################################################
#
# # STRESS V1
# testcase = "STRESSbenchmarkingV1"
# titelName = "Stress Test benchmarking"
# sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
# sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
# sourcefile3 = './RawLogFiles/stressKituraClientWrk2V1.txt'
# visualizeBenchmarks3Groups()
#
# # STRESS V1 Vapor Tools
# testcase = "STRESSbenchmarkingVaporManV1"
# titelName = "Stress Test benchmarking"
# sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
# sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
# sourcefile3 = './RawLogFiles/stressVaporClientWrk2V1C.txt'
# sourcefile4 = './RawLogFiles/stressKituraClientWrk2V1.txt'
# visualizeBenchmarks4Groups()
#
# # STATS benchmarking Perfect
# testcase = "STRESSbenchmarkingV1Perfect"
# titelName = "Perfect / Stress Test / Low load"
# sourcefile1 = './RawLogFiles/stressPerfectServerTopV1.txt'
# visualizeTop()
#
# # STATS benchmarking Vapor
# testcase = "STRESSbenchmarkingV1Vapor"
# titelName = "Vapor / Stress Test / Low load"
# sourcefile1 = './RawLogFiles/stressVaporServerTopV1.txt'
# visualizeTop()
#
# # STATS benchmarking Vapor manual
# testcase = "STRESSbenchmarkingV1VaporMan"
# titelName = "Vapor Manual / Stress Test / Low load"
# sourcefile1 = './RawLogFiles/stressVaporServerTopV1C.txt'
# visualizeTop()
#
# # STATS benchmarking Kitura
# testcase = "STRESSbenchmarkingV1Kitura"
# titelName = "Kitura / Stress Test / Low load"
# sourcefile1 = './RawLogFiles/stressKituraServerTopV1.txt'
# visualizeTop()
#
# ############################################################
#
# # STRESS V2
# testcase = "STRESSbenchmarkingV2"
# titelName = "Stress Test benchmarking / High Load"
# sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
# sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
# sourcefile3 = './RawLogFiles/stressKituraClientWrk2V2.txt'
# visualizeBenchmarks3Groups()
#
# # STRESS V2 Vapor Tools
# testcase = "STRESSbenchmarkingVaporManV2"
# titelName = "Stress Test benchmarking / High Load"
# sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
# sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
# sourcefile3 = './RawLogFiles/stressVaporClientWrk2V2C.txt'
# sourcefile4 = './RawLogFiles/stressKituraClientWrk2V2.txt'
# visualizeBenchmarks4Groups()
#
# # STATS benchmarking PerfectV2
# testcase = "STRESSbenchmarkingV2Perfect"
# titelName = "Perfect / Stress Test / High load"
# sourcefile1 = './RawLogFiles/stressPerfectServerTopV2.txt'
# visualizeTop()
#
# # STATS benchmarking VaporV2
# testcase = "STRESSbenchmarkingV2Vapor"
# titelName = "Vapor / Stress Test / High load"
# sourcefile1 = './RawLogFiles/stressVaporServerTopV2.txt'
# visualizeTop()
#
# # STATS benchmarking VaporV2
# testcase = "STRESSbenchmarkingV2VaporMan"
# titelName = "Vapor Manual / Stress Test / High load"
# sourcefile1 = './RawLogFiles/stressVaporServerTopV2C.txt'
# visualizeTop()
#
# # STATS benchmarking KituraV2
# testcase = "STRESSbenchmarkingV2Kitura"
# titelName = "Kitura / Stress Test / High load"
# sourcefile1 = './RawLogFiles/stressKituraServerTopV2.txt'
# visualizeTop()
#
# ############################################################
#
# # STRESS V3
# testcase = "STRESSbenchmarkingV3"
# titelName = "Stress Test benchmarking / Spike Load"
# sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
# sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/stressKituraClientWrk2V3.txt'
# visualizeBenchmarks3Groups()
#
# # STRESS V3 Vapor Tools
# testcase = "STRESSbenchmarkingV3VaporMan"
# titelName = "Stress Test benchmarking / Spike Load"
# sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
# sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
# sourcefile3 = './RawLogFiles/stressVaporClientWrk2V3C.txt'
# sourcefile4 = './RawLogFiles/stressKituraClientWrk2V3.txt'
# visualizeBenchmarks4Groups()
#
# # STATS benchmarking Perfect V3
# testcase = "STRESSbenchmarkingV3Perfect"
# titelName = "Perfect / Stress Test / Spike load"
# sourcefile1 = './RawLogFiles/stressPerfectServerTopV3.txt'
# visualizeTop()
#
# # STATS benchmarking Vapor V3
# testcase = "STRESSbenchmarkingV3Vapor"
# titelName = "Vapor / Stress Test / Spike load"
# sourcefile1 = './RawLogFiles/stressVaporServerTopV3.txt'
# visualizeTop()
#
# # STATS benchmarking Vapor V3
# testcase = "STRESSbenchmarkingV3VaporMan"
# titelName = "Vapor Manual / Stress Test / Spike load"
# sourcefile1 = './RawLogFiles/stressVaporServerTopV3C.txt'
# visualizeTop()
#
# # STATS benchmarking Kitura V3
# testcase = "STRESSbenchmarkingV3Kitura"
# titelName = "Kitura / Stress Test / Spike load"
# sourcefile1 = './RawLogFiles/stressKituraServerTopV3.txt'
# visualizeTop()
#


# # THREADS benchmarking
# testcase = "THREADSbenchmarkingV1"
# titelName = "Kitura / "
# sourcefile1 = './RawLogFiles/stressPerfectServerTopV1.txt'
# sourcefile2 = './RawLogFiles/stressVaporServerTopV1.txt'
# sourcefile3 = './RawLogFiles/stressKituraServerTopV1.txt'
# visualize1Group()


# ERRR benchmarking V3
testcase = "STRESSbenchmarkingV3ERROR"
titelName = "Kitura / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V3.txt'
visualizeWrk2Throuput()

# ERRR benchmarking V3
testcase = "STRESSbenchmarkingV2ERROR"
titelName = "Kitura / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V2.txt'
visualizeWrk2Throuput()

# ERRR benchmarking V3
testcase = "STRESSbenchmarkingV1ERROR"
titelName = "Kitura / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V1.txt'
visualizeWrk2Throuput()