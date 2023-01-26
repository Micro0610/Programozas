while(True):
    print("Szeretne kilépni? (I/N)")
    kilep = input()
    if len(kilep) >= 1 and kilep == "I" or kilep == "i":
        break
    else:
        list = []
        szam = int(input())
        for i in range(szam):
            i = i + 1
            list.append(i)
        for l in range(len(list)):
            print(list[l])

    

