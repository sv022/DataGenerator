import tkinter as tk
from tkinter import IntVar
from tkinter import ttk
from random import *
import tkinter.filedialog as fd
from os import getcwd
from time import time
# colors and fonts 

roboto6 = ('roboto', '6')
roboto7 = ('roboto', '7')
roboto8 = ('roboto', '8')
roboto10 = ('roboto', '10')
roboto12 = ('roboto', '12')
roboto16 = ('roboto', '16')
roboto18 = ('roboto', '18')

colorsdict = {'gray' : '#e7edf9', 'green' : '#00c3a3', 'darkgreen' : '#004a46', 'lightgray' : '#8f8f9d', 'darkblue' : '#1e325a', 
              'lightblue' : '#63a8e4'}

d = getcwd() # current directory

def Dataselection(*args):
    global datatype, startlabel, mainpanel, miscpanel, filenameent, genbutton, cdirlabel
    
    # --- misc / main panel gui ---
    try:
        startlabel.destroy()
        mainpanel.destroy()
    except NameError:
        pass
    mainpanel = tk.Frame(main, height=460, width=620, background='white')
    genbutton = tk.Button(main, text='Создать', width=16, height=2, background=colorsdict['green'], activebackground=colorsdict['green'], 
                          bd=0, relief='flat', font=roboto16, foreground=colorsdict['darkgreen'], activeforeground=colorsdict['darkgreen'])
    #tk.Label(main, text='Создать', font=roboto12, foreground=colorsdict['darkgreen']).place(x=650, y=460)
    miscpanel = tk.Frame(main, background='white', height=430, width=200)
    miscpanel.place(x=640, y=15)
    tk.Frame(miscpanel, background=colorsdict['darkblue'], height=50, width=miscpanel['width']).place(x=0, y=0)
    tk.Label(miscpanel, text='Имя файла', background='white', font=roboto8).place(x=5, y=60)
    tk.Label(miscpanel, text='(без расширения)', background='white', font=roboto6).place(x=70, y=62)
    tk.Frame(miscpanel, background=colorsdict['lightgray'], width=154, height=19).place(x=14, y=84)
    filenameent = tk.Entry(miscpanel, width=25, borderwidth=0, relief='flat')
    tk.Frame(miscpanel, background=colorsdict['lightblue'], width=82, height=24).place(x=79, y=174)
    dirselect = tk.Button(miscpanel, text='Выбор папки', command=dirpick, relief='flat', activebackground='white', background='white', borderwidth=0)
    tk.Label(miscpanel, text='Текущая директория:', background='white', font=roboto8).place(x=5, y=120)
    cdirlabel = tk.Label(miscpanel, text=d, background='white', font=roboto8, foreground='gray')
    
    mainpanel.place(x=10, y=70)
    genbutton.place(x=641, y=460)
    filenameent.place(x=15, y=85)
    dirselect.place(x=80, y=175)
    cdirlabel.place(x=5, y=140)
    
    # --- ---

    dt = datatype.get()
    
    if dt == 'Набор чисел из N строк':
        Datatype1()
    elif dt == 'Строка из N символов':
        Datatype2()


def Datatype1():
    global mainpanel, miscpanel
    def create():
        t = time()
        if filenameent.get() == '':
            fname = 'data'
        else:
            fname = filenameent.get()
        f = open(f'{d}/{fname}.txt', 'w+')
        def err():
            errmsg = tk.Label(mipanel, text='Неправильный диапазон / значения!', background='white', font=roboto12, foreground='red')
            errmsg.place(x=310, y=170)
            errmsg.after(600, lambda: errmsg.destroy())
            f.close()
        def writelines(nums, ncheck):
            for x in uicontent:
                f.write(x.get() + '\n')
            if ncheck == 1:
                try:
                    n = int(uicontent[0].get())
                except:
                    n = list(map(int, uicontent[0].get().split()))[0]
            else:
                n = int(nentry.get())
            if len(nums) == 1:
                for _ in range(n):
                    f.write(f'{randint(nums[0][0], nums[0][1])}\n')
            elif len(nums) == 2:
                for _ in range(n):
                    f.write(f'{randint(nums[0][0], nums[0][1])} {randint(nums[1][0], nums[1][1])}\n')
            elif len(nums) == 3:
                for _ in range(n):
                    f.write(f'{randint(nums[0][0], nums[0][1])} {randint(nums[1][0], nums[1][1])} {randint(nums[2][0], nums[2][1])}\n')

        n = numsperline
        if varmerge.get() == 1:
            n = 1
        nums = []
        try:
            for e in rangeentrieslist:
                try:
                    rstart, rend = map(int, e.get().split())
                except ValueError:
                    rstart, rend = 1, int(e.get())
                nums.append((rstart, rend))
                if n == 1:
                    writelines(nums=nums * numsperline, ncheck=varent.get())
                    break
            else:
                writelines(nums=nums, ncheck=varent.get())
            done = tk.Label(miscpanel, text=f'Файл создан за {round(time() - t, ndigits=3) * 1000} ms', foreground='green', background='white', font=roboto10)
            done.place(x=30, y=miscpanel['height'] - 25)
            done.after(800, lambda: done.destroy())
        except Exception:
            err()
            

    def uniqueinput():
        global uicontent, numsperline, range1entry, mipanel, varent, varmerge, rangeentrieslist
        try:
            if uniquelines.get() == '':
                linescount = 0
            else:
                linescount = int(uniquelines.get())
            numsperline = int(linestrack.get())
            if linescount > 3 or not(numsperline in (1, 2, 3)):
                raise NameError
        except Exception:
            errmsg = tk.Label(mainpanel, text='Неправильное значение!', background='white', font=roboto8, foreground='red')
            errmsg.place(x=305, y=45)
            errmsg.after(600, lambda: errmsg.destroy())
            return 0
        
        # unique lines input panel
        uipanel = tk.Frame(mainpanel, height=100, width=620, background='white')
        uipanel.place(x=0, y=115)
        uicontent = [None] * linescount
        
        for i in range(linescount):
            tk.Frame(uipanel, background=colorsdict['lightgray'], height=19, width=304).place(x=94, y=i*30 + 2)
            tk.Label(uipanel, text=f'Строка {i + 1}', font=roboto12, background='white').place(x=5, y=i*30)
            uicontent[i] = tk.Entry(uipanel, width=50, relief='flat', borderwidth=0)
            uicontent[i].place(x=95, y=i*30 + 3)
        
        # misc input parameters
        mipanel = tk.Frame(mainpanel, height=240, width=620, background='white')
        mipanel.place(x=0, y=220)
        
        rangeentrieslist = [None] * numsperline
        pos1 = [(0, 0), (53, 83), (106, 136)]
        pos2 = [33, 80, 132]
        rangelbtext = ['Диапазон значений:', 'Диапазон значений 2 элемента:', 'Диапазон значений 3 элемента:']
        
        for i in range(numsperline):
            if i == 0:
                range1label = tk.Label(mipanel, text=rangelbtext[i], font=roboto12, background='white')
                range1label.place(x=5, y=5)
                tk.Label(mipanel, text='(левая граница, правая граница через пробел)', font=roboto6, background='white').place(x=390, y=33)
                tk.Frame(mipanel, background=colorsdict['lightgray'], height=19, width=304).place(x=79, y=pos2[i] - 1)
                rangeentry = tk.Entry(mipanel, width=50, relief='flat', borderwidth=0)
                rangeentrieslist[i] = rangeentry
                rangeentrieslist[i].place(x=80, y=pos2[i])
            else:
                tk.Frame(mipanel, background=colorsdict['lightgray'], height=19, width=304).place(x=79, y=pos2[i] - 1)
                tk.Label(mipanel, text=rangelbtext[i], font=roboto12, background='white').place(x=5, y=pos1[i][0])
                tk.Label(mipanel, text='(левая граница, правая граница через пробел)', font=roboto6, background='white').place(x=390, y=pos1[i][1])
                rangeentry = tk.Entry(mipanel, width=50, state='disabled', relief='flat', borderwidth=0)
                rangeentrieslist[i] = rangeentry
                rangeentrieslist[i].place(x=80, y=pos2[i])

        varent = IntVar()
        varent.set(1)
        varmerge = IntVar()
        varmerge.set(1)
        
        def show():
            global nentry, nlabel, nframe
            if varent.get() == 1:
                try:
                    nentry.destroy()
                    nlabel.destroy()
                    nframe.destroy()
                except:
                    pass
            else:
                nframe = tk.Frame(mipanel, background=colorsdict['lightgray'], height=19, width=124)
                nentry = tk.Entry(mipanel, relief='flat', borderwidth=0)
                nlabel = tk.Label(mipanel, text='Введите количество строк', font=roboto8, background='white')
                nframe.place(x=209, y=199)
                nentry.place(x=210, y=200)
                nlabel.place(x=15, y=200)
        
        def merge():
            if varmerge.get() == 1:
                try:
                    range1label['text'] = 'Диапазон значений:'
                    rangeentrieslist[1]['state'] = 'disabled'
                    rangeentrieslist[2]['state'] = 'disabled'
                except:
                    pass
            else:
                try:
                    range1label['text'] = 'Диапазон значений 1 элемента:'
                    rangeentrieslist[1]['state'] = 'normal'
                    rangeentrieslist[2]['state'] = 'normal'
                except:
                    pass
        
        entrycount = tk.Checkbutton(mipanel, text='Количество строк - первый элемент первой строки', font=roboto8, background='white',
                                    variable=varent, command=show, onvalue=1, offvalue=0)
        entrycount.place(x=10, y=175)
        mergerange = tk.Checkbutton(mipanel, text='Объединить диапазон', font=roboto8, background='white', 
                                    variable=varmerge, command=merge, onvalue=1, offvalue=0)
        mergerange.place(x=340, y=175)
    
    # specified datatype gui
    
    genbutton['command'] = create
    
    tk.Frame(mainpanel, background=colorsdict['lightgray'], width=66, height=21).place(x=299, y=7)
    uniquelines = tk.Entry(mainpanel, width=10, relief='flat')
    applybtn = tk.Button(mainpanel, height=1, width=10, text='сохранить', font=roboto8, command=uniqueinput, bd=0, activeforeground=colorsdict['darkgreen'],
                         background=colorsdict['green'], relief='flat', activebackground=colorsdict['green'], foreground=colorsdict['darkgreen'])
    linestrack = IntVar()
    one = tk.Radiobutton(mainpanel, text='одно число', variable=linestrack, value=1, background='white', font=roboto8)
    two = tk.Radiobutton(mainpanel, text='пары чисел', variable=linestrack, value=2, background='white', font=roboto8)
    three = tk.Radiobutton(mainpanel, text='тройки чисел', variable=linestrack, value=3, background='white', font=roboto8)
    
    # --- specified datatype gui placing ---
    
    tk.Label(mainpanel, text='(не более 3)', font=roboto8, background='white').place(x=400, y=8)
    tk.Label(mainpanel, text='Количество уникальных строк', font=roboto12, background='white').place(x=15, y=5)
    applybtn.place(x=500, y=30)
    uniquelines.place(x=300, y=8)
    one.place(x=10, y=30)
    two.place(x=10, y=55)
    three.place(x=10, y=80)
    
    
def Datatype2():
    
    def create():
        def err():
            errmsg = tk.Label(mainpanel, text='Неправильные значения!', background='white', font=roboto12, foreground='red')
            errmsg.place(x=mainpanel['width'] - 220, y=mainpanel['height'] - 50)
            errmsg.after(600, lambda: errmsg.destroy())
            f.close()
        
        t = time()
        if filenameent.get() == '':
            fname = 'data'
        else:
            fname = filenameent.get()
        f = open(f'{d}/{fname}.txt', 'w+')
        alplist = []
        for code, v in alpvars.items():
            if v.get() == 1:
                if code == 'CS':
                    alplist += [x for x in custominputentry.get()]
                else:
                    alplist += alp[code]
        alpclean = alplist
        insertions = []
        inslen = 0
        if insertioncheck.get() == 1:
            try:
                insertions = [x for x in insertionentry.get().split() if x != '']
                alplist += insertions
                inslen = sum(len(x) for x in insertions)
            except Exception:
                insertions = list(insertionentry.get().strip())
                alplist += insertions
                inslen = len(insertions)
        if lengthentry.get() == '':
            n = randint(10, 50)
        else:
            try:
                n = int(lengthentry.get())
            except Exception:
                err()
                return 0
        res = insertions
        try:
            m = len(max(insertions))
        except:
            m = 0
        for i in range(n - inslen):
            try:
                if (n - inslen) - i >= m:
                    res.append(choice(alplist))
                else:
                    res.append(choice(alpclean))
            except:
                err()
                return 0
        shuffle(res)
        f.write(''.join(res))
        f.close()
        done = tk.Label(miscpanel, text=f'Файл создан за {round(time() - t, ndigits=3) * 1000} ms', foreground='green', background='white', font=roboto10)
        done.place(x=30, y=miscpanel['height'] - 25)
        done.after(800, lambda: done.destroy())
        
    
    def showunique():
        global custominputentry, custominputlabel, uframe
        if alpvars['CS'].get() == 1:
            uframe = tk.Frame(mainpanel, background=colorsdict['lightgray'], width=364, height=19)
            custominputlabel = tk.Label(mainpanel, text='(введите символы без пробелов)', background='white', font=roboto6)
            custominputentry = tk.Entry(mainpanel, width=60, relief='flat', borderwidth=0)
            uframe.place(x=39, y=174)
            custominputlabel.place(x=420, y=174)
            custominputentry.place(x=40, y=175)
        else:
            uframe.destroy()
            custominputlabel.destroy()
            custominputentry.destroy()
            
    
    def showinsertion():
        global insertionentry, insertionentrylabel, insframe
        if insertioncheck.get() == 1:
            insframe = tk.Frame(mainpanel, background=colorsdict['lightgray'], width=334, height=19)
            insertionentrylabel = tk.Label(mainpanel, text='(введите подстроки через пробел)', background='white', font=roboto6)
            insertionentry = tk.Entry(mainpanel, width=55, borderwidth=0, relief='flat')
            insframe.place(x=39, y=269)
            insertionentrylabel.place(x=415, y=269)
            insertionentry.place(x=40, y=270)
        else:
            insframe.destroy()
            insertionentry.destroy()
            insertionentrylabel.destroy()
    
    genbutton['command'] = create    
    
    tk.Label(mainpanel, text='Алфавит строки', font=roboto12, background='white').place(x=25, y=5)
    
    # variables
    codenames = ('LU', 'LL', 'CU', 'CL', 'N', 'CS')
    
    alp = {'LU' : [x for x in'ABCDEFGHIJKLMNOPQRSTUVWXYZ'], 'LL': [x for x in 'abcdefghijklmnopqrstuvwxyz'],
           'CU': [x for x in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'], 'CL': [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'],
           'N': [x for x in '0123456789']}
    
    alpvars = {}
    for x in codenames:
        alpvars[x] = IntVar()
        alpvars[x].set(0)
    # alplabet checkbuttons
    
    latinuppercb = tk.Checkbutton(mainpanel, text='Латинский алфавит, заглавные буквы (A-Z)', font=roboto10, background='white', 
                                  activebackground='white', onvalue=1, offvalue=0, variable=alpvars['LU'])
    latinlowercb = tk.Checkbutton(mainpanel, text='Латинский алфавит, строчные буквы (a-z)', font=roboto10, background='white', 
                                  activebackground='white', onvalue=1, offvalue=0, variable=alpvars['LL'])
    numberscb = tk.Checkbutton(mainpanel, text='Десятичные цифры (0-9)', font=roboto10, background='white', 
                               activebackground='white', onvalue=1, offvalue=0, variable=alpvars['N'])
    russianuppercb = tk.Checkbutton(mainpanel, text='Кириллица, заглавные буквы (А-Я)', font=roboto10, background='white', 
                               activebackground='white', onvalue=1, offvalue=0, variable=alpvars['CU'])
    russianlowercb = tk.Checkbutton(mainpanel, text='Кириллица, строчные буквы (а-я)', font=roboto10, background='white', 
                               activebackground='white', onvalue=1, offvalue=0, variable=alpvars['CL'])
    customcb = tk.Checkbutton(mainpanel, text='Уникальный алфавит', font=roboto10, background='white', 
                              activebackground='white', onvalue=1, offvalue=0, variable=alpvars['CS'], command=showunique)
    
    # checkbuttons placement
    
    latinuppercb.place(x=20, y=35)
    latinlowercb.place(x=20, y=58)
    numberscb.place(x=20, y=127)
    russianuppercb.place(x=20, y=81)
    russianlowercb.place(x=20, y=104)
    customcb.place(x=20, y=150)
    
    # custom insertions
    insertioncheck = IntVar()
    insertioncheck.set(0)
    insertioncheckcb = tk.Checkbutton(mainpanel, text='Дополнительно включать указанные подстроки', background='white', font=roboto8, 
                                      activebackground='white', offvalue=0, onvalue=1, variable=insertioncheck, command=showinsertion)
    
    insertioncheckcb.place(x=15, y=240)
    
    tk.Label(mainpanel, text='Длина строки', font=roboto12, background='white').place(x=25, y=320)
    tk.Label(mainpanel, text='(оставьте пустым, чтобы использовать случайное значение от 10 до 50)', background='white', font=roboto6).place(x=190, y=349)
    tk.Frame(mainpanel, background=colorsdict['lightgray'], width=124, height=19).place(x=39, y=349)
    lengthentry = tk.Entry(mainpanel, width=20, relief='flat', borderwidth=0)
    lengthentry.place(x=40, y=350)

def dirpick():
    global d
    dt = fd.askdirectory(title='Выбор папки', initialdir=d)
    if dt: d = dt
    cdirlabel['text'] = d
    cdirlabel['font'] = roboto8
    if len(d) > 35:
        cdirlabel['font'] = roboto7
    if len(d) > 45:
        cdirlabel['font'] = roboto6
    


main = tk.Tk()

datatypelb = tk.Label(main, text='Тип данных', font=roboto16, background='#e7edf9')
datatype = ttk.Combobox(main, state='readonly', values=['Набор чисел из N строк', 'Строка из N символов'], width=50)
datatype.bind("<<ComboboxSelected>>", Dataselection)
startlabel = tk.Label(text='Выберите тип данных, чтобы начать работу', background='#e7edf9', font=roboto18)


datatypelb.place(y=25, x=30)
datatype.place(x=175, y=30)
startlabel.place(x=200, y=230)


main.title('EGE Data Generator')
main.geometry('850x550+300+200')
main.configure(background=colorsdict['gray'])
main.resizable(False, False)
main.config()

main.mainloop()

#pyinstaller -F -w -i "D:\.11Main\bin\vscode\datagenerator\icon.ico" DataGenerator.py