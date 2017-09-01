import os
import time

# time out between testruns set to 3min
timeOutSec = 180
ipAdressServer = '192.168.9.132'
ipAdressLocal = 'http://localhost:8080'

os.system("echo 'This test will run for quite some time and log wrk2 test data for iteration B adn C'")
os.system("ls -q")
os.system("echo 'Test of 5 sec delay commencing'")
time.sleep(5)
os.system("echo 'Test of 5 sec delay ended'")