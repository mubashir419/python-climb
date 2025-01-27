i = 1
while i <= 10:
    print(i)
    i += 1

print("Number Pattern ")
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")


s = 0
n = int(input("Enter number "))
for i in range(1, n + 1, 1):
    s += i
print("\n")
print("Sum is: ", s)

