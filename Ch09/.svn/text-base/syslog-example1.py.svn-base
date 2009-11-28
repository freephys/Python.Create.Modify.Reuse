import syslog

print """
Enter a number and press [Enter]:
1 - Emergency
2 - Alert
3 - Critical
4 - Error
5 - Warning
6 - Notics
7 - Info
8 - Debug
"""
choice = raw_input("")

message = raw_input("Type the log message and press [Enter]:  ")

if choice == '1':
	log_priority = syslog.LOG_EMERG
elif choice == '2':
	log_priority = syslog.LOG_ALERT
elif choice == '3':
	log_priority = syslog.LOG_CRIT
elif choice == '4':
	log_priority = syslog.LOG_ERR
elif choice == '5':
	log_priority = syslog.LOG_WARNING
elif choice == '6':
	log_priority = syslog.LOG_NOTICE
elif choice == '7':
	log_priority = syslog.LOG_INFO
elif choice == '8':
	log_priority = syslog.LOG_DEBUG

try:
	syslog.syslog(log_priority, message)
	print "log entry recorded"
except:
	print "problem writing to syslog"
	raise

