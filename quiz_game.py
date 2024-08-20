questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Paris", "B) London", "C) Rome", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
        "answer": "B"
    },
    {
        "question": "Which continent is the Sahara Desert located on?",
        "choices": ["A) Asia", "B) North America", "C) Africa", "D) Australia"],
        "answer": "C"
    },
    {
        "question": "What is the longest river in the world?",
        "choices": ["A) Nile", "B) Amazon", "C) Yangtze", "D) Mississippi"],
        "answer": "A"
    },
    {
        "question": "Which element has the atomic number 1?",
        "choices": ["A) Helium", "B) Hydrogen", "C) Oxygen", "D) Carbon"],
        "answer": "B"
    },
    {
        "question": "In which year did World War II end?",
        "choices": ["A) 1945", "B) 1939", "C) 1944", "D) 1946"],
        "answer": "A"
    },
    {
        "question": "Which famous scientist developed the theory of general relativity?",
        "choices": ["A) Isaac Newton", "B) Nikola Tesla", "C) Galileo Galilei", "D) Albert Einstein"],
        "answer": "D"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    }
]



def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for choice in q["choices"]:
            print(choice)

        answer = input("Enter your answer (A, B, C, D): ").strip().upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answe was {q['answer']}.")

    print(f"\nYou completed the quiz! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz(questions)