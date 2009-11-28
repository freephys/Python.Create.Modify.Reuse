#!/usr/bin/env python

from xml.dom import minidom

def test_html_report(testpath):
    print """
    ================================
    GENERATE HTML REPORT
    ================================
    """
    prompt = """
    Enter the date of the test run in the
    following format: '01-01-2008'
    """
    test_date = raw_input (prompt)
    
    test_run_file = testpath + test_date + ".xml"
    
    #Get nodes from XML document
    try:
        test_run = minidom.parse(test_run_file)
    except:
        print "\n\tProblem opening test run file!\n"
        raw_input("Press [Enter] to continue:  ")
        return
    test_result_node = test_run.childNodes[0]
    test_firstname_node = test_result_node.childNodes[1]
    test_lastname_node = test_result_node.childNodes[3]
    test_prime_node = test_result_node.childNodes[5]
    test_passed_node = test_result_node.childNodes[7]
    test_failed_node = test_result_node.childNodes[9]
    test_error_node = test_result_node.childNodes[11]
    
    #Get text from relevant nodes
    test_firstname_result = test_firstname_node.firstChild.data
    test_lastname_result = test_lastname_node.firstChild.data
    test_prime_result = test_prime_node.firstChild.data
    test_passed_result = test_passed_node.firstChild.data
    test_failed_result = test_failed_node.firstChild.data
    test_error_result = test_error_node.firstChild.data
    
    #Produce result to html
    html_output = """
    <HTML>
    <TITLE>Test Report - %s</TITLE>
    <HR>
    <H1>TEST RUN RESULTS %s</H1>
    <HR>
    <BODY>
    Test first name - %s<br>
    Test last name - %s<br>
    Test prime number - %s<br>
    <HR>
    Total tests passed:  %s<br>
    Total tests failed:  %s<br>
    Total tests with errors:  %s<br>
    </BODY>
    </HTML>
    """ % (test_date, test_date, test_firstname_result, test_lastname_result, \
    test_prime_result, test_passed_result, test_failed_result, test_error_result)
    
    filename = os.path.join(os.curdir, 'test_report_html', test_date + ".html")
    output_file = open(filename, 'w')
    output_file.write(html_output)
    output_file.close()
    
    print "\n\t-- HTML Report Generated --"
    raw_input("\tPress [Enter] to continue:  ")
    

    
