from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--name", dest="name",
                  help="print name")

(options, args) = parser.parse_args()

print "your name is ", options.name

