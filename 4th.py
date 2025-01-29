def calc_sum (a, b, c):
    sum= a+b+c
    avg=sum/len([a,b,c])
    print (avg)
    return avg
calc_sum(7,4,3)
#-------------------------------
x=int(input("Enter a positive integar"))
def odd_check(x):
    if x%2==0:
        print("even")
    else:
        print("odd")    
    return x
odd_check(x) 
#--------------------------------
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)
n=int(input("Enter a positive integar"))    
print(facto(n))
#--------------------------------
