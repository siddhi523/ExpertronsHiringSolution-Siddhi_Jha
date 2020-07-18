import sys
def func(li):
    l = sys.maxsize #lowest marks
    sl = l #second lowest marks
    res =[]

    #Get second lowest value
    for i in range(len(li)):
        marks = li[i][1]
        if(marks < l):
            sl = l
            l = li[i][1]
        elif(marks > l and marks < sl):
            sl = li[i][1]

    #Get names corresponding to second lowest score
    for i in range(len(li)):
        if(li[i][1] == sl):
            res.append(li[i][0])
    #sort alphabetically
    res.sort()
    return res

List = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39], ['Anna', 37.21]]
Result = func(List)
for i in range(len(Result)):
    print(Result[i])
