import resource

resourcelist = ['time in user mode',
'time in system mode',
'maximum resident set size',
'shared memory size',
'unshared memory size',
'unshared stack size',
'page faults not requiring I//O',
'page faults requiring I//O',
'number of swap outs',
'block input operations',
'block output operations',
'messages sent',
'messages received',
'signals received',
'voluntary context switches',
'involuntary context switches']

getresource = resource.getrusage(resource.RUSAGE_SELF)

for i, item in enumerate(resourcelist):
	print item, ":  ", getresource[i]

