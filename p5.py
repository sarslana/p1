#p_5. Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

#print('Possible longest side of your choice triangle')

side1=int(input('What is the first side of your triangle in cm? '))
side2=int(input('What is the second side of your triangle in cm? '))


def maximum(side1,side2):
    return side1+side2-1
maximum(side1,side2)
n=maximum(side1,side2)

print(f"Maximum value of the third side is {n}")


