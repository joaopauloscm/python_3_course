def plus(x,y):
   return x + y
   


sum1 = plus(2,2)
sum2 = plus(3,3)

# print(sum1 + sum2)

# args

def test(*args):
    total = 0
    for number in args: 
        total += number
    return total


numbers = 0,5,10
test_1_5_10 =test(0,5,10)
print(test_1_5_10) 

numbers = 0,5,10
another_test = test(*numbers)
print(another_test)


# or use sum
print(sum((0,5,10)))