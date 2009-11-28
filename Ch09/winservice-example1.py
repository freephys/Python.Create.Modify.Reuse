import win32serviceutil, time

def service_info(action, machine, service):
    if action == 'stop': 
        win32serviceutil.StopService(service, machine)
        print '%s stopped successfully' % service
        time.sleep(3)
    elif action == 'start': 
        win32serviceutil.StartService(service, machine)
        print '%s started successfully' % service
        time.sleep(3)
    elif action == 'restart': 
        win32serviceutil.RestartService(service, machine)
        print '%s restarted successfully' % service
        time.sleep(3)
    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            print "%s is running normally" % service 
        else:
            print "%s is *not* running" % service

machine = 'localhost'
service = 'RemoteRegistry'

service_info('start', machine, service)
service_info('stop', machine, service)
service_info('start', machine, service)
service_info('restart', machine, service)
service_info('status', machine, service)