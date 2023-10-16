# CTI-110
# P4HW1 - Score List
# name redacted
# 10/10/2023
# This program asks the user for a number of scores, then gets inputs for each score, to display average and grade letter

score_count = int(input("How many scores do you want to enter? "))
print()

scores = []
enter_score_string = f"Enter score #{len(scores) + 1}: "

while len(scores) < score_count:
    next_input = float(input(enter_score_string))
    if 100 >= next_input >= 0:
        scores.append(next_input)
        enter_score_string = f"Enter score #{len(scores) + 1}: "
    else:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        enter_score_string = f"Enter score #{len(scores) + 1} again: "

lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average_score = sum(modified_scores) / len(modified_scores)
grade_letter = ""

if average_score >= 90:
    grade_letter = "A"
elif average_score >= 80:
    grade_letter = "B"
elif average_score >= 70:
    grade_letter = "C"
elif average_score >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"

print("\n\n----------Results----------")
print("Lowest Score  :", lowest_score)
print("Modified List :", modified_scores)
print(f"Scores Average: {average_score:.2f}")
print("Grade         :", grade_letter)
print("---------------------------")
