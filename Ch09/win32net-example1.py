import win32net

#print users
users = win32net.NetUserEnum('localhost', 0)
print "USERS"
print "=========="
for user in users[0]:
    print user['name']
print ""

#print groups
groups = win32net.NetGroupEnum('localhost', 0)
print "GROUPS"
print "=========="
for group in groups[0]:
    print group['name']
print ""

#print shares
shares = win32net.NetShareEnum('localhost', 0)
print "SHARES"
print "=========="
for share in shares[0]:
    print share['netname']
print ""

#print servers
servers = win32net.NetServerEnum(None, 100)
print "SERVERS"
print "=========="
for server in servers[0]:
    print server['name']
print ""
   

    