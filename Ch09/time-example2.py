import time

print "GMT Time as tuple:  ", time.gmtime()
print "GMT Time as string: ", time.asctime(time.gmtime())
print "Local Time as tuple:  ", time.localtime()
print "Local time as string:  ", time.asctime(time.localtime())
print "Formatted local time in <month day, year> format:  ", \
      time.strftime("%B %d, %Y")