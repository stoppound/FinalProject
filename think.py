import pandas as pd
df = pd.read_csv('database.csv')
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from PIL import Image

def data(thing, user):
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
            'Panaeng Mhoo':['pork','panaeng curry','coconut milk','red chilli'],
            'Panaeng Ghai':['chicken','panaeng curry','coconut milk','red chilli'],
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
            'Mhoo Manaw':['pork','garlic','red chilli','fish sauce','lemon'],
            'Tom Yam Koong Nam Khon':['mushroom','milk','shrimp','chili paste','chilli','lemon','tomato'],
            'Suki Mhoo':['garlic','egg','pork','suki sauce'],
            'Larb Mhoo':['pork','shallot','coriander','chilli','lemon'],
            'Larb Ghai':['chicken','shallot','coriander','chilli','lemon'],
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

    num = 0
    ans = lst0 + lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8 + lst9 + lst10
    print('')
    while num != 10:
        num += 1
        print(num, ans[num-1][1])

    choose = ''
    print('')
    while not(choose.isdigit() and 1 <= int(choose) <= 10):
        choose = input("NUMBER:")
    choose = int(choose)

    num = 0
    count = 1
    print('')
    while count != 11:
        count += 1
        num += 1
        if num == choose:
            print(ans[num-1][1])
            save2(ans[num-1][1], user)
            link(ans[num-1][1])

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
        print('')
    else:
        df = df.append(pd.DataFrame({'id': [name]}),  ignore_index=True)
        print('Add complete')
        print('')
    save(df)


def main():
    point = '*'
    print("Please Login")
    user = input("Username:")
    username(user)
    print('*'*145)
    print("*  pork    chicken    shrimp    fish     egg      milk      coriander   tomato     panaeng curry    curry powder     masman curry               *")
    print("*  kale    mushroom   potato    squid    palo     chilli    garlic      pumpkin    soy sauce        oyster sauce     shrimp paste               *")
    print("*  mama    rice       basil     onion    bean     lemon     shallot     tofu       red chilli       fish sauce       suki sauce                 *")
    # print("*                                                                                                                                               *")
    print('*'*145+'\n')
    # print(":"+"")
    print('When finish put \'end\'')
    check = input("Material:")
    thing = []
    while check != 'end':
        thing.append(check)
        check = input("Material:")
    data(thing, user)


main()
