for i in range(int(input())):
    n,m = input().split(" ")
    ErdosNumbers = {"Erdos, P." : 0}
    for i in range(int(n)):
        s = input()
        minNumber = 2**31 - 1
        for k in ErdosNumbers.keys():
            if k in s:
                newMin = ErdosNumbers[k] + 1
                if newMin < minNumber:
                    minNumber = newMin
        temp = s.split(":")
        listOfPeople = temp[0].split(",")
        actualList = []
        print(listOfPeople)
        for i in range(len(listOfPeople)):
            if i % 2 == 0:
                actualList.append(listOfPeople[i].strip() + "," + listOfPeople[i+1])
        for person in actualList:
            try:
                if ErdosNumbers[person] > minNumber:
                    ErdosNumbers[person] = minNumber
            except:
                ErdosNumbers[person] = minNumber
    for i in range(k):
        s = input()
        print(s + " " + ErdosNumbers[s])