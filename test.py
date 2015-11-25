import subprocess

def writeTest(str):
    f = open("TestFile","w")
    f.write(str)
    f.close()

def run():
    p = subprocess.Popen(["python", "DeductiveLogic.py", "TestFile"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out.splitlines()[-1].split()[-1]

def runTest(name,expected,str):
    writeTest(str)
    actual = run()
    status = "failed!"
    if actual == expected:
        status = "passed!"
    
    output = "Test '%s' %s" % (name,status)
    print output

############################################################
# TESTS
############################################################

runTest("OR-1","True","""Variable A True
Variable B False
Equation Test A or B""")

runTest("AND-1","True","""Variable A True
Variable B True
Equation Test A and B""")

runTest("AND-2","False","""Variable A True
Variable B False
Equation Test A and B""")
