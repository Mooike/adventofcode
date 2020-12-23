with open("data.txt") as f:
    raw = f.read().split("\n\n")
    
groups = []
counter = 0
solution = 0
for e in raw:
    groups.append(e.split("\n"))

for group in groups: 
    group_answers = []
    for person in group:
        answered_questions = set()
        for answer in person:
            answered_questions.add(answer)
        group_answers.append(answered_questions)
    
    intersection = group_answers[0].intersection(*group_answers)
    counter = counter + len(intersection)
print("The solution is: ", counter)
    