import os
from dotenv import load_dotenv
from openai import OpenAI

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
                           " to provide the answer. Also, make the question so that the student is able to solve"
                           " without a calculator. The question should be questions for grade nines and try to make"
                           "the questions questions from grade nine EQAO. Do not make the"
                           " question about cubic functions or need any functions. Only ask 1 question."
                           "Make it so students can solve the question able to solve with hand without a calculator."
            },
            {
                "role": "user",
                "content": str(level),
            }
        ],
        model="gpt-4",
    )
    message = chat_completion.choices[0].message.content
    return message




def checkgpt(a, q):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are going to check a question's answer with a students answer for math. The students "
                           "answer might contain an asterisks, which means multiply. The question and answer "
                           "are going to be formatted like this: students_answer | question. "
                           "Look at the question to see if the students answer is correct. Double check if you're "
                           "correct. If the students answer is a rounded version of the answer, it is correct. If "
                           "the students version doesn't have units, but the question doesn't explicitly ask for"
                           "units, its correct. Also, if the student provides like the answer as a power or a fraction"
                           ", the answer is correct."
                           " REPLY WITH EITHER 'yes' or 'no'. Respond yes if the"
                           "answer is correct and no if the answer is wrong. "
                           "Also, if the answer is wrong, You are "
                           "going to give an explanation on a math question and then provide the answer at the "
                           "start. The math question is going to be provided. This is how I want you to format it with"
                           "the answer at the front:"
                           "Explanation: your_explanation_here\nAnswer: your_answer_here. If the answer"
                           "is correct, answer with only 'yes'."
            },
            {
                "role": "user",
                "content": str(a) + " | " + str(q),
            }
        ],
        model="gpt-4",
    )
    answer = chat_completion.choices[0].message.content
    return answer


def explaingpt(q):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are going to give an explanation on a math question and then provide the answer at the "
                           "start. The math question is going to be provided. This is how I want you to format it with"
                           "the answer at the front:"
                           "Answer: your_answer_here\nExplanation: your_explanation_here"
            },
            {
                "role": "user",
                "content": str(q),
            }
        ],
        model="gpt-4",
    )
    explanation = chat_completion.choices[0].message.content
    return explanation


def replace_bracket(a):
    h = a.replace("(", "")
    e = h.replace(")", "")
    return e


continuing = True
level = 1
score = 0
while continuing:
    chatgpt_question = str(askgpt(level))
    print(f"\nScore: {score}\nLevel: {level}\n")
    print(chatgpt_question)

    print()
    user_answer = input("\nYour answer: ").replace(" ", "")

    # print(checkgpt(user_answer, chatgpt_answer, chatgpt_question))
    check = str(checkgpt(user_answer, chatgpt_question).lower())
    if check == "yes":
        print("Congratulations!! 🎉🎉")
        input("\nContinue: ")
    else:
        print("Sorry, that was not correct.")
        print(check)
        print(f"Score: {score}")
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
    score += int(level)
    level += 1
