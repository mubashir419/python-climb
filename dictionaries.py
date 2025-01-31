import random

firstdict={
    "name":"jese",
    "city":"Brampton",
    "age":22,
    "sports":["soccer","basketball","cricket"]
}
print(firstdict["sports"][random.randint(0,2)])
for key in firstdict:
    print(firstdict[key])
firstdict["name"]="Bhalvindar"
print(firstdict)
