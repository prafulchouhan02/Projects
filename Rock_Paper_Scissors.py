import random
iteam_list = ["ROCK","PAPER","SCISSOR"]

user_choice = input("Enter Your Move = ROCK, PAPER, SCISSOR = ").upper()
comp_chice = random.choice(iteam_list)

print(f"User choice = {user_choice}, computer choice = {comp_chice}")

if user_choice == comp_chice :
    print("Both chooses same : = Match Tie")

elif user_choice == "ROCK":
    if comp_chice == "PAPER":
        print("PAPER cover ROCK = Compter win")
    else:
        print("ROCK smashes SCISSOR = You Win")

elif user_choice == "PAPER":
    if comp_chice == "SCISSOR":
        print("SCISSOR cut PAPER = Computer win")
    else:
        print("PAPER cover ROCK= You win")
    
elif user_choice == "SCISSOR":
    if comp_chice == "ROCK":
        print("ROCK smashes SCISSOR = Computer Win")  
    else:
        ("SCISSOR cut PAPER = You win")
else:
    print("Invalid Choice...")
    
