## A simple quiz game


def answer_check(question, answer):
    global players_score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if question.lower() == answer.lower():
            print(f'Correct, the answer was {answer} ')
            players_score = players_score + 1
            print(f'your scores is {players_score}')
            print('Next Question:')
            still_guessing = False
        else:
            if attempt < 2:
                question = input('Incorrect, go watch the Marvel series on Netflix and try again')
                attempt = attempt + 1
    if attempt == 3:
        print(f'You are Suck the correct answer was {answer}')

players_score = 0;

print(f'Welcome to John\'s quiz game, you will whiz this quiz')

question1 = input('This Marvel super hero is blind and protects Hells Kitchen :')
answer_check(question1, 'dare devil')

question2 = input('This Harlem hero is bullet proof and almost indestrucatble?')
answer_check(question2, 'luke cage')

question3 = input('Danny Rand is also this Marvel super hero from Kung-lung?')
answer_check(question3, 'iron fist')

question4 = input('She is a private eye with super strength and a bad attitude?')
answer_check(question4, 'Jessica Jones')

question5 = input('He is know for grunting and screaming \'BILLY RUSSSSSOOOOOOO\'')
answer_check(question5, 'punisher')





