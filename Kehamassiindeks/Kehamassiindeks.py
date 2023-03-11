"""print("Tere! Olen sinu uus sõber - Python!")
nimi=input("\nMis su nimi on?")
print(nimi,", oi kui ilus nimi!")
vastus=input(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if vastus==1:
    pikkus=int(input"\nMis on Sinu pikkus?")
"""




tervitus=print("Tere! Olen sinu uus sõber - Python!") # Выводим на экран приветствия
print("Mis su nimi on?") 
nimi=input("Nimi: ")  # Присваивание переменной nimi введённого пользователем имени

while nimi . isalpha()!= True:  # Проверяем,  состоит ли ответ из букв. 
                                # Если же в ответе присудствуют цифры или спец символы, запрашиваем имя повторно.
    try:
        nimi=input("Nimi veel kord")
    except:
        ValueError
print(f"{nimi}, oi kui ilus nimi!") # Выводим на экран имя введенное пользователем и текст
vastus=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
#type (vastus)=str 1->"1"
if vastus =="1": # Если пользователь выбирает "1", то запрашиваем рост и вес
    pikkus=""
    while type(pikkus) != int or pikkus<45 or pikkus>250:
        try:
            pikkus= int (input("Sinu pikkus on ...")) # Присваивание переменной pikkus целого значения переменной введенной пользователем
        except:
            ValueError
    mass=""
    while type(mass) != int or mass<0 or mass>300:
        try:
            mass= int (input("Sinu kaal on ...")) # Присваивание переменной mass целого значения переменной введенной пользователем
        except:
            ValueError
    indeks=round (mass/ ((0.01*pikkus)**2), 1) # Присваивание переменной indeks значения выражения mass /(0.01pikkus)**2 , ответ выводим с одним знаком после запятой
    print(f"Sinu keha indeks on: {indeks}") # str+int/float # Выводим на экран индекс и оценку массы тела
    if indeks<16:
        print ("Tervisele ohtlik alakaal")
    elif 16<=indeks <19: # indeks>=16 and indeks <19
        print ("Alakaal")
    elif 19<=indeks <25:
        print("Normaalkaal")
    elif 25<=indeks <30:
        print("Ülekaal")
    elif 30<=indeks <35:
        print("Rasvumine")
    elif 35<=indeks <40:
        print("Tugev rasvumine")
    else:
        print("Tervisele ohtlik rasvumine")
 
   
else:  # Если пользователь ничего не выбирает, то прощаемся 
    print("\nKahju! See on väga kasulik info!")
 
    print("\nKohtumiseni, " + nimi + "! Igavesti Sinu, Python!")