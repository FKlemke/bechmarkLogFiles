import os
import time


def logTime(testcase, title):
    with open("./"+ testcase, "a") as f:
        f.write("\n" + time.strftime("%Y/%m/%d %H:%M:%S") + " " + testcase[:-4] + " " + title + "\n")


timeOutSec = 120
######################################
os.system('echo "WRK test started"')##
######################################

testcase = "JSONbenchmarkingV1Perfect.txt"
title = "Perfect JSON benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonPerfect > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "JSONbenchmarkingV1Vapor.txt"
title = "Vapor JSON benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonVapor > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "JSONbenchmarkingV1Kitura.txt"
title = "Kitura JSON benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonKitura > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

################################################################################################
# JSON 2

os.system('echo "WRK test started"')
testcase = "JSONbenchmarkingV2Perfect.txt"

title = "Perfect JSON benchmarking / Small"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortPerfect > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "JSONbenchmarkingV2Vapor.txt"
title = "Vapor JSON benchmarking / Small"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortVapor > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "JSONbenchmarkingV1Kitura.txt"
title = "Kitura JSON benchmarking / Small"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortKitura > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

################################################################################################
# HTML

testcase = "HTMLbenchmarkingV1Perfect.txt"
title = "Perfect HTML benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortPerfect > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "HTMLbenchmarkingV1Vapor.txt"
title = "Vapor HTML benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortVapor > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "HTMLbenchmarkingV1Kitura.txt"
title = "Kitura HTML benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortKitura > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

################################################################################################
# PLAINTEXT

testcase = "PLAINTEXTbenchmarkingV1Perfect.txt"
title = "Perfect plaintext benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortPerfect > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "PLAINTEXTbenchmarkingV1Vapor.txt"
title = "Vapor plaintext benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortVapor > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)

testcase = "PLAINTEXTbenchmarkingV1Kitura.txt"
title = "Kitura plaintext benchmarking"
print title
os.system("wrk -t2 -d10s -c100 --latency --timeout 2s http://169.254.90.222:8081/jsonShortKitura > "
          + testcase)
logTime(testcase,title)
time.sleep(timeOutSec)