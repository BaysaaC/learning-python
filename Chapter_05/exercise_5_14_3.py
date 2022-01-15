""""Chapter 5 examples and exercises"""

# Exercise 5.3.1


def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        print("No")
        return False
    print("Yes")
    return True


    
    
# Exercise 5.3.2

def is_triangle_v2():
    
    print("If any of the 3 lengths 'a', 'b', 'c' is greater than the sum of the other two, you cannot form a triangle.")

    input_a = input("Please enter an integer for length 'a':")
    input_b = input("Please enter an integer for length 'b':")
    input_c = input("Please enter an integer for length 'c':")
    
    a = int(input_a)
    b = int(input_b)
    c = int(input_c)
    
    print("Is it a triangle ?")
    is_triangle(a,b,c)

is_triangle_v2()

