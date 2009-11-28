import smtplib, csv, datetime, sys

WEBMASTER = "jknowlton525@gmail.com"
SMTP_SERVER = "localhost"

def writeCSVLog(name, phone, email, comment):
    python_exec = sys.executable
    if python_exec.find("exe") != -1:
        dir_root = "c:\\logs\\"
    else:
        dir_root = "//usr//local//logs//"
    today = datetime.datetime.now().strftime("%m/%d/%Y")
    row = [today, name, phone, email, comment]
    try:
        writer = csv.writer(open(dir_root + "feedbacklog.csv", "a"))
        writer.writerow(row)
    except:
        print "There was a problem writing to the logfile!"
        sys.exit
def email(req, name, phone, email, comment):

    # make sure the user provided all the parameters
    if not (name and phone and email and comment):
        return "A required parameter is missing, \
               please go back and correct the error"

    # create the message text
    msg = """\
From: %s                                                                                                                                           
Subject: feedback
To: %s

I have the following comment:

%s

Thank You,

%s
%s

""" % (email, WEBMASTER, comment, name, phone)

    # send it out
    try:
        conn = smtplib.SMTP(SMTP_SERVER)
        conn.sendmail(email, [WEBMASTER], msg)
        conn.quit()
    except:
        print "There was a problem sending the email!"
        sys.exit

    # provide feedback to the user
    s = """\
<html>
<BODY BGCOLOR="#ccffff" DIR="LTR">
Dear %s,<br>                                                                                                                                       
Thank You for your kind comments, we
will get back to you shortly.
</BODY>
</html>""" % name

    writeCSVLog(name, phone, email, comment)
    return s
