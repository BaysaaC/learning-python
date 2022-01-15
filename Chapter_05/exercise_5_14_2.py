""""Chapter 5 examples and exercises"""

# Exercise 5.2

# 5.2.1

def check_fermat(a,b,c,n):
    if n>2:
        if a**n+b**n == c**n:
            print("Holy smokes, Fermat was wrong !")
            return
        print("No, that doesn't work")
        return
        
    if a**n+b**n == c**n:
        print(True)
        return
    print(False)


# 5.2.2

def check_fermat_v2():
    
    print("Fermat's Last Theorem states : 'a^n + b^n = c^n' is true only for some integers a, b, c, to power n where n<=2")

    input_a = input("Please enter an integer for operand 'a':")
    input_b = input("Please enter an integer for operand 'b':")
    input_c = input("Please enter an integer for operand 'c':")
    input_n = input("Please enter an integer for power 'n':")
    
    a = int(input_a)
    b = int(input_b)
    c = int(input_c)
    n = int(input_n)
    
    print("Fermat's Last Theorem is checked? (a^n + b^n = c^n)")
    check_fermat(a,b,c,n)

check_fermat_v2()




