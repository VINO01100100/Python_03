
name, letter = input("enter a name and which letter count commaa seprated ").split(",")
name.lower().count(letter)
print(f"your name len is {len(name)}   your repeted char is {name.lower().count(letter)}")
