import os
import time
import re
import toolBox

timeWaitForEphePorts = 15
testParameterWrk =  "wrk -t2 -d20s -c10 --latency --timeout 100s"
httpAdd = " http://169.254.90.222"
directory = "./LogFiles/"
wrk2RatePercentage = 0.5
useCaseRequestSecValue = 100


######################################################################
def logTime(testcase, title, urlPath):
    with open(directory + testcase + ".txt", "a") as f:
        f.write("\n" + time.strftime("%Y/%m/%d %H:%M:%S") + " " + testcase + " " + title + "\n" + path + "\n")

def iterateDirectoryForWrk2Test():
    print "Iterating directory to process wrk2 tests"
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
                    runWrk2Test(values, wrk2RateValue, filename)
                    runWrk2Test(values,useCaseRequestSecValue,filename)

def runWrk2Test(wrk2req, wrk2RateValue, filename):
    wrk2req = "wrk2 " + wrk2req[1] + " " + wrk2req[2] + " " + wrk2req[3] \
              + " " + wrk2req[4] + " -R" + str(int(wrk2RateValue)) + " " \
              + wrk2req[5] + " " + wrk2req[6] + " " + wrk2req[7]
    fn = re.findall('[A-Z][^A-Z]*', filename)
    for index, item in enumerate(fn):
        if "Wrk" in item:
            fn[index] = "Wrk2"
            if wrk2RateValue == useCaseRequestSecValue:
                list2oString = ''.join(fn)[:-1]
                list2oString += "3"
                os.system(wrk2req + " > " + directory + list2oString)
            else:
                os.system(wrk2req + " > " + directory + ''.join(fn))



def jsonTest():
    time.sleep(timeWaitForEphePorts)
    testcase = directory + "JsonPerfectClientWrkV1"
    title = "Perfect JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    genericTestRun(testcase, title, path)

    testcase = directory + "JsonVaporClientWrkV1"
    title = "Vapor JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8080/jsonVapor"
    genericTestRun(testcase, title, path)

    testcase = directory + "JsonKituraClientWrkV1"
    title = "Kitura JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8282/jsonKitura"
    genericTestRun(testcase, title, path)
def jsonSmallTest():
    os.system('echo "WRK test started"')
    testcase = directory + "JsonPerfectClientWrkV2"
    title = "Perfect JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    testcase = directory + "JsonVaporClientWrkV2"
    title = "Vapor JSON benchmarking"
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    testcase = directory + "JsonKituraClientWrkV2"
    title = "Kitura JSON benchmarking"
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)
def htmlTest():
    testcase = directory + "HtmlPerfectClientWrkV1"
    title = "Perfect HTML benchmarking"
    path = testParameterWrk+httpAdd +":8181/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    testcase = directory + "HtmlVaporClientWrkV1"
    title = "Vapor HTML benchmarking"
    path = testParameterWrk+httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    testcase = directory + "HtmlKituraClientWrkV1"
    title = "Kitura HTML benchmarking"
    path = testParameterWrk+httpAdd +":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)
def plaintextTest():
    testcase = directory + "PlaintextPerfectClientWrkV1"
    title = "Perfect plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    genericTestRun(testcase, title, path)

    testcase = directory + "PlaintextVaporClientWrkV1"
    title = "Vapor plaintext benchmarking"
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    genericTestRun(testcase, title, path)

    testcase = directory + "PlaintextKituraClientWrkV1"
    title = "Kitura plaintext benchmarking"
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    genericTestRun(testcase, title, path)

def genericTestRun(testcase, title, path):
    print title
    os.system(path + " > " + directory + testcase + ".txt")
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)
######################################################################


def testMethod():
    testcase = "JsonPerfectClientWrkV1"
    title = "Perfect JSON benchmarking / Business case"
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    genericTestRun(testcase, title, path)
######################################################################

# jsonTest()
# jsonSmallTest()
# htmlTest()
# plaintextTest()
testMethod()
iterateDirectoryForWrk2Test()