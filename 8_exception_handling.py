"""
try:
    f = open('grades.txt')
except:
    raise Exception("can't do it")
    
try:
    f = open('grades.txt')
except IOError,e:
    print "can't open file" + str(e)
    sys.exit(0)
except ArithmeticError,e:
    raise ValueError("Bug" + str(e))
"""

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError,e:
        print "division by zero! " + str(e)
    except TypeError, e:
        divide(int(x),int(y))
    else:
        print "result is ", result
    finally:
        print "executing finally clause"
 
def FancyDivide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        FancyDivide(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    else:
        print "1"
    finally:
        print "0"
      

