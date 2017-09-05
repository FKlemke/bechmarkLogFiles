import os
import time


def logTime(testcase, title):
    with open("./"+ testcase, "a") as f:
        f.write("\n" + time.strftime("%Y/%m/%d %H:%M:%S") + " " + testcase[:-4] + " " + title + "\n")

timeWait = 20
testParameterWrk =  "wrk -t2 -d20s -c100 --latency --timeout 2s"
httpAdd = "http://169.254.90.222"


def plaintextTest():
    testcase = "PLAINTEXTbenchmarkingV1Perfect.txt"
    title = "Perfect plaintext benchmarking"
    print title
    os.system(testParameterWrk + httpAdd + ":8081/jsonShortPerfect > "
              + testcase)
    logTime(testcase, title)
    time.sleep(timeWait)

    testcase = "PLAINTEXTbenchmarkingV1Vapor.txt"
    title = "Vapor plaintext benchmarking"
    print title
    os.system(testParameterWrk + httpAdd +":8080/jsonShortVapor > "
              + testcase)
    logTime(testcase, title)
    time.sleep(timeWait)

    testcase = "PLAINTEXTbenchmarkingV1Kitura.txt"
    title = "Kitura plaintext benchmarking"
    print title
    os.system(testParameterWrk + httpAdd + ":8282/jsonShortKitura > "
              + testcase)
    logTime(testcase, title)
    time.sleep(timeWait)


def jsonTest():
    time.sleep(timeWait)
    testcase = "JSONbenchmarkingV1Perfect.txt"
    title = "Perfect JSON benchmarking"
    print title
    os.system(testParameterWrk +httpAdd +":8081/jsonPerfect > "
              + testcase)
    logTime(testcase,title)
    time.sleep(timeWait)

    testcase = "JSONbenchmarkingV1Vapor.txt"
    title = "Vapor JSON benchmarking"
    print title
    os.system(testParameterWrk+ httpAdd +":8080/jsonVapor > "
              + testcase)
    logTime(testcase,title)
    time.sleep(timeWait)

    testcase = "JSONbenchmarkingV1Kitura.txt"
    title = "Kitura JSON benchmarking"
    print title
    os.system(testParameterWrk+httpAdd +":8282/jsonKitura > "
              + testcase)
    logTime(testcase,title)
    time.sleep(timeWait)

def jsonSmallTest():
    os.system('echo "WRK test started"')
    testcase = "JSONbenchmarkingV2Perfect.txt"

    title = "Perfect JSON benchmarking / Small"
    print title
    os.system(testParameterWrk + httpAdd + ":8081/jsonShortPerfect > "
              + testcase)
    logTime(testcase, title)
    time.sleep(timeWait)

    testcase = "JSONbenchmarkingV2Vapor.txt"
    title = "Vapor JSON benchmarking / Small"
    print title
    os.system(testParameterWrk + httpAdd +":8080/jsonShortVapor > "
              + testcase)
    logTime(testcase, title)
    time.sleep(timeWait)

    testcase = "JSONbenchmarkingV1Kitura.txt"
    title = "Kitura JSON benchmarking / Small"
    print title
    os.system(testParameterWrk + httpAdd + ":8282/jsonShortKitura > "
              + testcase)
    logTime(testcase, title)
    time.sleep(timeWait)

def htmlTest():
    testcase = "HTMLbenchmarkingV1Perfect.txt"
    title = "Perfect HTML benchmarking"
    print title
    os.system(testParameterWrk+httpAdd +":8181/jsonShortPerfect > "
              + testcase)
    logTime(testcase,title)
    time.sleep(timeWait)

    testcase = "HTMLbenchmarkingV1Vapor.txt"
    title = "Vapor HTML benchmarking"
    print title
    os.system(testParameterWrk+httpAdd +":8080/jsonShortVapor > "
              + testcase)
    logTime(testcase,title)
    time.sleep(timeWait)

    testcase = "HTMLbenchmarkingV1Kitura.txt"
    title = "Kitura HTML benchmarking"
    print title
    os.system(testParameterWrk+httpAdd +":8282/jsonShortKitura > "
              + testcase)
    logTime(testcase,title)
    time.sleep(timeWait)

######################################
os.system('echo "WRK test started"')##
######################################

jsonTest()