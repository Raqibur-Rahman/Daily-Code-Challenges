def numberOfEmployeesWhoMetTarget(self, hours, target):
    result=0
    for hour in hours:
        if hour>=target:
            result=result+1
    print(result)

numberOfEmployeesWhoMetTarget(None,[5,1,4,2,2], 6)