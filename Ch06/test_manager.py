import os, sys
import test_run, test_list, test_results, test_html

if sys.executable.find("exe") != -1:
    clearscreen = "cls"
    testpath = ".\\test_runs\\"
else:
    clearscreen = "clear"
    testpath = "./test_runs/"

#MAIN MENU
def menu():
    os.system(clearscreen)
    print """
    ================================
    TEST MANAGEMENT/REPORTING SYSTEM
    ================================
    1 - Run tests
    2 - List test runs
    3 - Show test results
    4 - Generate HTML test report
    5 - Help
    6 - Exit
    ================================
    """
    choice = raw_input("Enter a choice and press enter:  ")
    return choice

#TAKE CHOICE AND LAUNCH MODULE
choice = ""
while choice != "6":    
    choice = menu()
    if choice == "1":
        os.system(clearscreen)
        test_run.run_tests(testpath)
    elif choice == "2":
        os.system(clearscreen)
        test_list.list_tests()
    elif choice == "3":
        os.system(clearscreen)
        test_results.show_test_results(testpath)
    elif choice == "4":
        os.system(clearscreen)
        test_html.test_html_report(testpath)
    elif choice == "5":
        os.system(clearscreen)
        print """
    ================================
    TEST MANAGEMENT/REPORTING SYSTEM
    ================================
    Welcome to the Test Management/Reporting system.
    Using this program, you can run tests, list test
    runs, show test results to the screen, and generate
    HTML reports.
        """
        raw_input("Press [Enter] to continue:  ")

