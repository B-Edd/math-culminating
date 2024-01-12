import os
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
)


def format_power(base, exponent):
    # Using Unicode superscript characters for formatting
    formatted_result = f"{base}^{str(exponent).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹'))}"
    return formatted_result


high_score = open('high-score.txt', 'r').read()

print("Welcome to ...")
print('''   ####    ####    ##       ##   ##    #####           #######  ##   ##    #####             #####    ####   ##   ##    ##     #######   ####     ####    ##   ## 
  ##  ##  ##  ##   ##       ##   ##   ##                 ##     ##   ##   ##                ##       ##  ##  ##   ##   ####      ##       ##     ##  ##   ###  ## 
 ##       ##   ##  ##       ##   ##  ##                  ##     ##   ##  ##                ##       ##   ##  ##   ##   ## ##     ##       ##     ##   ##  #### ## 
  #####   ##   ##  ##       ##   ##  ######              ##     #######  ######            ######   ##   ##  ##   ##  ##   ##    ##       ##     ##   ##  ####### 
      ##  ##   ##  ##       ##  ##   ##                  ##     ##   ##  ##                ##       ##   ##  ##   ##  #######    ##       ##     ##   ##  ## #### 
 ##   ##  ##   ##  ###       ## ##   ##                  ##     ##   ##  ##                ##        #####   ##  ##   ##   ##    ##       ##     ##   ##  ##  ### 
  #####    #####    ######    ###    #######             ##     ##   ##  #######           #######      ##    ####    ##   ##    ##      ####     #####   ##   ## 
                                                                                                                                                                  
''')

# os.system("clear")
print(
    "How to play: Solve math equations to gain points. As you solve more questions, the questions get increasingly "
    "harder, but each question is worth more points. \nTry to beat the Highscore: ",
    end='')
if high_score:
    print(high_score)
else:
    print("0")

cont = input("\nType 'ok' to start: ").lower()
while cont != 'ok':
    cont = input("Type 'ok' to start: ").lower()

os.system('clear')


# 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

def askgpt(level):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are going to give a mathematical question for grade 9's. There are different levels "
                           "that go up"
                           "infinitely and become harder as the levels progress. Level 1 is going to be about "
                           "scientific notation. Level 2 is going to be about evaluating and simplifying math"
                           " powers. Only give questions that include product rule, quotient rule, power of a power, "
                           "power of a product, power of a quotient, zero exponent, and negative exponent. As the "
                           "level increases to 3, make the questions harder by making it so that solving the "
                           "question needs multiple steps. From level 4, make questions about BEDMAS. As the "
                           "level get higher from 5, make it so more steps are needed to solve the question. "
                           "From level 6, make the questions be about fractions. Make it be about comparing "
                           "which fractions are bigger and include negative fractions, changing improper to mixed "
                           "and vice versa, adding, subtracting, multiplying, and dividing. Level 7 are going to "
                           "be about infinity, limit, and density. Level 8 are going to be about number sets. "
                           "Natural, whole, integers, rational, irrational, and real numbers. Level 9 are going to"
                           "be about slope, like finding slope when given a table or two points on a graph. You can use"
                           " words instead of slope like gradient, rate of change, etc. Level 10 are going to be "
                           "about the equation: y=mx+b like finding the slope, y-intercept, and equation from a table "
                           "or word questions. The level 11 are going to be about the point of interception. For"
                           " example, give a table to find the point of interception. You can write solution of a "
                           "linear system instead of point of interception. The level 12 are going to be about"
                           " giving a equation and asking if the line is a vertical or horizontal, negative, or "
                           "positive. The level 13 are going to be about the pythagorean theorem, or the right "
                           "angle triangle. The level 14 are going to be about financial literacy. Create word "
                           "questions containing words like Gross Income, Net Income, Balanced Budget, Deductions, "
                           "Income, Assets, Fixed Expenses, Variable Expenses, Non-discretionary, Expenses, "
                           "Discretionary expenses, Appreciation, Depreciation, Interest, Principal, Interest Rate, "
                           "Amount, Simple Interest, and Compound Interest."
                           "The user will specify the level for each question by giving you a number"
                           "Only give your question. Explicitely ask for the units you want it in. Make the "
                           "answer to the questions a whole number and not a "
                           "decimal. Make the questions so you don't have how to solve the question. Don't include "
                           "the steps to solve it. The student is trying to solve it and don't give any help."
                           "In addition, make the answer of the question lower than 500 and a whole number. Make"
                           " the questions so that students doesn't need to show their work and only needs"
                           " to provide the answer. Eg. answer is 1/2 and student answers 0.5, that is considered"
                           "correct. Also, make the question so that the student is able to solve"
                           " without a calculator. The question should be questions for grade nines and try to make"
                           "the questions questions from grade nine EQAO. Do not make the"
                           " question about cubic functions or need any functions. Only ask 1 question."
                           "Make it so students can solve the question able to solve with hand without a calculator. "
                           "Do not write your answer in your question."
            },
            {
                "role": "user",
                "content": "level" + str(level),
            }
        ],
        model="gpt-3.5-turbo",
    )
    message = chat_completion.choices[0].message.content
    return message


def checkgpt(a, q):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Evaluate the student's math answer, considering various factors. The student's response may involve asterisks to denote multiplication. The format for the question and answer will be: students_answer | corresponding question. Examine the question to determine the correctness of the student's answer. Confirm your assessment and consider the following criteria: If the student's answer is a rounded version of the actual answer, it is considered correct. If the question does not explicitly ask for units, and the student's answer lacks units, consider it correct. If the student's answer is a decimal instead of a fraction, consider it correct. Ignore every single period. Accept answers presented as powers or fractions as correct. Allow variations in comma placement or the absence of commas in the student's answer. For example, if the answer is 5,670 and the student writes 5670, it is considered correct. If the student writes a unit, but the numerical answer is correct, consider it correct. If the student's answer meets any of these conditions, respond with 'yes' without the quotations. For multiplication, use 'x,' and for division, use '/.' Otherwise, provide an explanation about how to solve the question and state the correct answer in the following format (without quotation marks): 'Explanation: your_explanation_here\nAnswer: your_answer_here.' Please provide the math question for evaluation."
            },
            {
                "role": "user",
                "content": str(a) + " | " + str(q),
            }
        ],
        model="gpt-3.5-turbo",
    )
    answer = chat_completion.choices[0].message.content
    return answer


def replace_bracket(a):
    h = a.replace("(", "")
    e = h.replace(")", "")
    return e


continuing = True
level = 1
score = 0
while continuing:
    chatgpt_question = str(askgpt(level)).replace("\\times", "x")
    print(f"\nScore: {score}\nLevel: {level}\n")
    print(chatgpt_question)

    print()
    user_answer = input("\nYour answer: ")

    # print(checkgpt(user_answer, chatgpt_answer, chatgpt_question))
    check = str(checkgpt(user_answer, chatgpt_question).lower())
    try:
        correct_ans = (check.replace(" ", "")).split("answer: ")[1]
        print("correctaseas", correct_ans)
    except IndexError:
        correct_ans = 3
    if 'y|es' in check or 'yes' in check or correct_ans == user_answer or str(user_answer) + "." in check:
        print("Congratulations!! 🎉🎉")
        score += int(level)
        print(f"Score: {score}")
        input("\nContinue: ")
    else:
        print("Sorry, that was not correct.")
        print(check)
        print(f"your answer: {user_answer}")
        print(f"Score: {score}")
        time.sleep(3)
    if level == 14:
        continuing = False
        if high_score:
            if score > int(high_score.split(", ")[1]):
                with open('high-score.txt', 'w') as file:
                    name = input("What is your name?: ")
                    file.write(name + ", " + str(score))
        else:
            with open('high-score.txt', 'w') as file:
                name = input("What is your name?: ")
                file.write(name + ", " + str(score))
        exit()
    print("...")
    os.system("clear")
    level += 1
