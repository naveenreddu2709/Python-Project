from tkinter import *
import random
import os

root=Tk()
# Set the screen size
screen_width=900
screen_height=600
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False,False)
root.title("Quiz Competition")

# gettin img path
script_dir = os.path.dirname(os.path.abspath(__file__))
def path(pth):
    return os.path.join(script_dir,f"images\{pth}")

# set background image
backimg=PhotoImage(file=path("quiz_bg.png"))
bgimg=Label(image=backimg).place(x=0,y=0,relheight=1,relwidth=1)
root.config(bg="black")

# Quiz variables
option1= StringVar()
option2= StringVar()
option3= StringVar()
option4= StringVar()
option1.set("")
option2.set("")
option3.set("")
option4.set("")
attempt=0
score =0
inc_done=True
next = False
repeat_ques=[]
ques_index=0

# 30 Questions for quiz
Question=["Python is a __ language.",
          "Elif used after_.",
          "Python is Slower than __.",
          "Which of the following data types in \nPython is mutable?",
          "Which of the following is the best way\n to comment multiple lines in Python?",
          "Which method is used to remove the last\n element from a list in Python?",
          "Which of the following is NOT a valid\n data type in Python?",
          'What is the correct syntax to open a \nfile named "example.txt" in read mode in Python?',
          "Which of the following statements is \nused to exit a loop prematurely in Python?",
          "Which of the following is used to define\n a function in Python?",
          "What does the len() function in Python\n return?",
          "What symbol is used for single-line comments in Python?",
          "Which of the following data types is mutable in Python?",
          "What is the result of '9%4' in Python?",
          "What will be the result of the expression\n 3 * 'abc' in Python?",
          "Which of the following is used to remove \nelement from a list in Python?",
          "What is the result of the expression 'abs(-5)'\n in Python?",
          "What is the result of the expression\n 'not False' in Python?",
          "Output of: my_string = 'Hello, World!'\nprint(my_string[3:7])",
          '''What is the output of the following code?\nprint("Hello" + 3)''',
          '''What will be the output of the following code?\nprint(5 == "5")''',
          '''Which of the following is used to check the\n data type of a variable in Python?''',
          '''What is the result of the expression \n'max([4, 7, 1, 9])' in Python?''',
          '''How do you remove an item from a set \nin Python?''',
          '''What is the output of the following code?\nprint("Hello".replace('l', 'w'))''',
          '''Which of the following methods is used to\n sort a list in Python?''',
          '''How do you create a tuple with a single\n element in Python?''',
          '''What is the result of the expression \nsum([1, 2, 3, 4]) in Python?''',
          '''How do you define a dictionary in Python?''',
          '''What will be the output of the following code?\nprint("Hello".upper())''',
          ]

# 30*4 Options according to their sequence
Option=[["Funny",
         "Machine",
         "High level",
         "Middle level"],

        ["If",
         "Else",
         "Break",
         "Continue"],

        ["C",
         "C++",
         "Both A and B",
         "None of the above"],

        ["int",
         "str",
         "list",
         "tuple"],

         ["/* */",
          "#",
          '""" """',
          "//"],
            
         ["remove()",
          "pop()",
          "delete()",
          "clear()"],
            
         ["list",
          "dictionary",
          "tuple",
          "struct"],
            
         ['file = open("example.txt", "r")',
          'open("example.txt", mode="read")',
          'open("example.txt", "read")',
          'file = open("example.txt", mode="r")'],
            
         ["stop",
          "break",
          "end",
          "exit"],
            
         ["def",
          "function",
          "define",
          "fun"],
            
         ["The length of a string",
          "The number of elements in a list or tuple",
          "The number of characters in a string",
          "All of the above"],
            
         [r"//",
          r"#",
          r"/*",
          r"--"],
            
         ["int",
          "float",
          "tuple",
          "list"],
            
         ["1",
          "3",
          "2.25",
          "0.25"],
            
         ["'abcabcabc'",
          "'9abc'",
          "'aabbcc'",
          "Error"],
            
         ["pop()",
          "remove()",
          "delete()",
          "del"],
            
         ["5",
          "-5",
          "Error",
          "None"],
            
         ["True",
          "False",
          "Error",
          "None"],
            
         ["ello",
          "o, W",
          "lo,",
          "lo, W"],
            
         ["Hello3",
          "Syntax Error",
          "HelloHelloHello",
          "3Hello"],
            
         ["True",
          "False",
          "Error",
          "None"],
            
         ["typeof()",
          "type()",
          "data_type()",
          "check_type()"],
            
         ["1",
          "9",
          "7",
          "[4, 7, 1, 9]"],
            
         ["remove()",
          "discard()",
          "pop()",
          "All of the above"],
            
         ["Hewwo",
          "Hellow",
          "Hewlo",
          "Error"],
            
         ["sort()",
          "sorted()",
          "order()",
          "arrange()"],
            
         ["(1)",
          "(1,)",
          "(1)",
          "1,"],
            
         ["10",
          "6",
          "1, 2, 3, 4",
          "Error"],
            
         ["{ }",
          "{ : }",
          "[ ]",
          "( )"],
            
         ["hello",
          "HELLO",
          "Hello",
          "Error"],
         ]

# Answer of all questions
Ans=["C","A","C","C","C","B","D","A","B","A","D","B","D","A","A","B","A","A","D","B","B","B","B","D","A","A","A","A","A","B"]

# Making list of users input
result=[]

# taking your choice
def click(event):
    global attempt
    global inc_done
    global next
    
    # getting option index
    text=event.widget.cget("text")
    guess=text[:1]
    result.append(guess)

    # checking the result
    if(guess==Ans[ques_index]):
        res.config(text="Correct....",font="Harrington 40 bold",fg="green")
        global score
        next = True
        if inc_done:
            score+=10
            inc_done=False
    else:
        inc_done=False
        next = True
        res.config(text=f"Incorrect....\nCorrect answer is {Ans[ques_index]}",font="Harrington 20 bold",fg="red")
    
    # display the score
    scr.config(text=f"Score: {score}/100")
    res.update()

# for next question
def next_ques():
    global next
    if next:    
        global inc_done
        inc_done=True
        res.config(text="")
        global attempt
        attempt+=1
        next = False
        quizstart()

# Show score at the end
def end_quiz(s):
    frame1=Frame(borderwidth=10,relief=GROOVE,bg="blue")
    frame1.place(x=150,y=100,width=600,height=300)
    scorefrm = Frame(borderwidth=10,relief=GROOVE,bg="white")
    scorefrm.place(x=170,y=120,width=560,height=260)
    res_Score=Label(scorefrm,text=f"Your Score :\n{s}/100",font="Harrington 70 bold",bg="red",fg="violet")
    res_Score.pack(pady=10)
    root.update()

# show question for quiz
def quizstart():
    global attempt
    global ques_index
    if attempt<=9:
        global repeat_ques
        while True:
            ques_index= random.randint(0,29)
            if ques_index in repeat_ques:
                pass
            else:
                repeat_ques.append(ques_index)
                break
        que.config(text=f"{attempt+1}. {Question[ques_index]}")
        option1.set(f"A. {Option[ques_index][0]}")
        option2.set(f"B. {Option[ques_index][1]}")
        option3.set(f"C. {Option[ques_index][2]}")
        option4.set(f"D. {Option[ques_index][3]}")
    else:
        scr.config(text="")
        end_quiz(score)
    root.update()

# question label
que=Label(root,text="",font="comicansms 20 bold",bg="Black",fg="white")
que.pack(pady=10)

# button with their options
optionA=Button(root,text="",textvariable=option1,font="comicansms 20 bold",bg="red",fg="white")
optionA.bind("<Button-1>",click)
optionA.place(x=100,y=(screen_height-480))
optionB=Button(root,text="",textvariable=option2,font="comicansms 20 bold",bg="white",fg="black")
optionB.bind("<Button-1>",click)
optionB.place(x=100,y=(screen_height-390))
optionC=Button(root,text="",textvariable=option3,font="comicansms 20 bold",bg="#0000FF",fg="white")
optionC.bind("<Button-1>",click)
optionC.place(x=100,y=(screen_height-290))
optionD=Button(root,text="",textvariable=option4,font="comicansms 20 bold",bg="#9400D3",fg="white")
optionD.bind("<Button-1>",click)
optionD.place(x=100,y=(screen_height-200))

# reply label
res = Label(text="",font="Harrington 20 bold",bg="black")
res.place(x=screen_width-300,y=screen_height-100)

# display the scores
scr = Label(text=f"Score: 0/100",font="Harrington 30 bold",bg="black",fg="white")
scr.place(x=80,y=screen_height-100)

# showing the next button
calimg = PhotoImage(file=path("next.png"),width=162,height=70)
sub=Button(root,image=calimg,bg="black",borderwidth=0,activebackground="black",command=next_ques)
sub.place(x=screen_width-550,y=screen_height-100)

# changeing the icon
root.title("Python Quiz")
try:
    icn = path("1.ico")
    root.wm_iconbitmap(icn)
except:
    pass

quizstart()
root.mainloop()