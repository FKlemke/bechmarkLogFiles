import os
import time

# time out between testruns set to 3min
timeOutSec = 120
# ipAdressServer = '192.168.9.132'
# ipAdressLocal = 'http://localhost:8080'
route = "http://169.254.247.94:"
tool = "wrk -d 10m -t 4 -c 20 "
tool2 = "wrk2 -d 10m -t 4 -c 20 -R20 --latency "

os.system("echo 'BENCHMARK test initiated'")

# os.system("echo 'Perfect starting ' date")
# filePath = "CCjsonPerfectWrk.txt"
# os.system(tool + route + "8181/json > " + filePath)
# os.system("echo 'Perfect stoped ' date")
# time.sleep(timeOutSec)
#
os.system("echo 'Vapor starting ' date")
filePath = "CCjsonVaporWrk_IT2.txt"
os.system(tool + route + "8080/json >" + filePath)
os.system("echo 'Vapor stoped ' date")
time.sleep(timeOutSec)
#
# os.system("echo 'Kitura starting ' date")
# filePath = "CCjsonKituraWrk.txt"
# os.system(tool + route + "8090/json > " + filePath)
# os.system("echo 'Kitura stoped ' date")
# time.sleep(timeOutSec)

###########################################
os.system("echo 'wrk Test ended'")
###########################################

# os.system("echo 'Perfect starting ' date")
# filePath = "CCjsonPerfectWrk2.txt"
# os.system(tool2 + route + "8181/json > " + filePath)
# os.system("echo 'Perfect stoped ' date")
# time.sleep(timeOutSec)

os.system("echo 'Vapor starting ' date")
filePath = "CCjsonVaporWrk2_IT2.txt"
os.system(tool2 + route + "8080/json >" + filePath)
os.system("echo 'Vapor stoped ' date")
time.sleep(timeOutSec)

# os.system("echo 'Kitura starting ' date")
# filePath = "CCjsonKituraWrk2.txt"
# os.system(tool2 + route + "8090/json > " + filePath)
# os.system("echo 'Kitura stoped ' date")
# time.sleep(timeOutSec)

os.system("echo 'wrk2 Test ended'")