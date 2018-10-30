# tshirt = ["small", "medium", "large"]
# price = [8, 9, 12]

# for i in range(len(tshirt)):
#     print("A shirt of", tshirt[i], "will cost you about\n$", price[i])
tshirts = [["small", 8], ["medium", 9], ["large", 12]]
for i in range(len(tshirts)):
    print(tshirts[i][0], tshirts[i][1])






# string formatting
name = "Navi"
age = 10
print(name, "is" , age , "years old.")
print("{} is {} years old.".format(name, age))
print(f"{name} is {age} years old.")