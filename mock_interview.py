questions = [
    "What is Python?",
    "Explain OOP.",
    "What is a REST API?"
]

for q in questions:
    print("Question:", q)
    answer = input("Your Answer: ")
    
    if len(answer) > 20:
        print("Good answer!\n")
    else:
        print("Try to explain more.\n")
