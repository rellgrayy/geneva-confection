testCases =  int(input())
list = []

for x in range(testCases):
    list.append([])
    f = input()
    for y in range(int(f)):
        list[x].append(int(input()))

for x in range(testCases):
    carList = list[x]
    branch = []
    desired = 1

    while True:
        if len(carList) > 0:
            if carList[-1] == desired:
                desired += 1
                carList.pop()
            else:
                branch.append(carList.pop()) 
        elif len(branch) > 0:
            if branch[-1] == desired:
                desired +=1
                branch.pop()
            else:
                print(" Not Applicable")
                break
        else:
            print(" Successful Movement")
            break
