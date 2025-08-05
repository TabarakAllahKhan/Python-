# Step 1: List of questions
questions = [
    "What is the capital of Pakistan?\n(a) Lahore\n(b) Karachi\n(c) Islamabad\n(d) Peshawar",
    "Which planet is known as the Red Planet?\n(a) Earth\n(b) Venus\n(c) Mars\n(d) Jupiter",
    "What is the currency of Japan?\n(a) Dollar\n(b) Rupee\n(c) Yen\n(d) Won",
    "Who wrote the national anthem of Pakistan?\n(a) Hafeez Jullundhri\n(b) Allama Iqbal\n(c) Faiz Ahmed Faiz\n(d) Ahmed Faraz"
]

# Step 2: Correct answers
answers = ['c', 'c', 'c', 'a']

# Step 3: Prize money per correct answer
prize_per_question = 10000
total_prize = 0

# Step 4: Game loop
print("🎮 Welcome to KBC Game!\nAnswer the following questions:\n")

for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")
    user_answer = input("Your answer (a/b/c/d): ").lower()

    if user_answer == answers[i]:
        total_prize += prize_per_question
        print("✅ Correct!\n")
    else:
        print("❌ Wrong answer!")
        print("Game Over.\n")
        break

# Step 5: Final result
print(f"🏆 You won Rs. {total_prize}")
