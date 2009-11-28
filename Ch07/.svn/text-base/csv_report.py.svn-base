#!/usr/bin/env python

import csv, datetime, sys

def write_csv_log(host, application, version):
    today = datetime.datetime.now().strftime("%m/%d/%Y")
    row = [today, host, application, version]
    try:
        writer = csv.writer(open("versionchecklog.csv", "a"))
        writer.writerow(row)
    except:
        print "Error writing to file!"
        sys.exit(1)

