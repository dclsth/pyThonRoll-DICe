import random
# ● ┌ ─ ┐ │ └ ┘
gambar_dadu = {
    1: ("┌───────────┐",
        "|           |",
        "|     ●     |",
        "|           |",
        "└───────────┘"), 
    2: ("┌───────────┐",
        "|  ●        |",
        "|           |",
        "|        ●  |",
        "└───────────┘"), 
    3: ("┌───────────┐",
        "|  ●        |",
        "|     ●     |",
        "|        ●  |",
        "└───────────┘"), 
    4: ("┌───────────┐",
        "|  ●     ●  |",
        "|           |",
        "|  ●     ●  |",
        "└───────────┘"), 
    5: ("┌───────────┐",
        "|  ●     ●  |",
        "|     ●     |",
        "|  ●     ●  |",
        "└───────────┘"),  
    6: ("┌───────────┐",
        "|  ●     ●  |",
        "|  ●     ●  |",
        "|  ●     ●  |",
        "└───────────┘"),  
}
dices = []
total = 0
print("Roll Ur Dice!".center(30, "-"))
jumlah_dice = int(input("How many dice ? "))


for i in range(jumlah_dice):
    dices.append(random.randint(1,6))



for x in range (5):
    for i in dices:
        print(gambar_dadu.get(i)[x], end="")
    print()

for i in dices:
    print(f"{i}".ljust(14, " ") , end="")
    total += i
print()
print(f"Your Dice Total: {total}")


