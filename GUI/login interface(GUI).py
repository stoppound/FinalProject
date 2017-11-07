"""login part"""

from tkinter import *
from tkinter import messagebox

# read csv file  ---> #def readFile():

# verify login  ---> #def verifyLogin(usernameEntry):

# creat username  ---> #def creatUser(usernameEntry):
    #--># after click creat username must check first
    #--># if there's already have a username 
    #--># got a error message

#"""use messagebox"""
# check signin  ---> #def checkSign():
# instruction button(help)  --> #def userHelp():
def userHelp():
    messagebox.showinfo('what this program does', 'this program blabla')



def Login():

    loginroot = Tk()
    loginroot.title('Login System')

# Username interface
    username_1 = Label(loginroot, text='Username       :')
    username_1.grid(row=1, sticky=W)
    signwarn = Label(loginroot, text="Doesn't have username?")
    signwarn.grid(row=2, sticky=W)

# Username input
    usernameInput = Entry(loginroot)
    usernameInput.grid(row=1, column=1)

# Entry of login
    usernameEntry = Entry(loginroot)
    usernameEntry.grid(row=1, column=1)

#Button(Login , Sign in and help)

    LoginButton = Button(loginroot, text='Login', padx=10,
        command = lambda:verifyLogin(usernameEntry))
    LoginButton.grid(row=3,columnspan=4,sticky=E)

    SigninButton = Button(loginroot, text='Sign in', padx=10,
        command = lambda:creatUser(usernameEntry))
    SigninButton.grid(row=3,columnspan=3,sticky=W)

    HelpButton = Button(loginroot, text='Help?', padx=10,
        command = lambda:userHelp())
    HelpButton.grid(row=4,sticky=W)

    loginroot.mainloop()

Login()
