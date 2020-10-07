
def calculate():
    n1 = float(input("First number : "))
    n2 = str(input("Operation : "))
    n3 = float(input("Second number : "))

    signs = ["+", "-", "*", "/"]

    if signs[0] in n2:
        print("\n")
        print(n1)
        print(n2+str(n3))
        print("----------")
        print(n1+n3)

    elif signs[1] in n2:
        print("\n")
        print(n1)
        print(n2+str(n3))
        print("----------")
        print(n1-n3)

    elif signs[2] in n2:
        print("\n")
        print(n1)
        print(n2+str(n3))
        print("----------")
        print(n1*n3)

    elif signs[3] in n2:
        print("\n")
        print(n1)
        print(n2+str(n3))
        print("----------")
        print(n1/n3)

    
run = True
while run:

    calculate()
    inp = input("Do you want to use me again, yes/no? : ")

    if inp == "no":
        break
    elif inp == "yes":
        continue
    else:
        print("enter only yes/no")
        re = str(input())
        if re == "no":
            break
        elif inp == "yes":
            continue
        else:
            break
        
