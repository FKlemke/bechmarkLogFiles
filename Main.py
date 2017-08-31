import ToolBox

##run this file for generation of csv and image files
plotVal1 = []
plotVal2 = []



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

plotVal1 = ToolBox.parseBuildTimes(sourcefile1,plotVal1,targetfile)
plotVal1 = ToolBox.parseBuildTimes(sourcefile2,plotVal1,targetfile)
plotVal1 = ToolBox.parseBuildTimes(sourcefile3,plotVal1,targetfile)
plotVal2 = ToolBox.parseBuildTimes(sourcefile4,plotVal2,targetfile)
plotVal2 = ToolBox.parseBuildTimes(sourcefile5,plotVal2,targetfile)
plotVal2 = ToolBox.parseBuildTimes(sourcefile6,plotVal2,targetfile)
ToolBox.visusalizeBuildTimes(titelName,plotVal1,plotVal2,testcase)

# JSON V1
testcase = "JSONbenchmarkingV1"
titelName = "JSON benchmarking"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V1.txt'
plotVal1 = []
plotVal2 = []

targetfile = 'datalyzed/csv/' + testcase + '.csv'

ToolBox.setHeaderLatRegSec(targetfile)
plotVal1, plotVal2 = ToolBox.parseHeaderWrk2(sourcefile1,plotVal1,plotVal2,targetfile)
plotVal1, plotVal2 = ToolBox.parseHeaderWrk2(sourcefile2,plotVal1,plotVal2,targetfile)
plotVal1, plotVal2 = ToolBox.parseHeaderWrk2(sourcefile3,plotVal1,plotVal2,targetfile)

ToolBox.visusalize3Vals(titelName,plotVal1,plotVal2,testcase)

# JSON V2
testcase = "JSONbenchmarkingV2"
titelName = "JSON benchmarking / Non generated"
sourcefile1 = './RawLogFiles/jsonPerfectClientWrk2V2.txt'
sourcefile2 = './RawLogFiles/jsonVaporClientWrk2V2.txt'
sourcefile3 = './RawLogFiles/jsonKituraClientWrk2V2.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testcase + '.csv'

ToolBox.setHeaderLatRegSec(targetfile)
plotVal1, plotVal2 = ToolBox.parseHeaderWrk2(sourcefile1,plotVal1,plotVal2,targetfile)
plotVal1, plotVal2 = ToolBox.parseHeaderWrk2(sourcefile2,plotVal1,plotVal2,targetfile)
plotVal1, plotVal2 = ToolBox.parseHeaderWrk2(sourcefile3,plotVal1,plotVal2,targetfile)

ToolBox.visusalize3Vals(titelName,plotVal1,plotVal2,testcase)

# HTML V1
testCase = "HTMLbenchmarkingV1"
titelName = "HTML benchmarking"
sourcefile1 = './RawLogFiles/htmlPerfectClientWrk2V1.txt'
sourcefile2 = './RawLogFiles/htmlVaporClientWrk2V1.txt'
sourcefile3 = './RawLogFiles/htmlKituraClientWrk2V1.txt'
plotVal1 = []
plotVal2 = []
targetfile = 'datalyzed/csv/' + testCase + '.csv'