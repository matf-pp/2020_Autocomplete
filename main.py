import sys
from sys import exit
from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter.messagebox import askyesno
import tkinter.font as font

import numpy as np



def lexicographic_sort(lista):
    lista.sort(key=lambda x:x[0])
    return lista

def weight_sort(lista):
    lista.sort(key=lambda x:x[1],reverse=True)
    return lista

def sort_first_r(lista,r):
    lista.sort(key=lambda x:x[0][0:r])

def binarna_pretraga(uzorak,lista):
    l=0
    r=len(lista)-1
    while l<=r:
        m=(r-l)/2+l
        m=int(m)
        if lista[m][0][0:len(uzorak)]==uzorak:
            return lista[m]
        elif lista[m][0][0:len(uzorak)]<uzorak:
            l=m+1
        elif lista[m][0][0:len(uzorak)]>uzorak:
            r=m-1
    return -1

def rastojanje(A,B):
    n = len(A)
    m = len(B)
    matrix = np.zeros((n + 1, m + 1))
    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = matrix[i - 1][j] + 1
            y = matrix[i][j - 1] + 1
            if A[i - 1] == B[j - 1]:
                z = matrix[i - 1][j - 1]
            else:
                z = matrix[i - 1][j - 1] + 1
            matrix[i][j] = min(x, y, z)
    return int(matrix[n][m])

print("Izaberite datoteku: [ 1 za wiktionary / 2 za cities]")
unos =input()
if unos=='1':
    try:
        f=open('wiktionary.txt',encoding="utf-8")
    except(IOError):
        exit('Neuspesno otvaranje datoteke')

if unos=='2':
    try:
        f=open('cities.txt',encoding="utf-8")
    except(IOError):
        exit('Neuspesno otvaranje datoteke')
print('Unesite broj rezultata za prikaz:')
br=int(input())
lista=[]
try:
    for linija in f:
        text=linija.split()
        if len(text)<2:
            continue
        text[0]=int(text[0])
        if len(text)>2:
            for i in range(2,len(text)):
                text[1]+=" "+text[i]
        torka=(text[1],text[0])
        lista.append(torka)
except(IndexError):
    pass






root=Tk()

root.title("Autocomplete me")
root.geometry("940x370")

style=ttk.Style()
style.configure("TButton", padding=6, relief="flat",font=('Helvetica', 12))

photo=PhotoImage(file="novaslika.png")
label=Label(root,image=photo)
label.place(x=260,y=15)

style.configure('TEntry', padding=6, relief="flat",font=('Courier', 15))

photo=PhotoImage(file="novaslika.png")
label=Label(root,image=photo)
label.place(x=350,y=15)
mojFont=font.Font(family='Courier',size=13)

l1=Label(root,text="Search query:",bg="white",fg="black")
l1['font']=mojFont
l1.place(x=35,y=120)
sv=StringVar()
def Klik():
    webbrowser.open("www.google.com/search?q="+te.get())

b=ttk.Button( text='Search Google',command=Klik)
b.place(x=783,y=110)

def callback(sv,lista,br):
    a=sv.get().strip()
    l = Listbox(root, width=73, font=('courier', 10))
    l.place(x=190, y=153)
    if a=="":
        l.insert(END,"")
        return None
    if unos=='2':
        if len(a)>0:
            veliko_slovo=a[0].upper()
            a=veliko_slovo+a[1:]
    pom_lista = lista[:]
    bin_lista = []
    sort_first_r(pom_lista,len(a))
    x = binarna_pretraga(a, pom_lista)
    while x != -1:
        bin_lista.append(x)
        pom_lista.remove(x)
        x = binarna_pretraga(a, pom_lista)
    i = 0
    if not bin_lista:
        if unos=='1':
            a=a.lower()
            x = binarna_pretraga(a, pom_lista)
            while x != -1:
                bin_lista.append(x)
                pom_lista.remove(x)
                x = binarna_pretraga(a, pom_lista)
            i = 0


    if not bin_lista:
        for el in pom_lista:
            if rastojanje(te.get(),el[0])==1 and len(te.get())==len(el[0]):
                 bin_lista.append(el)


    weight_sort(bin_lista)
    if len(bin_lista) == 0 or len(a) == 0:
            l.delete(0, END)
    else:
        for list in bin_lista:
            if i == br:
                break
            if var1.get()==1:
                tmp1=list[0].strip()
                tmp2=str(list[1]).strip()
                l.insert(END,f'{" "+tmp1:<{55}} {tmp2:>{15}}')
            else:
                l.insert(END,list[0])
            i += 1

    def CurSelet(evt):
        try:
            value = str((l.get(l.curselection())))
            pom = ""
            for c in value:
                if not c.isdecimal():
                    pom += c
            sv.set(pom)
        except(TclError):
            pass

    l.bind('<<ListboxSelect>>', CurSelet)

lexicographic_sort(lista)
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv,lista,br))
te = ttk.Entry(textvariable=sv, width=71,font = ('courier', 10))
te.place(x=190,y=115)
var1=IntVar()
c=Checkbutton(root, text="Show weights", variable=var1)
c['font']=mojFont
c.place(x=20,y=160)
root.mainloop()
