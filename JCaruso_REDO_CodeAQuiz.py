blanks = ["__1__", "__2__", "__3__", "__4__"]

easy_level = """What is a computer? How does it do so many things? A computer\n has been defined as essentially a machine that stores and\n manipulates __1__. It does this under the control of a computer\n __2__. So the __1__ goes into a computer and is changed by a __2__\n as __1__ in new forms; it is then displayed as __3__. If the __2__\n changes, the computer performs different actions, different tasks.\n Computers are basically machines for carrying out -- or __4__ --\n different tasks through varying sequences of actions.\n"""

easy_correct_answers = ["information", "program", "output", "executing"]

medium_level = """Iteration can also be called a __1__ mechanism. Like a conditional\n statement, a __1__ begins with a test. If the test evaluates to __2__,\n the computer program executes the __1__ body once and then goes\n back to re-evaluate the test. The syntax of a __3__ __1__ in\n Python programming language is - __3__ expression: statement(s). Another\n conditional language mechanism, the __4__ __1__, is used more\n often in Python to simplify programs that contain iteration.\n"""

medium_correct_answers = ["loop", "true", "while", "for"]

hard_level = """When you're trying to solve some coding problem, often you'll\n find an existing __1__ that creates objects that do ALMOST\n what you need. What can you do? You could modify this old\n __1__, but you'll make it more complicated. The solution is\n __2__, creating a new __1__ from an existing one, but with\n some additions or changes. With __2__, you define only what\n you need to add or change. The original is called the __3__,\n the new one the __4__.\n"""

hard_correct_answers = ["class", "inheritance", "parent", "child"]

# This function checks for the exact match (no punctuation) of the blank and its place in the level paragraph.
def match_blanks(match, blanks):
    for same in blanks:
        if same in match:
            return same
    return None

# function_one -- it and the others will be properly named once I get things to work -- prompts user to input a
#  level selection -- easy/medium/hard.
# Then it passes the correct level string, and answers, to Function_two
# It still needs to check that those words have actually been input.


def function_one():
    level_selection = raw_input("Choose a game difficulty (lower case) by typing in easy, medium, or hard: \n")
    if level_selection == "easy":
        print "You chose an easy quiz. 4 guesses. Let's go! \n \n"
        print "The paragraph now reads: \n"
        print easy_level
        return easy_level, easy_correct_answers
    elif level_selection == "medium":
        print "You chose a medium quiz. 3 guesses. Let's go! \n \n"
        print "The paragraph now reads: \n"
        print medium_level
        return medium_level, medium_correct_answers
    elif level_selection == "hard":
        print "You chose a hard quiz. Only 2 guesses. Let's go! \n \n"
        print "The paragraph now reads: \n"
        print hard_level
        return hard_level, hard_correct_answers
    else:
        return "Not valid input. You'll need to relaunch the quiz."

# I based function_two on the final MadLibs generator project for the IPND. It grabs the user response to what should
# go into the first blank. I pass this to function_three, which checks whether it's in the chosen level's answers.

def function_two():
    level, answers = function_one()
    level = level.split()
    for match in level:
        switch = match_blanks(match, blanks)
        if switch != None:
            answer_input = raw_input("What should be substituted in " + switch + " ?")
            return function_three(answer_input, answers)

# The only way I was able successfully to pass the user's response to function_three was by returning it with
# the user response and level answers from function_two as parameters. It does check that the response is in
# the right level's answers, but exits if the response is correct and, if incorrect, prints 4 "Wrong!"s if the
# response is not in the answers or, if the response is in the answers but not the right answer for the first blank,
# a "Wrong!" for each index for which the response does not match and the "OKAY!" for where it does.
# I put in the prints to see that I was at least getting to function_three. I cannot get back to function_two from
# it after many tries, with and without passing in function_two's returns as parameters, or through any other of
# my many, many attempts.

def function_three(answer_input, answers):
    # answer_input, answers = function_two()
    for i in range(len(answers)):
        guess = answers[i]
        if answer_input == guess:
            print "OKAY!"
            return guess
        elif answer_input != guess:
            print "Wrong!"
    return function_two()

# I want, per the response to my initial submission, to pass to a fourth function, from function_two, an answer
# deemed as correct by function_three along with an "updated level string," but I have not been able to get past
# passing data to and from functions one and two. If I could, I believe what I'd want to do in function_four,
# would be, again using the MadLibs generator as example, to append and join the split level paragraph.

#def function_four():
#    ???

#


function_two()
