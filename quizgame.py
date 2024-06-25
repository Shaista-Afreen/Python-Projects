selection=input("Select any quiz type A.GK QUIZ B.SPORTS/GAMES: C.SCIENCE QUIZ ").upper()
if selection == 'A':
    print("You selected General Knowledge Quiz")
    questions1=("What is the closest planet to the sun?",
           "How many continents are there?",
           "Which planet is known as the Red Planet?",
           "What is the largest ocean on Earth?",
           "What is the largest mammal in the world?")
    options1=(("A.Mercury ","B.Earth ","C.Venus ","D.Jupiter "),
        ("A.Seven ","B.Six ","C.Five ","D.Eight "),
        ("A.Venus ","B.Earth ","C.Mars ","D.Jupiter "),
        ("A.The Pacific Ocean ","B.Atlantic","C.Indian ","D.Arctic"),
        ("A.The African Elephant ","B.The Blue Whale ","C.The Fin Whale ","D.Giraffe "))
    answers1=("A","A","C","A","B")
    guesses1=[]
    score1=0
    question_num1=0

    for question1 in questions1:
        print("**************************")
        print(question1)
        for option1 in options1[question_num1]:
            print(option1)

        guess1=input("Enter (A,B,C,D): ").upper()
        guesses1.append(guess1)
        if guess1 == answers1[question_num1]:
            score1 += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers1[question_num1]} is the correct answer")
        question_num1 += 1


    print("******************")
    print("  RESULTS   ")
    print("*******************")
    print("Answers: ", end="")
    for answer1 in answers1:
        print(answer1,end=" ")
    print()
    print("Guesses: ", end="")
    for guess1 in guesses1:
        print(guess1,end=" ")
    print()
        # score = int(score / len(questions))
    print(f"Your score is {score1}/5")


elif selection == 'B':
    print("You have selected Sports/Game Quiz")
    questions2=("What sport is considered the most popular in the world? ",
           "Which country won the first ever cricket world cup in 1975? ",
           "Which country has won the most icc cricket world cup titles ? ",
           "Which country is known for introducing the game of cricket to the world? ",
           "Which is the national sport of america ?")
    options2=(("A.Football ","B.Tennis ","C.Golf ","D.Basketball "),
        ("A.Australia ","B.West Indies ","C.England ","D.India "),
        ("A.West Indies ","B.India ","C.Australia ","D.Pakistan "),
        ("A.India ","B.England ","C.Australia ","D.West Indies "),
        ("A.Baseball ","B.Ice Hockey ","C.Tennis ","D.Golf "))
    answers2=("A","B","C","B","A")
    guesses2=[]
    score2=0
    question_num2=0


    for question2 in questions2:
        print("------------------------")
        print(question2)
        for option2 in options2[question_num2]:
            print(option2)

        guess2=input("Enter (A,B,C,D): ").upper()
        guesses2.append(guess2)
        if guess2 == answers2[question_num2]:
            score2 += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers2[question_num2]} is the correct answer")
        question_num2 += 1


    print("******************")
    print("  RESULTS   ")
    print("*******************")
    print("Answers: ", end="")
    for answer2 in answers2:
        print(answer2,end=" ")
    print()
    print("Guesses: ", end="")
    for guess2 in guesses2:
        print(guess2,end=" ")
    print()
        # score = int(score / len(questions))
    print(f"Your score is {score2}/5")
    # print(f"Your score is {score/len(questions)}")
    # score = int(score / len(questions) * 100)
    # print(f"Your score is : {score}%")

elif selection == 'C':
    print("You have selected SCIENCE Quiz")
    questions3=("What is the powerhouse of the cell?",
           "What is the largest organ in the human body?",
           "Which gas is most abundant in the Earth's atmosphere?",
           "Which planet has the most moons?",
           "What is the most common type of star in the Milky Way galaxy?")
    options3=(("A.Nucleus ","B.Ribosome ","C.Mitochondria ","D.Endoplasmic reticulum "),
        ("A.Heart ","B.Liver ","C.Lungs ","D.Skin "),
        ("A.Oxygen ","B.Carbondioxide ","C.Nitrogen ","D.Hydrogen "),
        ("A.Jupiter ","B.Mars ","C.Earth ","D.Saturn "),
        ("A.Red giant ","B.White dwarf ","C.Red dwarf ","D.Blue giant "))
    answers3=("C","D","C","A","C")
    guesses3=[]
    score3=0
    question_num3=0


    for question3 in questions3:
        print("***************************")
        print(question3)
        for option3 in options3[question_num3]:
            print(option3)

        guess3=input("Enter (A,B,C,D): ").upper()
        guesses3.append(guess3)
        if guess3 == answers3[question_num3]:
            score3 += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers3[question_num3]} is the correct answer")
        question_num3 += 1


    print("******************")
    print("  RESULTS   ")
    print("*******************")
    print("Answers: ", end="")
    for answer3 in answers3:
        print(answer3,end=" ")
    print()
    print("Guesses: ", end="")
    for guess3 in guesses3:
        print(guess3,end=" ")
    print()
        # score = int(score / len(questions))
    print(f"Your score is {score3}/5")
        # print(f"Your score is {score/len(questions)}")
        # score = int(score / len(questions) * 100)
        # print(f"Your score is : {score}%")


else :
    print("No proper option selected")
