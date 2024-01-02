from functools import reduce

sum = lambda a,b: a + b

print( sum(4,5) ) # 9
print( sum(14,5) ) # 19


def generateLambda(num):
    return lambda a: a * num

doubler = generateLambda(2)
print( doubler(4) ) # 8


listData = [0,1,2,3]

result = list( map(lambda a: a * 3, listData ) )
print(result)

result = reduce( lambda x,y: x + " " + y, ("Ola", "Ania") )
print(result)

result = list( filter(lambda a: a > 1, listData) )
print(result)
