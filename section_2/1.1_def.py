"""
# def

def hello(): 
    print("Hello")
    print("Hello")
    print("Hello")

hello()

def numbers(a,b,c): 
    print(a,b,c)
  

numbers(1,2,3)

def salutation(name = "No name"):
    print (f"Hello, {name}! ")

salutation('Luiz')
salutation('Joao Paulo')
salutation()


def sum(x,y):
    print(x + y)

sum(1,2)
sum(y=2,x=1)
""" 

#Code Refactoring
def sum(x,y, z=0):
    if z:
        print(x+y+z)
    else:
        print(x+y)
    


sum(2,2)