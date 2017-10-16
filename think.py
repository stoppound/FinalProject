"""think"""
def data(thing):
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
    output(lst)


def output(out):
    all_lst = []
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
            lst0.append(i[1])
        elif i[0] == 1:
            lst1.append(i[1])
        elif i[0] == 2:
            lst2.append(i[1])
        elif i[0] == 3:
            lst3.append(i[1])
        elif i[0] == 4:
            lst4.append(i[1])
        elif i[0] == 5:
            lst5.append(i[1])
        elif i[0] == 6:
            lst6.append(i[1])
        elif i[0] == 7:
            lst7.append(i[1])
        elif i[0] == 8:
            lst8.append(i[1])
        elif i[0] == 9:
            lst9.append(i[1])
        elif i[0] == 10:
            lst10.append(i[1])
    num = 0
    lst_ans = []
    while num != 10:
        num += 1
        print(num, out[num-1][1])
        lst_ans.append(out[num-1][1])

    choose = int(input("NUMBER:"))
    while not(1 <= choose <= 10):
        choose = int(input("NUMBER:"))

    num = 0
    count = 1
    while count != 11:
        count += 1
        num += 1
        if num == choose:
            print(out[num-1][1])


def username(name):
    lst_name = []
    if name in lst_name:
        check = lst_name.find(name)

    else:
        lst_name.append(name)


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
    data(thing)


main()
