aryList = ["biscuits", "sweets", "tea"]

for i in range(3):
    print("What else would you like to add?")
    choice = input()
    aryList.append(choice)
print("###################################################################################################################")
for i in range(6):
    print(aryList[i])