def solution():
    deleteList = [1,2,3]
    testList = [1,2,3,4,5]
    newList = [i for i in testList if i not in deleteList]
    print(newList)

solution()