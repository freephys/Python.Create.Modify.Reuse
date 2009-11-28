import time

raw_input("Press the [Enter] key: ")
time1 = time.time()
raw_input("Wait a few seconds, then press the [Enter] key again: ")
time2 = time.time()
difference = int(time2 - time1)

print "There were ",  difference, "seconds bettween the two choices"