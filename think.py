import pandas as pd
df = pd.read_csv('database.csv')
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from PIL import Image
from tkinter import *
from tkinter import messagebox
import math

def data(thing, user, root):
    root.destroy()

    menu = {'Khao Phad Mhoo':['rice','pork','egg','soy sauce'],
            'Khao Phad Ghai':['rice','chicken','egg','soy sauce'],
            'Mhoo Thord Kratiem':['pork','garlic','oyster sauce','soy sauce'],
            'Ghai Thord Kratiem':['chicken','garlic','oyster sauce','soy sauce'],
            'Mhoo Phad Kra Phrao':['pork','basil','chilli','garlic','oyster sauce'],
            'Ghai Phad Kra Phrao':['chicken','basil','chilli','garlic','oyster sauce'],
            'Mama Phad Mhoo':['mama','pork','egg'],
            'Mama Phad Ghai':['mama','chicken','egg'],
            'Mhoo Thord Nam Plar':['pork','fish sauce','soy sauce','oyster sauce'],
            'Ghai Thord Nam Plar':['chicken','fish sauce','soy sauce','oyster sauce'],
            'Panaeng Mhoo':['pork','panaeng curry','coconut milk','chilli'],
            'Panaeng Ghai':['chicken','panaeng curry','coconut milk','chilli'],
            'Fak Tong Phad Khai':['pumpkin','egg','garlic','coriander'],
            'Khai Palo':['egg','tofu','palo','garlic'],
            'Khai Jiew Mhoo Sahb':['egg','pork','soy sauce'],
            'Mhoo Phad Nammun Hoy':['pork','oyster sauce','garlic'],
            'Mhoo Phad Phonk Kraree':['pork','curry powder','onion','milk','egg'],
            'Phad Prick Gaenk Mhoo':['pork','curry paste','garlic'],
            'Phad Phonk Kraree Thale':['squid','shrimp','onion','milk','egg','curry powder'],
            'Khaw Thom Mhoo':['pork','rice','soy sauce'],
            'Khaw Thom Koong':['shrimp','rice','soy sauce'],
            'Masman Ghai':['chicken','onion','coconut milk','potato','masman curry'],
            'Mhoo Manaw':['pork','garlic','chilli','fish sauce','lime'],
            'Tom Yam Koong Nam Khon':['mushroom','milk','shrimp','chilli','lime','tomato'],
            'Suki Mhoo':['garlic','egg','pork','suki sauce'],
            'Larb Mhoo':['pork','shallot','coriander','chilli','lime'],
            'Larb Ghai':['chicken','shallot','coriander','chilli','lime'],
            'Tom Jued Mhoo Sub':['pork','tofu','soup cube','garlic'],
            'Hed Phud Nammun Hoy':['mushroom','oyster sauce','soy sauce'],
            'Khaw Thom Plar':['fish','rice','garlic','soy sauce'],
            'Khana Mhoo':['pork','kale','soy sauce','oyster sauce'],
            'Mhoo Phad Prick Phao':['pork','chilli paste','garlic','fish sauce'],
            'Ghai Phad Prick Phao':['chicken','chilli paste','garlic','fish sauce'],
            'Makuer Phad Khai':['egg','tomato','garlic','onion'],
            'Gaenk Som Mhoo':['pork','curry paste','chilli','shrimp paste'],
            'Ghai Thom Nam plar':['chicken','fish sauce','soy sauce','coriander']
            }
    lst = []
    for m in menu:
        num_count = 0
        for i in thing:
            if i in menu[m]:
                num_count += 1
        if len(menu[m])==(len(menu[m])-num_count):
            num_count = -3

        lst.append((len(menu[m])-num_count, m))
    lst.sort()
    output(lst, user)

def getValue(user, menu):
    df = load()
    return df[df['id'] == user][menu].values[0]

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
            lst0 = sorted(lst0, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 1:
            lst1.append([getValue(user, i[1]), i[1]])
            lst1 = sorted(lst1, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 2:
            lst2.append([getValue(user, i[1]), i[1]])
            lst2 = sorted(lst2, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 3:
            lst3.append([getValue(user, i[1]), i[1]])
            lst3 = sorted(lst3, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 4:
            lst4.append([getValue(user, i[1]), i[1]])
            lst4 = sorted(lst4, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 5:
            lst5.append([getValue(user, i[1]), i[1]])
            lst5 = sorted(lst5, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 6:
            lst6.append([getValue(user, i[1]), i[1]])
            lst6 = sorted(lst6, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 7:
            lst7.append([getValue(user, i[1]), i[1]])
            lst7 = sorted(lst7, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 8:
            lst8.append([getValue(user, i[1]), i[1]])
            lst8 = sorted(lst8, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 9:
            lst9.append([getValue(user, i[1]), i[1]])
            lst9 = sorted(lst9, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
        elif i[0] == 10:
            lst10.append([getValue(user, i[1]), i[1]])
            lst10 = sorted(lst10, reverse=True, key=lambda x: -1000 if math.isnan(x[0]) else x[0])
    lst_show=[]
    ans = lst0 + lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8 + lst9 + lst10

    num = 0
    while num != 10:
        num += 1
        lst_show.append(ans[num-1][1])

    root = Tk()
    root.title('เเนะนำเมนู10อันดับ')
    root.resizable(width=False,height=False)
    # root.geometry('{}x{}'.format(700,400))
    name=Label(root,text='กรุณาเลือกเมนู',font = ('Helvetica 16 bold',30),fg='blue')
    name.grid(row=0,columnspan=4)
    for i in range(0, 5):
        num = Label(root,font = ('Helvetica 16 bold',20),text=str(i+1)+': '+showname(lst_show[i]))
        num.grid(row=i+1,column=0,sticky=W)
    for j in range(0,5):
        showpic(lst_show[j],root,j)
    for k in range(0, 5):
        num = Label(root,font = ('Helvetica 16 bold',20),text=str(k+6)+': '+showname(lst_show[k+5]))
        num.grid(row=k+1,column=2,sticky=W)
    for l in range(0,5):
        showpic2(lst_show[l+5],root,l)
    number = Entry(root,state='normal')
    number.grid(row=6,column=0,columnspan=2,sticky=E)
    ok = Button(root,text='ตกลง',font=15,bg='sky blue',padx=5,pady=5,command=lambda:checknum(number,ans,user,root))
    ok.grid(row=6,column=2,sticky=W)

    root.mainloop()

def checknum(number,ans,user,root):
    if not(number.get().isdigit() and 1 <= int(number.get()) <= 10):
        messagebox.showerror('Error','Invalid Number')
        number.delete(0, 'end')
    else:
        number = int(number.get())
        messagebox.showinfo('Correct','Successfully')
        num = 0
        count = 1
        while count != 11:
            count += 1
            num += 1
            if num == number:
                save2((ans[num-1][1]), user)
                showans((ans[num-1][1]),root,user)

def showans(ans,root,user):
    root.destroy()
    master=Tk()
    master.title('Do It')
    master.resizable(width=False,height=False)
    showpic3(ans,master)
    login = Button(master, text='Logout', command=lambda:again(master),font=15)
    login.grid(row=2,column=1)
    master.mainloop()


def showpic(text,root,j):
    if text == 'Khao Phad Mhoo':
        pic = PhotoImage(file='image(gif)/Khao Phad Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khao Phad Ghai':
        pic = PhotoImage(file='image(gif)/Khao Phad Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Thord Kratiem':
        pic = PhotoImage(file='image(gif)/Mhoo Thord Kratiem.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Ghai Thord Kratiem':
        pic = PhotoImage(file='image(gif)/Ghai Thord Kratiem.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Kra Phrao':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Kra Phrao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Ghai Phad Kra Phrao':
        pic = PhotoImage(file='image(gif)/Ghai Phad Kra Phrao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mama Phad Mhoo':
        pic = PhotoImage(file='image(gif)/Mama Phad Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mama Phad Ghai':
        pic = PhotoImage(file='image(gif)/Mama Phad Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Thord Nam Plar':
        pic = PhotoImage(file='image(gif)/Mhoo Thord Nam Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Ghai Thord Nam Plar':
        pic = PhotoImage(file='image(gif)/Ghai Thord Nam Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Panaeng Mhoo':
        pic = PhotoImage(file='image(gif)/Panaeng Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Panaeng Ghai':
        pic = PhotoImage(file='image(gif)/Panaeng Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Fak Tong Phad Khai':
        pic = PhotoImage(file='image(gif)/Fak Tong Phad Khai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khai Palo':
        pic = PhotoImage(file='image(gif)/Khai Palo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khai Jiew Mhoo Sahb':
        pic = PhotoImage(file='image(gif)/Khai Jiew Mhoo Sahb.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Nammun Hoy':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Nammun Hoy.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Phonk Kraree':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Phonk Kraree.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Phad Prick Gaenk Mhoo':
        pic = PhotoImage(file='image(gif)/Phad Prick Gaenk Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Phad Phonk Kraree Thale':
        pic = PhotoImage(file='image(gif)/Phad Phonk Kraree Thale.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khaw Thom Mhoo':
        pic = PhotoImage(file='image(gif)/Khaw Thom Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khaw Thom Koong':
        pic = PhotoImage(file='image(gif)/Khaw Thom Koong.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Masman Ghai':
        pic = PhotoImage(file='image(gif)/Masman Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Manaw':
        pic = PhotoImage(file='image(gif)/Mhoo Manaw.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Tom Yam Koong Nam Khon':
        pic = PhotoImage(file='image(gif)/Tom Yam Koong Nam Khon.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Suki Mhoo':
        pic = PhotoImage(file='image(gif)/Suki Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Larb Mhoo':
        pic = PhotoImage(file='image(gif)/Larb Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Larb Ghai':
        pic = PhotoImage(file='image(gif)/Larb Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Tom Jued Mhoo Sub':
        pic = PhotoImage(file='image(gif)/Tom Jued Mhoo Sub.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Hed Phud Nammun Hoy':
        pic = PhotoImage(file='image(gif)/Hed Phud Nammun Hoy.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khaw Thom Plar':
        pic = PhotoImage(file='image(gif)/Khaw Thom Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Khana Mhoo':
        pic = PhotoImage(file='image(gif)/Khana Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Prick Phao':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Prick Phao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Ghai Phad Prick Phao':
        pic = PhotoImage(file='image(gif)/Ghai Phad Prick Phao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Makuer Phad Khai':
        pic = PhotoImage(file='image(gif)/Makuer Phad Khai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Gaenk Som Mhoo':
        pic = PhotoImage(file='image(gif)/Gaenk Som Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return
    elif text == 'Ghai Thom Nam plar':
        pic = PhotoImage(file='image(gif)/Ghai Thom Nam plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=1,sticky=W)
        return

def showpic2(text,root,j):
    if text == 'Khao Phad Mhoo':
        pic = PhotoImage(file='image(gif)/Khao Phad Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khao Phad Ghai':
        pic = PhotoImage(file='image(gif)/Khao Phad Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Thord Kratiem':
        pic = PhotoImage(file='image(gif)/Mhoo Thord Kratiem.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Ghai Thord Kratiem':
        pic = PhotoImage(file='image(gif)/Ghai Thord Kratiem.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Phad Kra Phrao':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Kra Phrao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Ghai Phad Kra Phrao':
        pic = PhotoImage(file='image(gif)/Ghai Phad Kra Phrao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mama Phad Mhoo':
        pic = PhotoImage(file='image(gif)/Mama Phad Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mama Phad Ghai':
        pic = PhotoImage(file='image(gif)/Mama Phad Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Thord Nam Plar':
        pic = PhotoImage(file='image(gif)/Mhoo Thord Nam Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Ghai Thord Nam Plar':
        pic = PhotoImage(file='image(gif)/Ghai Thord Nam Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Panaeng Mhoo':
        pic = PhotoImage(file='image(gif)/Panaeng Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Panaeng Ghai':
        pic = PhotoImage(file='image(gif)/Panaeng Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Fak Tong Phad Khai':
        pic = PhotoImage(file='image(gif)/Fak Tong Phad Khai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khai Palo':
        pic = PhotoImage(file='image(gif)/Khai Palo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khai Jiew Mhoo Sahb':
        pic = PhotoImage(file='image(gif)/Khai Jiew Mhoo Sahb.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Phad Nammun Hoy':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Nammun Hoy.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Phad Phonk Kraree':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Phonk Kraree.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Phad Prick Gaenk Mhoo':
        pic = PhotoImage(file='image(gif)/Phad Prick Gaenk Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Phad Phonk Kraree Thale':
        pic = PhotoImage(file='image(gif)/Phad Phonk Kraree Thale.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khaw Thom Mhoo':
        pic = PhotoImage(file='image(gif)/Khaw Thom Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khaw Thom Koong':
        pic = PhotoImage(file='image(gif)/Khaw Thom Koong.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Masman Ghai':
        pic = PhotoImage(file='image(gif)/Masman Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Manaw':
        pic = PhotoImage(file='image(gif)/Mhoo Manaw.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Tom Yam Koong Nam Khon':
        pic = PhotoImage(file='image(gif)/Tom Yam Koong Nam Khon.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Suki Mhoo':
        pic = PhotoImage(file='image(gif)/Suki Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Larb Mhoo':
        pic = PhotoImage(file='image(gif)/Larb Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Larb Ghai':
        pic = PhotoImage(file='image(gif)/Larb Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Tom Jued Mhoo Sub':
        pic = PhotoImage(file='image(gif)/Tom Jued Mhoo Sub.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Hed Phud Nammun Hoy':
        pic = PhotoImage(file='image(gif)/Hed Phud Nammun Hoy.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khaw Thom Plar':
        pic = PhotoImage(file='image(gif)/Khaw Thom Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Khana Mhoo':
        pic = PhotoImage(file='image(gif)/Khana Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Mhoo Phad Prick Phao':
        pic = PhotoImage(file='image(gif)/Mhoo Phad Prick Phao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Ghai Phad Prick Phao':
        pic = PhotoImage(file='image(gif)/Ghai Phad Prick Phao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Makuer Phad Khai':
        pic = PhotoImage(file='image(gif)/Makuer Phad Khai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Gaenk Som Mhoo':
        pic = PhotoImage(file='image(gif)/Gaenk Som Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return
    elif text == 'Ghai Thom Nam plar':
        pic = PhotoImage(file='image(gif)/Ghai Thom Nam plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=j+1,column=3,sticky=W)
        return

def showpic3(text,root):
    if text == 'Khao Phad Mhoo':
        pic = PhotoImage(file='last(gif)/Khao Phad Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khao Phad Ghai':
        pic = PhotoImage(file='last(gif)/Khao Phad Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Thord Kratiem':
        pic = PhotoImage(file='last(gif)/Mhoo Thord Kratiem.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Ghai Thord Kratiem':
        pic = PhotoImage(file='last(gif)/Ghai Thord Kratiem.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Kra Phrao':
        pic = PhotoImage(file='last(gif)/Mhoo Phad Kra Phrao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Ghai Phad Kra Phrao':
        pic = PhotoImage(file='last(gif)/Ghai Phad Kra Phrao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mama Phad Mhoo':
        pic = PhotoImage(file='last(gif)/Mama Phad Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mama Phad Ghai':
        pic = PhotoImage(file='last(gif)/Mama Phad Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Thord Nam Plar':
        pic = PhotoImage(file='last(gif)/Mhoo Thord Nam Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Ghai Thord Nam Plar':
        pic = PhotoImage(file='last(gif)/Ghai Thord Nam Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Panaeng Mhoo':
        pic = PhotoImage(file='last(gif)/Panaeng Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Panaeng Ghai':
        pic = PhotoImage(file='last(gif)/Panaeng Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Fak Tong Phad Khai':
        pic = PhotoImage(file='last(gif)/Fak Tong Phad Khai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khai Palo':
        pic = PhotoImage(file='last(gif)/Khai Palo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khai Jiew Mhoo Sahb':
        pic = PhotoImage(file='last(gif)/Khai Jiew Mhoo Sahb.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Nammun Hoy':
        pic = PhotoImage(file='last(gif)/Mhoo Phad Nammun Hoy.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Phonk Kraree':
        pic = PhotoImage(file='last(gif)/Mhoo Phad Phonk Kraree.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Phad Prick Gaenk Mhoo':
        pic = PhotoImage(file='last(gif)/Phad Prick Gaenk Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Phad Phonk Kraree Thale':
        pic = PhotoImage(file='last(gif)/Phad Phonk Kraree Thale.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khaw Thom Mhoo':
        pic = PhotoImage(file='last(gif)/Khaw Thom Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khaw Thom Koong':
        pic = PhotoImage(file='last(gif)/Khaw Thom Koong.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Masman Ghai':
        pic = PhotoImage(file='last(gif)/Masman Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Manaw':
        pic = PhotoImage(file='last(gif)/Mhoo Manaw.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Tom Yam Koong Nam Khon':
        pic = PhotoImage(file='last(gif)/Tom Yam Koong Nam Khon.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Suki Mhoo':
        pic = PhotoImage(file='last(gif)/Suki Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Larb Mhoo':
        pic = PhotoImage(file='last(gif)/Larb Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Larb Ghai':
        pic = PhotoImage(file='last(gif)/Larb Ghai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Tom Jued Mhoo Sub':
        pic = PhotoImage(file='last(gif)/Tom Jued Mhoo Sub.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Hed Phud Nammun Hoy':
        pic = PhotoImage(file='last(gif)/Hed Phud Nammun Hoy.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khaw Thom Plar':
        pic = PhotoImage(file='last(gif)/Khaw Thom Plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Khana Mhoo':
        pic = PhotoImage(file='last(gif)/Khana Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Mhoo Phad Prick Phao':
        pic = PhotoImage(file='last(gif)/Mhoo Phad Prick Phao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Ghai Phad Prick Phao':
        pic = PhotoImage(file='last(gif)/Ghai Phad Prick Phao.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Makuer Phad Khai':
        pic = PhotoImage(file='last(gif)/Makuer Phad Khai.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Gaenk Som Mhoo':
        pic = PhotoImage(file='last(gif)/Gaenk Som Mhoo.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return
    elif text == 'Ghai Thom Nam plar':
        pic = PhotoImage(file='last(gif)/Ghai Thom Nam plar.gif')
        tmpphoto=Label(root, image=pic)
        tmpphoto.photo = pic
        tmpphoto.grid(row=1,column=1,sticky=W)
        return


def showname(output):
    if output == 'Khao Phad Mhoo':
        return("ข้าวผัดหมู")
    elif output == 'Khao Phad Ghai':
        return("ข้าวผัดไก่")    
    elif output == 'Mhoo Thord Kratiem':
        return("หมูทอดกระเทียม")
    elif output == 'Ghai Thord Kratiem':
        return("ไก่ทอดกระเทียม")
    elif output == 'Mhoo Phad Kra Phrao':
        return("หมูผัดกระเพรา")
    elif output == 'Ghai Phad Kra Phrao':
        return("ไก่ผัดกระเพรา")
    elif output == 'Mama Phad Mhoo':
        return("มาม่าผัดหมู")
    elif output == 'Mama Phad Ghai':
        return("มาม่าผัดไก่")
    elif output == 'Mhoo Thord Nam Plar':
        return("หมูทอดน้ำปลา")
    elif output == 'Ghai Thord Nam Plar':
        return("ปีกไก่ทอดน้ำปลา")
    elif output == 'Panaeng Mhoo':
        return("พะแนงหมู")
    elif output == 'Panaeng Ghai':
        return("พะแนงไก่")
    elif output == 'Fak Tong Phad Khai':
        return("ฟักทองผัดไข่")
    elif output == 'Khai Palo':
        return("ไข่พะโล้")
    elif output == 'Khai Jiew Mhoo Sahb':
        return("ไข่เจียวหมูสับ")
    elif output == 'Mhoo Phad Nammun Hoy':
        return("หมูผัดน้ำมันหอย")
    elif output == 'Mhoo Phad Phonk Kraree':
        return("หมูผัดผงกระหรี่")
    elif output == 'Phad Prick Gaenk Mhoo':
        return("ผัดพริกแกงหมู")
    elif output == 'Phad Phonk Kraree Thale':
        return("ผัดผงกระหี่ทะเล")
    elif output == 'Khaw Thom Mhoo':
        return("ข้าวต้มหมู")
    elif output == 'Khaw Thom Koong':
        return("ข้าวต้มกุ้ง")
    elif output == 'Masman Ghai':
        return("มัสมั่นไก่")
    elif output == 'Mhoo Manaw':
        return("หมูมะนาว")
    elif output == 'Tom Yam Koong Nam Khon':
        return("ต้มยำกุ้งน้ำข้น")
    elif output == 'Suki Mhoo':
        return("สุกี้หมู")
    elif output == 'Larb Mhoo':
        return("ลาบหมู")
    elif output == 'Larb Ghai':
        return("ลาบไก่")
    elif output == 'Tom Jued Mhoo Sub':
        return("ต้มจืดหมูสับ")
    elif output == 'Hed Phud Nammun Hoy':
        return("เห็ดผัดน้ำมันหอย")
    elif output == 'Khaw Thom Plar':
        return("ข้าวต้มปลา")
    elif output == 'Khana Mhoo':
        return("คะน้าหมู")
    elif output == 'Mhoo Phad Prick Phao':
        return("หมูผัดพริกเผา")
    elif output == 'Ghai Phad Prick Phao':
        return("ไก่ผัดพริกเผา")
    elif output == 'Makuer Phad Khai':
        return("มะเขือเทศผัดไข่")
    elif output == 'Gaenk Som Mhoo':
        return("แกงส้มหมู")
    elif output == 'Ghai Thom Nam plar':
        return("ไก่ต้มน้ำปลา")

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
        pass
    else:
        df = df.append(pd.DataFrame({'id': [name]}),  ignore_index=True)


    save(df)

def main(user):
    root = Tk()
    root.title('Material')
    root.resizable(width=False,height=False)
    root.geometry('{}x{}'.format(700,400))
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

    name=Label(root,text='กรุณาเลือกวัตถุดิบ',font = ('Helvetica 16 bold',30),fg='blue')
    name.grid(row=0,columnspan=5)
#row0
    rice = Checkbutton(root, text='ข้าว',variable=var_rice,padx=10,pady=5,font=15,command=lambda:check(var_rice,'rice',thing))
    rice.grid(row=1,column=0,sticky=W)
    mama = Checkbutton(root, text='มาม่า',variable=var_mama,padx=10,pady=5,font=15,command=lambda:check(var_mama,'mama',thing))
    mama.grid(row=1,column=1,sticky=W)
    tofu = Checkbutton(root, text='เต้าหู้',variable=var_tofu,padx=10,pady=5,font=15,command=lambda:check(var_tofu,'tofu',thing))
    tofu.grid(row=1,column=2,sticky=W)
    egg = Checkbutton(root, text='ไข่',variable=var_egg,padx=10,pady=5,font=15,command=lambda:check(var_egg,'egg',thing))
    egg.grid(row=1,column=3,sticky=W)
    milk = Checkbutton(root, text='นม',variable=var_milk,padx=10,pady=5,font=15,command=lambda:check(var_milk,'milk',thing))
    milk.grid(row=1,column=4,sticky=W)
#row1
    pork = Checkbutton(root, text='หมู',variable=var_pork,padx=10,pady=5,font=15,command=lambda:check(var_pork,'pork',thing))
    pork.grid(row=2,column=0,sticky=W)
    chicken = Checkbutton(root, text='ไก่',variable=var_chicken,padx=10,pady=5,font=15,command=lambda:check(var_chicken,'chicken',thing))
    chicken.grid(row=2,column=1,sticky=W)
    squid = Checkbutton(root, text='หมึก',variable=var_squid,padx=10,pady=5,font=15,command=lambda:check(var_squid,'squid',thing))
    squid.grid(row=2,column=2,sticky=W)
    shrimp = Checkbutton(root, text='กุ้ง',variable=var_shrimp,padx=10,pady=5,font=15,command=lambda:check(var_shrimp,'shrimp',thing))
    shrimp.grid(row=2,column=3,sticky=W)
    fish = Checkbutton(root, text='ปลา',variable=var_fish,padx=10,pady=5,font=15,command=lambda:check(var_fish,'fish',thing))
    fish.grid(row=2,column=4,sticky=W)
#row2
    garlic = Checkbutton(root, text='กระเทียม',variable=var_garlic,padx=10,pady=5,font=15,command=lambda:check(var_garlic,'garlic',thing))
    garlic.grid(row=3,column=0,sticky=W)
    basil = Checkbutton(root, text='กระเพรา',variable=var_basil,padx=10,pady=5,font=15,command=lambda:check(var_basil,'basil',thing))
    basil.grid(row=3,column=1,sticky=W)
    chilli = Checkbutton(root, text='พริก',variable=var_chilli,padx=10,pady=5,font=15,command=lambda:check(var_chilli,'chilli',thing))
    chilli.grid(row=3,column=2,sticky=W)
    pumpkin = Checkbutton(root, text='ฟักทอง',variable=var_pumpkin,padx=10,pady=5,font=15,command=lambda:check(var_pumpkin,'pumpkin',thing))
    pumpkin.grid(row=3,column=3,sticky=W)
    onion = Checkbutton(root, text='หัวหอม',variable=var_onion,padx=10,pady=5,font=15,command=lambda:check(var_onion,'onion',thing))
    onion.grid(row=3,column=4,sticky=W)
    lime = Checkbutton(root, text='มะนาว',variable=var_lime,padx=10,pady=5,font=15,command=lambda:check(var_lime,'lime',thing))
    lime.grid(row=4,column=0,sticky=W)
    potato = Checkbutton(root, text='มันฝรั่ง',variable=var_potato,padx=10,pady=5,font=15,command=lambda:check(var_potato,'potato',thing))
    potato.grid(row=4,column=1,sticky=W)
    mushroom = Checkbutton(root, text='เห็ด',variable=var_mushroom,padx=10,pady=5,font=15,command=lambda:check(var_mushroom,'mushroom',thing))
    mushroom.grid(row=4,column=2,sticky=W)
    tomato = Checkbutton(root, text='มะเขือเทศ',variable=var_tomato,padx=10,pady=5,font=15,command=lambda:check(var_tomato,'tomato',thing))
    tomato.grid(row=4,column=3,sticky=W)
    coriander = Checkbutton(root, text='ผักชี',variable=var_coriander,padx=10,pady=5,font=15,command=lambda:check(var_coriander,'coriander',thing))
    coriander.grid(row=4,column=4,sticky=W)
    shallot = Checkbutton(root, text='หอมเเดง',variable=var_shallot,padx=10,pady=5,font=15,command=lambda:check(var_shallot,'shallot',thing))
    shallot.grid(row=5,column=0,sticky=W)
    kale = Checkbutton(root, text='คะน้า',variable=var_kale,padx=10,pady=5,font=15,command=lambda:check(var_kale,'kale',thing))
    kale.grid(row=5,column=1,sticky=W)
#row3
    soysauce = Checkbutton(root, text='ซอสถั่วเหลือง',variable=var_soysauce,padx=10,pady=5,font=15,command=lambda:check(var_soysauce,'soy sauce',thing))
    soysauce.grid(row=5,column=2,sticky=W)
    oystersauce = Checkbutton(root, text='ซอสหอยนางรม',variable=var_oystersauce,padx=10,pady=5,font=15,command=lambda:check(var_oystersauce,'oyster sauce',thing))
    oystersauce.grid(row=5,column=3,sticky=W)
    fishsauce = Checkbutton(root, text='น้ำปลา',variable=var_fishsauce,padx=10,pady=5,font=15,command=lambda:check(var_fishsauce,'fish sauce',thing))
    fishsauce.grid(row=5,column=4,sticky=W)
    panaengcurry = Checkbutton(root, text='ผงเเกงพะเเนง',variable=var_panaengcurry,padx=10,pady=5,font=15,command=lambda:check(var_panaengcurry,'panaeng curry',thing))
    panaengcurry.grid(row=6,column=0,sticky=W)
    coconutmilk = Checkbutton(root, text='กะทิ',variable=var_coconutmilk,padx=10,pady=5,font=15,command=lambda:check(var_coconutmilk,'coconut milk',thing))
    coconutmilk.grid(row=6,column=1,sticky=W)
    currypowder = Checkbutton(root, text='ผงกะหรี่',variable=var_currypowder,padx=10,pady=5,font=15,command=lambda:check(var_currypowder,'curry powder',thing))
    currypowder.grid(row=6,column=2,sticky=W)
    palo = Checkbutton(root, text='พะโล้',variable=var_palo,padx=10,pady=5,font=15,command=lambda:check(var_palo,'palo',thing))
    palo.grid(row=6,column=3,sticky=W)
    soupcube = Checkbutton(root, text='ซุปก้อน',variable=var_soupcube,padx=10,pady=5,font=15,command=lambda:check(var_soupcube,'soup cube',thing))
    soupcube.grid(row=6,column=4,sticky=W)
    currypaste = Checkbutton(root, text='พริกเเกง',variable=var_currypaste,padx=10,pady=5,font=15,command=lambda:check(var_currypaste,'curry paste',thing))
    currypaste.grid(row=7,column=0,sticky=W)
    masmancurry = Checkbutton(root, text='เเกงมัสมั่น',variable=var_masmancurry,padx=10,pady=5,font=15,command=lambda:check(var_masmancurry,'masman curry',thing))
    masmancurry.grid(row=7,column=1,sticky=W)
    chillipaste = Checkbutton(root, text='พริกเผา',variable=var_chillipaste,padx=10,pady=5,font=15,command=lambda:check(var_chillipaste,'chilli paste',thing))
    chillipaste.grid(row=7,column=2,sticky=W)
    sukisauce = Checkbutton(root, text='น้ำจิ้มสุกี้',variable=var_sukisauce,padx=10,pady=5,font=15,command=lambda:check(var_sukisauce,'suki sauce',thing))
    sukisauce.grid(row=7,column=3,sticky=W)
    shrimppaste = Checkbutton(root, text='กะปิ',variable=var_shrimppaste,padx=10,pady=5,font=15,command=lambda:check(var_shrimppaste,'shrimp paste',thing))
    shrimppaste.grid(row=7,column=4,sticky=W)

    ok = Button(root, text='ตกลง',font=10,padx=15,pady=5,command=lambda:data(thing, user,root))
    ok.grid(row=8,columnspan=5,sticky=S)
    root.mainloop()

def check(var,text,thing):
    if var.get():
        thing.append(text)
    else:
        if text in thing:
            thing.remove(text)


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
    messagebox.showinfo('Complete signup', 'Create Successfully')
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
    signroot.resizable(width=False,height=False)
    signroot.geometry('{}x{}'.format(600,180))
    signroot.title('Sign Up')
    top = Frame(signroot)
    top.pack()
    mid = Frame(signroot)
    mid.pack()
    bot = Frame(signroot)
    bot.pack()

    textsay = Label(top, text='Create your username and password',
        fg = 'red',
        font = ('Verdana 8',25))
    textsay.grid(row=2,columnspan=2)

    nameins = Label(mid, text='New Username: ',font=30)
    nameins.grid(row=3,column=0,padx=5)
    passins = Label(mid, text='New Password: ',font=30)
    passins.grid(row=4,column=0,padx=5)

    nameEntry = Entry(mid)
    nameEntry.grid(row=3,column=1,sticky=W,padx=15)
    passEntry = Entry(mid, show='*')
    passEntry.grid(row=4,column=1,sticky=W,padx=15)

    signButton = Button(mid, text='Sign Up',padx=10,pady=10,
        command=lambda:WriteUs(nameEntry, passEntry,signroot))
    signButton.grid(row=6,columnspan=2)
    z = Label(mid,text='')
    z.grid(row=5)

    signroot.mainloop()

def userHelp():
    messagebox.showinfo('Help!', 'วิธีการใช้งาน\n1.กรอกบัญชีผู้ใช้งาน(ถ้าหากยังไม่มีบัญชีผู้ใช้ให้ทำการสมัครบัญชีผู้ใช้ก่อน)\n2.เลือกวัตถุดิบที่ผู้ใช้มีอยู่\n3.เลือกเมนูที่ผู้ใช้สนใจจะทำ(กรอกเป็นตัวเลข1-10)')

#password display
def displayPassword(passwordEntry, var):

    if var.get():
        passwordEntry.config(show='')
    else:
        passwordEntry.config(show='*')
def again(master):
    master.destroy()
    Login()

def Login():
    loginroot = Tk()
    top = Frame(loginroot)
    top.pack()
    mid = Frame(loginroot)
    mid.pack()
    bot = Frame(loginroot)
    bot.pack()
    loginroot.resizable(width=False,height=False)
    loginroot.geometry('{}x{}'.format(500,250))
    loginroot.title('จะกินอะไรดี')

    Login_1 = Label(mid, text='จะกินอะไรดี',
        fg = 'green',
        font = ('Helvetica 16 bold',50))
    Login_1.grid(row=1,columnspan=10)

# Username interface
    username_1 = Label(mid, text='Username :',font=30)
    username_1.grid(row=3, sticky=E)
    password_1 = Label(mid, text='Password :',font=30)
    password_1.grid(row=4,sticky=E)

# Entry of login
    usernameEntry = Entry(mid)
    usernameEntry.grid(row=3, column=2)

    passwordEntry = Entry(mid, show='*')
    passwordEntry.grid(row=4, column=2)

#Button(Login , Sign in and help)

    LoginButton = Button(bot, text='Login', padx=10, pady=10,
        command = lambda:verifyLogin(usernameEntry, passwordEntry,loginroot))
    LoginButton.grid(row=7,column=2)

    var=IntVar()

#password show or close
    ShowPass = Checkbutton(bot, text='Show password',font=20,
        variable=var,
        command=lambda:displayPassword(passwordEntry, var))
    ShowPass.grid(row=5,column=0,columnspan=2)

#signup button
    SigninButton = Button(bot, text='Signup', padx=10,pady=10,
        command = lambda:CreateUser())
    SigninButton.grid(row=7,column=1,sticky=W)

    HelpButton = Button(bot, text='Help?', padx=10,pady=10,
        command = lambda:userHelp())
    HelpButton.grid(row=7,column=0,sticky=W)

    loginroot.mainloop()

Login()
