def show_employee(name, salary=9000):
    print("Employee:",name,"salary is:",salary)    
    return name, salary
show_employee("Ben",12000)
show_employee("Bhalvindar")
#-------------------------------------
movies=[]
for i in range(3):
    ask_movies=input("Enter your favourite movies:")
    movies.append(ask_movies)
print(movies)
#-------------------------------------
def fibonacci(a):
    if a<=0:
        print("Incorrect input")
    elif a==0:
        return 0
    elif a==1 or a==2:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)
b=int(input("Enter a positive integar"))
print(fibonacci(b))
