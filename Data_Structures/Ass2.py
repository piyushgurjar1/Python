voters = set()
vote_count = {"Piyush": 0, "Pavesh": 0, "Bajpai": 0}

def vote():
    voter_name = input("Enter your name: ")
    if voter_name in voters:
        print(f"{voter_name}, you have already voted!")
        return    
    candidate = input("Enter the candidate you want to vote for: ")

    if candidate not in vote_count:
        print("Invalid candidate!")
        return
    vote_count[candidate] += 1
    voters.add(voter_name)
    print(f"Thank you for voting!")

def show_results():
    print("Voting Results:")
    for candidate, votes in vote_count.items():
        print(f"{candidate}: {votes} votes")

print('''Menu:
1. Vote
2. Show Results''')

while True:    
    choice = input("Choose an option (1-2): ")

    if choice == "1":
        vote()
    elif choice == "2":
        show_results()
    else:
        print("Invalid choice")
        break
