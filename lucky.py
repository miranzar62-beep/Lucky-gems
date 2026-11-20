import json
import random
import os
from datetime import date

FILE = "lucky_data.json"

def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                d = json.load(f)
                if "users" not in d:
                    d["users"] = {}
                if "history" not in d:
                    d["history"] = []
                return d
        except:
            pass
    return {"users": {}, "history": []}

def save():
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

print("\n💎 WELCOME TO LUCKY GEMS 💎")
username = input("Enter Username: ")
password = input("Enter Password: ")

if username not in data["users"]:
    data["users"][username] = {
        "password": password,
        "coins": 1000,
        "bonus_date": ""
    }
    save()
    print("Account created! 1000 demo coins added.")
elif data["users"][username]["password"] != password:
    print("Wrong password!")
    raise SystemExit

user = data["users"][username]
user.setdefault("bonus_date", "")
user.setdefault("coins", 1000)

def add_history(message):
    data["history"].append({
        "user": username,
        "message": message
    })
    data["history"] = data["history"][-50:]
    save()

while True:
    print("\033[96m\n💎 LUCKY GEMS MENU 💎\033[0m")
    print("1. Play RED")
    print("2. Play GREEN")
    print("3. Play BLUE")
    print("4. Game History")
    print("5. Exit")
    print("6. Daily Bonus")
    print("7. Add Demo Coins")
    print("8. Coins to Cash Calculator")
    print("9. Demo Recharge")
    print("10. Check Balance")
    print("11. Demo Withdrawal")
    print("12. Admin Panel")
    print("13. Aeroplane Crash Winner ✈️")
    choice = input("\nChoose option: ")


    if choice in ["1", "2", "3"]:
        colors = {"1": "RED", "2": "GREEN", "3": "BLUE"}
        selected = colors[choice]
        print("Your balance:", user["coins"])
        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if bet <= 0 or bet > user["coins"]:
            print("Invalid bet or insufficient coins!")
            continue

        result = random.choice(["RED", "GREEN", "BLUE"])
        print("Result:", result)

        if selected == result:
            win = bet * 2
            user["coins"] += win
            print("🎉 You won", win, "coins!")
            add_history(f"{selected}: WIN +{win}")
        else:
            user["coins"] -= bet
            print("You lost", bet, "coins.")
            add_history(f"{selected}: LOSS -{bet}")

        print("New balance:", user["coins"])
        save()

    elif choice == "4":
        print("\n--- GAME HISTORY ---")
        records = [h["message"] for h in data["history"]
                   if h["user"] == username]
        if records:
            for item in records[-10:]:
                print(item)
        else:
            print("No history yet.")

    elif choice == "5":
        save()
        print("Thank you for playing Lucky Gems!")
        break

    elif choice == "6":
        today = date.today().isoformat()
        if user["bonus_date"] == today:
            print("Daily bonus already claimed today!")
        else:
            user["coins"] += 100
            user["bonus_date"] = today
            print("🎁 100 demo coins added!")
            add_history("Daily bonus +100")
            save()

    elif choice == "7":
        try:
            amount = int(input("Enter demo coins to add: "))
            if amount <= 0:
                print("Enter a positive amount!")
            else:
                user["coins"] += amount
                print(amount, "demo coins added!")
                add_history(f"Demo coins added +{amount}")
                save()
        except ValueError:
            print("Invalid amount!")

    elif choice == "8":
        print("\n💰 DEMO CASH CALCULATOR")
        print("Rate: 1 demo coin = Rs 1")
        print("Your demo balance:", user["coins"], "coins")
        print("Estimated demo value: Rs", user["coins"])
        print("This is only a calculation. No real cash withdrawal.")

    elif choice == "9":
        print("\n🔋 DEMO RECHARGE")
        try:
            amount = int(input("Enter demo recharge coins: "))
            if amount <= 0:
                print("Enter a positive amount!")
            else:
                user["coins"] += amount
                print("Demo recharge successful!")
                add_history(f"Demo recharge +{amount}")
                save()
        except ValueError:
            print("Invalid amount!")

    elif choice == "10":
        print("Your username:", username)
        print("Your balance:", user["coins"], "demo coins")

    elif choice == "11":
        print("\n--- DEMO WITHDRAWAL ---")
        print("Your balance:", user["coins"])

        try:
            amount = int(input("Enter coins to withdraw: "))
            if amount <= 0 or amount > user["coins"]:
                print("Invalid amount or insufficient coins!")
            else:
                user["coins"] -= amount
                print("Demo withdrawal request submitted!")
                print("No real money transferred.")
                print("Remaining balance:", user["coins"])
                add_history(f"DEMO WITHDRAWAL: {amount} coins")
                save()
        except ValueError:
            print("Enter a valid number!")


    elif choice == "12":
        admin_password = input("Enter Admin Password: ")

        if admin_password == os.getenv("LUCKY_ADMIN_PASSWORD"):
            print("\n👑 WELCOME OWNER")
            print("Total users:", len(data["users"]))

            for name, info in data["users"].items():
                print(name, ":", info["coins"], "coins")

            print("\n1. Add Coins")
            print("2. Minus Coins")

            action = input("Choose option: ")
            target = input("Enter Username: ")

            if target in data["users"]:
                try:
                    amount = int(input("Enter Coins: "))

                    if amount <= 0:
                        print("Enter a positive amount!")

                    elif action == "1":
                        data["users"][target]["coins"] += amount
                        save()
                        print("Coins added successfully!")

                    elif action == "2":
                        if amount <= data["users"][target]["coins"]:
                            data["users"][target]["coins"] -= amount
                            save()
                            print("Coins deducted successfully!")
                        else:
                            print("Insufficient coins!")

                    else:
                        print("Wrong option!")

                except ValueError:
                    print("Enter a valid number!")

            else:
                print("Username not found!")

        else:
            print("Wrong Admin Password!")
    elif choice == "13":
        print("\n✈️ AEROPLANE CRASH WINNER")
        print("Your Balance:", user["coins"])

        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if bet <= 0 or bet > user["coins"]:
            print("Invalid bet or insufficient coins!")
            continue

        crash_point = random.uniform(1.2, 5.0)
        multiplier = 1.0
        user["coins"] -= bet

        while True:
            height = max(0, 8 - int(multiplier * 2))
            print("\033[2J\033[H", end="")
            print("\n" * height + "       ✈️")
            print(f"PLANE FLYING: {multiplier:.2f}x")
            action = input("Cash Out ke liye C dabao, warna Enter: ")
            if action.lower() == "c":
                payout = int(bet * multiplier)
                user["coins"] += payout
                print("CASH OUT SUCCESS!")
                print("You won:", payout, "coins")
                add_history(f"Aeroplane win: {payout} coins")
                save()
                break

            multiplier = round(multiplier + 0.1, 2)

            if multiplier >= crash_point:
                print("PLANE CRASHED!")
                print("You lost:", bet, "coins")
                add_history(f"Aeroplane loss: {bet} coins")
                save()
                break
    else:
        print("Wrong choice! Select 1 to 13.")






