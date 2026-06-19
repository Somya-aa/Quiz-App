questions = [
    {
        "question": "What does HTML stand for?",
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which language is used for styling web pages?",
        "answer": "CSS"
    },
    {
        "question": "Which language is commonly used with Flask?",
        "answer": "Python"
    },
    {
        "question": "What does CPU stand for?",
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "answer": "#"
    },
    {
        "question": "What does RAM stand for?",
        "answer": "Random Access Memory"
    },
    {
        "question": "Which HTML tag is used for the largest heading?",
        "answer": "h1"
    },
    {
        "question": "Which company developed Python?",
        "answer": "None"
    },
    {
        "question": "What does CSS stand for?",
        "answer": "Cascading Style Sheets"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "answer": "def"
    }
]

score = 0

print("=== TECH QUIZ APP ===\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}. {q['question']}")
    user_answer = input("Your Answer: ")

    if user_answer.lower() == q["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}\n")

print("=== QUIZ COMPLETED ===")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")