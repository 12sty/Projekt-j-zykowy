import tkinter as tk
from tkinter import *
from googletrans import Translator
import random
import time

#numery pytań
pytania = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#punkty liczą punkty
punkty=0

#zycia ilość możliwych błędów jak zero to koniec na ich podstawie wyświetla wynik
zycie=4

#łatwy poziom trudnści
def latwy():
    windowL=tk.Tk()
    label=tk.Label(windowL, text=translate_text("aby odblokowac poziom łatwy nalezy wykupić"), font=('Helvetica', 16)).pack()
    label=tk.Label(windowL, text=translate_text("!!PAKIET PREMIUM!!"), font=('Trajan PRO', 75, 'bold'), fg='gold').pack()
    label=tk.Label(windowL, text=translate_text("za 150.000 zł"), font=('Helvetica', 10)).pack()
    print('PROBLEM Z ZDJĘCIAMI \n ZDJĘCIA NIEDZIALAŁY')
    windowL.mainloop()
    
#średni poziom trudność 
def sredny():
    global punkty, pytania

    
    #wyświetla wynik w zależności od pozostałych życ
    def wyniksred():
        window42=tk.Tk()
        window42.geometry = ()
        if zycie==1:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='😒', font=('Helvetica', 20)).pack()
        if zycie==2:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='😊', font=('Helvetica', 20)).pack()
        if zycie==3:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='😁', font=('Helvetica', 20)).pack()
        if zycie==4:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='😍', font=('Helvetica', 20)).pack()
        if zycie==0:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='☠️', font=('Helvetica', 20)).pack()
        window42.mainloop()

    #po złej odpowiedzi odejmuje życie i wraza do sredny
    def zlesred():
        global zycie
        zycie -= 1
        sredny()

    #po poprawnej odpowiedzi dodaje punkt i wraca do zredny
    def dobsred():
        global punkty
        punkty+=1
        if zycie > 0 and pytania == 00 and punkty >= 5:
            wyniksred()
        elif zycie > 0:
             sredny()


    if pytania == []:
         wyniksred()
    #dopuki jest jakie kolwiek życie można grac
    elif zycie >0:
        pyt = random.randint(1, 20) #losuje pytanie z listy pytań
        
        
        if pyt == 1: # pyt to pytanie losowane powyżej
            if pyt in pytania:  #jeżeli pytanie w liście pytań
                pytania.remove(pyt) #usuwa pytanie z listy pytań
                pyt=0
                window23=tk.Tk()
                window23.geometry('800x800')
                label=tk.Label(window23, text=translate2_text("apple"), font=('Helvetica', 20)).pack()          #pytanie
                label=tk.Label(window23, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0) #punkty
                label=tk.Label(window23, text=punkty, font=('Helvetica', 16)).place(x=700, y=0) #liczba punktów
                button=tk.Button(window23, text=translate_text('jabłko'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)  #odpowiedź1     #po wybraniu poprawnej odpowiedzi dobsred idzie do dobsred
                button=tk.Button(window23, text=translate_text("banan"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)   #odpowiedź2
                button=tk.Button(window23, text=translate_text('ogórek'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)  #odpowiedx3     # po wybraniu złej odpowiedzi zlesred idzie do zlesred
                button=tk.Button(window23, text=translate_text("ananas"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)  #odpowieź4
                window23.mainloop()
            #jeżeli pytanie 1 niejest w liście pytan (bo jusz się pojawiło) to idzie do średnie i losuje kolejne pytanie
            elif pyt not in pytania:
                sredny()

    #=================================komentarze takie same do reszty pytań==========================================================

        elif pyt == 2:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                window24=tk.Tk()
                window24.geometry('800x800')
                label=tk.Label(window24, text=translate2_text("bed"), font=('Helvetica', 20)).pack()
                label=tk.Label(window24, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window24, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                button=tk.Button(window24, text=translate_text('sofa'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                button=tk.Button(window24, text=translate_text("łóżko"), font=('Helvetica', 16), command=dobsred).place(x=470, y=130)
                button=tk.Button(window24, text=translate_text('fotel'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                button=tk.Button(window24, text=translate_text("szafa"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                window24.mainloop()
            elif pyt not in pytania:
                sredny()


        elif pyt == 3:
            if pyt in pytania:
                pytania.remove(pyt)
                window25=tk.Tk()
                window25.geometry('800x800')
                label=tk.Label(window25, text=translate2_text("window"), font=('Helvetica', 20)).pack()
                label=tk.Label(window25, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window25, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                button=tk.Button(window25, text=translate_text('lis'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                button=tk.Button(window25, text=translate_text("firanka"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                button=tk.Button(window25, text=translate_text('okno'), font=('Helvetica', 16), command=dobsred).place(x=230, y=230)
                button=tk.Button(window25, text=translate_text("szerokość"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                window25.mainloop()
            elif pyt not in pytania:
                sredny()


        elif pyt == 4:
            if pyt in pytania:
                pytania.remove(pyt)
                window26=tk.Tk()
                window26.geometry('800x800')
                label=tk.Label(window26, text=translate2_text("fridge"), font=('Helvetica', 20)).pack()
                label=tk.Label(window26, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window26, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                button=tk.Button(window26, text=translate_text('zamrażarka'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                button=tk.Button(window26, text=translate_text("lodówka"), font=('Helvetica', 16), command=dobsred).place(x=470, y=130)
                button=tk.Button(window26, text=translate_text('miecz'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                button=tk.Button(window26, text=translate_text("biały"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                window26.mainloop()
            elif pyt not in pytania:
                sredny()


        elif pyt == 5:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                window27=tk.Tk()
                window27.geometry('800x800')
                text2=tk.StringVar()
                label=tk.Label(window27, text=translate2_text("mouse"), font=('Helvetica', 20)).pack()
                label=tk.Label(window27, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window27, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                button=tk.Button(window27, text=translate_text('szczur'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                button=tk.Button(window27, text=translate_text("chomik"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                button=tk.Button(window27, text=translate_text('ogon'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                button=tk.Button(window27, text=translate_text("mysz"), font=('Helvetica', 16), command=dobsred).place(x=470, y=230)
                window27.mainloop()
            elif pyt not in pytania:
                sredny()


        elif pyt == 6:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                window28=tk.Tk()
                window28.geometry('800x800')
                text2=tk.StringVar()
                label=tk.Label(window28, text=translate2_text("door"), font=('Helvetica', 20)).pack()
                label=tk.Label(window28, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window28, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                button=tk.Button(window28, text=translate_text('furtka'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                button=tk.Button(window28, text=translate_text("drzwi"), font=('Helvetica', 16), command=dobsred).place(x=470, y=130)
                button=tk.Button(window28, text=translate_text('klapa'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                button=tk.Button(window28, text=translate_text("piec"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                window28.mainloop()
            elif pyt not in pytania:
                sredny()


        elif pyt == 7:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window29=tk.Tk()
                    window29.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window29, text=translate2_text("cat"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window29, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window29, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window29, text=translate_text('kot'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)
                    button=tk.Button(window29, text=translate_text("ciąć"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window29, text=translate_text('pies'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window29, text=translate_text("jeść"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window29.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 8:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window30=tk.Tk()
                    window30.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window30, text=translate2_text("eat"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window30, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window30, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window30, text=translate_text('pić'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window30, text=translate_text("zupa"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window30, text=translate_text('kot'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window30, text=translate_text("jeść"), font=('Helvetica', 16), command=dobsred).place(x=470, y=230)
                    window30.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 9:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window31=tk.Tk()
                    window31.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window31, text=translate2_text("chair"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window31, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window31, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window31, text=translate_text('krzesło'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)
                    button=tk.Button(window31, text=translate_text("fotel"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window31, text=translate_text('stać'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window31, text=translate_text("usiąść"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window31.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 10:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window32=tk.Tk()
                    window32.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window32, text=translate2_text("get up"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window32, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window32, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window32, text=translate_text('wstać'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)
                    button=tk.Button(window32, text=translate_text("krzesło"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window32, text=translate_text('stać'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window32, text=translate_text("łóżko"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window32.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 11:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window33=tk.Tk()
                    window33.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window33, text=translate2_text("bow"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window33, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window33, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window33, text=translate_text('łuk'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)
                    button=tk.Button(window33, text=translate_text("autobus"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window33, text=translate_text('przystanek'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window33, text=translate_text("automat"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window33.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 12:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window34=tk.Tk()
                    window34.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window34, text=translate2_text("home"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window34, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window34, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window34, text=translate_text('garaz'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window34, text=translate_text("wieżowiec"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window34, text=translate_text('dom'), font=('Helvetica', 16), command=dobsred).place(x=230, y=230)
                    button=tk.Button(window34, text=translate_text("ryba"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window34.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 13:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window35=tk.Tk()
                    window35.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window35, text=translate2_text("tree"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window35, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window35, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window35, text=translate_text('drzewo'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)
                    button=tk.Button(window35, text=translate_text("krzak"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window35, text=translate_text('las'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window35, text=translate_text("ziemia"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window35.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 14:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window36=tk.Tk()
                    window36.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window36, text=translate2_text("book"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window36, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window36, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window36, text=translate_text('bomba'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window36, text=translate_text("drzwi"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window36, text=translate_text('piła'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window36, text=translate_text("książka"), font=('Helvetica', 16), command=dobsred).place(x=470, y=230)
                    window36.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 15:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window37=tk.Tk()
                    window37.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window37, text=translate2_text("pen"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window37, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window37, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window37, text=translate_text('ołówek'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window37, text=translate_text("długopis"), font=('Helvetica', 16), command=dobsred).place(x=470, y=130)
                    button=tk.Button(window37, text=translate_text('okno'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window37, text=translate_text("kalkulator"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window37.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 16:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window38=tk.Tk()
                    window38.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window38, text=translate2_text("calculator"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window38, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window38, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window38, text=translate_text('obliczyć'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window38, text=translate_text("liczyc"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window38, text=translate_text('kalkulator'), font=('Helvetica', 16), command=dobsred).place(x=230, y=230)
                    button=tk.Button(window38, text=translate_text("kartka"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window38.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 17:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window38=tk.Tk()
                    window38.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window38, text=translate2_text("far"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window38, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window38, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window38, text=translate_text('daleko'), font=('Helvetica', 16), command=dobsred).place(x=230, y=130)
                    button=tk.Button(window38, text=translate_text("zadaleko"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window38, text=translate_text('pierd'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window38, text=translate_text("droga"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window38.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 18:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window39=tk.Tk()
                    window39.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window39, text=translate2_text("price"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window39, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window39, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window39, text=translate_text('mydło'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window39, text=translate_text("drogie"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window39, text=translate_text('nie'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window39, text=translate_text("cena"), font=('Helvetica', 16), command=dobsred).place(x=470, y=230)
                    window39.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 19:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window40=tk.Tk()
                    window40.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window40, text=translate2_text("shoes"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window40, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window40, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window40, text=translate_text('gróby'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window40, text=translate_text("buty"), font=('Helvetica', 16), command=dobsred).place(x=470, y=130)
                    button=tk.Button(window40, text=translate_text('spodnie'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                    button=tk.Button(window40, text=translate_text("kurtki"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window40.mainloop()
                elif pyt not in pytania:
                    sredny()


        elif pyt == 20:
                if pyt in pytania:

                    pytania.remove(pyt)
                    pyt=0
                    window41=tk.Tk()
                    window41.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window41, text=translate2_text("notebook"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window41, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window41, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    button=tk.Button(window41, text=translate_text('stać'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                    button=tk.Button(window41, text=translate_text("ławka"), font=('Helvetica', 16), command=zlesred).place(x=470, y=130)
                    button=tk.Button(window41, text=translate_text('zeszyt'), font=('Helvetica', 16), command=dobsred).place(x=230, y=230)
                    button=tk.Button(window41, text=translate_text("mysz"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                    window41.mainloop()
                elif pyt not in pytania:
                    sredny()
        elif zycie >0 and pytania == 00:
             wyniksred()
        # po ukończeniu wszystkich pytań powinno iść do wynik i wyświetlic wynik             
    elif zycie ==0 or zycie <0 and pytania == 00:
         wyniksred()
    
#sredno trudny
def sredtrud():
    global pynkty, pytania
    
    windowL=tk.Tk()
    label=tk.Label(windowL, text=translate_text("aby odblokowac poziom średnio trudny nalezy wykupić"), font=('Helvetica', 16)).pack()
    label=tk.Label(windowL, text=translate_text("!!PAKIET PREMIUM!!"), font=('Trajan PRO', 75, 'bold'), fg='gold').pack()
    label=tk.Label(windowL, text=translate_text("za 150.000 zł"), font=('Helvetica', 10)).pack()
    print('DA SIĘ WPISAC ALE PROBLEM Z TYM ŻEBY SPRAWDZAŁO DOBRZE I DZIAŁAŁO\ngdybym mial robic żeby działłał to było by owiele zadużo')
    windowL.mainloop()

    #def wyniksredtrud():
        ###############################tabela z poprawnością
        #window42=tk.Tk()
        #
        #if punkty>=4 and punkty<=9:
        #    label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()################################zamiast emoji cytat czy tekst
        #    label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)#######################################niemusisz zmieniać numerów okien
        #    label=tk.Label(window42, text='nienajgorzej', font=('Helvetica', 20)).pack()
        #if punkty<=14 and punkty>=10:
        #    label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
        #    label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
        #    label=tk.Label(window42, text='dobrze', font=('Helvetica', 20)).pack()
        #if punkty<=19 and punkty >= 15:
        #    label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
        #    label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
        #    label=tk.Label(window42, text='bardzo dobrze', font=('Helvetica', 20)).pack()
        #if punkty==20:
        #    label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
        #    label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
        #    label=tk.Label(window42, text='perfekcyjnie', font=('Helvetica', 20)).pack()
        #if zycie==0 or punkty<=3:
        #    label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
        #    label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
        #    label=tk.Label(window42, text='zaraza', font=('Helvetica', 20)).pack()
        #window42.mainloop()

        #po złej odpowiedzi odejmuje życie i wraza do trudny
    def zlesredtrud():
        global zycie
        zycie -= 1
        sredtrud()
    #po poprawnej odpowiedzi dodaje punkt i wraca do zredny
    def dobsredtrud():
        global punkty
        punkty+=1
        if zycie > 0 and pytania == 00:
            wyniksredtrud()
        elif zycie > 0:
            sredtrud()
    if pytania == []:
        wyniksredtrud()
    #dopuki jest jakie kolwiek życie można grac
    elif zycie >0:
        pyt = random.randint(1, 20) #losuje pytanie z listy pytań
        
        if pyt==1:
            window41=tk.Tk()
            slowo11=translate2_text('gun')
            slowo1= list(slowo11.strip(" "))
            litera=random.randint(1, len(slowo1))
            if litera==1:
                slowo1[0]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo1[1]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo1[2]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo1[3]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo1[4]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo1[5]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo1[6]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo1[7]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo1[8]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo1[9]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo1[10]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo1[11]=''
                label=tk.Label(window41, text=slowo1).pack()
                label=tk.Label(window41, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window41).pack()
                if en==slowo1[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window41.mainloop()
        if pyt==2:
            window42=tk.Tk()
            slowo21=translate2_text('sword')
            slowo2= list(slowo21.strip(" "))
            litera=random.randint(1, len(slowo2))
            if litera==1:
                slowo2[0]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo2[1]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo2[2]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo2[3]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo2[4]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo2[5]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo2[6]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo2[7]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo2[8]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo2[9]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo2[10]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo2[11]=''
                label=tk.Label(window42, text=slowo2).pack()
                label=tk.Label(window42, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window42).pack()
                if en==slowo2[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window42.mainloop()
        if pyt==3:
            window43=tk.Tk()
            slowo31=translate2_text('dad')
            slowo3= list(slowo31.strip(" "))
            litera=random.randint(1, len(slowo3))
            if litera==1:
                slowo3[0]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo3[1]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo3[2]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo3[3]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo3[4]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo3[5]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo3[6]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo3[7]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo3[8]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo3[9]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo3[10]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo3[11]=''
                label=tk.Label(window43, text=slowo3).pack()
                label=tk.Label(window43, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window43).pack()
                if en==slowo3[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window43.mainloop()
        if pyt==4:
            window44=tk.Tk()
            slowo41=translate2_text('mom')
            slowo4= list(slowo41.strip(" "))
            litera=random.randint(1, len(slowo4))
            if litera==1:
                slowo4[0]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo4[1]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo4[2]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo4[3]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo4[4]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo4[5]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo4[6]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo4[7]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo4[8]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo4[9]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo4[10]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo4[11]=''
                label=tk.Label(window44, text=slowo4).pack()
                label=tk.Label(window44, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window44).pack()
                if en==slowo4[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window44.mainloop()
        if pyt==5:
            window45=tk.Tk()
            slowo51=translate2_text('sister')
            slowo5= list(slowo51.strip(" "))
            litera=random.randint(1, len(slowo5))
            if litera==1:
                slowo5[0]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo5[1]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo5[2]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo5[3]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo5[4]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo5[5]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo5[6]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo5[7]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo5[8]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo5[9]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo5[10]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo5[11]=''
                label=tk.Label(window45, text=slowo5).pack()
                label=tk.Label(window45, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window45).pack()
                if en==slowo5[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window45.mainloop()
        if pyt==6:
            window46=tk.Tk()
            slowo61=translate2_text('hood')
            slowo6= list(slowo61.strip(" "))
            litera=random.randint(1, len(slowo6))
            if litera==1:
                slowo6[0]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo6[1]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo6[2]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo6[3]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo6[4]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo6[5]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo6[6]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo6[7]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo6[8]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo6[9]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo6[10]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo6[11]=''
                label=tk.Label(window46, text=slowo6).pack()
                label=tk.Label(window46, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window46).pack()
                if en==slowo6[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window46.mainloop()
        if pyt==7:
            window47=tk.Tk()
            slowo71=translate2_text('phone')
            slowo7= list(slowo71.strip(" "))
            litera=random.randint(1, len(slowo7))
            if litera==1:
                slowo7[0]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo7[1]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo7[2]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo7[3]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo7[4]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo7[5]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo7[6]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo7[7]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo7[8]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo7[9]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo7[10]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo7[11]=''
                label=tk.Label(window47, text=slowo7).pack()
                label=tk.Label(window47, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window47).pack()
                if en==slowo7[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window47.mainloop()
        if pyt==8:
            window48=tk.Tk()
            slowo81=translate2_text('king')
            slowo8= list(slowo81.strip(" "))
            litera=random.randint(1, len(slowo8))
            if litera==1:
                slowo8[0]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo8[1]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo8[2]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo8[3]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo8[4]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo8[5]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo8[6]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo8[7]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo8[8]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo8[9]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo8[10]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo8[11]=''
                label=tk.Label(window48, text=slowo8).pack()
                label=tk.Label(window48, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window48).pack()
                if en==slowo8[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window48.mainloop()
        if pyt==9:
            window49=tk.Tk()
            slowo91=translate2_text('basketball')
            slowo9= list(slowo91.strip(" "))
            litera=random.randint(1, len(slowo9))
            if litera==1:
                slowo9[0]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo9[1]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo9[2]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo9[3]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo9[4]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo9[5]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo9[6]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo9[7]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo9[8]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo9[9]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo9[10]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo9[11]=''
                label=tk.Label(window49, text=slowo9).pack()
                label=tk.Label(window49, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window49).pack()
                if en==slowo9[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window49.mainloop()
        if pyt==10:
            window50=tk.Tk()
            slowo101=translate2_text('dog')
            slowo10= list(slowo101.strip(" "))
            litera=random.randint(1, len(slowo10))
            if litera==1:
                slowo10[0]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo10[1]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo10[2]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo10[3]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo10[4]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo10[5]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo10[6]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo10[7]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo10[8]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo10[9]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo10[10]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo10[11]=''
                label=tk.Label(window50, text=slowo10).pack()
                label=tk.Label(window50, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window50).pack()
                if en==slowo10[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window50.mainloop()
        if pyt==11:
            window51=tk.Tk()
            slowo111=translate2_text('cat')
            slowo11= list(slowo111.strip(" "))
            litera=random.randint(1, len(slowo11))
            if litera==1:
                slowo11[0]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo11[1]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo11[2]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo11[3]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo11[4]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo11[5]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo11[6]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo11[7]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo11[8]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo11[9]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo11[10]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo11[11]=''
                label=tk.Label(window51, text=slowo11).pack()
                label=tk.Label(window51, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window51).pack()
                if en==slowo11[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window51.mainloop()
        if pyt==12:
            window52=tk.Tk()
            slowo121=translate2_text('fruit')
            slowo12= list(slowo121.strip(" "))
            litera=random.randint(1, len(slowo12))
            if litera==1:
                slowo12[0]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo12[1]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo12[2]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo12[3]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo12[4]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo12[5]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo12[6]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo12[7]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo12[8]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo12[9]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo12[10]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo12[11]=''
                label=tk.Label(window52, text=slowo12).pack()
                label=tk.Label(window52, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window52).pack()
                if en==slowo12[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window52.mainloop()
        if pyt==13:
            window53=tk.Tk()
            slowo131=translate2_text('egg')
            slowo13= list(slowo131.strip(" "))
            litera=random.randint(1, len(slowo13))
            if litera==1:
                slowo13[0]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo13[1]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo13[2]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo13[3]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo13[4]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo13[5]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo13[6]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo13[7]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo13[8]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo13[9]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo13[10]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo13[11]=''
                label=tk.Label(window53, text=slowo13).pack()
                label=tk.Label(window53, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window53).pack()
                if en==slowo13[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window53.mainloop()
        if pyt==14:
            window54=tk.Tk()
            slowo141=translate2_text('bed')
            slowo14= list(slowo141.strip(" "))
            litera=random.randint(1, len(slowo14))
            if litera==1:
                slowo14[0]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo14[1]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo14[2]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo14[3]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo14[4]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo14[5]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo14[6]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo14[7]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo14[8]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo14[9]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo14[10]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo14[11]=''
                label=tk.Label(window54, text=slowo14).pack()
                label=tk.Label(window54, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window54).pack()
                if en==slowo14[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window54.mainloop()
        if pyt==15:
            window55=tk.Tk()
            slowo151=translate2_text('tree')
            slowo15= list(slowo151.strip(" "))
            litera=random.randint(1, len(slowo15))
            if litera==1:
                slowo15[0]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo15[1]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo15[2]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo15[3]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo15[4]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo15[5]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo15[6]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo15[7]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo15[8]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo15[9]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo15[10]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo15[11]=''
                label=tk.Label(window55, text=slowo15).pack()
                label=tk.Label(window55, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window55).pack()
                if en==slowo15[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window55.mainloop()
        if pyt==16:
            window56=tk.Tk()
            slowo161=translate2_text('store')
            slowo16= list(slowo161.strip(" "))
            litera=random.randint(1, len(slowo16))
            if litera==1:
                slowo16[0]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo16[1]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo16[2]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo16[3]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo16[4]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo16[5]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo16[6]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo16[7]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo16[8]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo16[9]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo16[10]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo16[11]=''
                label=tk.Label(window56, text=slowo16).pack()
                label=tk.Label(window56, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window56).pack()
                if en==slowo16[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window56.mainloop()
        if pyt==17:
            window57=tk.Tk()
            slowo171=translate2_text('pen')
            slowo17= list(slowo171.strip(" "))
            litera=random.randint(1, len(slowo17))
            if litera==1:
                slowo17[0]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo17[1]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo17[2]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo17[3]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo17[4]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo17[5]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo17[6]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo17[7]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo17[8]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo17[9]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo17[10]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo17[11]=''
                label=tk.Label(window57, text=slowo17).pack()
                label=tk.Label(window57, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window57).pack()
                if en==slowo17[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window57.mainloop()
        if pyt==18:
            window58=tk.Tk()
            slowo181=translate2_text('bird')
            slowo18= list(slowo181.strip(" "))
            litera=random.randint(1, len(slowo18))
            if litera==1:
                slowo18[0]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo18[1]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo18[2]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo18[3]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo18[4]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo18[5]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo18[6]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo18[7]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo18[8]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo18[9]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo18[10]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo18[11]=''
                label=tk.Label(window58, text=slowo18).pack()
                label=tk.Label(window58, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window58).pack()
                if en==slowo18[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window58.mainloop()
        if pyt==19:
            window59=tk.Tk()
            slowo191=translate2_text('airplane')
            slowo19= list(slowo191.strip(" "))
            litera=random.randint(1, len(slowo19))
            if litera==1:
                slowo19[0]=''
                label=tk.Label(window59, text=slowo19).pack()
                label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window59).pack()
                if en==slowo19[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo19[1]=''
                label=tk.Label(window59, text=slowo19).pack()
                label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window59).pack()
                if en==slowo19[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo19[2]=''
                label=tk.Label(window59, text=slowo19).pack()
                label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window59).pack()
                if en==slowo19[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo19[3]=''
                label=tk.Label(window59, text=slowo19).pack()
                label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window59).pack()
                if en==slowo19[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo19[4]=''
                label=tk.Label(window59, text=slowo19).pack()
                label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window59).pack()
                if en==slowo19[4]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==6:
                slowo19[5]=''
                label=tk.Label(window59, text=slowo19).pack()
                label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window59).pack()
                if en==slowo19[5]:
                    dobsredtrud()
                else:
                        zlesredtrud()
                if litera==7:
                    slowo19[6]=''
                    label=tk.Label(window59, text=slowo19).pack()
                    label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                    en=tk.Entry(window59).pack()
                    if en==slowo19[6]:
                        dobsredtrud()
                    else:
                        zlesredtrud()
                if litera==8:
                    slowo19[7]=''
                    label=tk.Label(window59, text=slowo19).pack()
                    label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                    en=tk.Entry(window59).pack()
                    if en==slowo19[7]:
                        dobsredtrud()
                    else:
                        zlesredtrud()
                if litera==9:
                    slowo19[8]=''
                    label=tk.Label(window59, text=slowo19).pack()
                    label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                    en=tk.Entry(window59).pack()
                    if en==slowo19[8]:
                        dobsredtrud()
                    else:
                        zlesredtrud()
                if litera==10:
                    slowo19[9]=''
                    label=tk.Label(window59, text=slowo19).pack()
                    label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                    en=tk.Entry(window59).pack()
                    if en==slowo19[9]:
                        dobsredtrud()
                    else:
                        zlesredtrud()
                if litera==11:
                    slowo19[10]=''
                    label=tk.Label(window59, text=slowo19).pack()
                    label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                    en=tk.Entry(window59).pack()
                    if en==slowo19[10]:
                        dobsredtrud()
                    else:
                        zlesredtrud()
                if litera==12:
                    slowo19[11]=''
                    label=tk.Label(window59, text=slowo19).pack()
                    label=tk.Label(window59, text=translate_text('wpisz litere')).pack()
                    en=tk.Entry(window59).pack()
                    if en==slowo19[11]:
                        dobsredtrud()
                    else:
                        zlesredtrud()
            window59.mainloop()
        if pyt==20:
            window60=tk.Tk()
            slowo201=translate2_text('flying')
            slowo20= list(slowo201.strip(" "))
            litera=random.randint(1, len(slowo20))
            if litera==1:
                slowo20[0]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[0]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==2:
                slowo20[1]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[1]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==3:
                slowo20[2]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[2]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==4:
                slowo20[3]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[3]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==5:
                slowo20[4]=''
            label=tk.Label(window60, text=slowo20).pack()
            label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
            en=tk.Entry(window60).pack()
            if en==slowo20[4]:
                dobsredtrud()
            else:
                zlesredtrud()
            if litera==6:
                slowo20[5]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[5]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==7:
                slowo20[6]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[6]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==8:
                slowo20[7]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[7]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==9:
                slowo20[8]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[8]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==10:
                slowo20[9]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[9]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==11:
                slowo20[10]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[10]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            if litera==12:
                slowo20[11]=''
                label=tk.Label(window60, text=slowo20).pack()
                label=tk.Label(window60, text=translate_text('wpisz litere')).pack()
                en=tk.Entry(window60).pack()
                if en==slowo20[11]:
                    dobsredtrud()
                else:
                    zlesredtrud()
            window60.mainloop()
        elif zycie >0 and pytania == 00:
            wyniksredtrud()
    

#trudny poziom trudność 
def trudny():
    global punkty, pytania
#################################################statystyki znaków średni czas na pytanie ile czasu na poziom w yniku##############################
    
    #wyświetla wynik w zależności od pozostałych życ
    def wyniktrud():
        window42=tk.Tk()
        window42.geometry = ()
        if punkty>=4 and punkty<=9:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()################################zamiast emoji cytat czy tekst
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)#######################################niemusisz zmieniać numerów okien
            label=tk.Label(window42, text='nienajgorzej', font=('Helvetica', 20)).pack()
        if punkty<=14 and punkty>=10:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='dobrze', font=('Helvetica', 20)).pack()
        if punkty<=19 and punkty >= 15:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='bardzo dobrze', font=('Helvetica', 20)).pack()
        if punkty==20:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='perfekcyjnie', font=('Helvetica', 20)).pack()
        if zycie==0 or punkty<=3:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='zaraza', font=('Helvetica', 20)).pack()
        window42.mainloop()

    #po złej odpowiedzi odejmuje życie i wraza do trudny
    def zletrud():
        global zycie
        zycie -= 1
        trudny()

    #po poprawnej odpowiedzi dodaje punkt i wraca do zredny
    def dobtrud():
        global punkty
        punkty+=1
        if zycie > 0 and pytania == 00:
            wyniktrud()
        elif zycie > 0:
             trudny()


    if pytania == []:
         wyniktrud()
    #dopuki jest jakie kolwiek życie można grac
    elif zycie >0:
        pyt = random.randint(1, 20) #losuje pytanie z listy pytań
        
        
        if pyt == 1: # pyt to pytanie losowane powyżej
            if pyt in pytania:  #jeżeli pytanie w liście pytań
                pytania.remove(pyt) #usuwa pytanie z listy pytań
                pyt=0
                window23=tk.Tk()
                window23.geometry('800x800')
                label=tk.Label(window23, text=translate2_text("knight"), font=('Helvetica', 20)).pack() #############################zamieniasz tom linijke na obrazek
                label=tk.Label(window23, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0) #punkty
                label=tk.Label(window23, text=punkty, font=('Helvetica', 16)).place(x=700, y=0) #liczba punktów#######################################################w odpowiedziach po translate i przed _ 2
                slowo1=tk.Entry(window23).pack()
                def sprawdz1():
                        if slowo1 == 'rycerz' or slowo1=='Rycerz' or slowo1=='RYCERZ':
                           zletrud()
                        else:
                          dobtrud()
                button=tk.Button(window23, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz1)
                button.pack()
                window23.mainloop()
            #jeżeli pytanie 1 niejest w liście pytan (bo jusz się pojawiło) to idzie do średnie i losuje kolejne pytanie
            elif pyt not in pytania:
                trudny()

    #=================================komentarze takie same do reszty pytań==========================================================

        elif pyt == 2:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                window24=tk.Tk()
                window24.geometry('800x800')
                label=tk.Label(window24, text=translate2_text("king"), font=('Helvetica', 20)).pack()
                label=tk.Label(window24, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window24, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                slowo2=tk.Entry(window24).pack()
                def sprawdz2():
                        if slowo2 == 'król' or slowo2 =='Król' or slowo2=='KRÓL':
                           zletrud()
                        else:
                          dobtrud()
                button=tk.Button(window24, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz2)
                button.pack()
                window24.mainloop()
            elif pyt not in pytania:
                trudny()


        elif pyt == 3:
            if pyt in pytania:
                pytania.remove(pyt)
                window25=tk.Tk()
                window25.geometry('800x800')
                label=tk.Label(window25, text=translate2_text("fire"), font=('Helvetica', 20)).pack()
                label=tk.Label(window25, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window25, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                slowo3=tk.Entry(window25).pack()
                def sprawdz3():
                        if slowo3 == 'ogień' or slowo3=='Ogień' or slowo3=='OGIEŃ':
                           zletrud()
                        else:
                          dobtrud()
                button=tk.Button(window25, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz3)
                button.pack()
                window25.mainloop()
            elif pyt not in pytania:
                trudny()


        elif pyt == 4:
            if pyt in pytania:
                pytania.remove(pyt)
                window26=tk.Tk()
                window26.geometry('800x800')
                label=tk.Label(window26, text=translate2_text("sleep"), font=('Helvetica', 20)).pack()
                label=tk.Label(window26, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window26, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                slowo4=tk.Entry(window26).pack()
                def sprawdz4():
                        if slowo4 == 'spać' or slowo4=='Spać' or slowo4=='SPAĆ':
                           zletrud()
                        else:
                          dobtrud()
                button=tk.Button(window26, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz4)
                button.pack()
                window26.mainloop()
            elif pyt not in pytania:
                trudny()


        elif pyt == 5:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                window27=tk.Tk()
                window27.geometry('800x800')
                text2=tk.StringVar()
                label=tk.Label(window27, text=translate2_text("alien"), font=('Helvetica', 20)).pack()
                label=tk.Label(window27, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window27, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                slowo5=tk.Entry(window27).pack()
                def sprawdz5():
                        if slowo5 == 'kosmita' or slowo5=='Kosmita' or slowo5=='KOSMITA':
                           zletrud()
                        else:
                          dobtrud()
                button=tk.Button(window27, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz5)
                button.pack()
                window27.mainloop()
            elif pyt not in pytania:
                trudny()


        elif pyt == 6:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                window28=tk.Tk()
                window28.geometry('800x800')
                text2=tk.StringVar()
                label=tk.Label(window28, text=translate2_text("skyscraper"), font=('Helvetica', 20)).pack()
                label=tk.Label(window28, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window28, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                slowo6=tk.Entry(window28).pack()
                def sprawdz6():
                        if slowo6 == 'jeż' or slowo6=='Jeż' or slowo6=='JEŻ':
                           zletrud()
                        else:
                          dobtrud()
                button=tk.Button(window28, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz6)
                button.pack()
                window28.mainloop()
            elif pyt not in pytania:
                trudny()


        elif pyt == 7:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window29=tk.Tk()
                    window29.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window29, text=translate2_text("hedgehog"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window29, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window29, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo7=tk.Entry(window29).pack()
                    def sprawdz7():
                        if slowo7 == 'wieżowiec' or slowo7=='Wieżowiec' or slowo7=='WIEŻOWIEC':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window29, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz7)
                    button.pack()
                    window29.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 8:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window30=tk.Tk()
                    window30.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window30, text=translate2_text("eat"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window30, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window30, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo8=tk.Entry(window30).pack()
                    def sprawdz8():
                        if slowo8 == 'jeść' or slowo8=='Jeść' or slowo8=='JEŚĆ':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window30, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz8)
                    button.pack()
                    window30.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 9:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window31=tk.Tk()
                    window31.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window31, text=translate2_text("rocket"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window31, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window31, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo9=tk.Entry(window31).pack()
                    def sprawdz9():
                        if slowo9 == 'rakieta' or slowo9=='Rakieta' or slowo9=='RAKIETA':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window31, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz9)
                    button.pack()
                    window31.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 10:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window32=tk.Tk()
                    window32.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window32, text=translate2_text("bed"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window32, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window32, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo10=tk.Entry(window32).pack()
                    def sprawdz10():
                        if slowo10 == 'łóżko' or slowo10=='Łóżko' or slowo10=='ŁÓŻKO':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window32, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz10)
                    button.pack()
                    window32.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 11:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window33=tk.Tk()
                    window33.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window33, text=translate2_text("sword"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window33, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window33, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo11=tk.Entry(window33).pack()
                    def sprawdz11():
                        if slowo11 == 'miecz' or slowo11=='Miecz' or slowo11=='MIECZ':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window33, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz11)
                    button.pack()
                    window33.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 12:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window34=tk.Tk()
                    window34.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window34, text=translate2_text("master"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window34, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window34, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo12=tk.Entry(window34).pack()
                    def sprawdz12():
                        if slowo12 == 'mistrz' or slowo12=='Mistrz' or slowo12=='MISTRZ':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window34, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz12)
                    button.pack()
                    window34.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 13:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window35=tk.Tk()
                    window35.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window35, text=translate2_text("game"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window35, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window35, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo13=tk.Entry(window35).pack()
                    def sprawdz13():
                        if slowo13 == 'gra' or slowo13=='Gra' or slowo13=='GRA':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window35, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz13)
                    button.pack()
                    window35.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 14:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window36=tk.Tk()
                    window36.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window36, text=translate2_text("airplane"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window36, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window36, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo14=tk.Entry(window36).pack()
                    def sprawdz14():
                        if slowo14 == 'samolot' or slowo14=='Samolot' or slowo14=='SAMOLOT':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window36, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz14)
                    button.pack()
                    window36.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 15:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window37=tk.Tk()
                    window37.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window37, text=translate2_text("rat"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window37, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window37, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo15=tk.Entry(window37).pack()
                    def sprawdz15():
                        if slowo15 == 'szczur' or slowo15=='Szczur' or slowo15=='SZCZUR':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window37, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz15)
                    button.pack()
                    window37.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 16:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window38=tk.Tk()
                    window38.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window38, text=translate2_text("crocodile"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window38, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window38, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo16=tk.Entry(window38).pack()
                    def sprawdz16():
                        if slowo16 == 'krokodyl' or slowo16=='Krokodyl' or slowo16=='KROKODYL':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window38, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz16)
                    button.pack()
                    window38.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 17:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window38=tk.Tk()
                    window38.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window38, text=translate2_text("train"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window38, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window38, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo17=tk.Entry(window38).pack()
                    def sprawdz17():
                        if slowo17 == 'pociąg' or slowo17=='Pociąg' or slowo17=='POCIĄG':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window38, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz17)
                    button.pack()
                    window38.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 18:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window39=tk.Tk()
                    window39.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window39, text=translate2_text("computer"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window39, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window39, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo18=tk.Entry(window39).pack()
                    def sprawdz18():
                        if slowo18 == 'komputer' or slowo18=='Komputer' or slowo18=='KOMPUTER':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window39, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz18)
                    button.pack()
                    window39.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 19:
                if pyt in pytania:
                    pytania.remove(pyt)
                    pyt=0
                    window40=tk.Tk()
                    window40.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window40, text=translate2_text("basketball"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window40, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window40, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo19=tk.Entry(window40).pack()
                    def sprawdz19():
                        if slowo19 == 'koszykówka' or 'KOSZYKÓWKA' or 'Koszykówka':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window40, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz19)
                    button.pack()
                    
                    window40.mainloop()
                elif pyt not in pytania:
                    trudny()


        elif pyt == 20:
                if pyt in pytania:

                    pytania.remove(pyt)
                    pyt=0
                    window41=tk.Tk()
                    window41.geometry('800x800')
                    text2=tk.StringVar()
                    label=tk.Label(window41, text=translate2_text("slave"), font=('Helvetica', 20)).pack()
                    label=tk.Label(window41, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                    label=tk.Label(window41, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                    slowo20=tk.Entry(window41).pack()
                    def sprawdz20():
                        if slowo20 == 'niewolnik' or slowo20=='NIEWOLNIK' or slowo20=='Niewolnik':
                           zletrud()
                        else:
                          dobtrud()
                    button=tk.Button(window41, text=translate_text('sprawdź'), font=('Helvetica', 16), command=sprawdz20)
                    button.pack()
                    
                    window41.mainloop()
                elif pyt not in pytania:
                    trudny()
        elif zycie >0 and pytania == 00:
             wyniktrud()
        # po ukończeniu wszystkich pytań powinno iść do wynik i wyświetlic wynik             
    elif zycie ==0 or zycie <0 and pytania == 00:
         wyniktrud()
    
 
# tłumaczenie jak wybierze się polski angielski
#translate2 to pytania    translate to odpowiedzi
def jenzpl():
    global translate_text, translate2_text
    def translate2_text(text, source_lang='en', target_lang='en'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    def translate_text(text, source_lang='pl', target_lang='pl'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    p_trud()

# tłumaczenie jak wybierze się polski niemiecki
#translate2 to pytania    translate to odpowiedzi
def jenzpl2():
    global translate_text, translate2_text
    def translate2_text(text, source_lang='en', target_lang='de'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    def translate_text(text, source_lang='pl', target_lang='pl'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    p_trud()

# tłumaczenie jak wybierze się angielsi polski
#translate2 to pytania    translate to odpowiedzi
def jenzen():
    global translate_text, translate2_text
    def translate2_text(text, source_lang='en', target_lang='pl'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text

    def translate_text(text, source_lang='pl', target_lang='en'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    p_trud()

# tłumaczenie jak wybierze się niemiecko polski
#translate2 to pytania    translate to odpowiedzi
def jenzde():
    global translate_text, translate2_text

    def translate2_text(text, source_lang='en', target_lang='pl'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    
    def translate_text(text, source_lang='pl', target_lang='de'): # pl polski  de niemiecki en angielski
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    p_trud()

#wybur poziomu trudności
def p_trud():
    window1 = tk.Tk()
    window1.geometry("800x800")
    
    label = tk.Label(window1, text=translate_text("wybierz poziom trudności"), font=('Helvetica', 20)).pack()
    button = tk.Button(window1, text=translate_text("łatwy"), font=('Helvetica', 16), command=latwy).place(x=360, y=100)
    button = tk.Button(window1, text=translate_text("średni"), font=('Helvetica', 16), command=sredny).place(x=356, y=150)
    button = tk.Button(window1, text=translate_text("średnio-trudny"), font=('Helvetica', 16), command=sredtrud).place(x=320, y=200)
    button = tk.Button(window1, text=translate_text("trudny"), font=('Helvetica', 16), command=trudny).place(x=357, y=250)
    window1.mainloop()

#wybur języka
def index():
    global translate_text
    window = tk.Tk()
    window.geometry("800x800")
    label = tk.Label(window, text="duolingo", font=('Helvetica', 20)).pack()
    label_lang = tk.Label(window, text="wybierz język \n choose your language \n sprache wählen", font=('Helvetica', 20)).place(x=260, y=90)

    button = tk.Button(window, text="polski-angielski", font=('Helvetica', 16), command=jenzpl).place(x=200, y=200)

    button = tk.Button(window,  text="english-polish", font=('Helvetica', 16), command=jenzen).place(x=450, y=200)

    button = tk.Button(window, text="polski-niemiecki", font=('Helvetica', 16), command=jenzpl2).place(x=195, y=300)

    button = tk.Button(window,  text="deustschland-polish", font=('Helvetica', 16), command=jenzde).place(x=445, y=300)
    window.mainloop()
index()