from tkinter import *
import numpy as np
from matplotlib.figure import Figure
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from pandastable import Table, TableModel
import pygame
import mysql.connector as c

con = c.connect(host = "localhost", user = "root", passwd = "Aditya2003$", database = "seriesstatistics")
cursor = con.cursor()
query = "select * from data"
cursor.execute(query)
data = cursor.fetchall()

countA, countB = 0, 0
for stat in data:
    if 'Team A' in stat:
        countA += 1
    elif 'Team B' in stat:
        countB += 1

pygame.mixer.init()
pygame.mixer.music.load("Ipl Scorecard Bgm.mp3")
pygame.mixer.music.play(loops=2)
root = Tk()
root.geometry("1400x814")
title = Label(root, text="Cricket Data Analyser", font=('times new roman', 20, 'bold'), pady=2, bd=12, bg="#00B2EE", fg="Black", relief = GROOVE)
title.pack(fill = X)
bg_color = "#00B2EE"

def Gen_Line_graph():
    fig = Figure(figsize=(6, 6), dpi = 98)
    plot1 = fig.add_subplot(111)


    overNo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    teamA_runs = [tAOver1.get(), tAOver2.get(), tAOver3.get(), tAOver4.get(), tAOver5.get(), tAOver6.get(), tAOver7.get(), tAOver8.get(), tAOver9.get(), tAOver10.get()]
    teamB_runs = [tBOver1.get(), tBOver2.get(), tBOver3.get(), tBOver4.get(), tBOver5.get(), tBOver6.get(), tBOver7.get(), tBOver8.get(), tBOver9.get(), tBOver10.get()]


    teamA_runs_upto_this_point = []
    teamB_runs_upto_this_point = []

    for i in range(len(teamA_runs)):
        sum = 0
        for j in range(i + 1):
            sum += teamA_runs[j]
        teamA_runs_upto_this_point.append(sum)

    for i in range(len(teamB_runs)):
        sum = 0
        for j in range(i + 1):
            sum += teamB_runs[j]
        teamB_runs_upto_this_point.append(sum)

    plot1.plot(overNo, teamA_runs_upto_this_point, label='Team A', marker='o', markerfacecolor='green')
    plot1.plot(overNo, teamB_runs_upto_this_point, label='Team B', marker='o', markerfacecolor='green')
    plot1.set_title('Innings Progression')
    plot1.legend()

    canvas1 = FigureCanvasTkAgg(fig, master=canvas)
    canvas1.draw()
    canvas1.get_tk_widget().pack(padx = 2, pady = 2)
    #toolbar = NavigationToolbar2Tk(canvas1, root)
    #toolbar.update()
    canvas1.get_tk_widget().pack(side = TOP, fill = BOTH)

def Gen_Bar_graph():
    fig = Figure(figsize=(6, 6), dpi=100)
    plot2 = fig.add_subplot(111)

    plot2.set_ylabel("Runs")

    X = ['Over1', 'Over2', 'Over3', 'Over4', 'Over5', 'Over6', 'Over7', 'Over8', 'Over9', 'Over10']
    Team_A = [tAOver1.get(), tAOver2.get(), tAOver3.get(), tAOver4.get(), tAOver5.get(), tAOver6.get(), tAOver7.get(), tAOver8.get(), tAOver9.get(), tAOver10.get()]
    Team_B = [tBOver1.get(), tBOver2.get(), tBOver3.get(), tBOver4.get(), tBOver5.get(), tBOver6.get(), tBOver7.get(), tBOver8.get(), tBOver9.get(), tBOver10.get()]

    X_axis = np.arange(len(X))
    rects1 = plot2.bar(X_axis - 0.2 , Team_A, 0.4, label='Team A')
    rects2 = plot2.bar(X_axis + 0.2, Team_B, 0.4, label='Team B')
    plot2.set_xticks(X_axis, X)
    plot2.bar_label(rects1, padding=3)
    plot2.bar_label(rects2, padding=3)
    plot2.set_title('Runs per over comparision')
    plot2.legend()

    canvas1 = FigureCanvasTkAgg(fig, master=canvasNew)
    canvas1.draw()
    canvas1.get_tk_widget().pack(padx=2, pady=2)
    #toolbar = NavigationToolbar2Tk(canvas1, root)
    #toolbar.update()
    canvas1.get_tk_widget().pack(side=TOP, fill=BOTH)

def get_Pie_Chart_A():
    fig = Figure(figsize=(6, 6), dpi=100)
    plot3 = fig.add_subplot(111)

    y = np.array([tAOver1.get() + tAOver2.get() + tAOver3.get(), tAOver4.get() + tAOver5.get() + tAOver6.get() + tAOver7.get(), tAOver8.get() + tAOver9.get() + tAOver10.get()])
    mylabels = ["Power\nPlay", "Middle", "Death"]

    plot3.pie(y, labels=mylabels,startangle = 90, autopct='%.1f%%',
       wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'})
    plot3.set_title('Phase Wise Runs')


    canvas2 = FigureCanvasTkAgg(fig, master=canvasPieA)
    canvas2.draw()
    canvas2.get_tk_widget().pack(padx=2, pady=2)
    #toolbar = NavigationToolbar2Tk(canvas2, root)
    #toolbar.update()
    canvas2.get_tk_widget().pack(side=TOP, fill=BOTH)

def get_Pie_Chart_B():
    fig = Figure(figsize=(6, 6), dpi=100)
    plot4 = fig.add_subplot(111)

    y = np.array(
        [tBOver1.get() + tBOver2.get() + tBOver3.get(), tBOver4.get() + tBOver5.get() + tBOver6.get() + tBOver7.get(),
         tBOver8.get() + tBOver9.get() + tBOver10.get()])
    mylabels = ["Power\nPlay", "Middle", "Death"]

    plot4.pie(y, labels=mylabels, startangle=90, autopct='%.1f%%',
              wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'})
    plot4.set_title('Phase Wise Runs')

    canvas2 = FigureCanvasTkAgg(fig, master=canvasPieB)
    canvas2.draw()
    canvas2.get_tk_widget().pack(padx=2, pady=2)
    #toolbar = NavigationToolbar2Tk(canvas2, root)
    #toolbar.update()
    canvas2.get_tk_widget().pack(side=TOP, fill=BOTH)

def getResult():
    try:
        tAdata = [tAOver1.get(), tAOver2.get(), tAOver3.get(), tAOver4.get(), tAOver5.get(), tAOver6.get(), tAOver7.get(),
                  tAOver8.get(), tAOver9.get(), tAOver10.get()]
        tATotal.set(sum(tAdata))
        tBdata = [tBOver1.get(), tBOver2.get(), tBOver3.get(), tBOver4.get(), tBOver5.get(), tBOver6.get(), tBOver7.get(),
                  tBOver8.get(), tBOver9.get(), tBOver10.get()]
        tBTotal.set(sum(tBdata))
        if sum(tAdata) > sum(tBdata):
            winner.set("Team A");
        elif sum(tBdata) > sum(tAdata):
            winner.set("Team B");
        else:
            winner.set("Tie")
        w = winner.get()
        a = tATotal.get()
        b = tBTotal.get()

        global cursor
        global data
        query = "Insert into data values ('{}', {}, {})".format(w, a, b)
        cursor.execute(query)
        con.commit()

        cursor = con.cursor()
        query = "select * from data"
        cursor.execute(query)
        data = cursor.fetchall()

        countA, countB = 0, 0
        for stat in data:
            if 'Team A' in stat:
                countA += 1
            elif 'Team B' in stat:
                countB += 1
        SA1_lbl['text'] = countA
        SB1_lbl['text'] = countB
    except:
        winner.set("Invalid Input")
        tAOver1.set(0), tAOver2.set(0), tAOver3.set(0), tAOver4.set(0), tAOver5.set(0), tAOver6.set(0), tAOver7.set(0),
        tAOver8.set(0), tAOver9.set(0), tAOver10.set(0)
        tBOver1.set(0), tBOver2.set(0), tBOver3.set(0), tBOver4.set(0), tBOver5.set(0), tBOver6.set(0), tBOver7.set(0),
        tBOver8.set(0), tBOver9.set(0), tBOver10.set(0)

def clear():
    cursor = con.cursor()
    query = "TRUNCATE TABLE data"
    cursor.execute(query)
    con.commit()
    SA1_lbl['text'] = 0
    SB1_lbl['text'] = 0

F2 = LabelFrame(root, text="Runs Scored Per Over", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F2.place(x=0, y=54, width=380, height=380)

tAOver1 = IntVar()
tAOver2 = IntVar()
tAOver3 = IntVar()
tAOver4 = IntVar()
tAOver5 = IntVar()
tAOver6 = IntVar()
tAOver7 = IntVar()
tAOver8 = IntVar()
tAOver9 = IntVar()
tAOver10 = IntVar()

lst = [tAOver1, tAOver2, tAOver3, tAOver4, tAOver5]
lst1 = [tAOver6, tAOver7, tAOver8, tAOver9, tAOver10]

r = 0
lbl = Label(F2, text="Over\nNo", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
lbl.grid(row=r, column=0, padx=0, pady=10, sticky='W')
lbl = Label(F2, text="Team\nA", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
lbl.grid(row=r, column=1, padx=0, pady=10, sticky='W')
lbl = Label(F2, text="Team\nB", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
lbl.grid(row=r, column=2, padx=0, pady=10, sticky='W')
lbl = Label(F2, text="Over\nNo", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
lbl.grid(row=r, column=3, padx=0, pady=10, sticky='W')
lbl = Label(F2, text="Team\nA", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
lbl.grid(row=r, column=4, padx=0, pady=10, sticky='W')
lbl = Label(F2, text="Team\nB", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
lbl.grid(row=r, column=5, padx=0, pady=10, sticky='W')


for over in lst:
    r += 1
    lbl = Label(F2, text=str(r), font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
    lbl.grid(row=r, column=0, padx=10, pady=10, sticky='W')
    txt = Entry(F2, width=3, textvariable=over, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
    txt.grid(row=r, column=1, padx=10, pady=10)
    lbl = Label(F2, text=str(r + 5), font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
    lbl.grid(row=r, column=3, padx=10, pady=10, sticky='W')
    txt = Entry(F2, width=3, textvariable=lst1[r - 1], font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
    txt.grid(row=r, column=4, padx=10, pady=10)

tBOver1 = IntVar()
tBOver2 = IntVar()
tBOver3 = IntVar()
tBOver4 = IntVar()
tBOver5 = IntVar()
tBOver6 = IntVar()
tBOver7 = IntVar()
tBOver8 = IntVar()
tBOver9 = IntVar()
tBOver10 = IntVar()

lst = [tBOver1, tBOver2, tBOver3, tBOver4, tBOver5]
lst1 = [tBOver6, tBOver7, tBOver8, tBOver9, tBOver10]
r = 0

for over in lst:
    r += 1
    txt = Entry(F2, width=3, textvariable=over, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
    txt.grid(row=r, column=2, padx=10, pady=10)
    txt = Entry(F2, width=3, textvariable=lst1[r - 1], font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
    txt.grid(row=r, column=5, padx=10, pady=10)

F3 = LabelFrame(root, text="Double Line Graph", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F3.place(x=751, y=54, width=612, height=322)
canvas = Canvas(master=F3, width = 600, height = 300)
canvas.pack()

F5 = LabelFrame(root, text="Buttons", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F5.place(x=381, y=54, width=170, height=380)
B1 = Button(F5, text = "Generate Double Line Graph", command = Gen_Line_graph)
B1.grid(row = 0, column = 0, padx = 5, pady = 5)
B2 = Button(F5, text = "Generate Bar Graph", command = Gen_Bar_graph)
B2.grid(row = 1, column = 0, padx = 5, pady = 5)
B5 = Button(F5, text = "Get Winner", command = getResult)
B5.grid(row = 2, column = 0, padx = 5, pady = 5)
B6 = Button(F5, text = "Pie Chart A", command = get_Pie_Chart_A)
B6.grid(row = 3, column = 0, padx = 5, pady = 5)
B7 = Button(F5, text = "Pie Chart B", command = get_Pie_Chart_B)
B7.grid(row = 4, column = 0, padx = 5, pady = 5)
B8 = Button(F5, text = "Clear Series Data", command = clear)
B8.grid(row = 5, column = 0, padx = 5, pady = 5)


F6 = LabelFrame(root, text="Series Statistics", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F6.place(x=451, y=435, width=300, height=300)
F10 = LabelFrame(F6, fg="Black", bg="#00B2EE")
F10.place(x=0, y=0, width=140, height=300)
F11 = LabelFrame(F6, fg="Black", bg="#00B2EE")
F11.place(x=141, y=0, width=140, height=300)

SA_lbl = Label(F10, text="Team A", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
SA_lbl.grid(row=0, column=0, padx=40, pady=30, sticky='W')
SB_lbl = Label(F11, text="Team B", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
SB_lbl.grid(row=0, column=0, padx=40, pady=30, sticky='W')
SA1_lbl = Label(F10, text=countA, font=('times new roman', 50, 'bold'), bg="#00B2EE", fg="black")
SA1_lbl.grid(row=1, column=0, padx=50, pady=10, sticky='W')
SB1_lbl = Label(F11, text=countB, font=('times new roman', 50, 'bold'), bg="#00B2EE", fg="black")
SB1_lbl.grid(row=1, column=0, padx=50, pady=10, sticky='W')


F7 = LabelFrame(root, text="Results", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F7.place(x=551, y=54, width=200, height=380)

tATotal = StringVar()
tBTotal = StringVar()


RO1_lbl = Label(F7, text="Team A", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
RO1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
R01_txt = Label(F7, width=10, textvariable=tATotal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
R01_txt.grid(row=1, column=0, padx=10, pady=10)

RO2_lbl = Label(F7, text="Team B", font=('times new roman', 16, 'bold'), bg="#00B2EE", fg="black")
RO2_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
R02_txt = Label(F7, width=10, textvariable=tBTotal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
R02_txt.grid(row=3, column=0, padx=10, pady=10)

winner = StringVar()

RO3_lbl = Label(F7, text="Winner", font=('times new roman', 20, 'bold'), bg="#00B2EE", fg="black")
RO3_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
R03_txt = Label(F7, width=10, textvariable=winner, font=('times new roman', 20, 'bold'), bd=5, relief=GROOVE)
R03_txt.grid(row=5, column=0, padx=10, pady=10)

F8 = LabelFrame(root, text="Double-Bar-Graph", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F8.place(x=751, y=376, width=612, height=322)
canvasNew = Canvas(master=F8, width = 600, height = 300)
canvasNew.pack()

F4 = LabelFrame(root, text="Pie Chart Team A", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F4.place(x=0, y=435, width=225, height=300)
canvasPieA = Canvas(master=F4, width = 210, height = 280)
canvasPieA.pack()

F12 = LabelFrame(root, text="Pie Chart Team B", font=('times new roman', 13, 'bold'), bd=10, fg="Black", bg="#00B2EE")
F12.place(x=226, y=435, width=225, height=300)
canvasPieB = Canvas(master=F12, width = 210, height = 280)
canvasPieB.pack()

root.mainloop()
