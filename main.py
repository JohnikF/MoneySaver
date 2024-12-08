print("This program helps you save up money.")

saved_money: int = int(input("How much money did you already earn? "))
added_money: int = int(input("How much money do you plan to add to your bank everyday? "))
days: int = int(input("How many days do you want to save up money for? "))

#print("You already have " + str(saved_money) + " money")
print(f"You already have {saved_money} money.")
for i in range(days):
    saved_money = saved_money + added_money
    print(f"Day {i + 1}, summary:{saved_money}")

print(f"...You will earn {saved_money} dollars")
