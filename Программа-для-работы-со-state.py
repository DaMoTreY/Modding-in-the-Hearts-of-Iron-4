import re
import os
from array import *
from tkinter import *

global search2
search2 = False

def start():
    textBox.pack()
    
    btn_prisv.place_forget()
    btn_nac.place_forget()
    btn_two.place_forget()
    btn_manpower.place_forget()
    
    btn_prisvoit.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

    
def click_button():
    label['text'] = "Что вы хотите сделать с облястями?"

    btn_in_menu.place_forget()
    
    btn.place_forget()
    
    btn_manpower.place(relx=.5, rely=.6, anchor="c", height=30, width=170, bordermode=OUTSIDE)
    
    btn_prisv.place(relx=.3, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
    
    btn_nac.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
    
    btn_two.place(relx=.7, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)


def manpower():
    label['text'] = "В каких регионах вы хотите изменить количество людских ресурсов? (Напишите ID через пробел)"
    
    btn_manpower.place_forget()

    btn_nac.place_forget()
    
    btn_prisv.place_forget()
    
    btn_two.place_forget()

    btn_daleemanpower.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

    textBoxManpower.pack()

def manpower2():
    label['text'] = "Какое количество людских ресурсов в них станет соответственно?"

    btn_daleemanpower.place_forget()

    mnr = textBoxManpower.get("1.0","end-1c")
    
    global ManpowerREG
    
    ManpowerREG = mnr.split(" ")

    textBoxManpower.pack_forget()

    textBoxKolvo.pack()

    btn_kolvomanpower.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
    

def kolvomanpower():
    mnp  = textBoxKolvo.get("1.0","end-1c")
    
    global Manpower
    
    Manpower = mnp.split(" ")

    textBoxKolvo.pack_forget()
    
    label['text'] = "Укажите путь к папке со списком регионов ДЛЯ ВАШЕГО МОДА, А НЕ ОРИГИНАЛЬНОЙ ИГРЫ.\nНапример:\nC:\Program Files (x86)\Steam\steamapps\workshop\content\\394360\Rise of Mongol\history\states"

    btn_kolvomanpower.place_forget()

    textBox3.pack()

    btn_tofinishmanpower.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
    
def lastmanpower():
    z = 0
    w = textBox3.get("1.0","end-1c")
    way = w.replace("\\", "/")
    directory = way
    files = os.listdir(directory)
    y = 0
    
    for y in range(len(ManpowerREG)):
        
        for i in range(len(files)):
    
            mystate = re.findall(r'^%s-' % ManpowerREG[y], r'%s' % files[z], flags = re.MULTILINE)
            if mystate:
    
                #print(files[z])
                with open (way+"/"+files[z]) as f:
                    wordsinfiles = f.readlines()
                popi = 0
                for i in range(len(wordsinfiles)):
                    nusniy = re.findall(r'%s' % "manpower", r'%s' % wordsinfiles[popi])
                    
                    if nusniy:
                        #print (wordsinfiles[popi] + " - строчка, в которой определется владелец")
                        number = re.findall(r'\d[\d]', r'%s' % wordsinfiles[popi])
                        #print (teg[0] + " - тег страны, которой принадлежит регион")
                        wordsinfiles[popi] = wordsinfiles[popi].replace(max(number),Manpower[y])
                        #print(wordsinfiles[popi] + " - как будет выглядеть замена")
                        with open (way+"/"+files[z],"w") as f1:
                             f1.writelines(wordsinfiles)
                    popi = popi+1
                    
                break

            z = z+1
        z = 0
    btn_tofinishmanpower.place_forget()
    textBox3.pack_forget()
    label['text'] = "Готово!\nВернитесь в главное меню"
    btn_in_menu.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

    
def prisv():
    global search
    search = "owner"
    global job
    job = " присваивать "
    label['text'] = "Какой стране вы будете" + job + "регионы? (Напишите её тег, на пример, FRA)"
    start()


def nac():
    global search
    search = "add_core_of"
    global job
    job = " национализировать "
    label['text'] = "Какой стране вы будете" + job + "регионы? (Напишите её тег, на пример, FRA)"
    start()
    

def two():
    global search
    search = "owner"
    global search2
    search2 = "add_core_of"
    global job
    job = " присваивать и национализировать "
    label['text'] = "Какой стране вы будете" + job + "регионы? (Напишите её тег, на пример, FRA)"
    start()
    
def prisvoenie():
    global REG
    REG=textBox.get("1.0","end-1c")
    
    btn_prisvoit.place_forget()

    textBox.pack_forget()

    textBox2.pack()

    btn_dalee.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

    label['text'] = "Какие регионы вы будете" + job + "? (Напишите ID через пробел)"


def dalee():
    vrm = textBox2.get("1.0","end-1c")
    global regions
    
    regions = vrm.split(" ")
    label['text'] = "Укажите путь к папке со списком регионов ДЛЯ ВАШЕГО МОДА, А НЕ ОРИГИНАЛЬНОЙ ИГРЫ.\nНапример:\nC:\Program Files (x86)\Steam\steamapps\workshop\content\\394360\Rise of Mongol\history\states"

    textBox2.pack_forget()
    textBox3.pack()

    btn_dalee.place_forget()

    btn_last_dalee.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

def start_of_the_programm():

    z = 0
    w = textBox3.get("1.0","end-1c")
    way = w.replace("\\", "/")
    directory = way
    files = os.listdir(directory)
    y = 0
    for y in range(len(regions)):
        
        for i in range(len(files)):
            mystate = re.findall(r'^%s-' % regions[y], r'%s' % files[z], flags = re.MULTILINE)
            if mystate:
    
                with open (way+"/"+files[z]) as f:
                    wordsinfiles = f.readlines()
                popi = 0
                for i in range(len(wordsinfiles)):
                    nusniy = re.findall(r'%s' % search, r'%s' % wordsinfiles[popi])
                    if search2:
                        nusniy2 = re.findall(r'%s' % search2, r'%s' % wordsinfiles[popi])
                        if nusniy2:
                            teg = re.findall(r'[A-Z]{3}', r'%s' % wordsinfiles[popi])
                            wordsinfiles[popi] = wordsinfiles[popi].replace(teg[0],REG)
                            with open (way+"/"+files[z],"w") as f1:
                                f1.writelines(wordsinfiles)
                    if nusniy:
                        #print (wordsinfiles[popi] + " - строчка, в которой определется владелец")
                        teg = re.findall(r'[A-Z]{3}', r'%s' % wordsinfiles[popi])
                        #print (teg[0] + " - тег страны, которой принадлежит регион")
                        wordsinfiles[popi] = wordsinfiles[popi].replace(teg[0],REG)
                        #print(wordsinfiles[popi] + " - как будет выглядеть замена")
                        with open (way+"/"+files[z],"w") as f1:
                             f1.writelines(wordsinfiles)
                    popi = popi+1
                    
                break
            z = z+1
        z = 0
    btn_last_dalee.place_forget()
    label['text'] = "Готово!\nВернитесь в главное меню"
    textBox3.pack_forget()
    btn_in_menu.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
            

def in_menu():
    click_button()
    textBox.delete ('1.0',END)
    textBox2.delete ('1.0',END)
    textBoxWay.delete ('1.0',END)
    textBoxManpower.delete ('1.0',END)
    textBoxKolvo.delete ('1.0',END)
    textBoxManpowerWay.delete ('1.0',END)
    
root = Tk()
root.title("Работа со state")
root.geometry("1000x500")

FirstText = ("Привет! Это программа для работы со state в Hearts of Irom 4. \nОна создана, чтобы облегчить работу с ними. \nВ этой программе можно присваивать быстро одному государству любой state, даже если вы сами его создали.\nПривет всем мододелам :)")
label = Label(text=FirstText, justify=LEFT)
label.pack()

btn_manpower = Button(text = "Добавить людских ресурсов", command = manpower)
btn_two = Button(text = "Оба сразу", command = two)
btn_nac = Button(text = "Национализировать", command = nac)
btn_prisv = Button(text = "Присвоить", command = prisv)
btn_prisvoit = Button(text = "Далее", command = prisvoenie)
btn_dalee = Button(text = "Далее", command = dalee)
btn_last_dalee = Button(text = "Далее", command = start_of_the_programm)
btn = Button(text="Начать работу!", command = click_button)
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn_daleemanpower = Button(text = ['Далее'], command = manpower2)
btn_kolvomanpower = Button(text = ['Далее'], command = kolvomanpower)
btn_tofinishmanpower = Button(text = ['Далее'], command = lastmanpower)
btn_in_menu = Button(text = "МЕНЮ", command = in_menu)

textBoxWay = Text(root, height=1, width=50)
textBox = Text(root, height=1, width=10)
textBox2 = Text(root, height=1, width=30)
textBox3 = Text(root, height=1, width=50)
textBoxManpower = Text(root, height = 1, width = 50)
textBoxKolvo = Text(root, height = 1, width = 50)
textBoxManpowerWay = Text(root, height = 1, width = 50)


root.mainloop()
z = 0

    #way = w.replace("\\", "/")
    #directory = way
    #files = os.listdir(directory)
    #y = 0
    #for y in range(len(regions)):
    #    
    #    for i in range(len(files)):
    #
    #        mystate = re.findall(r'^%s-' % regions[y], r'%s' % files[z], flags = re.MULTILINE)
    #        if mystate:
    #
    #            print(files[z])
    #            with open (way+"/"+files[z]) as f:
    #                wordsinfiles = f.readlines()
    #            popi = 0
    #            for i in range(len(wordsinfiles)):
    #                nusniy = re.findall(r'owner', r'%s' % wordsinfiles[popi])
    #                if nusniy:
    #                    print (wordsinfiles[popi] + " - строчка, в которой определется владелец")
    #                    teg = re.findall(r'[A-Z]{3}', r'%s' % wordsinfiles[popi])
    #                    print (teg[0] + " - тег страны, которой принадлежит регион")
    #                    wordsinfiles[popi] = wordsinfiles[popi].replace(teg[0],REG)
    #                    print(wordsinfiles[popi] + " - как будет выглядеть замена")
    #                    with open (way+"/"+files[z],"w") as f1:
    #                         f1.writelines(wordsinfiles)
    #                popi = popi+1
    #                
    #            break
#
    #        z = z+1
    #        
    #    y = y+1
        
        
    
