print 'welcome'
print 'please enter one integer'
num1 = raw_input()
print 'please enter another integer'
num2 = raw_input()
print 'would you like to add or subtract your integers? Enter 1 for add and 2 for subtract'
ans = int(raw_input())
if ans == 1:
    print int(num1) + int(num2)
else:
    pass
if ans == 2:
    print int(num1) - int(num2)
else:
    pass
print 'and lastly, please enter your name'
name = raw_input()
print name