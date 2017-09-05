import os
import time

timeWaitForEphePorts = 3
testParameterWrk =  "wrk -t2 -d10s -c10 --latency --timeout 100s"
httpAdd = " http://169.254.90.222"
directory = "./LogFiles/"
wrk2RatePercentage = 0.5

#####################################################################################################
def logTime(testcase, title, path):
    with open("./"+ testcase, "a") as f:
        f.write("\n" + time.strftime("%Y/%m/%d %H:%M:%S") + " " + testcase[:-4] + " " + title + "\n" + path + "\n")



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
                    runWrk2Test(values, wrk2RateValue)

def runWrk2Test(wrk2req, wrk2RateValue):
    wrk2req = "wrk2 " + wrk2req[1] + " " + wrk2req[2] + " " + wrk2req[3] + " " + wrk2req[4] + " -R" + str(int(wrk2RateValue)) + " " + wrk2req[5] + " " + wrk2req[6] + " " + wrk2req[7]
    os.system(wrk2req)


def jsonTest():
    time.sleep(timeWaitForEphePorts)
    testcase = directory + "JSONbenchmarkingV1Perfect.txt"
    title = "Perfect JSON benchmarking / Business case"
    print title
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "JSONbenchmarkingV1Vapor.txt"
    title = "Vapor JSON benchmarking / Business case"
    print title
    path = testParameterWrk + httpAdd + ":8080/jsonVapor"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "JSONbenchmarkingV1Kitura.txt"
    title = "Kitura JSON benchmarking / Business case"
    print title
    path = testParameterWrk + httpAdd + ":8282/jsonKitura"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

def jsonSmallTest():
    os.system('echo "WRK test started"')
    testcase = directory + "JSONbenchmarkingV2Perfect.txt"
    title = "Perfect JSON benchmarking"
    print title
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "JSONbenchmarkingV2Vapor.txt"
    title = "Vapor JSON benchmarking"
    print title
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "JSONbenchmarkingV1Kitura.txt"
    title = "Kitura JSON benchmarking"
    print title
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)
def htmlTest():
    testcase = directory + "HTMLbenchmarkingV1Perfect.txt"
    title = "Perfect HTML benchmarking"
    print title
    path = testParameterWrk+httpAdd +":8181/jsonShortPerfect"
    os.system(path + " > " + testcase)
    logTime(testcase,title,path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "HTMLbenchmarkingV1Vapor.txt"
    title = "Vapor HTML benchmarking"
    print title
    path = testParameterWrk+httpAdd +":8080/jsonShortVapor"
    os.system(path+" > " + testcase)
    logTime(testcase,title,path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "HTMLbenchmarkingV1Kitura.txt"
    title = "Kitura HTML benchmarking"
    print title
    path = testParameterWrk+httpAdd +":8282/jsonShortKitura"
    os.system(path+" > " + testcase)
    logTime(testcase,title,path)
    time.sleep(timeWaitForEphePorts)
def plaintextTest():
    testcase = directory + "PLAINTEXTbenchmarkingV1Perfect.txt"
    title = "Perfect plaintext benchmarking"
    print title
    path = testParameterWrk + httpAdd + ":8081/jsonShortPerfect"
    os.system(path + " > " + testcase)
    logTime(testcase, title,path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "PLAINTEXTbenchmarkingV1Vapor.txt"
    title = "Vapor plaintext benchmarking"
    print title
    path = testParameterWrk + httpAdd +":8080/jsonShortVapor"
    os.system(path + " > " + testcase)
    logTime(testcase, title,path)
    time.sleep(timeWaitForEphePorts)

    testcase = directory + "PLAINTEXTbenchmarkingV1Kitura.txt"
    title = "Kitura plaintext benchmarking"
    print title
    path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

def testMethod():
    # time.sleep(timeWaitForEphePorts)
    # testcase = directory +  "PLAINTEXTbenchmarkingV1Kitura.txt"
    # title = "Kitura plaintext benchmarking"
    # print title
    # path = testParameterWrk + httpAdd + ":8282/jsonShortKitura"
    # os.system(path + " > " + testcase)
    # logTime(testcase, title, path)
    # time.sleep(timeWaitForEphePorts)

    time.sleep(timeWaitForEphePorts)
    testcase = directory + "JSONbenchmarkingV1Perfect.txt"
    title = "Perfect JSON benchmarking / Business case"
    print title
    path = testParameterWrk + httpAdd + ":8081/jsonPerfect"
    os.system(path + " > " + testcase)
    logTime(testcase, title, path)
    time.sleep(timeWaitForEphePorts)

#####################################################################################################

# jsonTest()
# jsonSmallTest()
# htmlTest()
# plaintextTest()
testMethod()
iterateDirectoryForWrk2Test()