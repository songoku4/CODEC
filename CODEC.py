#Codec VERSION 1.07.02.19
#Runtime Modules:
import tkinter
from tkinter import *
from bracket_test import autocorrect
from block_test import indent_block_test_main
from file_methods import save
from Spelling_check import spell_check_main

####################Setting up GUI#########################################################################################################################################################


#________________________________DATA COLLECTOR____________________________________________________________________________________________________________________________________________

master = Tk()
master.title('CODEC v1.29.10.18')
Label(master,
      text='WELCOME TO CODEC',
      justify=CENTER,
      fg='red',
      bg='yellow',
      font='times 42 bold italic').grid(row=1, sticky=W, padx=20)
t=Message(master,
         font='times 15')
t.grid(row=2, sticky=N)
T1='THIS PROGRAM CHECKS YOUR PROGRAM FOR '
T2="\nSOME VERY SILLY ERRORS THAT COULD RUIN YOUR PROGRAM."
T3=" HOWEVER, THEY CAN BE CORRECTED \nQUITE EFFORTLESSLY"
t.config(text=T1+T2+T3)
Label(master,
      text='Enter the following details :',
      bg='light green',
      font='times 15').grid(row=3, stick=W)
Label(master,
      text="ABSOLUTE PATH OF YOUR PROGRAM=>",
      font='times 10').grid(row=4, column=0, stick=W)
Label(master,
      text="NAME OF YOUR PROGRAM.....................=>",
      font='times 10').grid(row=5, column=0, stick=W, pady=25)
e1=Entry(master, width=60)
e1.grid(row=4, column=0, stick=E, padx=5)
e2=Entry(master, width=60)
e2.grid(row=5, column=0, stick=E, padx=5)
path=e1.get()
name=e2.get()

#________________________________DATA COLLECTOR____________________________________________________________________________________________________________________________________________

def Start_test(x,path,name):
    #Spelling_check
    if C==1:
        print ('spell_test time')
        print ('x>>>>>>>>>',x)
        spell_check_main(x)
        for i in range(len(x)):
            print (type(x[i]),i,x[i])
    #Block_test function
    if B==1:
        indent_block_test_main(x)
    #Bracket_test function
    if D==1:
        autocorrect(x)
    #Program save function
    save(x,path,name)
def enter_det():
    global path
    global name
    path=e1.get()
    name=e2.get()
    print (path,name)
def load():
    global master
    master.destroy()
    exec(open("CODEC.py").read())

#^^^^^^^^^^^^^^TEST SETTINGS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def var_states():
    global B
    global C
    global D
    B=var2.get()
    C=var3.get()
    D=var4.get()
    if B==1:
        print ('test selected > COLON TEST')
    if C==1:
        print ('test selected > SPELLING TEST')
    if D==1:
        print ('test selected > BRACKET TEST')
line='_'*122
Label(master, text=line, pady=4,padx=3).grid(row=8, sticky=W)
Label(master,
      text=" TESTS : ",
      font='times 14 bold',
      fg='red',
      bg='white'
      ,pady=4,
      padx=3).grid(row=9, sticky=W)
var2 = IntVar()
Checkbutton(master,
            text="COLON TEST",
            variable=var2).grid(row=11, sticky=W)
var3 = IntVar()
Checkbutton(master,
            text="SPELLING TEST",
            variable=var3).grid(row=12, sticky=W)
var4 = IntVar()
Checkbutton(master,
            text="BRACKET TEST",
            variable=var4).grid(row=13, sticky=W)
Button(master,
       text='ACCEPT TEST METHODS',
       command=var_states).grid(row=15, sticky=W, pady=4)
Label(master, text=line, pady=4,padx=3).grid(row=16, sticky=W)
#^^^^^^^^^^^^^^TEST SETTINGS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def proceed():
    f=open(path+'\\'+name+'.py','r')
    x=f.readlines()
    f.close()
    for i in range(len(x)):
        a=x[i]
        a=a.lstrip('\n')
        a=a.rstrip('\n')
        x[i]=a
    Start_test(x,path,name)
    window = Toplevel(master)
    Button(window, text='QUIT!', command=master.destroy).pack()
    Button(window, text='RETRY?', command=load).pack()

Button(master, text='QUIT', command=master.destroy).grid(row=18, sticky=W, pady=4,)
Button(master, text='ACCEPT DETAILS', command=enter_det).grid(row=17, sticky=W, pady=4)
Button(master, text='START TESTING', command=proceed).grid(row=18, sticky=N, pady=4, padx=4)
mainloop()

####################Setting up GUI#########################################################################################################################################################
