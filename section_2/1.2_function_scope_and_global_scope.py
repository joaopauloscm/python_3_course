x = 1

def scope():
    x=10
    
    def another_function():   
        x=11
        y=2
        print(x,y)
    another_function()

scope()
print(x)
scope()
print(x)

