### recursive_multiply.py
### Multiplication is a series of additions!!
### Let multiply(a, b) be the recursive method
### multiply(a, 1) = a, Aha! Base case when b = 1
### multiply(a, 3) = a + a + a
### But multiply(a, 3) = a + multiply(a, 2) Aha! Recursive case!

def main():
    factor1 = int(input('Enter first factor '))
    factor2 = int(input('Enter second factor '))

    print('The product is',multiply(factor1,factor2))
    

def multiply(fac1, fac2):
    if fac2 == 1:
        return fac1
    else:
        fac2 -= 1
        return fac1 + multiply(fac1,fac2)
    

        
main()
