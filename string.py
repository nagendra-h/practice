n1=input("Enter a First String")
n2=input("Enter a Second String")
while True:
    print('1.length of the string')
    print('2.concatenation of the string')
    print('3.maximum of string')
    print('4.minimum of string')
    print('5.sorting of string')
    print('6.reverse of string')
    print('7.upper of string')
    print('8.lower of string')
    print('9.Replace Character')
    print('10.Split a String into List')
    ch = int(input('Enter the Number'))
    if ch == 1:
        print(len(n1))
    elif ch == 2:
        print(n1+n2)
    elif ch == 3:
        print(max(n1))
    elif ch == 4:
        print(min(n1))
    elif ch == 5:
        print(sorted(n1))
    elif ch == 6:
        print(n1[::-1])
    elif ch == 7:
        print(n1.upper())
    elif ch == 8:
        print(n1.lower())
    elif ch == 9:
        print(n1.replace("b","a"))
    elif ch == 10:
        print(n1.split())
    else:
        exit()
    
   
