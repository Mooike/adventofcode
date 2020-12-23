with open("data.txt") as f:
    raw = f.read().split("\n\n")
    
groups = []
counter = 0
solution = 0
for e in raw:
    groups.append(e.split("\n"))

for group in groups: 
    answered_questions = []
    for person in group:
        for question in person:
            if question not in answered_questions:
                answered_questions.append(question)
            else:
                pass
    counter = counter + len(answered_questions)

print("The solution is: ", counter)