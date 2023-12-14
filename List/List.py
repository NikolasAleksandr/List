


#4 Postiindex
#Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda

indexid=["Tallinn","Narva, Narva-Joesuu","Kohtla-Jarve","Ida-Virumaa, Laane-Virumaa, Jogevamaa", "Tartu linn","Tartumaa, Polvamaa, Vorumaa, Valgamaa","Viljandimaa, Jarvamaa, Harjumaa, Raplamaa","Parnumaa", "Laanemaa, Hiiumaa, Saaremaa"]
while True:
    try: 
        index=int(input(f"Sisesta postiindex:"))#12345
        if len(str(index))==5: #"12345"
            break
    except :
        print("Viga!")
print("Indexi analyys")
index_str = str(index)
s1 = int(index_str[0]) #1-<0 Tallin indexiga 0
print("Index {0} on {1} piirkonnas".format(index, indexid[s1 - 1]))

if s1 == 1 or s1 == 2 or s1 == 3:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")


#5 Vahetus
#Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.

from random import *

kokku = randint(2, 20)
num_list = []
for i in range(kokku):
    num_list.append(randint(-100, 100))

print("Algne nimekiri:", num_list)
print()

while True:
    try:
        kogus = int(input("Mitu positsiooni vahetada? "))
        if kogus <= len(num_list) / 2:
            break
    except ValueError:
        print("Proovi uuesti.")

for i in range(0, kogus):
    X_tmp = num_list[i]
    print(f"{i}  {num_list[i]}  {num_list[len(num_list) - i - 1]}\n")
    num_list[i] = num_list[len(num_list) - i - 1]
    num_list[len(num_list) - i - 1] = X_tmp

print("\nUus nimekiri pärast vahetusi:", num_list)


#6 Бесполезные числа

from random import *

kokku = randint(2, 20)
print("Kokku järjendis on:", kokku, "elementi")

num_list = []
for i in range(kokku):
    num_list.append(round(random() * 1000, 2))

print("Algse järjendi väärtused:", num_list)

if not num_list:
    print("Järjend on tühi.")
else:
    maksimum = max(num_list)
    kasutu_number = maksimum / len(num_list)
    print("Kasutu number:", kasutu_number)

#7 Sorteerimine

numeric = randint(2,20)
numeric_list=[]
for i in range(numeric):
    numeric_list.append(randint(-1000,1000))
print(numeric_list)
print()
print("Len of numeric list - " + str(len(numeric_list)))
for i in range (0,numeric,1):
    numeric_list[i] = abs(numeric_list[i])

numeric_list.sort()
print(numeric_list)
numeric_list.sort(reverse=True)
print(numeric_list)







