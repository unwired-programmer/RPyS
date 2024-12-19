#RANDOM
while True:
    import random
    rps = ["rock","paper","scissors"]
    rpss = random.choice(rps)

#USER-INPUT
    rpu = input("rock,paper,scissors!: ")

#TRY-AGAIN
    if rpu == rpss:
        print(f"[bot: {rpss}] [you: {rpu}] Try again!")


#YOU-LOST
    if rpss == "rock" and rpu == "scissors":
        print(f"[bot: {rpss}]  [you: {rpu}] YOU LOST! ")

    if rpss == "paper" and rpu == "rock":
        print(f"[bot: {rpss}]  [you: {rpu}] YOU LOST! ")

    if rpss == "scissors" and rpu == "paper":
        print(f"[bot: {rpss}]  [you: {rpu}] YOU LOST! ")
        
#YOU-WON
    if rpss == "scissors" and rpu == "rock":
        print(f"[bot: {rpss}]  [you: {rpu}] YOU WON! ")
    
    if rpss == "rock" and rpu == "paper":
        print(f"[bot: {rpss}]  [you: {rpu}] YOU WON! ")

    if rpss == "paper" and rpu == "scissors":
        print(f"[bot: {rpss}]  [you: {rpu}] YOU WON! ")
