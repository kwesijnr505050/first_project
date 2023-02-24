    # creating funtions using python
def lambdP():
    # usign the lambda in python
    x = lambda a,b,c : a + b + c
    print(x(2,3,1))
    # dont forget to call the name of the function
lambdP()

# creating a funtion containing loop within it having an array

def array():
    names = ["james","kofi","madam","love"]
    for x in names:
        print(x)
array()

def math():
    x = lambda a,b : a *b
    x(3,4)

    y = lambda y,x : y+x
    y(3,9)
        # making an if condition
    if x == y :
        print(" the value in y is greater than the value in x")
    else:
        print("is not greater than the value")
        # calling the function for the code within that function to be executed
math()

    # using the if condition
school= {"ucc","kumasi","knust","winneba"}
if "winneba"  in school:
    print("yes")
else:
    print("no")

    

