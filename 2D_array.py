# fruit = ["apple", "banana", "orange", "coconut"]
# veggies = ["celery", "tomato", "potato"]
# meats = ["chicken", "mutton", "steak"]

# groceries = [fruit, veggies, meats]

# print(fruit)
# print(groceries)
# print(groceries[0])
# print(groceries[1])
# print(groceries[2])
# print(groceries[0][1])

# groceries = [["apple", "banana", "orange", "coconut"],["celery", "tomato", "potato"],["chicken", "mutton", "steak"]]
# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()

keypad = ((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))
for i in keypad:
    for j in i:
        print(j,end = " ")
    print()
