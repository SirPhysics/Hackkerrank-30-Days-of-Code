num = int(input())

for case in range(0,num):
    string = input()
    for letter in range(0,len(string)):
        if letter%2 == 0:
            print(string[letter], end ='')
            
    print(" ", end = '')

    for letter in range(0,len(string)):
        if letter%2 == 1:
            print(string[letter],end ='')
    print("")
