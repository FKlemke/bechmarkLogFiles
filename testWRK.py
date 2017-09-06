import os
import time
import re
import toolBox as tb

timeWaitForEphePorts = 5
testParameterWrk =  "wrk -t2 -d65s -c10 --latency --timeout 100s"
httpAdd = " http://169.254.90.222"
directory = "./LogFiles/"
wrk2RatePercentage = 0.5
useCaseRequestSecValue = 100


######################################################################

def logTime(startTime, urlReq, testcase, title):
    with open(directory + testcase + ".txt", "a") as f:
        f.write("\n >> " + "|" + startTime + "|" + testcase + "|" + title)
        f.write("\n" + urlReq)

def getLogData(filename):
    with open(directory + filename) as inF:
        lines = inF.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if ">>" in line:
                values = line.split("|")
                fileLogData = [values[2],values[3][:-1]]
                return fileLogData

    # with open(directory + filename, "a") as f:
    #     f.write("\n >> " + " | " + time.strftime(
    #         "%Y/%m/%d %H:%M:%S") + " | " + testcase + " | " + title + "\n" + path + "\n")

def getTime():
    return time.strftime("%Y/%m/%d %H:%M:%S")

def iterateDirectoryForWrk2Test():
    print "iterating directory to process wrk2 tests"
    time.sleep(10)
    for filename in os.listdir(directory):
        with open(directory + filename) as inF:
            lines = inF.readlines()
            requests = 0
            wrk2RateValue = 0

            for i in range(0, len(lines)):
                line = lines[i]
                if "Requests/sec:" in line:
                    values = line.split()
                    requests = float(values[1])
                    wrk2RateValue = requests * wrk2RatePercentage
                if "wrk" in line:
                    values = line.split()
                    fileLogData = getLogData(filename)
                    runWrk2Test(values, wrk2RateValue, filename, fileLogData)
                    #run here for business case
                    runWrk2Test(values,useCaseRequestSecValue,filename, fileLogData)

def runWrk2Test(wrk2req, wrk2RateValue, filename, fileLogData):
    wrk2req = "wrk2 " + wrk2req[1] + " " + wrk2req[2] + " " + wrk2req[3] \
              + " " + wrk2req[4] + " -R" + str(int(wrk2RateValue)) + " " \
              + wrk2req[5] + " " + wrk2req[6] + " " + wrk2req[7]

    fn = re.findall('[A-Z][^A-Z]*', filename)
    for index, item in enumerate(fn):
        if "Wrk" in item and not wrk2RateValue == useCaseRequestSecValue:
            fn[index] = "Wrk2"
            print "running wrk2 latency test " + filename
            startTime = getTime()
            path = ''.join(fn)
            os.system(wrk2req + " > " + directory + path)
            logTime(fileLogData[0],fileLogData[1],path,startTime)

        if "Wrk" in item and wrk2RateValue == useCaseRequestSecValue:
            fn[index+1] = "V1bc.txt"
            print "running wrk2 latency test for business case " + filename
            startTime = getTime()
            path = ''.join(fn)
            os.system(wrk2req + " > " + directory + path)
            logTime(fileLogData[0], fileLogData[1], path, startTime)

######################################################################
def jsonTest():
    time.sleep(timeWaitForEphePorts)
    testcase = "JsonPerfectClientWrkV1"
    title = "Perfect JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    genericTestRun(testcase, title, path)

    testcase = "JsonVaporClientWrkV1"
    title = "Vapor JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8080/jsonVapor"
    genericTestRun(testcase, title, path)

    testcase = "JsonKituraClientWrkV1"
    title = "Kitura JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8282/jsonKitura"
    genericTestRun(testcase, title, path)
def jsonSmallTest():
    os.system('echo "WRK test started"')
    testcase = "JsonPerfectClientWrkV2"
    title = "Perfect JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    testcase ="JsonVaporClientWrkV2"
    title = "Vapor JSON benchmarking"
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    testcase = "JsonKituraClientWrkV2"
    title = "Kitura JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)
def htmlTest():
    testcase ="HtmlPerfectClientWrkV1"
    title = "Perfect HTML benchmarking"
    path = testParameterWrk+httpAdd +":8181/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    testcase = "HtmlVaporClientWrkV1"
    title = "Vapor HTML benchmarking"
    path = testParameterWrk+httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    testcase = "HtmlKituraClientWrkV1"
    title = "Kitura HTML benchmarking"
    path = testParameterWrk+httpAdd +":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)
def plaintextTest():
    testcase = "PlaintextPerfectClientWrkV1"
    title = "Perfect plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    testcase ="PlaintextVaporClientWrkV1"
    title = "Vapor plaintext benchmarking"
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    testcase ="PlaintextKituraClientWrkV1"
    title = "Kitura plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)

def genericTestRun(testcase, title, urlReg):
    print "starting wrk test for " + title + " " + time.strftime("%Y/%m/%d %H:%M:%S")
    startTime = getTime()
    os.system(urlReg + " > " + directory + testcase + ".txt")
    logTime(startTime,urlReg,testcase,title)
    time.sleep(timeWaitForEphePorts)
######################################################################
def testMethod():
    testcase = "JsonPerfectClientWrkV1"
    title = "Perfect JSON benchmarking / Business case"
    urlReg = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    genericTestRun(testcase, title, urlReg)

def alarm():
    os.system('say -v Veena "put down that cocktail felix, your benchmarks are ready!"')
######################################################################
def parseAndVisualizeWrkVsWrk2(testcase, title, srcfile1List, srcfile2List, srcfile3List):
    tcValues1 = []
    tcValues2 = []
    tcValues3 = []
    tcValues4 = []
    targetfile = 'datalyzed/csv/' + testcase + '.csv'
    tb.setHeaderLatRegSec(targetfile)
    for srcfile in srcfile1List:
        tcValues1, tcValues2 = tb.parseHeaderWrk(srcfile, tcValues1, tcValues2, targetfile)
    for srcfile in srcfile2List:
        tcValues3 = tb.parseHeaderWrk2VsWrkVal(srcfile, tcValues3, targetfile)
    for srcfile in srcfile3List:
        tcValues4 = tb.parseHeaderWrk2VsWrkVal(srcfile, tcValues4, targetfile)

    print tcValues1
    print tcValues2
    print tcValues3
    print tcValues4

    tb.visusalizeWrkVsWrk2ValueSets(title, tcValues1, tcValues2, tcValues3, tcValues4, testcase)

# jsonTest()
# jsonSmallTest()
# htmlTest()
# plaintextTest()
testMethod()
iterateDirectoryForWrk2Test()
alarm()

# srcfile1P = "./LogFiles/JsonPerfectClientWrkV1.txt"
# srcfile1V = "./LogFiles/JsonVaporClientWrkV1.txt"
# srcfile1K = "./LogFiles/JsonKituraClientWrkV1.txt"
# srcfile1List = [srcfile1P,srcfile1V,srcfile1K]
#
# srcfile2P = "./LogFiles/JsonPerfectClientWrk2V1.txt"
# srcfile2V = "./LogFiles/JsonVaporClientWrk2V1.txt"
# srcfile2K = "./LogFiles/JsonKituraClientWrk2V1.txt"
# srcfile2List = [srcfile2P,srcfile2V,srcfile2K]
#
# srcfile3P = "./LogFiles/JsonPerfectClientWrk2V1bc.txt"
# srcfile3V = "./LogFiles/JsonVaporClientWrk2V1bc.txt"
# srcfile3K = "./LogFiles/JsonKituraClientWrk2V1bc.txt"
# srcfile3List = [srcfile3P,srcfile3V,srcfile3K]
#
# parseAndVisualizeWrkVsWrk2("test", "testtitle", srcfile1List,srcfile2List,srcfile3List)
