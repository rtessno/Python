### powers.py
### To understand recursion, you first have to understand recursion!
### find power of a base recursively
### base case: if the exponent is 1, answer is base
### 2 to power 5 = 2 times 2 to the power 4. Aha!!
### recursive case: if not, reduce exponent by one and recall method

def main():
    base = int(input('Enter an integer for the base '))
    exp = int(input('Enter an integer for the exponent '))

    print(base,'to the power',exp,'equals',power(base,exp))



def power(base,exp):
    if exp == 1:            ### this is the base case (p 511)
        return base
    elif exp > -1:          ### this is the recursive case (p 511)
        exp -= 1
        return base * power(base,exp)
        
main()
