import pandas as pd
df = pd.read_csv('database.csv')
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from PIL import Image
from tkinter import *
from tkinter import messagebox

def data(thing, user, root):
    root.destroy()

    menu = {'Khao Phad Mhoo':['rice','pork','egg','soy sauce','oyster sauce'],
            'Khao Phad Ghai':['rice','chicken','egg','soy sauce','oyster sauce'],
            'Mhoo Thord Kratiem':['pork','garlic'],
            'Ghai Thord Kratiem':['chicken','garlic'],
            'Mhoo Phad Kra Phrao':['pork','basil','chilli','garlic','oyster sauce'],
            'Ghai Phad Kra Phrao':['chicken','basil','chilli','garlic','oyster sauce'],
            'Mama Phad Mhoo':['mama','pork','egg'],
            'Mama Phad Ghai':['mama','chicken','egg'],
            'Mhoo Thord Nam Plar':['pork','fish sauce'],
            'Ghai Thord Nam Plar':['chicken','fish sauce'],
            'Panaeng Mhoo':['pork','panaeng curry','coconut milk','chilli'],
            'Panaeng Ghai':['chicken','panaeng curry','coconut milk','chilli'],
            'Fak Tong Phad Khai':['pumpkin','egg','garlic'],
            'Khai Palo':['egg','tofu','palo','garlic'],
            'Khai Jiew Mhoo Sahb':['egg','pork','soy sauce'],
            'Mhoo Phad Nammun Hoy':['pork','oyster sauce','garlic'],
            'Mhoo Phad Phonk Kraree':['pork','curry powder','onion','milk','egg'],
            'Phad Prick Gaenk Mhoo':['pork','curry'],
            'Phad Phonk Kraree Thale':['squid','shrimp','onion','milk','egg','curry powder'],
            'Khaw Thom Mhoo':['pork','rice'],
            'Khaw Thom Koong':['shrimp','rice'],
            'Masman Ghai':['chicken','onion','coconut milk','potato','masman curry'],
            'Mhoo Manaw':['pork','garlic','chilli','fish sauce','lime'],
            'Tom Yam Koong Nam Khon':['mushroom','milk','shrimp','chili paste','chilli','lime','tomato'],
            'Suki Mhoo':['garlic','egg','pork','suki sauce'],
            'Larb Mhoo':['pork','shallot','coriander','chilli','lime'],
            'Larb Ghai':['chicken','shallot','coriander','chilli','lime'],
            'Tom Jued Mhoo Sub':['pork','tofu','soup cube'],
            'Hed Phud Nammun Hoy':['mushroom','oyster sauce','soy sauce'],
            'Khaw Thom Plar':['fish','rice'],
            'Khana Mhoo':['pork','kale','soy sauce','oyster sauce'],
            'Mhoo Phad Prick Phao':['pork','chili paste'],
            'Ghai Phad Prick Phao':['chicken','chili paste'],
            'Makuer Phad Khai':['egg','tomato'],
            'Gaenk Som Mhoo':['pork','curry','chilli','shrimp paste'],
            'Ghai Thom Nam plar':['chicken','fish sauce','soy sauce']
            }
    lst = []
    for m in menu:
        num_count = 0
        for i in thing:
            if i in menu[m]:
                num_count += 1
        lst.append((len(menu[m])-num_count, m))
    lst.sort()
    output(lst, user)

def output(out, user):
    lst0 = []
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst10 = []
    for i in out:
        if i[0] == 0:
            lst0.append([getValue(user, i[1]), i[1]])
            lst0.sort(reverse=True)
        elif i[0] == 1:
            lst1.append([getValue(user, i[1]), i[1]])
            lst1.sort(reverse=True)
        elif i[0] == 2:
            lst2.append([getValue(user, i[1]), i[1]])
            lst2.sort(reverse=True)
        elif i[0] == 3:
            lst3.append([getValue(user, i[1]), i[1]])
            lst3.sort(reverse=True)
        elif i[0] == 4:
            lst4.append([getValue(user, i[1]), i[1]])
            lst4.sort(reverse=True)
        elif i[0] == 5:
            lst5.append([getValue(user, i[1]), i[1]])
            lst5.sort(reverse=True)
        elif i[0] == 6:
            lst6.append([getValue(user, i[1]), i[1]])
            lst6.sort(reverse=True)
        elif i[0] == 7:
            lst7.append([getValue(user, i[1]), i[1]])
            lst7.sort(reverse=True)
        elif i[0] == 8:
            lst8.append([getValue(user, i[1]), i[1]])
            lst8.sort(reverse=True)
        elif i[0] == 9:
            lst9.append([getValue(user, i[1]), i[1]])
            lst9.sort(reverse=True)
        elif i[0] == 10:
            lst10.append([getValue(user, i[1]), i[1]])
            lst10.sort(reverse=True)
    lst_show=[]
    num = 0
    ans = lst0 + lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8 + lst9 + lst10
    while num != 10:
        num += 1
        lst_show.append(ans[num-1][1])

    root = Tk()
    for i in range(0, 10):
        num = Label(root,text=str(i+1)+': '+lst_show[i])
        num.pack()
    number = Entry(root,state='normal')
    number.pack()
    ok = Button(root,text='OK',command=lambda:checknum(number))
    ok.pack()
    num = 0
    count = 1
    while count != 11:
        count += 1
        num += 1
        if num == number:
            save2(ans[num-1][1], user)
            link(ans[num-1][1])
            showans((ans[num-1][1]).root)
    root.mainloop()
def checknum(number):
    if not(number.get().isdigit() and 1 <= int(number.get()) <= 10):
        messagebox.showerror('Error','Invalid Number')
        number.delete(0, 'end')
    else:
        number = int(number.get())
        messagebox.showerror('Correct','Successfully')

def showans(ans,root):
    root.destroy()
    master=Tk()
    show = Label(master,text='FUNNY')
    master.mainloop()

def link(output):
    if output == 'Khao Phad Mhoo':
        img = Image.open("ข้าวผัดหมู.jpg")
        img.show()
        return
    elif output == 'Khao Phad Ghai':
        img = Image.open("ข้าวผัดไก่.jpg")
        img.show()
        return
    elif output == 'Mhoo Thord Kratiem':
        img = Image.open("หมูทอดกระเทียม.jpg")
        img.show()
        return
    elif output == 'Ghai Thord Kratiem':
        img = Image.open("ไก่ทอดกระเทียม.jpg")
        img.show()
        return
    elif output == 'Mhoo Phad Kra Phrao':
        img = Image.open("หมูผัดกระเพรา.jpg")
        img.show()
        return
    elif output == 'Ghai Phad Kra Phrao':
        img = Image.open("ไก่ผัดกระเพรา.jpg")
        img.show()
        return
    elif output == 'Mama Phad Mhoo':
        img = Image.open("มาม่าผัดหมู.jpg")
        img.show()
        return
    elif output == 'Mama Phad Ghai':
        img = Image.open("มาม่าผัดไก่.jpg")
        img.show()
        return
    elif output == 'Mhoo Thord Nam Plar':
        img = Image.open("หมูทอดน้ำปลา.jpg")
        img.show()
        return
    elif output == 'Ghai Thord Nam Plar':
        img = Image.open("ปีกไก่ทอดน้ำปลา.jpg")
        img.show()
        return
    elif output == 'Panaeng Mhoo':
        img = Image.open("พะแนงหมู.jpg")
        img.show()
        return
    elif output == 'Panaeng Ghai':
        img = Image.open("พะแนงไก่.jpg")
        img.show()
        return
    elif output == 'Fak Tong Phad Khai':
        img = Image.open("ฟักทองผัดไข่.jpg")
        img.show()
        return
    elif output == 'Khai Palo':
        img = Image.open("ไข่พะโล้.jpg")
        img.show()
        return
    elif output == 'Khai Jiew Mhoo Sahb':
        img = Image.open("ไข่เจียวหมูสับ.jpg")
        img.show()
        return
    elif output == 'Mhoo Phad Nammun Hoy':
        img = Image.open("หมูผัดน้ำมันหอย.jpg")
        img.show()
        return
    elif output == 'Mhoo Phad Phonk Kraree':
        img = Image.open("หมูผัดผงกระหรี่.jpg")
        img.show()
        return
    elif output == 'Phad Prick Gaenk Mhoo':
        img = Image.open("ผัดพริกแกงหมู.jpg")
        img.show()
        return
    elif output == 'Phad Phonk Kraree Thale':
        img = Image.open("ผัดผงกระหี่ทะเล.jpg")
        img.show()
        return
    elif output == 'Khaw Thom Mhoo':
        img = Image.open("ข้าวต้มหมู.jpg")
        img.show()
        return
    elif output == 'Khaw Thom Koong':
        img = Image.open("ข้าวต้มกุ้ง.jpg")
        img.show()
        return
    elif output == 'Masman Ghai':
        img = Image.open("มัสมั่ยไก่.jpg")
        img.show()
        return
    elif output == 'Mhoo Manaw':
        img = Image.open("หมูมะนาว.jpg")
        img.show()
        return
    elif output == 'Tom Yam Koong Nam Khon':
        img = Image.open("ต้มยำกุ้งน้ำข้น.jpg")
        img.show()
        return
    elif output == 'Suki Mhoo':
        img = Image.open("สุกี้หมูjpg")
        img.show()
        return
    elif output == 'Larb Mhoo':
        img = Image.open("ลาบหมู.jpg")
        img.show()
        return
    elif output == 'Larb Ghai':
        img = Image.open("ลาบไก่.jpg")
        img.show()
        return
    elif output == 'Tom Jued Mhoo Sub':
        img = Image.open("ต้มจืดหมูสับ.jpg")
        img.show()
        return
    elif output == 'Hed Phud Nammun Hoy':
        img = Image.open("เห็ดผัดน้ำมันหอย.jpg")
        img.show()
        return
    elif output == 'Khaw Thom Plar':
        img = Image.open("ข้าวต้มปลา.jpg")
        img.show()
        return
    elif output == 'Khana Mhoo':
        img = Image.open("คะน้าหมู.jpg")
        img.show()
        return
    elif output == 'Mhoo Phad Prick Phao':
        img = Image.open("หมูผัดพริกเผา.jpg")
        img.show()
        return
    elif output == 'Ghai Phad Prick Phao':
        img = Image.open("ไก่ผัดพริกเผา.jpg")
        img.show()
        return
    elif output == 'Makuer Phad Khai':
        img = Image.open("มะเขือเทศผัดไข่.jpg")
        img.show()
        return
    elif output == 'Gaenk Som Mhoo':
        img = Image.open("แกงส้มหมู.jpg")
        img.show()
        return
    elif output == 'Ghai Thom Nam plar':
        img = Image.open("ไก่ต้มน้ำปลา.jpg")
        img.show()
        return

def getValue(user, menu):
    df = load()
    return df[df['id'] == user][menu].values[0]

def save(df):
    df.to_csv('database.csv')

def save2(menu, user):
    df = load()
    if np.isnan(df.ix[df.id[df.id == user].index[0], menu]):
        df.ix[df.id[df.id == user].index[0], menu] = 0
    df.ix[df.id[df.id == user].index[0], menu] += 1
    save(df)

def load():
    return pd.read_csv('database.csv',index_col=0)

def username(name):
    df = load()
    if name in df.id.values:
        print('Have user')

    else:
        df = df.append(pd.DataFrame({'id': [name]}),  ignore_index=True)
        print('Add complete')

    save(df)

def main(user):
    root = Tk()
    thing = []
    username(user)
# meat
    var_pork=IntVar()
    var_chicken=IntVar()
    var_squid=IntVar()
    var_shrimp=IntVar()
    var_fish=IntVar()
#vatgetable    
    var_garlic=IntVar()
    var_basil=IntVar()
    var_chilli=IntVar()
    var_pumpkin=IntVar()
    var_onion=IntVar()
    var_lime=IntVar()
    var_potato=IntVar()
    var_mushroom=IntVar()
    var_tomato=IntVar()
    var_coriander=IntVar()
    var_shallot=IntVar()
    var_kale=IntVar()
#lhak
    var_rice=IntVar()
    var_mama=IntVar()
    var_tofu=IntVar()
    var_egg=IntVar()
    var_milk=IntVar()
#other
    var_soysauce=IntVar()
    var_oystersauce=IntVar()
    var_fishsauce=IntVar()
    var_panaengcurry=IntVar()
    var_coconutmilk=IntVar()
    var_currypowder=IntVar()
    var_palo=IntVar()
    var_soupcube=IntVar()
    var_currypaste=IntVar()
    var_masmancurry=IntVar()
    var_chillipaste=IntVar()
    var_sukisauce=IntVar()
    var_shrimppaste=IntVar()
#row0
    rice = Checkbutton(root, text='ข้าว',variable=var_rice,command=lambda:check(var_rice,'rice',thing))
    rice.grid(row=0,column=0)
    mama = Checkbutton(root, text='มาม่า',variable=var_mama,command=lambda:check(var_mama,'mama',thing))
    mama.grid(row=0,column=1)
    tofu = Checkbutton(root, text='เต้าหู้',variable=var_tofu,command=lambda:check(var_tofu,'tofu',thing))
    tofu.grid(row=0,column=2)
    egg = Checkbutton(root, text='ไข่',variable=var_egg,command=lambda:check(var_egg,'egg',thing))
    egg.grid(row=0,column=3)
    milk = Checkbutton(root, text='นม',variable=var_milk,command=lambda:check(var_milk,'milk',thing))
    milk.grid(row=0,column=4)
#row1
    pork = Checkbutton(root, text='หมู',variable=var_pork,command=lambda:check(var_pork,'pork',thing))
    pork.grid(row=1,column=0)
    chicken = Checkbutton(root, text='ไก่',variable=var_chicken,command=lambda:check(var_chicken,'chicken',thing))
    chicken.grid(row=1,column=1)
    squid = Checkbutton(root, text='หมึก',variable=var_squid,command=lambda:check(var_squid,'squid',thing))
    squid.grid(row=1,column=2)
    shrimp = Checkbutton(root, text='กุ้ง',variable=var_shrimp,command=lambda:check(var_shrimp,'shrimp',thing))
    shrimp.grid(row=1,column=3)
    fish = Checkbutton(root, text='ปลา',variable=var_fish,command=lambda:check(var_fish,'fish',thing))
    fish.grid(row=1,column=4)
#row2
    garlic = Checkbutton(root, text='กระเทียม',variable=var_garlic,command=lambda:check(var_garlic,'garlic',thing))
    garlic.grid(row=2,column=0)
    basil = Checkbutton(root, text='กระเพรา',variable=var_basil,command=lambda:check(var_basil,'basil',thing))
    basil.grid(row=2,column=1)
    chilli = Checkbutton(root, text='พริก',variable=var_chilli,command=lambda:check(var_chilli,'chilli',thing))
    chilli.grid(row=2,column=2)
    pumpkin = Checkbutton(root, text='ฟักทอง',variable=var_pumpkin,command=lambda:check(var_pumpkin,'pumpkin',thing))
    pumpkin.grid(row=2,column=3)
    onion = Checkbutton(root, text='หัวหอม',variable=var_onion,command=lambda:check(var_onion,'onion',thing))
    onion.grid(row=2,column=4)
    lime = Checkbutton(root, text='มะนาว',variable=var_lime,command=lambda:check(var_lime,'lime',thing))
    lime.grid(row=2,column=5)
    potato = Checkbutton(root, text='มันฝรั่ง',variable=var_potato,command=lambda:check(var_potato,'potato',thing))
    potato.grid(row=2,column=6)
    mushroom = Checkbutton(root, text='เห็ด',variable=var_mushroom,command=lambda:check(var_mushroom,'mushroom',thing))
    mushroom.grid(row=2,column=7)
    tomato = Checkbutton(root, text='มะเขือเทศ',variable=var_tomato,command=lambda:check(var_tomato,'tomato',thing))
    tomato.grid(row=2,column=8)
    coriander = Checkbutton(root, text='ผักชี',variable=var_coriander,command=lambda:check(var_coriander,'coriander',thing))
    coriander.grid(row=2,column=9)
    shallot = Checkbutton(root, text='หอมเเดง',variable=var_shallot,command=lambda:check(var_shallot,'shallot',thing))
    shallot.grid(row=2,column=10)
    kale = Checkbutton(root, text='คะน้า',variable=var_kale,command=lambda:check(var_kale,'kale',thing))
    kale.grid(row=2,column=11)
#row3
    soysauce = Checkbutton(root, text='ซอสถั่วเหลือง',variable=var_soysauce,command=lambda:check(var_soysauce,'soysauce',thing))
    soysauce.grid(row=3,column=0)
    oystersauce = Checkbutton(root, text='ซอสหอยนางรม',variable=var_oystersauce,command=lambda:check(var_oystersauce,'oystersauce',thing))
    oystersauce.grid(row=3,column=1)
    fishsauce = Checkbutton(root, text='น้ำปลา',variable=var_fishsauce,command=lambda:check(var_fishsauce,'fishsauce',thing))
    fishsauce.grid(row=3,column=2)
    panaengcurry = Checkbutton(root, text='ผงเเกงพะเเนง',variable=var_panaengcurry,command=lambda:check(var_panaengcurry,'panaengcurry',thing))
    panaengcurry.grid(row=3,column=3)
    coconutmilk = Checkbutton(root, text='กะทิ',variable=var_coconutmilk,command=lambda:check(var_coconutmilk,'coconutmilk',thing))
    coconutmilk.grid(row=3,column=4)
    currypowder = Checkbutton(root, text='ผใกะหรี่',variable=var_currypowder,command=lambda:check(var_currypowder,'currypowder',thing))
    currypowder.grid(row=3,column=5)
    palo = Checkbutton(root, text='พะโล้',variable=var_palo,command=lambda:check(var_palo,'palo',thing))
    palo.grid(row=3,column=6)
    soupcube = Checkbutton(root, text='ซุปก้อน',variable=var_soupcube,command=lambda:check(var_soupcube,'soupcube',thing))
    soupcube.grid(row=3,column=7)
    currypaste = Checkbutton(root, text='พริกเเกง',variable=var_currypaste,command=lambda:check(var_currypaste,'currypaste',thing))
    currypaste.grid(row=3,column=8)
    masmancurry = Checkbutton(root, text='เเกงมัสมั่น',variable=var_masmancurry,command=lambda:check(var_masmancurry,'masmancurry',thing))
    masmancurry.grid(row=3,column=9)
    chillipaste = Checkbutton(root, text='พริกเผา',variable=var_chillipaste,command=lambda:check(var_chillipaste,'chillipaste',thing))
    chillipaste.grid(row=3,column=10)
    sukisauce = Checkbutton(root, text='น้ำจิ้มสุกี้',variable=var_sukisauce,command=lambda:check(var_sukisauce,'sukisauce',thing))
    sukisauce.grid(row=3,column=11)
    shrimppaste = Checkbutton(root, text='กะปิ',variable=var_shrimppaste,command=lambda:check(var_shrimppaste,'shrimppaste',thing))
    shrimppaste.grid(row=3,column=12)

    ok = Button(root, text='OK',command=lambda:data(thing, user,root))
    ok.grid(row=4)
    root.mainloop()

def check(var,text,thing):
    print(var)
    if var.get():
        thing.append(text)
    else:
        if text in thing:
            thing.remove(text)
    print(thing)

def readFile(fname):
    try:
        infile = open(fname, 'r')
        lines = infile.read().splitlines()
        infile.close()
        return(lines)
    except Exception as e:
        print(e)
        return([])

def readWrite(fname):
    try:
        infile = open(fname, 'w')
        lines = infile.read()
        infile.close()
        return(lines)
    except Exception as e:
        print(e)
        return()

# write text in file
def WriteUs(nameEntry, passEntry,signroot):
    nameList = readFile('Username.txt')
    passList = readFile('Password.txt')

    #already have username
    namesame = nameEntry.get()
    if namesame in nameList:
        #say you already have username
        messagebox.showerror('Error', 'You already have this username')
        return
    else:
        namefile = open('Username.txt','a')
        namefile.writelines('\n'+namesame)
        namefile.close
    #already have password
    passsame = passEntry.get()
    if passsame in passList:
        #say you already have password
        messagebox.showerror('Error', 'You already have this password')
        return
    else:
        passfile = open('Password.txt','a')
        passfile.writelines('\n'+passsame)
        passfile.close
    messagebox.showinfo('Complete signup', 'you finally got new username')
    signroot.destroy()



#but im gonna use the first method to easy guide

def verifyLogin(usernameEntry, passwordEntry,loginroot):
    valid_username = False
    valid_password = False
    usernameList = readFile('Username.txt')
    passwordList = readFile('Password.txt')
    check_user = 0
    check_pass = 0
    #try fucking tryyyyy
    try:
        username1 = usernameEntry.get()
        # print(username)
        if username1 in usernameList:
            for i in range(len(usernameList)):
                check_user += 1
                if usernameList[i] == username1:
                    break
            valid_username = True
        else:
            valid_username = False
        
        passwordcheck = passwordEntry.get()
        if passwordcheck in passwordList:
            for i in range(len(passwordList)):
                check_pass += 1
                if passwordList[i] == passwordcheck:
                    break
            valid_password = True
        else:
            valid_password = False
    except:
        print('Error loading username and password')
        tkinter.messagebox.showerror('Error',
            'Error loading username and password')

    if valid_username and valid_password:
        if check_user == check_pass: #check if password and username are match
            messagebox.showinfo('Welcome', 'Login Successfully')
            #username out
            loginroot.destroy()
            main(username1)
        else:
            messagebox.showerror('Error', 'Invalid password')
    else:
        messagebox.showerror('Error', 'Invalid username or password')

def CreateUser():   #<---  create username and password

    signroot = Tk()
    signroot.title('Signup')
    textsay = Label(signroot, text='Create your username and password',
        fg = 'red',
        font = 'Verdana 8')
    textsay.grid(row=2,columnspan=2)

    nameins = Label(signroot, text='new username        : ')
    nameins.grid(row=3, sticky=W)
    passins = Label(signroot, text='new password         : ')
    passins.grid(row=4, sticky=W)

    nameEntry = Entry(signroot)
    nameEntry.grid(row=3,column=1)
    passEntry = Entry(signroot, show='*')
    passEntry.grid(row=4,column=1)

    signButton = Button(signroot, text='signup',
        command=lambda:WriteUs(nameEntry, passEntry,signroot))
    signButton.grid(row=5,column=1,sticky=E)


    var=IntVar()

    ShowPass = Checkbutton(signroot, text='Show password',
        variable=var,
        command=lambda:displayPassword(passEntry, var))
    ShowPass.grid(row=5,column=0, sticky=W)

    signroot.mainloop()

    #--># after click creat username must check first
    #--># if there's already have a username 
    #--># got a error message


#"""use messagebox"""
# check signin  ---> #def checkSign():
# instruction button(help)  --> #def userHelp():
def userHelp():
    messagebox.showinfo('what this program does', 'this program blabla')

#password display
def displayPassword(passwordEntry, var):
    if var.get():
        passwordEntry.config(show='')
    else:
        passwordEntry.config(show='*')

def Login():

    loginroot = Tk()
    loginroot.title('Login System')

    Login_1 = Label(loginroot, text='Login',
        fg = 'dark green',
        font = 'Helvetica 16 bold')
    Login_1.grid(row=1, columnspan=2)

# Username interface
    username_1 = Label(loginroot, text='Username       :')
    username_1.grid(row=2, sticky=W)
    password_1 = Label(loginroot, text='Password        :')
    password_1.grid(row=3,sticky=W)
    signwarn = Label(loginroot, text="Doesn't have username?")
    signwarn.grid(row=5, sticky=W)

# Username input
    usernameInput = Entry(loginroot)
    usernameInput.grid(row=2, column=2)

    passwordInput = Entry(loginroot, show='*')
    passwordInput.grid(row=3, column=2)
# Entry of login
    usernameEntry = Entry(loginroot)
    usernameEntry.grid(row=2, column=2)

    passwordEntry = Entry(loginroot, show='*')
    passwordEntry.grid(row=3, column=2)

#Button(Login , Sign in and help)

    LoginButton = Button(loginroot, text='Login', padx=10, pady=10,
        command = lambda:verifyLogin(usernameEntry, passwordEntry,loginroot))
    LoginButton.grid(row=6,columnspan=4,sticky=E)

    var=IntVar()

#password show or close
    ShowPass = Checkbutton(loginroot, text='Show password',
        variable=var,
        command=lambda:displayPassword(passwordEntry, var))
    ShowPass.grid(row=4,column=0,columnspan=2)

#signup button
    SigninButton = Button(loginroot, text='Signup', padx=10,pady=10,
        command = lambda:CreateUser())
    SigninButton.grid(row=6,columnspan=3,sticky=W)

    HelpButton = Button(loginroot, text='Help?', padx=10,
        command = lambda:userHelp())
    HelpButton.grid(row=4,column=2,sticky=E)

    loginroot.mainloop()

Login()
