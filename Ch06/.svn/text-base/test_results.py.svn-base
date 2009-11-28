#!/usr/bin/env python

from xml.dom import minidom
import time

def show_test_results(testpath):
    
    print """
    ================================
    SHOW TEST RESULTS
    ================================
    """
    prompt = """
    Enter the date of the test run in the
    following format: '01-01-2008'
    (or type 'today' for today)
    """
    test_date = raw_input (prompt)
    if test_date == "today":
        test_date == datetime.datetime.now().strftime("%m-%d-%Y")
    
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
    
    #Produce result to screen
    print """
    ================================
    TEST RUN RESULTS %s
    ================================
    Test first name - %s
    Test last name - %s
    Test prime number - %s
    ================================
    Total tests passed:  %s
    Total tests failed:  %s
    Total tests with errors:  %s
    """ % (test_date, test_firstname_result, test_lastname_result, \
    test_prime_result, test_passed_result, test_failed_result, \
    test_error_result)
    
    raw_input("Press [Enter] to continue:  ")