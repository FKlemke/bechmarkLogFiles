import os
import time
import re
import toolBox as tb

timeWaitForEphePorts = 15
testParameterWrk =  "wrk -t2 -d30s -c5 --latency --timeout 100s"
httpAdd = " " + "http://169.254.162.211"
directory = "./LogFiles/"
directoryWrk2 = "./LogFilesWrk2/"
wrk2RatePercentage = 0.5
businessCaseReqRate = 100

######################################################################
def logTime(startTime, urlReq, testcase, title):
    with open(directory + testcase + ".txt", "a") as f:
        f.write("\n >> " + "|" + startTime + "|" + testcase + "|" + title)
        f.write("\n" + urlReq)
def startMsg():
    print "benchmark process started @ " + getTime() + " process finish in approx. 3.5 hours... get yourself a cocktail "
def logTimeWrk2(startTime, urlReq, testcase, title):
    with open(directoryWrk2 + testcase + ".txt", "a") as f:
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

def getTime():
    return time.strftime("%Y/%m/%d %H:%M:%S")

def iterateDirectoryForWrk2Test():
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
                    #calc new rate value
                    wrk2RateValue = requests * wrk2RatePercentage

                if "wrk" in line:
                    wrkReq = line.split()
                    fileLogData = getLogData(filename)

                    #run wrk2 test for latency
                    runWrk2Test(wrkReq, wrk2RateValue, filename, fileLogData)
                    #run wrk2 test for latency for business case
                    runWrk2Test(wrkReq, businessCaseReqRate, filename, fileLogData)

def runWrk2Test(wrk2req, wrk2RateValue, filename, fileLogData):
    wrk2req = "wrk2 " + wrk2req[1] + " " + wrk2req[2] + " " + wrk2req[3] \
              + " " + wrk2req[4] + " -R" + str(int(wrk2RateValue)) + " " \
              + wrk2req[5] + " " + wrk2req[6] + " " + wrk2req[7]

    fn = re.findall('[A-Z][^A-Z]*', filename)

    for index, item in enumerate(fn):
        if "Wrk" in item and wrk2RateValue != businessCaseReqRate:
            fn[index] = "Wrk2"
            print "running wrk2 latency test " + filename + " @ " + getTime()
            startTime = getTime()
            path = ''.join(fn)
            testcase = path[:-4]
            time.sleep(timeWaitForEphePorts)
            os.system(wrk2req + " > " + directoryWrk2 + path)
            logTimeWrk2(startTime,wrk2req,testcase,fileLogData[1])

        if "Wrk" in item and wrk2RateValue == businessCaseReqRate:
            fn[index+1] = "V1bc.txt"
            print "running wrk2 latency BC " + filename + " @ " + getTime()
            startTime = getTime()
            path = ''.join(fn)
            testcase = path[:-4]
            time.sleep(timeWaitForEphePorts)
            os.system(wrk2req + " > " + directoryWrk2 + path)
            logTimeWrk2(startTime, wrk2req, testcase, fileLogData[1])

def getLogDataFromFile(srcfile):
    with open(srcfile) as inF:
        lines = inF.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if ">>" in line:
                values = line.split("|")
                fileLogData = [values[2],values[3][:-1]]
                return fileLogData

######################################################################
def jsonTest():
    time.sleep(timeWaitForEphePorts)
    testcase = "JsonPerfectClientWrkV1"
    title = "Perfect JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "JsonVaporClientWrkV1"
    title = "Vapor JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8080/jsonVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "JsonKituraClientWrkV1"
    title = "Kitura JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8282/jsonKitura"
    genericTestRun(testcase, title, path)
def jsonSmallTest():
    time.sleep(timeWaitForEphePorts)
    testcase = "JsonPerfectClientWrkV2"
    title = "Perfect JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase ="JsonVaporClientWrkV2"
    title = "Vapor JSON benchmarking"
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "JsonKituraClientWrkV2"
    title = "Kitura JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)
def htmlTest():
    time.sleep(timeWaitForEphePorts)
    testcase ="HtmlPerfectClientWrkV1"
    title = "Perfect HTML benchmarking"
    path = testParameterWrk+httpAdd +":8181/htmlPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "HtmlVaporClientWrkV1"
    title = "Vapor HTML benchmarking"
    path = testParameterWrk+httpAdd +":8080/htmlVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "HtmlKituraClientWrkV1"
    title = "Kitura HTML benchmarking"
    path = testParameterWrk+httpAdd +":8282/htmlKitura"
    genericTestRun(testcase, title, path)
def plaintextTest():
    time.sleep(timeWaitForEphePorts)
    testcase = "PlaintextPerfectClientWrkV1"
    title = "Perfect plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8081/plaintextPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase ="PlaintextVaporClientWrkV1"
    title = "Vapor plaintext benchmarking"
    path = testParameterWrk + httpAdd +":8080/plaintextVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase ="PlaintextKituraClientWrkV1"
    title = "Kitura plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8282/plaintextKitura"
    genericTestRun(testcase, title, path)
def genericTestRun(testcase, title, urlReg):
    print "running wrk test for " + title + " @ " + time.strftime("%Y/%m/%d %H:%M:%S")
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

    tb.visusalizeWrkVsWrk2ValueSets(title, tcValues1, tcValues2, tcValues3, tcValues4, testcase)
######################################################################
def runPerfect():
    time.sleep(timeWaitForEphePorts)
    testcase = "JsonPerfectClientWrkV1"
    title = "Perfect JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "JsonPerfectClientWrkV2"
    title = "Perfect JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase ="HtmlPerfectClientWrkV1"
    title = "Perfect HTML benchmarking"
    path = testParameterWrk+httpAdd +":8181/htmlPerfect"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "PlaintextPerfectClientWrkV1"
    title = "Perfect plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8081/plaintextPerfect"
    genericTestRun(testcase, title, path)
def runVapor():
    time.sleep(timeWaitForEphePorts)
    testcase = "JsonVaporClientWrkV1"
    title = "Vapor JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8080/jsonVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase ="JsonVaporClientWrkV2"
    title = "Vapor JSON benchmarking"
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "HtmlVaporClientWrkV1"
    title = "Vapor HTML benchmarking"
    path = testParameterWrk+httpAdd +":8080/htmlVapor"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase ="PlaintextVaporClientWrkV1"
    title = "Vapor plaintext benchmarking"
    path = testParameterWrk + httpAdd +":8080/plaintextVapor"
    genericTestRun(testcase, title, path)
def runKitura():
    time.sleep(timeWaitForEphePorts)
    testcase = "JsonKituraClientWrkV1"
    title = "Kitura JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8282/jsonKitura"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "JsonKituraClientWrkV2"
    title = "Kitura JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "HtmlKituraClientWrkV1"
    title = "Kitura HTML benchmarking"
    path = testParameterWrk + httpAdd + ":8282/htmlKitura"
    genericTestRun(testcase, title, path)

    time.sleep(timeWaitForEphePorts)
    testcase = "PlaintextKituraClientWrkV1"
    title = "Kitura plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8282/plaintextKitura"
    genericTestRun(testcase, title, path)

def runVisual():
    srcfile1P = "./LogFiles/JsonPerfectClientWrkV1.txt"
    srcfile1V = "./LogFiles/JsonVaporClientWrkV1.txt"
    srcfile1K = "./LogFiles/JsonKituraClientWrkV1.txt"
    srcfile1List = [srcfile1P,srcfile1V,srcfile1K]

    srcfile2P = "./LogFilesWrk2/JsonPerfectClientWrk2V1.txt"
    srcfile2V = "./LogFilesWrk2/JsonVaporClientWrk2V1.txt"
    srcfile2K = "./LogFilesWrk2/JsonKituraClientWrk2V1.txt"
    srcfile2List = [srcfile2P,srcfile2V,srcfile2K]

    srcfile3P = "./LogFilesWrk2/JsonPerfectClientWrk2V1bc.txt"
    srcfile3V = "./LogFilesWrk2/JsonVaporClientWrk2V1bc.txt"
    srcfile3K = "./LogFilesWrk2/JsonKituraClientWrk2V1bc.txt"
    srcfile3List = [srcfile3P,srcfile3V,srcfile3K]

    logData = getLogDataFromFile(srcfile1P)
    parseAndVisualizeWrkVsWrk2(logData[0], logData[1], srcfile1List,srcfile2List,srcfile3List)

    srcfile1P = "./LogFiles/JsonPerfectClientWrkV2.txt"
    srcfile1V = "./LogFiles/JsonVaporClientWrkV2.txt"
    srcfile1K = "./LogFiles/JsonKituraClientWrkV2.txt"
    srcfile1List = [srcfile1P, srcfile1V, srcfile1K]

    srcfile2P = "./LogFilesWrk2/JsonPerfectClientWrk2V2.txt"
    srcfile2V = "./LogFilesWrk2/JsonVaporClientWrk2V2.txt"
    srcfile2K = "./LogFilesWrk2/JsonKituraClientWrk2V2.txt"
    srcfile2List = [srcfile2P, srcfile2V, srcfile2K]

    srcfile3P = "./LogFilesWrk2/JsonPerfectClientWrk2V2bc.txt"
    srcfile3V = "./LogFilesWrk2/JsonVaporClientWrk2V2bc.txt"
    srcfile3K = "./LogFilesWrk2/JsonKituraClientWrk2V2bc.txt"
    srcfile3List = [srcfile3P, srcfile3V, srcfile3K]

    logData = getLogDataFromFile(srcfile1P)
    parseAndVisualizeWrkVsWrk2(logData[0], logData[1], srcfile1List, srcfile2List, srcfile3List)

    srcfile1P = "./LogFiles/HtmlPerfectClientWrkV1.txt"
    srcfile1V = "./LogFiles/HtmlVaporClientWrkV1.txt"
    srcfile1K = "./LogFiles/HtmlKituraClientWrkV1.txt"
    srcfile1List = [srcfile1P,srcfile1V,srcfile1K]

    srcfile2P = "./LogFilesWrk2/HtmlPerfectClientWrk2V1.txt"
    srcfile2V = "./LogFilesWrk2/HtmlVaporClientWrk2V1.txt"
    srcfile2K = "./LogFilesWrk2/HtmlKituraClientWrk2V1.txt"
    srcfile2List = [srcfile2P,srcfile2V,srcfile2K]

    srcfile3P = "./LogFilesWrk2/HtmlPerfectClientWrk2V1bc.txt"
    srcfile3V = "./LogFilesWrk2/HtmlVaporClientWrk2V1bc.txt"
    srcfile3K = "./LogFilesWrk2/HtmlKituraClientWrk2V1bc.txt"
    srcfile3List = [srcfile3P,srcfile3V,srcfile3K]

    logData = getLogDataFromFile(srcfile1P)
    parseAndVisualizeWrkVsWrk2(logData[0], logData[1], srcfile1List,srcfile2List,srcfile3List)

    srcfile1P = "./LogFiles/PlaintextPerfectClientWrkV1.txt"
    srcfile1V = "./LogFiles/PlaintextVaporClientWrkV1.txt"
    srcfile1K = "./LogFiles/PlaintextKituraClientWrkV1.txt"
    srcfile1List = [srcfile1P,srcfile1V,srcfile1K]

    srcfile2P = "./LogFilesWrk2/PlaintextPerfectClientWrk2V1.txt"
    srcfile2V = "./LogFilesWrk2/PlaintextVaporClientWrk2V1.txt"
    srcfile2K = "./LogFilesWrk2/PlaintextKituraClientWrk2V1.txt"
    srcfile2List = [srcfile2P,srcfile2V,srcfile2K]

    srcfile3P = "./LogFilesWrk2/PlaintextPerfectClientWrk2V1bc.txt"
    srcfile3V = "./LogFilesWrk2/PlaintextVaporClientWrk2V1bc.txt"
    srcfile3K = "./LogFilesWrk2/PlaintextKituraClientWrk2V1bc.txt"
    srcfile3List = [srcfile3P,srcfile3V,srcfile3K]

    logData = getLogDataFromFile(srcfile1P)
    parseAndVisualizeWrkVsWrk2(logData[0], logData[1], srcfile1List,srcfile2List,srcfile3List)

startMsg()

runPerfect()
runVapor()
runKitura()

# jsonTest()
# jsonSmallTest()
# htmlTest()
# plaintextTest()

# testMethod()
iterateDirectoryForWrk2Test()
alarm()


