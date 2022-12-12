t1 = tuple(input("Enter the tuple: "))
t2 = tuple(input("Enter the tuple: "))

while True:
        print("1. Extract a element from tuple ")
        print("2. Length of tuple")
        print("3. Combine two tuples")
        print("4. Repetition of elements in tuple")
        print("5. Count a element in tuple")
        print("6. Print max value in tuple")
        print("7. Print min value in tuple")
        print("8. Convert a tuple to list")
        print("9. Print the last element of tuple")
        print("10. Extract a part of tuple")
        print("0. Exit")
        ch = int(input("Enter the choice: "))
        if ch == 1:
            c = int(input("Enter location: "))
            print(t1[c])
        elif ch == 2:
            print(len(t))
        elif ch == 3:
            print (t1 + t2)
        elif ch == 4:
            t1=readinput()
            print(t1 * 2)
        elif ch == 5:
            i = input("Enter the element to count: ")
            print(t1.count(i))
        elif ch == 6:
            print(max(t1))
        elif ch == 7:
            print(min(t1))
        elif ch == 8:
            l = list(t1)
            print(l)
        elif ch == 9:
            print(t1[-1])
        elif ch == 10:
            s = int(input("Enter starting index: "))
            e = int(input("Enter ending index: "))
            print(t[s:e])
        else:
            exit()

