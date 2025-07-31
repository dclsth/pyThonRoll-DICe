import random
# ● ┌ ─ ┐ │ └ ┘
gambar_dadu = {
    1: ("┌───────────┐\n",
        "|           |\n",
        "|     ●     |\n",
        "|           |\n",
        "└───────────┘\n"), 
    2: ("┌───────────┐\n",
        "|  ●        |\n",
        "|           |\n",
        "|        ●  |\n",
        "└───────────┘\n"), 
    3: ("┌───────────┐\n",
        "|  ●        |\n",
        "|     ●     |\n",
        "|        ●  |\n",
        "└───────────┘"), 
    4: ("┌───────────┐\n",
        "|  ●     ●  |\n",
        "|           |\n",
        "|  ●     ●  |\n",
        "└───────────┘\n"), 
    5: ("┌───────────┐\n",
        "|  ●     ●  |\n",
        "|     ●     |\n",
        "|  ●     ●  |\n",
        "└───────────┘\n"),  
    6: ("┌───────────┐\n",
        "|  ●     ●  |\n",
        "|  ●     ●  |\n",
        "|  ●     ●  |\n",
        "└───────────┘\n"),  
}
dices = []
print("Roll Ur Dice!".center(30, "-"))
jumlah_dice = int(input("How many dice ? "))


for i in range(jumlah_dice):
    dices.append(random.randint(1,6))



for x in range (5):
    for i in dices:
        print(gambar_dadu.get(i)[x], end=" ")