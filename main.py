

def main():


    x = None
    min = None
    while True:
            x = input("Enter the number: ")
            if (x == "q") or (x == "Q"):
                break
            x = int(x)
            if min is not None:
                if x < min:
                    min = x
            else:
                min = x


    print ("Minimum is: " + str(min))


main()
