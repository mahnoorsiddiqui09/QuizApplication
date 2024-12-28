# QUIZ APPLICATION APP
def quiz_app():
    print("           Wellcome to the application")
    print("      Answer these questions in (a , b , c , d) ")

    questions = [
        {
            "question": "1. What is the capital of France?",
            "options": {
                "a": "Berlin",
                "b": "Madrid",
                "c": "Paris",
                "d": "Rome"
            },
            "answer": "c"
        },
        {
            "question": "2. What is 5 + 7?",
            "options": {
                "a": "10",
                "b": "11",
                "c": "12",
                "d": "13"
            },
            "answer": "c"
        },
        {
            "question": "3. Who wrote 'To Kill a Mockingbird'?",
            "options": {
                "a": "Harper Lee",
                "b": "Mark Twain",
                "c": "Ernest Hemingway",
                "d": "F. Scott Fitzgerald"
            },
            "answer": "a"
        },
        {
            "question": "4. What is the largest planet in our solar system?",
            "options": {
                "a": "Earth",
                "b": "Mars",
                "c": "Jupiter",
                "d": "Saturn"
            },
            "answer": "c"
        },
        {
            "question": "5. What is the boiling point of water in Celsius?",
            "options": {
                "a": "90",
                "b": "100",
                "c": "110",
                "d": "120"
            },
            "answer": "b"
        }

    ]
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"{key}.{value}")

        user_answer = input("Your answer :")

        if user_answer == q["answer"]:
            print("Correct")
            score += 1
        else:
            print(f"Wrong! The correct answer is :  '{q['answer']}'.")

    print("/nQuiz Finished")
    print(f"You final sccore is : {score}/{len(questions)}")


quiz_app()