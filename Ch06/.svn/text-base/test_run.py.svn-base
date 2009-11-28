import datetime, math

def test_firstname(fname):
    fname_input = raw_input("\tEnter your first name: ")
    if fname_input == fname:
        return "PASSED"
    else:
        return "FAILED - EXPECTED " + fname + " but was " + fname_input

def test_lastname(lname):
    lname_input = raw_input("\tEnter your last name: ")
    if lname_input == lname:
        return "PASSED"
    else:
        return "FAILED - EXPECTED " + lname + " but was " + lname_input

def test_prime_number():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    num = raw_input("\tPrime number test - enter a number from 1 to 99: ")
    number = int(num)
    if number in primes:
        return "PASSED"
    else:
        return "FAILED - " + str(number) + " is not a prime number 1 to 99"
    

def run_tests(testpath):
    
    def testcount(test_results):
    #Compile test results and return them in a list
        tests_passed = 0
        tests_failed = 0
        tests_error = 0
        for test_result in test_results:
            if test_result == "PASSED":
                tests_passed += 1
            elif test_result[0:6] == "FAILED":
                tests_failed += 1
            else:
                tests_error += 1
        results = [tests_passed, tests_failed, tests_error]
        return results
    
    #Run tests
    print """
    ================================
    RUN TESTS
    ================================
    """
    result_firstname = test_firstname("Jim")
    result_lastname = test_lastname("Knowlton")
    result_prime_number = test_prime_number()
    total_results = [result_firstname, result_lastname, result_prime_number]
    results = testcount(total_results)
    
    #Output test results to screen
    print """
    ================================
    TEST RUN RESULTS
    ================================
    Test first name - %s
    Test last name - %s
    Test prime number - %s
    ================================
    Total tests passed:  %i
    Total tests failed:  %i
    Total tests with errors:  %i
    """ % (result_firstname, result_lastname, result_prime_number, \
    results[0], results[1], results[2])
    
    #Format XML output for test run
    test_output_xml =  """<testresult>
    <testfirstname>%s</testfirstname>
    <testlastname>%s</testlastname>
    <testprimenumber>%s</testprimenumber>
    <testspassed>%i</testspassed>
    <testsfailed>%i</testsfailed>
    <testserror>%i</testserror>
    </testresult>""" % \
    (result_firstname, result_lastname, result_prime_number, \
        results[0], results[1], results[2])
    
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    output_filename = testpath + today + ".xml"
    test_output = open(output_filename, "w")
    test_output.write(test_output_xml)
    test_output.close()
    raw_input("Press [Enter] to continue:  ")



