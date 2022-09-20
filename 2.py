z = [[31, 32, 33],
     [55, 56, 57],
     [19, 10, 11]]

for i in range(len(z)):
    for j in range(len(z[i])):
        if z[i][j] %2 != 0:
            print(z[i][j], "is an odd number")
        else:
            print(z[i][j], "is an even number")
        
