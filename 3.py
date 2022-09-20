y = [[1, 2, 3],
     [5, 6, 7],
     [9, 10, 11]]

z = [[31, 32, 33],
     [55, 56, 57],
     [19, 10, 11]]

sum = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print("Sum of [y]&[z]\n")

for i in range(len(y)):
   for j in range(len(y[0])):
       sum[i][j] = y[i][j] + z[i][j]

for s in sum:

    print(s)
    print("\n")
    
diff = [[0,0,0],
         [0,0,0],
         [0,0,0]]
print("Difference of [z]&[y]\n")

for i in range(len(z)):
     for j in range(len(z[0])):
        diff[i][j] = z[i][j] - y[i][j]

for d in diff:
       
        print(d)
        print("\n")
mult = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print("Multiplication of [y]&[z]\n")

for i in range(len(z)):
     for j in range(len(z[0])):
        mult[i][j] = y[i][j] * z[i][j]

for m in mult:
    print(m)
    print("\n")
