def calculate():
    print("""
SELECT ONE OF THE FOLLOWING:
1. ADDITION
2. SUPSTRACT
3. MULTIPLICATION
4. DIVISION
5. EXIT""")
    choice = int(input())
    if (choice>=1 and choice<=4):
        print("ENTER TWO NUMBERS")
        num1 = int(input("ENTER THE 1ST NUMBER:"))
        num2 = int(input("ENTER THE 2ND NUMBER:"))
    if choice==1:
        res= num1 + num2
        print("RESULT: {} + {} = ".format(num1,num2),(res))
    elif choice ==2:
        res= num1 - num2
        print("RESULT: {} - {} = ".format(num1,num2),(res))
    elif choice==3:
        res= num1 * num2
        print("RESULT: {} * {} = ".format(num1,num2),(res))
    elif choice==4:
        res= num1 / num2
        print("RESULT: {} / {} = ".format(num1,num2),(res))
    elif choice==5:
        exit()
    else:
        ("WRONG INPUT TRY AGAIN")

    again()
def again():
    choice = input("""
DO YOU WANT TO CACULATE AGAIN?
TYPE 'Y' FOR YES and 'N' FOR NO.""")
    if choice=='Y':
        calculate()
    elif choice=='N':
        print("SEE YOU LATER")
    else:
        again()
calculate()
    
    
    
