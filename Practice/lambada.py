List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12, 2, 4, 2, 3, 18, 18]]

sortList = lambda x: ( sorted(i) for i in x)
secondLargest = lambda x, sortList : [y[len(y)-2] for y in sortList(x)]
res = secondLargest(List, sortList)

print(res)