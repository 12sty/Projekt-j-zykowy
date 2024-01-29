import tkinter as tk
from googletrans import Translator
import random
################################################################### po ukończeniu 19 pytań jest bład ########################################################################################################

#numery pytań
pytania = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#punkty nic nierobią ale muszą być żeby było zgodnie z zadaniem
punkty=0

#zycia ilość możliwych błędów jak zero to koniec na ich podstawie wyświetla wynik
zycie=4
okna = []
#średni poziom trudność 
def sredny():
    global punkty

        
    def usun():
        global okna
        x = window23 and window24
        if x in okna:
            x.destroy()
        

    #po złej odpowiedzi odejmuje życie i wraza do sredny
    def zlesred():
        global zycie
        zycie -= 1
        sredny()

    #po poprawnej odpowiedzi dodaje punkt i wraca do zredny
    def dobsred():
        global punkty
        punkty+=1
        sredny()

    #dopuki jest jakie kolwiek życie można grac
    while zycie > 0:
        pyt = random.randint(1, 2) #losuje pytanie z listy pytań
        if pyt == 1: # pyt to pytanie losowane powyżej
            if pyt in pytania:  #jeżeli pytanie w liście pytań
                pytania.remove(pyt) #usuwa pytanie z listy pytań
                pyt=0
                usun()
                window23=tk.Tk()
                okna.append(window23)
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
            else:
                sredny()

    #=================================komentarze takie same do reszty pytań==========================================================

        elif pyt == 2:
            if pyt in pytania:
                pytania.remove(pyt)
                pyt=0
                usun()
                window24=tk.Tk()
                okna.append(window24)
                window24.geometry('800x800')
                label=tk.Label(window24, text=translate2_text("bed"), font=('Helvetica', 20)).pack()
                label=tk.Label(window24, text=translate_text("punkty: "), font=('Helvetica', 16)).place(x=600, y=0)
                label=tk.Label(window24, text=punkty, font=('Helvetica', 16)).place(x=700, y=0)
                button=tk.Button(window24, text=translate_text('sofa'), font=('Helvetica', 16), command=zlesred).place(x=230, y=130)
                button=tk.Button(window24, text=translate_text("łóżko"), font=('Helvetica', 16), command=dobsred).place(x=470, y=130)
                button=tk.Button(window24, text=translate_text('fotel'), font=('Helvetica', 16), command=zlesred).place(x=230, y=230)
                button=tk.Button(window24, text=translate_text("szafa"), font=('Helvetica', 16), command=zlesred).place(x=470, y=230)
                window24.mainloop()
            else:
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
            else:
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
            else:
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
            else:
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
            else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
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
                else:
                    sredny()

        # po ukończeniu wszystkich pytań powinno iść do wynik i wyświetlic wynik             
        else:
             wynik()
    
    #wyświetla wynik w zależności od pozostałych życ
    def wynik():
        window42=tk.Tk()
        if zycie==1:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='😒', font=('Helvetica', 20)).pack()
        if zycie==2:
            label=tk.Label(window42, text=translate_text('punkty:'), font=('Helvetica', 16)).pack()
            label=tk.Label(window42, text=punkty, font=('Helvetica', 16)).place(x=100, y=0)
            label=tk.Label(window42, text='😊', font=('Helvetica', 20)).pack()
        if zycie==4:
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
    button = tk.Button(window1, text=translate_text("łatwy"), font=('Helvetica', 16)).place(x=360, y=100)
    button = tk.Button(window1, text=translate_text("średni"), font=('Helvetica', 16), command=sredny).place(x=356, y=150)
    button = tk.Button(window1, text=translate_text("średnio-trudny"), font=('Helvetica', 16)).place(x=320, y=200)
    button = tk.Button(window1, text=translate_text("trudny"), font=('Helvetica', 16)).place(x=357, y=250)
    window1.mainloop()

#wybur języka
def index():
    global translate_text
    window = tk.Tk()
    window.geometry("800x800")
    label = tk.Label(window, text="dudolungo", font=('Helvetica', 20)).pack()
    label_lang = tk.Label(window, text="wybierz język \n choose your language \n sprache wählen", font=('Helvetica', 20)).place(x=260, y=90)

    button = tk.Button(window, text="polski-angielski", font=('Helvetica', 16), command=jenzpl).place(x=200, y=200)

    button = tk.Button(window,  text="english-polish", font=('Helvetica', 16), command=jenzen).place(x=450, y=200)

    button = tk.Button(window, text="polski-niemiecki", font=('Helvetica', 16), command=jenzpl2).place(x=195, y=300)

    button = tk.Button(window,  text="deustschland-polish", font=('Helvetica', 16), command=jenzde).place(x=445, y=300)
    window.mainloop()
index()