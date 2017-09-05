######################################################
# run this file for generation of csv and image files#
######################################################

import toolBox

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

def visualizeTopClient():
    plotVal1 = []
    plotVal2 = []
    plotVal3 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    plotVal1, plotVal2, plotVal3 = toolBox.parseTopClient(sourcefile1, plotVal1, plotVal2, plotVal3, targetfile)
    toolBox.visusalizeTopServer(titelName, plotVal1, plotVal2, plotVal3, testcase)

def visualizeWrk2Errs():
    plotVal1 = []
    plotVal2 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    plotVal1, plotVal2 = toolBox.parseErrorsWrk2(sourcefile1, plotVal1, plotVal2, targetfile)
    toolBox.visusalize2Pie(titelName,plotVal1,plotVal2,testcase)

def visualizeCR():
    plotVal1 = []
    plotVal2 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    plotVal1, plotVal2 = toolBox.parseHeaderWrk(sourcefile1, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk(sourcefile2, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk(sourcefile3, plotVal1, plotVal2, targetfile)

    plotVal1, plotVal2 = toolBox.parseHeaderWrk22(sourcefile4, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk22(sourcefile5, plotVal1, plotVal2, targetfile)
    plotVal1, plotVal2 = toolBox.parseHeaderWrk22(sourcefile6, plotVal1, plotVal2, targetfile)

    #Ryan's restults
    ryLat = [3.39,6.4,4.03]
    ryReq = [12270.0,6242.0,9138.0]

    for e in ryLat:
        plotVal1.append(e)
    for e in ryReq:
        plotVal2.append(e)
    toolBox.visusalizeValueSetsCR(titelName,plotVal1,plotVal2,testcase)

# toolBox.visualizeStd()


# ###############################################
# # The following a list of the visualized data #
# ###############################################

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

############################################################

# JSON V1
testcase = "JSONbenchmarkingV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2= './RawLogFiles/jsonVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
visualizeBenchmarks3Groups()


#Error Check
testcase = "JSONbenchmarkingV1ERRORPerfect"
titelName = "Perfect / JSON benchmarking / Errors "
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
visualizeWrk2Errs()

#Error Check
testcase = "JSONbenchmarkingV1ERRORVapor"
titelName = "Vapor / JSON benchmarking / Errors"
sourcefile1 = './RawLogFiles/jsonVaporClientWrk2V3.txt'
visualizeWrk2Errs()

#Error Check
testcase = "JSONbenchmarkingV1ERRORKitura"
titelName = "Kitura / JSON benchmarking / Errors"
sourcefile1 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
visualizeWrk2Errs()

# JSON V1 Vapor Tools
testcase = "JSONbenchmarkingVaporToolsV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
sourcefile4 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
visualizeBenchmarks4Groups()

# JSON V1 PERFECT TOP SERVER
testcase = "JSONbenchmarkingV1Perfect"
titelName = "Perfect JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectServerTopV1.txt'
visualizeTop()

# JSON V1 Vapor TOP SERVER
testcase = "JSONbenchmarkingV1VaporManual"
titelName = "Vapor Manual JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonVaporServerTopV1.txt'
visualizeTop()

# JSON V1 Vapor Tools TOP SERVER
testcase = "JSONbenchmarkingV1Vapor"
titelName = "Vapor JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonVaporServerTopV3.txt'
visualizeTop()

# JSON V1 Kitura TOP SERVER
testcase = "JSONbenchmarkingV1Kitura"
titelName = "Kitura JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonKituraServerTopV1.txt'
visualizeTop()

# JSON V1 PERFECT TOP CLIENT
testcase = "JSONbenchmarkingV1PerfectCLIENT"
titelName = "Perfect JSON benchmarking / Client"
sourcefile1 = './RawLogFiles/jsonPerfectClientTopV1.txt'
visualizeTopClient()

# JSON V1 Vapor Tools TOP CLIENT
testcase = "JSONbenchmarkingV1VaporCLIENT"
titelName = "Vapor JSON benchmarking / Client"
sourcefile1 = './RawLogFiles/jsonVaporClientTopV3.txt'
visualizeTopClient()

# JSON V1 Kitura TOP CLIENT
testcase = "JSONbenchmarkingV1KituraCLIENT"
titelName = "Kitura JSON benchmarking / Client"
sourcefile1 = './RawLogFiles/jsonKituraClientTopV1.txt'
visualizeTopClient()

############################################################

# JSON V2
testcase = "JSONbenchmarkingV2"
titelName = "JSON benchmarking / Non generated"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V4.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
visualizeBenchmarks3Groups()

# JSON V2 Vapor Tools
testcase = "JSONbenchmarkingVaporToolsV2"
titelName = "JSON benchmarking / Non generated"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V4.txt'
sourcefile3 = './RawLogFiles/jsonVaporClientWrk2V2.txt'
sourcefile4 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
visualizeBenchmarks4Groups()

#Error Check
testcase = "JSONbenchmarkingV2ERRORPerfect"
titelName = "Perfect / JSON benchmarking / Errors"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
visualizeWrk2Errs()

#Error Check
testcase = "JSONbenchmarkingV2ERRORVapor"
titelName = "Vapor / JSON benchmarking / Errors"
sourcefile1 = './RawLogFiles/jsonVaporClientWrk2V4.txt'
visualizeWrk2Errs()

#Error Check
testcase = "JSONbenchmarkingV2ERRORKitura"
titelName = "Kitura / JSON benchmarking / Errors"
sourcefile1 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
visualizeWrk2Errs()

# JSON V2 PERFECT SERVER
testcase = "JSONbenchmarkingV2Perfect"
titelName = "Perfect JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectServerTopV2.txt'
visualizeTop()

# JSON V2 Vapor SERVER
testcase = "JSONbenchmarkingV2VaporMan"
titelName = "Vapor Manual JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonVaporServerTopV2.txt'
visualizeTop()

# JSON V2 Vapor SERVER
testcase = "JSONbenchmarkingV2Vapor"
titelName = "Vapor JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonVaporServerTopV4.txt'
visualizeTop()

# JSON V2 Kitura SERVER
testcase = "JSONbenchmarkingV2Kitura"
titelName = "Kitura JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonKituraServerTopV2.txt'
visualizeTop()

# JSON V2 PERFECT CLIENT
testcase = "JSONbenchmarkingV2PerfectCLIENT"
titelName = "Perfect JSON benchmarking / Client"
sourcefile1 = './RawLogFiles/jsonPerfectClientTopV2.txt'
visualizeTopClient()

# JSON V2 Vapor CLIENT
testcase = "JSONbenchmarkingV2VaporCLIENT"
titelName = "Vapor JSON benchmarking / Client"
sourcefile1 = './RawLogFiles/jsonVaporClientTopV4.txt'
visualizeTopClient()

# JSON V2 Kitura CLIENT
testcase = "JSONbenchmarkingV2KituraCLIENT"
titelName = "Kitura JSON benchmarking / Client"
sourcefile1 = './RawLogFiles/jsonKituraClientTopV2.txt'
visualizeTopClient()

############################################################

# HTML V1
testcase = "HTMLbenchmarkingV1"
titelName = "HTML benchmarking"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
visualizeBenchmarks3Groups()

# HTML V1 Vapor Tools
testcase = "HTMLbenchmarkingVaporToolsV1"
titelName = "HTML benchmarking"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/htmlVaporClientWrk2V1.txt'
sourcefile4 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
visualizeBenchmarks4Groups()

#ERROR Check
testcase = "HTMLbenchmarkingV1ERRORPerfect"
titelName = "Perfect / HTML benchmarking / Errors"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
visualizeWrk2Errs()

testcase = "HTMLbenchmarkingV1ERRORVapor"
titelName = "HTML benchmarking / Errors / Vapor"
sourcefile1 = './RawLogFiles/htmlVaporClientWrk2V3.txt'
visualizeWrk2Errs()

testcase = "HTMLbenchmarkingV1ERRORKitura"
titelName = "Kitura / HTML benchmarking / Errors"
sourcefile1 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
visualizeWrk2Errs()

#top ststs SERVER
testcase = "HTMLbenchmarkingV1Perfect"
titelName = "Perfect HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectServerTopV2.txt'
visualizeTop()

testcase = "HTMLbenchmarkingV1Vapor"
titelName = "Vapor HTML benchmarking / HTML"
sourcefile1 = './RawLogFiles/htmlVaporServerTopV4.txt'
visualizeTop()

testcase = "HTMLbenchmarkingV1VaporMan"
titelName = "Vapor Manual HTML benchmarking / HTML"
sourcefile1 = './RawLogFiles/htmlVaporServerTopV1.txt'
visualizeTop()

testcase = "HTMLbenchmarkingV1Kitura"
titelName = "Kitura HTML benchmarking / HTML"
sourcefile1 = './RawLogFiles/htmlKituraServerTopV2.txt'
visualizeTop()

#top ststs CLIENT
testcase = "HTMLbenchmarkingV1PerfectCLIENT"
titelName = "Perfect HTML benchmarking / HTML / Client"
sourcefile1 = './RawLogFiles/htmlPerfectClientTopV2.txt'
visualizeTopClient()

testcase = "HTMLbenchmarkingV1VaporCLIENT"
titelName = "Vapor HTML benchmarking / HTML / Client"
sourcefile1 = './RawLogFiles/htmlVaporClientTopV4.txt'
visualizeTopClient()

testcase = "HTMLbenchmarkingV1KituraCLIENT"
titelName = "Kitura HTML benchmarking / HTML / Client"
sourcefile1 = './RawLogFiles/htmlKituraClientTopV2.txt'
visualizeTopClient()

############################################################

# HTML V2
testcase = "HTMLbenchmarkingV2"
titelName = "HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V4.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
visualizeBenchmarks3Groups()

# HTML V2 Vapor Tools
testcase = "HTMLbenchmarkingVaporToolsV2"
titelName = "HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V4.txt'
sourcefile3 = './RawLogFiles/htmlVaporClientWrk2V2.txt'
sourcefile4 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
visualizeBenchmarks4Groups()

#HTML ERRORS CHECK
testcase = "HTMLbenchmarkingV2ERRORPerfect"
titelName = "Perfect / HTML benchmarking / Large HTML / Errors"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V2.txt'
visualizeWrk2Errs()

testcase = "HTMLbenchmarkingV2ERRORVapor"
titelName = "Vapor / HTML benchmarking / Large HTML / Errors"
sourcefile1 = './RawLogFiles/htmlVaporClientWrk2V4.txt'
visualizeWrk2Errs()

testcase = "HTMLbenchmarkingV2ERRORKitura"
titelName = "Kitura / HTML benchmarking / Large HTML / Errors"
sourcefile1 = './RawLogFiles/htmlKituraClientWrk2V2.txt'
visualizeWrk2Errs()

# top SERVER
testcase = "HTMLbenchmarkingV2Perfect"
titelName = "Perfect HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlPerfectServerTopV2.txt'
visualizeTop()

testcase = "HTMLbenchmarkingV2Vapor"
titelName = "Vapor HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlVaporServerTopV4.txt'
visualizeTop()

testcase = "HTMLbenchmarkingV2VaporMan"
titelName = "Vapor Manual HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlVaporServerTopV1.txt'
visualizeTop()

testcase = "HTMLbenchmarkingV2Kitura"
titelName = "Kitura HTML benchmarking / Large HTML"
sourcefile1 = './RawLogFiles/htmlKituraServerTopV2.txt'
visualizeTop()

# top CLIENT
testcase = "HTMLbenchmarkingV2PerfectCLIENT"
titelName = "Perfect HTML benchmarking / Large HTML / Client"
sourcefile1 = './RawLogFiles/htmlPerfectClientTopV2.txt'
visualizeTopClient()

testcase = "HTMLbenchmarkingV2VaporCLIENT"
titelName = "Vapor HTML benchmarking / Large HTML / Client"
sourcefile1 = './RawLogFiles/htmlVaporClientTopV4.txt'
visualizeTopClient()

testcase = "HTMLbenchmarkingV2KituraCLIENT"
titelName = "Kitura HTML benchmarking / Large HTML / Client"
sourcefile1 = './RawLogFiles/htmlKituraClientTopV2.txt'
visualizeTopClient()
############################################################

# STRESS V1
testcase = "STRESSbenchmarkingV1"
titelName = "Stress Test benchmarking"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V1.txt'
visualizeBenchmarks3Groups()

# STRESS V1 Vapor Tools
testcase = "STRESSbenchmarkingVaporManV1"
titelName = "Stress Test benchmarking"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/stressVaporClientWrk2V1C.txt'
sourcefile4 = './RawLogFiles/stressKituraClientWrk2V1.txt'
visualizeBenchmarks4Groups()

# STATS benchmarking Perfect
testcase = "STRESSbenchmarkingV1Perfect"
titelName = "Perfect / Stress Test / Low load"
sourcefile1 = './RawLogFiles/stressPerfectServerTopV1.txt'
visualizeTop()

# STATS benchmarking Vapor
testcase = "STRESSbenchmarkingV1Vapor"
titelName = "Vapor / Stress Test / Low load"
sourcefile1 = './RawLogFiles/stressVaporServerTopV1.txt'
visualizeTop()

# STATS benchmarking Vapor manual
testcase = "STRESSbenchmarkingV1VaporMan"
titelName = "Vapor Manual / Stress Test / Low load"
sourcefile1 = './RawLogFiles/stressVaporServerTopV1C.txt'
visualizeTop()

# STATS benchmarking Kitura
testcase = "STRESSbenchmarkingV1Kitura"
titelName = "Kitura / Stress Test / Low load"
sourcefile1 = './RawLogFiles/stressKituraServerTopV1.txt'
visualizeTop()

# STATS benchmarking Perfect CLIENT
testcase = "STRESSbenchmarkingV1PerfecCLIENT"
titelName = "Perfect / Stress Test / Low load / Client"
sourcefile1 = './RawLogFiles/stressPerfectClientTopV1.txt'
visualizeTopClient()

# STATS benchmarking Vapor CLIENT
testcase = "STRESSbenchmarkingV1VaporCLIENT"
titelName = "Vapor / Stress Test / Low load / Client"
sourcefile1 = './RawLogFiles/stressVaporClientTopV1.txt'
visualizeTopClient()

# STATS benchmarking Kitura CLIENT
testcase = "STRESSbenchmarkingV1KituraCLIENT"
titelName = "Kitura / Stress Test / Low load / Client"
sourcefile1 = './RawLogFiles/stressKituraClientTopV1.txt'
visualizeTopClient()

# ERRR benchmarking V1
testcase = "STRESSbenchmarkingV1ERRORPerfect"
titelName = "Perfect / Low load / Errors"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V1.txt'
visualizeWrk2Errs()

testcase = "STRESSbenchmarkingV1ERRORVapor"
titelName = "Vapor / Low load / Errors"
sourcefile1 = './RawLogFiles/stressVaporClientWrk2V1C.txt'
visualizeWrk2Errs()

testcase = "STRESSbenchmarkingV1ERRORKitura"
titelName = "Kitura / Low load / Errors"
sourcefile1 = './RawLogFiles/stressKituraClientWrk2V1.txt'
visualizeWrk2Errs()

############################################################

# STRESS V2
testcase = "STRESSbenchmarkingV2"
titelName = "Stress Test benchmarking / High Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V2.txt'
visualizeBenchmarks3Groups()

# STRESS V2 Vapor Tools
testcase = "STRESSbenchmarkingVaporManV2"
titelName = "Stress Test benchmarking / High Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/stressVaporClientWrk2V2C.txt'
sourcefile4 = './RawLogFiles/stressKituraClientWrk2V2.txt'
visualizeBenchmarks4Groups()

# STATS benchmarking PerfectV2
testcase = "STRESSbenchmarkingV2Perfect"
titelName = "Perfect / Stress Test / High load"
sourcefile1 = './RawLogFiles/stressPerfectServerTopV2.txt'
visualizeTop()

# STATS benchmarking VaporV2
testcase = "STRESSbenchmarkingV2Vapor"
titelName = "Vapor / Stress Test / High load"
sourcefile1 = './RawLogFiles/stressVaporServerTopV2.txt'
visualizeTop()

# STATS benchmarking VaporV2
testcase = "STRESSbenchmarkingV2VaporMan"
titelName = "Vapor Manual / Stress Test / High load"
sourcefile1 = './RawLogFiles/stressVaporServerTopV2C.txt'
visualizeTop()

# STATS benchmarking KituraV2
testcase = "STRESSbenchmarkingV2Kitura"
titelName = "Kitura / Stress Test / High load"
sourcefile1 = './RawLogFiles/stressKituraServerTopV2.txt'
visualizeTop()

# STATS benchmarking PerfectV2 CLIENT
testcase = "STRESSbenchmarkingV2PerfectCLIENT"
titelName = "Perfect / Stress Test / High load / Client"
sourcefile1 = './RawLogFiles/stressPerfectClientTopV2.txt'
visualizeTopClient()

# STATS benchmarking VaporV2 CLIENT
testcase = "STRESSbenchmarkingV2VaporCLIENT"
titelName = "Vapor / Stress Test / High load / Client"
sourcefile1 = './RawLogFiles/stressVaporClientTopV2.txt'
visualizeTopClient()

# STATS benchmarking KituraV2 CLIENT
testcase = "STRESSbenchmarkingV2KituraCLIENT"
titelName = "Kitura / Stress Test / High load / Client"
sourcefile1 = './RawLogFiles/stressKituraClientTopV2.txt'
visualizeTopClient()

# ERRR benchmarking V2
testcase = "STRESSbenchmarkingV2ERRORPerfect"
titelName = "Perfect / High load / Errors"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V2.txt'
visualizeWrk2Errs()

testcase = "STRESSbenchmarkingV2ERRORVapor"
titelName = "Vapor / High load / Errors"
sourcefile1 = './RawLogFiles/stressVaporClientWrk2V2.txt'
visualizeWrk2Errs()

testcase = "STRESSbenchmarkingV2ERRORKitura"
titelName = "Kitura / High load / Errors"
sourcefile1 = './RawLogFiles/stressKituraClientWrk2V2.txt'
visualizeWrk2Errs()

############################################################

# STRESS V3
testcase = "STRESSbenchmarkingV3"
titelName = "Stress Test benchmarking / Spike Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/stressKituraClientWrk2V3.txt'
visualizeBenchmarks3Groups()

# STRESS V3 Vapor Tools
testcase = "STRESSbenchmarkingV3VaporMan"
titelName = "Stress Test benchmarking / Spike Load"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
sourcefile2 = './RawLogFiles/stressVaporClientWrk2V3.txt'
sourcefile3 = './RawLogFiles/stressVaporClientWrk2V3C.txt'
sourcefile4 = './RawLogFiles/stressKituraClientWrk2V3.txt'
visualizeBenchmarks4Groups()

# STATS benchmarking Perfect V3
testcase = "STRESSbenchmarkingV3Perfect"
titelName = "Perfect / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressPerfectServerTopV3.txt'
visualizeTop()

# STATS benchmarking Vapor V3
testcase = "STRESSbenchmarkingV3Vapor"
titelName = "Vapor / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressVaporServerTopV3.txt'
visualizeTop()

# STATS benchmarking Vapor V3
testcase = "STRESSbenchmarkingV3VaporMan"
titelName = "Vapor Manual / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressVaporServerTopV3C.txt'
visualizeTop()

# STATS benchmarking Kitura V3
testcase = "STRESSbenchmarkingV3Kitura"
titelName = "Kitura / Stress Test / Spike load"
sourcefile1 = './RawLogFiles/stressKituraServerTopV3.txt'
visualizeTop()

# ERRR benchmarking V3
testcase = "STRESSbenchmarkingV3ERRORPerfect"
titelName = "Perfect / Spike load / Errors"
sourcefile1 = './RawLogFiles/stressPerfectClientWrk2V3.txt'
visualizeWrk2Errs()

testcase = "STRESSbenchmarkingV3ERRORVapor"
titelName = "Vapor / Spike load / Errors"
sourcefile1 = './RawLogFiles/stressVaporClientWrk2V3.txt'
visualizeWrk2Errs()

testcase = "STRESSbenchmarkingV3ERRORKitura"
titelName = "Kitura / Spike load / Errors"
sourcefile1 = './RawLogFiles/stressKituraClientWrk2V3.txt'
visualizeWrk2Errs()

# STATS benchmarking Perfect V3 CLIENT
testcase = "STRESSbenchmarkingV3PerfectCLIENT"
titelName = "Perfect / Stress Test / Spike load / Client"
sourcefile1 = './RawLogFiles/stressPerfectClientTopV3.txt'
visualizeTopClient()

# STATS benchmarking Vapor V3 CLIENT
testcase = "STRESSbenchmarkingV3VaporCLIENT"
titelName = "Vapor / Stress Test / Spike load / Client"
sourcefile1 = './RawLogFiles/stressVaporClientTopV3.txt'
visualizeTopClient()

# STATS benchmarking Kitura V3 CLIENT
testcase = "STRESSbenchmarkingV3KituraCLIENT"
titelName = "Kitura / Stress Test / Spike load / Client"
sourcefile1 = './RawLogFiles/stressKituraClientTopV3.txt'
visualizeTopClient()

############################################################

#CROSS REFERENCE

# Cross Reference JSON Ryan Collins
testcase = "CROSSREFjsonV1"
titelName = "Cross Reference / JSON Requests"
sourcefile1 = './CrossReferenceRawData/CCjsonPerfectWrk.txt'
sourcefile2 = './CrossReferenceRawData/CCjsonVaporWrk_IT2.txt'
sourcefile3 = './CrossReferenceRawData/CCjsonKituraWrk.txt'

sourcefile4 = './CrossReferenceRawData/CCjsonPerfectWrk2.txt'
sourcefile5 = './CrossReferenceRawData/CCjsonVaporWrk2_IT2.txt'
sourcefile6 = './CrossReferenceRawData/CCjsonKituraWrk2.txt'
visualizeCR()
