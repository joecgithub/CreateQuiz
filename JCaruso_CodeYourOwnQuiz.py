import textwrap
#Assignments for answer trys variables:
easy_trys = 4
med_trys = 3
hard_trys = 2

#Introduction, user chooses difficulty level, and invalid input check:
def choose_difficulty():
    print "Hello to Joe's quiz!\n"
    print "The difficulty level determines how many trys you get: "
    print "easy = 4, medium = 3, hard = only 2!\n"
    start = raw_input("Type in (lower case) your difficulty choice - easy, medium, or hard: ")
    if start == "easy":
       print "You chose an easy quiz. 4 total chances - Let's go!\n"
       return easy_question_1()
    elif start == "medium":
       print "You chose a medium quiz. 3 total chances - Let's go!\n"
       return med_question_1()
    elif start == "hard":
       print "You chose a hard quiz. 2 total chances - Let's go!\n"
       return hard_question_1()
    else:
        print "Not valid input. You'll need to launch the quiz again."

#Functions for failing and exit, and for checking 3 levels' trys: 
def failure():
    print "Sorry! No more tries!"
    print "Type 'exit' to quit."
    exit = raw_input(" ")
    if exit == "exit":
        quit()
    else:
        print "Not valid input"
        failure()

def check_easy_trys():
    if easy_trys == 0:
        failure()
    else:
        print "Incorrect! You have:", easy_trys, "more chances!\n"

def check_med_trys():
    if med_trys == 0:
        failure()
    else:
        print "Incorrect! You have:", med_trys, "more chances!\n"

def check_hard_trys():
    if hard_trys == 0:
        failure()
    else:
        print "Incorrect! You have:", hard_trys, "more chances!\n"

# 4 functions for easy quiz questions:
def easy_question_1():
    #I'd strongly recommend against calling global variables. Global variables are so notoriously problematic, that some programmers refer to them as evil:
    # http://stackoverflow.com/questions/19158339/why-are-global-variables-evil
    # Instead, pass your variables between your functions using return statements.
    global easy_trys
    print "In the following paragraph, you need to replace the numbered\n blanks with the correct answers - all lowercase - one by one:\n"
    print "What is a computer? How does it do so many things? A computer\n has been defined as essentially a machine that stores and\n manipulates __1__. It does this under the control of a computer\n __2__. So the __1__ goes into a computer and is changed by a __2__\n as __1__ in new forms; it is then displayed as __3__. If the __2__\n changes, the computer performs different actions, different tasks.\n Computers are basically machines for carrying out -- or __4__ --\n different tasks through varying sequences of actions.\n"
    easy_answer_1 = raw_input("What should be substituted in __1__? ")
    if easy_answer_1 == "information":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "What is a computer? How does it do so many things? A computer\n has been defined as essentially a machine that stores and\n manipulates information. It does this under the control of a computer\n __2__. So the information goes into a computer and is changed\n by a __2__ as information in new forms; it is then displayed as\n __3__. If the __2__ changes, the computer performs different actions,\n different tasks. Computers are basically machines for carrying\n out -- or __4__ -- different tasks through varying sequences of actions.\n"
        easy_question_2()
    else:
        easy_trys -= 1
        check_easy_trys()
        easy_question_1()

def easy_question_2():
    global easy_trys
    easy_answer_2 = raw_input("What should go in __2__? ")
    if easy_answer_2 == "program":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "What is a computer? How does it do so many things? A computer\n has been defined as essentially a machine that stores and\n manipulates information. It does this under the control of a computer\n program. So the information goes into a computer and is changed by a program\n as information in new forms; it is then displayed as __3__. If the program\n changes, the computer performs different actions, different tasks.\n Computers are basically machines for carrying out -- or __4__ --\n different tasks through varying sequences of actions.\n"
        easy_question_3()
    else:
        easy_trys -= 1
        check_easy_trys()
        easy_question_2()

def easy_question_3():
    global easy_trys
    easy_answer_3 = raw_input("What should go in __3__? ")
    if easy_answer_3 == "output":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "What is a computer? How does it do so many things? A computer\n has been defined as essentially a machine that stores and\n manipulates information. It does this under the control of a computer\n program. So the information goes into a computer and is changed by a program\n as information in new forms; it is then displayed as output. If the program\n changes, the computer performs different actions, different tasks.\n Computers are basically machines for carrying out -- or __4__ --\n different tasks through varying sequences of actions.\n"
        easy_question_4()
    else:
        easy_trys -= 1
        check_easy_trys()
        easy_question_3()

def easy_question_4():
    global easy_trys
    easy_answer_4 = raw_input("What should go in __4__? ")
    if easy_answer_4 == "executing":
        print "Correct!\n"
        print "Congrats! The completed, correct paragraph now reads:\n "
        print "What is a computer? How does it do so many things? A computer\n has been defined as essentially a machine that stores and\n manipulates information. It does this under the control of a computer\n program. So the information goes into a computer and is changed by a program\n as information in new forms; it is then displayed as output. If the program\n changes, the computer performs different actions, different tasks.\n Computers are basically machines for carrying out -- or executing --\n different tasks through varying sequences of actions.\n"
        quit()
    else:
        easy_trys -= 1
        check_easy_trys()
        easy_question_4()

# 4 functions for medium quiz questions: 
def med_question_1():
    global med_trys
    print "In the following paragraph, you need to replace the numbered\n blanks with the correct answers - all lowercase - one by one:\n"
    print "Iteration can also be called a __1__ mechanism. Like a conditional\n statement, a __1__ begins with a test. If the test evaluates to __2__,\n the computer program executes the __1__ body once and then goes\n back to re-evaluate the test. The syntax of a __3__ __1__ in\n Python programming language is - __3__ expression: statement(s). Another\n conditional language mechanism, the __4__ __1__, is used more\n often in Python to simplify programs that contain iteration.\n"
    med_answer_1 = raw_input("What should be substituted in __1__? ")
    if med_answer_1 == "loop":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "Iteration can also be called a loop mechanism. Like a conditional\n statement, a loop begins with a test. If the test evaluates to __2__,\n the computer program executes the loop body once and then goes back to\n re-evaluate the test. The syntax of a __3__ loop in Python programming\n language is - __3__ expression: statement(s). Another conditional language\n mechanism, the __4__ loop, is used more often in Python to simplify\n programs that contain iteration.\n"
        med_question_2()
    else:
        med_trys -= 1
        check_med_trys()
        med_question_1()

def med_question_2():
    global med_trys
    med_answer_2 = raw_input("What should go in __2__? ")
    if med_answer_2 == "true":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "Iteration can also be called a loop mechanism. Like a conditional\n statement, a loop begins with a test. If the test evaluates to True,\n the computer program executes the loop body once and then goes back to\n re-evaluate the test. The syntax of a __3__ loop in Python programming\n language is - __3__ expression: statement(s). Another conditional language\n mechanism, the __4__ loop, is used more often in Python to simplify\n programs that contain iteration.\n"
        med_question_3()
    else:
        med_trys -= 1
        check_med_trys()
        med_question_2()

def med_question_3():
    global med_trys
    med_answer_3 = raw_input("What should go in __3__? ")
    if med_answer_3 == "while":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "Iteration can also be called a loop mechanism. Like a conditional\n statement, a loop begins with a test. If the test evaluates to True,\n the computer program executes the loop body once and then goes back to\n re-evaluate the test. The syntax of a while loop in Python programming\n language is - while expression: statement(s). Another conditional language\n mechanism, the __4__ loop, is used more often in Python to simplify\n programs that contain iteration.\n"
        med_question_4()
    else:
        med_trys -= 1
        check_med_trys()
        med_question_3()

def med_question_4():
    global med_trys
    med_answer_4 = raw_input("What should go in __4__? ")
    if med_answer_4 == "for":
        print "Correct!\n"
        print "Congrats! The completed, correct paragraph now reads:\n "
        print "Iteration can also be called a loop mechanism. Like a conditional\n statement, a loop begins with a test. If the test evaluates to True,\n the computer program executes the loop body once and then goes back to\n re-evaluate the test. The syntax of a while loop in Python programming\n language is - while expression: statement(s). Another conditional language\n mechanism, the for loop, is used more often in Python to simplify\n programs that contain iteration.\n"
        quit()
    else:
        med_trys -= 1
        check_med_trys()
        med_question_4()

# 4 functions for hard quiz questions:
def hard_question_1():
    global hard_trys
    print "In the following paragraph, you need to replace the numbered\n blanks with the correct answer - all lowercase - one by one:\n"
    print "When you're trying to solve some coding problem, often you'll\n find an existing __1__ that creates objects that do ALMOST\n what you need. What can you do? You could modify this old\n __1__, but you'll make it more complicated. The solution is\n __2__, creating a new __1__ from an existing one, but with\n some additions or changes. With __2__, you define only what\n you need to add or change. The original is called the __3__,\n the new one the __4__.\n"
    hard_answer_1 = raw_input("What should be substituted in __1__? ")
    if hard_answer_1 == "class":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "When you're trying to solve some coding problem, often you'll\n find an existing class that creates objects that do ALMOST\n what you need. What can you do? You could modify this old\n class, but you'll make it more complicated. The solution is\n __2__, creating a new class from an existing one, but with\n some additions or changes. With __2__, you define only what\n you need to add or change. The original is called the __3__,\n the new one the __4__.\n"
        hard_question_2()
    else:
        hard_trys -= 1
        check_hard_trys()
        hard_question_1()

def hard_question_2():
    global hard_trys
    hard_answer_2 = raw_input("What should go in __2__? ")
    if hard_answer_2 == "inheritance":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "When you're trying to solve some coding problem, often you'll\n find an existing class that creates objects that do ALMOST\n what you need. What can you do? You could modify this old\n class, but you'll make it more complicated. The solution is\n inheritance, creating a new class from an existing one, but with\n some additions or changes. With inheritance, you define only what\n you need to add or change. The original is called the __3__,\n the new one the __4__.\n"
        hard_question_3()
    else:
        hard_trys -= 1
        check_hard_trys()
        hard_question_2()

def hard_question_3():
    global hard_trys
    hard_answer_3 = raw_input("What should go in __3__? ")
    if hard_answer_3 == "parent":
        print "Correct!\n"
        print "The paragraph now reads: "
        print "When you're trying to solve some coding problem, often you'll\n find an existing class that creates objects that do ALMOST\n what you need. What can you do? You could modify this old\n class, but you'll make it more complicated. The solution is\n inheritance, creating a new class from an existing one, but with\n some additions or changes. With inheritance, you define only what\n you need to add or change. The original is called the parent,\n the new one the __4__.\n"
        hard_question_4()
    else:
        hard_trys -= 1
        check_hard_trys()
        hard_question_3()

def hard_question_4():
    global hard_trys
    hard_answer_4 = raw_input("What should go in __4__? ")
    if hard_answer_4 == "child":
        print "Correct!\n"
        print "Congrats! The completed, correct paragraph now reads:\n "
        print "When you're trying to solve some coding problem, often you'll\n find an existing class that creates objects that do ALMOST\n what you need. What can you do? You could modify this old\n class, but you'll make it more complicated. The solution is\n inheritance, creating a new class from an existing one, but with\n some additions or changes. With inheritance, you define only what\n you need to add or change. The original is called the parent,\n the new one the child.\n"
        quit()
    else:
        hard_trys -= 1
        check_hard_trys()
        hard_question_4()

choose_difficulty()