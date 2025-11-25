
print("====== Quiz Game ======")

# Step 1: Store the questions and answers in a dictionary
quiz = {
    "In Git, what command uploads your code to GitHub? ": "push",
    "What data type uses key-value pairs in Python? ": "dictionary",
    "In Python loops, which keyword stops the loop immediately? ": "break",
    "What function do we use to get user input? ": "input",
    "What symbol do we use to connect in Python? ": "+"
}

# Step 2: Create a score variable
score = 0

# Step 3: Use a loop to ask each question
for question in quiz:
    answer = input(question)
    # Step 4: Compare user’s answer to the correct one
    if answer.lower() == quiz[question].lower():
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong! The correct answer is:", quiz[question])

# Step 5: Show the final score
print("===============")
print("You got", score, "out of", len(quiz), "questions correct!")
print("===============")






















