#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from pdb import set_trace as st
from tkinter import *
from functools import partial
import sys

# Main window
mw = Tk()
mw.title('fréquences <-> périodes')
mw.config(background='#1E90FF')
mw.geometry('480x300+100+30')
_GREEN = '#1E900D'
GREEN_LIGHT = '#B8FFAD'

def _quitUI():
    sys.exit()


def convertP2F(ui):
    """
    Conversion de la prériode en fréquence
    """
    periode = ui['periode']
    p_Unit = ui['p_Unit']
    freq = ui['freq']
    f_Unit = ui['f_Unit']
    fUnitSelects = ui['fUnitSelects']
    fFormat = '.6f'
    str_val = periode.get().replace(',', '.')
    val = float(str_val)
    unit = p_Unit.get()
    if unit == 'm':
        val = val / 1000
    if unit == 'u':
        val = val / 1000000
    if unit == 'n':
        val = val / 1000000000
    f = 1 / val
    fresult = StringVar()
    if f >= 1000000.0:
        fresult = format(f / 1000000, fFormat)
        fUnitSelects[2].select()
    elif f >= 1000.0:
        fresult = format(f / 1000, fFormat)
        fUnitSelects[1].select()
    else:
        fresult = format(f, fFormat)
        fUnitSelects[0].select()
    ui['freqPer'] = fresult
    freq.delete(0, 'end')
    freq.insert(0, fresult)

def convertF2P(ui):
    """
    Conversion de la fréquence en prériode
    """
    freq = ui['freq']
    f_Unit = ui['f_Unit']
    fUnitSelects = ui['fUnitSelects']
    pUnitSelects = ui['pUnitSelects']
    periode = ui['periode']
    fFormat = '.6f'
    str_val = freq.get().replace(',', '.')
    val = float(str_val)
    unit = f_Unit.get()

    if unit == 'MHz':
        val = val * 1000000
    if unit == 'KHz':
        val = val * 1000
    p = 1 / val
    if p >= 1:
        presult = format(p, fFormat)
        pUnitSelects[0].select()
    elif p >= .001:
        presult = format(p * 1000, fFormat)
        pUnitSelects[1].select()
    elif p >= .000001:
        presult = format(p * 1000000, fFormat)
        pUnitSelects[2].select()
    else:
        presult = format(p * 1000000000, fFormat)
        pUnitSelects[3].select()
    """
    if p <= .000000001:
        presult = format(p * 1000000000, fFormat)
        pUnitSelects[3].select()
    elif p <= .000001:
        presult = format(p * 1000000, fFormat)
        pUnitSelects[2].select()
    elif p >= 0.001:
        presult = format(p * 1000, fFormat)
        pUnitSelects[1].select()
    else:
        presult = format(p, fFormat)
        pUnitSelects[0].select()
    """
    periode.delete(0, 'end')
    periode.insert(0, presult)
    

def initP2F(ui):
    # ui : user interface, dictionary of interface components
    # Period Entry
    p = DoubleVar()
    p.set(654)
    lPeriod = Label(text="Période")
    lPeriod.grid(column=1, row=2, padx=5)
    # ---
    periode = Entry(mw, textvariable=p)
    periode.grid(column=2, row=2, padx=10)
    # periode.insert(0, str(65444))
    ui['periode'] = periode
    # ---
    pUnitsCell = Frame(mw, bg=GREEN_LIGHT)
    pUnitsCell.config(bg=GREEN_LIGHT)
    pUnitsCell.grid(row=2, column=3, pady=5)
    p_Units = ["secondes", "mili sec (ms)", "micro sec (us)", "nano sec (ns)"]
    p_UnitsV = ["s", "m", "u", "n"]
    pUnitSelects = []
    p_Unit = StringVar()
    i = 0
    for u in p_Units:
        pUnitSelect = Radiobutton(pUnitsCell,
                             variable=p_Unit,
                             text=p_Units[i],
                             value=p_UnitsV[i],
                             )
        pUnitSelect.grid(row=i, column=1, sticky="nsew")
        
        if i == 1:
            pUnitSelect.select()
        pUnitSelects.append(pUnitSelect)
        i += 1
    ui['pUnitSelects'] = pUnitSelects
    ui['p_Unit'] = p_Unit
    # computation
    p2f = Button(text="période -> frequence",
                     command=partial(convertP2F, ui),
                     background='black', fg='green')
    p2f.grid(column=1, row=3, pady=5, padx=3, columnspan=1)
    p2f.config(bg=GREEN_LIGHT, width=15)
    ui['p2f'] = p2f
    f2p = Button(text="frequence -> période",
                     command=partial(convertF2P, ui),
                     background='black', fg='black')
    f2p.grid(column=2, row=3, pady=5, padx=3, columnspan=1)
    f2p.config(bg=GREEN_LIGHT, width=15)
    ui['f2p'] = f2p

    # Frequency
    lFreq = Label(mw)
    lFreq.config(text='Fréquence')
    lFreq.grid(column=1, row=4, padx=5)
    freqPer = DoubleVar()
    freqPer.set(9999)
    freq = Entry(mw, textvariable=freqPer)
    freq.grid(column=2, row=4)
    ui['freqPer'] = freqPer
    ui['freq'] = freq
    fUnitsCell = Frame(mw, bg=GREEN_LIGHT)
    fUnitsCell.config(bg=GREEN_LIGHT)
    fUnitsCell.grid(row=4, column=3, pady=5)
    f_Units = ['Hz', 'KHz', 'MHz']
    ui['f_Units'] = f_Units
    f_Unit = StringVar()
    ui['f_Unit'] = f_Unit
    fUnitSelects = []
    i = 0
    for u in f_Units:
        fUnitSelect = Radiobutton(fUnitsCell,
                             variable=f_Unit,
                             text=u,
                             value=u,
                             )
        fUnitSelect.grid(row=i, column=1, sticky="nsew")
        fUnitSelects.append(fUnitSelect)
        i += 1
    fUnitSelects[1].select()
    ui['f_Unit'] = f_Unit
    ui['fUnitSelects'] = fUnitSelects
    quitUI = Button(mw, text='Quit', command=_quitUI)
    quitUI.grid(column=2, row=6)

def initUI(ui):
    initP2F(ui)


# Main
ui = {}
initUI(ui)
# print(ui.keys())
mw.mainloop() # Lancement de la boucle principale

