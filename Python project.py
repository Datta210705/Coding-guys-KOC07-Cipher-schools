N = input("Enter the number you want to check: ")
n_list = N.split()

# 0 and 1 both are fibonacci numbers
for N in n_list:
    # variables for generating fibonacci sequence
    f3 = 0
    f1 = 1
    f2 = 1
    if (int(N.strip()) == 0 or int(N.strip()) == 1):
        print(f"{N.strip()} is valid")

    else:
        # generating the fibonacci numbers until the generated number is less than  N
        while f3 < int(N.strip()):
            f3 = f1 + f2
            f2 = f1
            f1 = f3
        if f3 == int(N.strip()):
            print(f"{N.strip()} is valid")
        else:
            print(f"{N.strip()} is invalid")