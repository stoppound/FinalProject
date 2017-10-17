"""think"""
import pandas as pd
df = pd.read_csv('database.csv')
import numpy as np
import warnings
warnings.filterwarnings("ignore")

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
    while num != 10:
        num += 1
        print(num, ans[num-1][1])

    choose = ''
    while not(choose.isdigit() and 1 <= int(choose) <= 10):
        choose = input("NUMBER:")
    choose = int(choose)

    num = 0
    count = 1
    while count != 11:
        count += 1
        num += 1
        if num == choose:
            print(ans[num-1][1])
            save2(ans[num-1][1], user)

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
    return pd.read_csv('database.csv')

def username(name):
    df = load()
    if name in df.id.values:
        print('have user')
    else:
        df = df.append(pd.DataFrame({'id': [name]}),  ignore_index=True)
        print('add complete')
    save(df)


def main():
    user = input("USERNAME:")
    username(user)
    print("PROTEIN:    "+"pork    chicken    shrimp    fish    egg    milk    coconut milk    bean    tofu")
    print("CARBOHY:    "+"rice    mama    ")
    print("VITAMIN:    "+"basil    chilli    red chilli    onion    lemon    tomato    pumpkin    kale")
    print("SAUCE:      "+"soy sauce    oyster sauce    fish sauce    suki sauce")
    # print(":"+"")
    check = input("MATERIAL:")
    thing = []
    while check != 'end':
        thing.append(check)
        check = input("MATERIAL:")
    data(thing, user)


main()
