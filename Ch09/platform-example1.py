import platform

if platform.platform().find("Windows") != -1:
    print "The platform is Windows"
    #put Windows-specific code here
elif platform.platform().find("Linux") != -1:
    print "The platform is Linux"
    #put Linux-specific code here