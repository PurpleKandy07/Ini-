x=5
y=3
print(x+y)
###
x="123"
x = int('123')
print(x)
###
greeting=("Hello, World")

###
numbers=[1,2,3,4,5]
x= len(numbers)
fruits= ["apple", "watermelon", "pineapple"]
print(fruits[0])


x=int(input(x))
if x < 10:
    print("x is less than 10")
else: 
    print("x is greater than 10")

def myfunction(z):
    return lambda z: z*z
square = myfunction(13) 
print(square(13)) 
###
z=lambda x,y: x+y
print(z(3,5))
###
def find_average(x,y,z):
    return x+y+z/3
result=int(input(x,y,z))
print(result)

    
