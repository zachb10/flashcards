import sys

try:
	file = open(sys.argv[1], "r")
except IndexError:
	print("\nPlease provide a flashcard text file as an argument.")
	print("Format of flashcard file: ")
	print("[Q]: <question>")
	print("<answer>")
	print("[Q] <question>")
	print("<answer>")
	print("etc...\n")


# Create lists of questions and answers
questions = []
answers = []

for line in file:
	if "[Q]: " in line:
		questions.append(line.strip())
	else:
		answers.append(line.strip())

# Create question/answer dictionary
qa_dict = {}
for x in range(0, len(questions)):
	qa_dict[questions[x]] = answers[x]

'''
# Print keys and values of qa_dict
for entry in qa_dict:
	print(entry, qa_dict[entry])
'''

# Quiz the user
correct = 0
incorrect = 0
for question in qa_dict:
	print(question)
	answer = input("Answer: ")
	if answer == qa_dict[question]:
		print("Correct!")
		correct += 1
	else:
		print("**INCORRECT**")
		incorrect += 1

print("Quiz complete")
print("Correct: ", correct)
print("Incorrect: ", incorrect)
print("Percentage: ", correct/len(questions)*100, "%")
