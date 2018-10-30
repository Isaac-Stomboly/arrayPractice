import random
aryList = ["biscuits", "sweets", "tea"]

for i in range(3):
    print("What else would you like to add?")
    choice = input()
    aryList.append(choice)
print("#########################################")
for i in range(len(aryList)):
    print(aryList[i])
print(random.choice(aryList))
