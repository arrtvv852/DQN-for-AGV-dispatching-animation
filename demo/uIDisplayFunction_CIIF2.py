'''
Created on 2017年7月21日
打點在UI上呈現
基於孟維版本的改寫成函數，加上充電樁跟牆柱子，
TODO: 讓AGV數目動態彈性

@author: I-MENGWEI.HSYU 徐孟維, CW.TSAI
'''

import json
import os
import numpy as np
import tkinter as tk
from tkinter import ttk
import time
#import algorithm.jsonParserAPI as cw

speed, temp = 0, 0

class uIDisplay(object):

    def __init__(self):
        None
        # Select demo speed
        #print("Please select the demo speed (0:slow, 1:normal, 2:fast, 3: super fast):")

    def active(self):
        global tempo
        with open('UI4Analytics.json', 'r') as f:
            layout = json.load(f)
        with open('Output4UI.json', 'r') as f:
            path = json.load(f)
        global trigger, speed
        if speed.get() == "Slow":
            tempo = 1
        elif speed.get() == "Normal":
            tempo = 0.1
        elif speed.get() == "Fast":
            tempo = 0.05
        elif speed.get() == "Extremely Fast":
            tempo = 0.025

        uIDisplay().displaySolution(layout, path)


    def Init_user(self):
        gridRange = []
        unit = 22

        window1 = tk.Tk()
        window1.title("AGV Fleet Management Solution_Analytics")
        window1.geometry("900x280")

        speed = self.Button(window1, unit)
        printer = self.draw_description(window1, unit)
        window1.mainloop()


    def Button(self, window, unit):

        global speed
        t = tk.Label(window, text = "Simulation Speed", width = 20, height = 1)
        t.pack()

        speed = tk.StringVar()
        m = ttk.Combobox(window, width = 10, textvariable = speed)
        m['values'] = ("Slow", "Normal", "Fast", "Extremely Fast")
        m.current(1)
        m.pack()

        tempo = 1
        if speed.get() == "Slow":
            tempo = 2
        elif speed.get() == "Normal":
            tempo = 0.2
        elif speed.get() == "Fast":
            tempo = 0.1
        elif speed.get() == "Extremely Fast":
            tempo = 0.05

        #AGV_pos, canvas, AGV1, AGV2, AGV3, AGV4, agv1, agv2, agv3, agv4 = self.draw_layout(layout, window, unit)
        #button = tk.Button(window, text="Start", width=10, height=1,command=self.active(path, tempo, AGV_pos, canvas, unit, window, AGV1, AGV2, AGV3, AGV4, agv1,agv2,agv3, agv4, layout))
        button =  tk.Button(window, text="Start", width=10, height=1, command = self.active)
        button.pack()

        return speed


    def draw_description(self, window, unit):
        printer = tk.Canvas(window, bg="snow", height= 210, width=900)
        #Input
        L = [
            [3, 0, 5, 1, 2, 0],
            [2, 1, 0, 4, 3, 2],
            [0, 3, 0, 2, 2, 3],
            [4, 3, 2, 1, 0, 0],
            [2, 2, 2, 2, 2, 2],
            [1, 2, 3, 4, 5, 3]
        ]
        S = [
            [2, 2, 2, 1, 2, 2],
            [23, 18, 10, 0, 0, 0],
            [0, 0, 13, 11, 14, 0],
            [0, 0, 0, 18, 14, 8]
        ]
        C = [
            [20, 20, 20, 20],
            [0.25, 15, 50, 75]
        ]
        C1 = [
            "0.3/120", "18/120", "60/120", "90/120"
        ]

        #Print Demand
        dmd = printer.create_text(50, 15, text="Demand:", font=("arial", 15))
        for c in range(10, int(10 + 5 * 1.2 * unit), int(1.2 * unit)):
            x0, y0, x1, y1 = 100 + c, 20, 100 + c, 20 + 8.3 * unit
            printer.create_line(x0, y0, x1, y1)
        for r in range(10, int(10 + 5 * 1.2 * unit), int(1.2 * unit)):
            x0, y0, x1, y1 = 50, 35 + r, 50 + 10 * unit, 35 + r
            printer.create_line(x0, y0, x1, y1)
        for i in range(6):
            for j in range(6):
                x = (5.4+i) * 1.2 * unit - 20
                y = (2.2+j) * 1.2 * unit
                printer.create_text(x, y, text=L[i][j], font=("arial", 12))
        for i in range(6):
            x = (5.4+i) * 1.2 * unit - 20
            y = 1.2 * 1.2 * unit
            printer.create_text(x, y, text="M"+str(i+1), font=("arial", 12))
        for i in range(6):
            x = 4 * 1.2 * unit - 30
            y = (2.2 + i) * 1.2 * unit
            printer.create_text(x, y, text="Line " + str(i + 1), font=("arial", 12))

        #print supply
        sply = printer.create_text(330, 15, text="Supply:", font=("arial", 15))
        for c in range(10, int(10 + 5 * 1.2 * unit), int(1.2 * unit)):
            x0, y0, x1, y1 = 380 + c, 20, 380 + c, 20 + 6 * unit
            printer.create_line(x0, y0, x1, y1)
        for r in range(10, int(10 + 3 * 1.2 * unit), int(1.2 * unit)):
            x0, y0, x1, y1 = 330, 35 + r, 330 + 10 * unit, 35 + r
            printer.create_line(x0, y0, x1, y1)
        for i in range(4):
            for j in range(6):
                x = 260 + (5.4 + j) * 1.2 * unit
                y = (2.2 + i) * 1.2 * unit
                printer.create_text(x, y, text=S[i][j], font=("arial", 12))
        for i in range(6):
            x = 260 + (5.4 + i) * 1.2 * unit
            y = 1.2 * 1.2 * unit
            printer.create_text(x, y, text="M" + str(i + 1), font=("arial", 12))
        for i in range(4):
            x = 250 + 4 * 1.2 * unit
            y = (2.2 + i) * 1.2 * unit
            printer.create_text(x, y, text="Shelf " + str(i + 1), font=("arial", 12))

        #print AGV
        agv = printer.create_text(610, 15, text="AGV:", font=("arial", 15))
        for c in range(10, int(10 + 4 * 2.6 * unit), int(2.6 * unit)):
            x0, y0, x1, y1 = 650 + c, 20, 650 + c, 20 + 6 * unit
            printer.create_line(x0, y0, x1, y1)
        for r in range(10, int(10 + 2 * 2 * unit), int(2 * unit)):
            x0, y0, x1, y1 = 590, 35 + r, 590 + 13.2 * unit, 35 + r
            printer.create_line(x0, y0, x1, y1)
        for i in range(2):
            for j in range(4):
                x = 382 + (5.4 + j) * 2.58 * unit
                y = (2.2 + i) * 2 * unit - 30
                if i == 0:
                    printer.create_text(x, y, text=str(C[i][j]), font=("arial", 12))
                else:
                    printer.create_text(x, y+10, text=str(C1[j])+"\n("+str(C[i][j])+"%)", font=("arial", 12))
        for i in range(4):
            x = 385 + (5.4 + i) * 2.55 * unit
            y = 1.2 * 1.2 * unit
            printer.create_text(x, y, text="AGV" + str(i + 1), font=("arial", 12))
        x = 515 + 4 * 1.2 * unit
        y = (2.2) * 2 * unit - 30
        printer.create_text(x, y, text="Loading\nCapacity", font=("arial", 12))
        x = 515 + 4 * 1.2 * unit
        y = (3.4) * 2 * unit - 30
        printer.create_text(x, y, text="Battery\nCapacity\n(Ah)", font=("arial", 12))




        printer.pack()
        return printer
    
    def draw_layout(self, layout, window, unit):
        Shelf = []
        Line = []
        Spot = []
        AGV = []
        charger = []
        wall = []
        chargePort = []
        for i in range(0, len(layout)):
            if layout[i]["Type"] == "gridRange":
                x = layout[i]["XNumber"]
                y = layout[i]["YNumber"]
            elif layout[i]["Type"] == "shelf":
                Shelf.append(layout[i]["Position"])
            elif layout[i]["Type"] == "line":
                Line.append(layout[i]["Position"])
            elif layout[i]["Type"] == "agv":
                AGV.append(layout[i]["Position"][0])
            elif layout[i]["Type"] == "parkingLot":
                Spot.append(layout[i]["Position"][0])
            elif layout[i]["Type"] == "charger":
                charger.append(layout[i]["Position"])
            elif layout[i]["Type"] == "wall":
                wall.append(layout[i]["Position"])
            elif layout[i]["Type"] == "chargePort":
                chargePort.append(layout[i]["Position"][0])

        # Create Space
        canvas = tk.Canvas(window, bg = "gray85", height = y * unit, width = x * unit +100)
        canvas.pack()
         
         
         
         
# #         TBD: 把AGV數量改成彈性的             
#         agvInfo = []
#         for record in range(len(layout)):
#             agvInfoTemp = []
#             if layout[record].get("Type") == "agv":
#                 agvInfoTemp.append(layout[record].get("AGV_ID"))
#                 for i in range(len(layout[record].get("Position"))):
#                     agvInfoTemp.append((layout[record].get("Position"))[i][0])
#                     agvInfoTemp.append((layout[record].get("Position"))[i][1])   
#                 agvInfo.append(agvInfoTemp)
#         print("agvInfo")
#         print(agvInfo)
#         
#         listAGV = []
#         listagv = []
#         for i in range(len(agvInfo)):    
#             idxAGV = agvInfo[i][0]
#             idxAGV_x = agvInfo[i][1]
#             idxAGV_y = agvInfo[i][2]
#             
#             strAGV = ''
#             stragv = ''  
#             strAGV = 'AGV' + str(idxAGV)
#             stragv = 'agv' + str(idxAGV)
# 
#             p1 = [idxAGV_x * unit, (y - 1) * unit - idxAGV_y * unit]
#             p2 = [idxAGV_x * unit + unit, y * unit - idxAGV_y * unit]
#             strAGV = canvas.create_oval(p1[0], p1[1], p2[0], p2[1], fill="purple")
#             stragv = canvas.create_text((idxAGV_x + 0.5) * unit, (y - idxAGV_y - 0.5) * unit, text = 'AGV' + str(idxAGV), fill="yellow")
# 
#             listAGV.append(strAGV)
#             listagv.append(stragv)
            

        
     

        #Dashboard
        canvas.create_rectangle(0, 0, 100, y * unit, fill="snow")

        # Draw Lines
        for c in range(0, x * unit, unit):
            x0, y0, x1, y1 = c +100, 0, c +100, y * unit
            canvas.create_line(x0, y0, x1, y1)
        for r in range(0, y * unit, unit):
            x0, y0, x1, y1 = 100, r, x * unit +100, r
            canvas.create_line(x0, y0, x1, y1)
            
        # Draw Shelves
        for i in range(0, len(Shelf)):
            p1 = [Shelf[i][0][0] * unit +100, (y - 1) * unit - Shelf[i][0][1] * unit]
            p2 = [Shelf[i][len(Shelf[i]) - 1][0] * unit + unit +100, y * unit - Shelf[i][len(Shelf[i]) - 1][1] * unit]
            p3 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            canvas.create_rectangle(p1[0], p1[1], p2[0], p2[1], fill="goldenrod1") #orange
            canvas.create_text(p3[0], p3[1], text="Shelf " + str(i+1), font = ("comic sans ms", '12', 'bold'), fill = ('goldenrod4'))
            
        # Draw Production Lines
        for i in range(0, len(Line)):
            p1 = [Line[i][0][0] * unit +100, (y) * unit - Line[i][0][1] * unit]
            p2 = [Line[i][len(Line[i]) - 1][0] * unit + unit +100, (y-1) * unit - Line[i][len(Line[i]) - 1][1] * unit]
            p3 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            canvas.create_rectangle(p1[0], p1[1], p2[0], p2[1], fill="MediumPurple1")  #red
            canvas.create_text(p3[0], p3[1], text="Line " + str(i+1), font = ("comic sans ms", '12', 'bold'), fill = ('MediumPurple4'))

        # charger
        for i in range(0, len(charger)):
            p1 = [charger[i][0][0] * unit +100, (y - 1) * unit - charger[i][0][1] * unit]
            p2 = [charger[i][len(charger[i]) - 1][0] * unit + unit +100, y * unit - charger[i][len(charger[i]) - 1][1] * unit]
            p3 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            canvas.create_rectangle(p1[0], p1[1], p2[0], p2[1], fill="yellow green")
            canvas.create_text(p3[0], p3[1], text="C" + str(i+1), font = ("comic sans ms", '12', 'bold'), fill = ('dark green'))
            
        # wall
        wallCal = wall[0]
        for i in range(0, len(wallCal)):
            p1 = [wallCal[i][0] * unit +100, (y - 1) * unit - wallCal[i][1] * unit]
            p2 = [wallCal[i][0] * unit + unit +100, y * unit - wallCal[i][1] * unit]
            p3 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            canvas.create_rectangle(p1[0], p1[1], p2[0], p2[1], fill="gray37")
            canvas.create_text(p3[0], p3[1], text="W", font = ("comic sans ms", '12', 'bold'), fill = "snow")
               
        # Parking Point
        for i in range(0, len(Spot)):
            canvas.create_text((Spot[i][0] + 0.5) * unit +100, (y - Spot[i][1] - 0.5) * unit, text="P", font = ("arial 14 points", '12', 'bold'), fill = "red")
        
        # ChargePort
        for i in range(0, len(chargePort)):
            canvas.create_text((chargePort[i][0] + 0.5) * unit +100, (y - chargePort[i][1] - 0.5) * unit, text="C", font = ("arial 14 points", '12', 'bold'), fill = "red")
        
           
        # Put AGVs 
        # 0
        p1 = [AGV[0][0] * unit +100, (y - 1) * unit - AGV[0][1] * unit]
        p2 = [AGV[0][0] * unit + unit +100, y * unit - AGV[0][1] * unit]
        AGV1 = canvas.create_oval(p1[0], p1[1], p2[0], p2[1], fill="midnight blue")
#         agv1 = canvas.create_text((AGV[0][0] + 0.5) * unit, (y - AGV[0][1] - 0.5) * unit, text="AGV" + str(1), fill="yellow")
        agv1 = canvas.create_text((AGV[0][0] + 0.5) * unit +100, (y - AGV[0][1] - 0.5) * unit, text=str(1), fill="snow", font = ("arial", '12', 'bold'))
        # 2
        p1 = [AGV[1][0] * unit +100, (y - 1) * unit - AGV[1][1] * unit]
        p2 = [AGV[1][0] * unit + unit +100, y * unit - AGV[1][1] * unit]
        AGV2 = canvas.create_oval(p1[0], p1[1], p2[0], p2[1], fill="midnight blue")
#         agv2 = canvas.create_text((AGV[1][0] + 0.5) * unit, (y - AGV[1][1] - 0.5) * unit, text="AGV" + str(2), fill="yellow")
        agv2 = canvas.create_text((AGV[1][0] + 0.5) * unit +100, (y - AGV[1][1] - 0.5) * unit, text=str(2), fill="snow", font = ("arial", '12', 'bold'))
        # 2
        p1 = [AGV[2][0] * unit +100, (y - 1) * unit - AGV[2][1] * unit]
        p2 = [AGV[2][0] * unit + unit +100, y * unit - AGV[2][1] * unit]
        AGV3 = canvas.create_oval(p1[0], p1[1], p2[0], p2[1], fill="midnight blue")
#         agv3 = canvas.create_text((AGV[2][0] + 0.5) * unit, (y - AGV[2][1] - 0.5) * unit, text="AGV" + str(3), fill="yellow")
        agv3 = canvas.create_text((AGV[2][0] + 0.5) * unit +100, (y - AGV[2][1] - 0.5) * unit, text=str(3), fill="snow", font = ("arial", '12', 'bold'))
        # 3
        p1 = [AGV[3][0] * unit +100, (y - 1) * unit - AGV[3][1] * unit]
        p2 = [AGV[3][0] * unit + unit +100, y * unit - AGV[3][1] * unit]
        AGV4 = canvas.create_oval(p1[0], p1[1], p2[0], p2[1], fill="midnight blue")
#         agv4 = canvas.create_text((AGV[3][0] + 0.5) * unit, (y - AGV[3][1] - 0.5) * unit, text="AGV" + str(4), fill="yellow")
        agv4 = canvas.create_text((AGV[3][0] + 0.5) * unit +100, (y - AGV[3][1] - 0.5) * unit, text=str(4), fill="snow", font = ("arial", '12', 'bold'))

        return AGV, canvas, AGV1, AGV2, AGV3, AGV4, agv1, agv2, agv3, agv4
    
    
    def path_demo(self, path, tempo, AGV_pos, canvas, unit, window, AGV1, AGV2, AGV3, AGV4, agv1, agv2, agv3, agv4):
        global move, dist, index
        Path = []
        Time = []
        Wait = []

        #Draft Data
        for i in range(0, len(path)):
            pathT = path[i]["Route"]
            timeT = []
            waitT = path[i]["Wait_Time"]
            t = 1
            for j in range(0, len(pathT)):
                for k in range(0, len(pathT[j])):
                    timeT.append(t)
                    t += 1
                t += path[i]["Wait_Time"][j] - 1
            Path.append(pathT)
            Time.append(timeT)
            Wait.append(waitT)
     
        #List Time Horizon
        allT = list(set().union(sum(Time,[])))
        #Time_all.sort()
        top = max(allT)
        bot = min(allT)
        # TBD
        Time_all = np.linspace(bot, top, (top-bot)*40*tempo+1)
        Agv_pos = []
        for i in range(0, len(path)):
            agv_pos = Path[i]
            agv_pos = sum(agv_pos, [])
            agv_time = Time[i]
            agv_allpos = []
            k = 0
            for j in range(0, len(Time_all)):
                while True:
                    if k >= len(agv_time):
                        agv_allpos.append(agv_pos[k-1])
                    elif agv_time[k] == Time_all[j]:
                        agv_allpos.append(agv_pos[k])
                        temp = agv_time[k]
                        k += 1
                    elif agv_time[k] > Time_all[j]:
                        portion = (Time_all[j]-temp)/(agv_time[k]-temp)
                        x = (agv_pos[k][0]-agv_pos[k-1][0])*portion + agv_pos[k-1][0]
                        y = (agv_pos[k][1]-agv_pos[k-1][1])*portion + agv_pos[k-1][1]
                        agv_allpos.append([x,y])
                    break
            Agv_pos.append(agv_allpos)
     
        #first move
        canvas.create_text(2.3*unit, 0.8*unit, text="Time: ", fill = "Red", font = ("comic sans ms", '18'))
        show = canvas.create_text(3*unit, 2*unit, text = str(0), fill = "Red", font = ("comic sans ms", '18'))
        time.sleep(tempo)
        window.update()
        for i in range(0, len(path)):
            index = i
            move = -1
            dist = 0
            if Agv_pos[i][0][1] > AGV_pos[i][1]:
                move = 1
                dist = Agv_pos[i][0][1] - AGV_pos[i][1]
            elif Agv_pos[i][0][1] < AGV_pos[i][1]:
                move = 2
                dist = AGV_pos[i][1] - Agv_pos[i][0][1]
            elif Agv_pos[i][0][0] < AGV_pos[i][0]:
                move = 3
                dist = AGV_pos[i][0] - Agv_pos[i][0][0]
            elif Agv_pos[i][0][0] > AGV_pos[i][0]:
                move = 4
                dist = Agv_pos[i][0][0] - AGV_pos[i][0]
            else:
                move = 0
            if move == 1:
                if i == 0:
                    canvas.move(AGV1, 0, -dist*unit)
                    canvas.move(agv1, 0, -dist*unit)
                elif i == 1:
                    canvas.move(AGV2, 0, -dist*unit)
                    canvas.move(agv2, 0, -dist*unit)
                elif i == 2:
                    canvas.move(AGV3, 0, -dist*unit)
                    canvas.move(agv3, 0, -dist*unit)
                elif i == 3:
                    canvas.move(AGV4, 0, -dist*unit)
                    canvas.move(agv4, 0, -dist*unit)      
            elif move == 2:
                if i == 0:
                    canvas.move(AGV1, 0, dist*unit)
                    canvas.move(agv1, 0, dist*unit)
                elif i == 1:
                    canvas.move(AGV2, 0, dist*unit)
                    canvas.move(agv2, 0, dist*unit)
                elif i == 2:
                    canvas.move(AGV3, 0, dist*unit)
                    canvas.move(agv3, 0, dist*unit)
                elif i == 3:
                    canvas.move(AGV4, 0, dist*unit)
                    canvas.move(agv4, 0, dist*unit)    
            elif move == 3:
                if i == 0:
                    canvas.move(AGV1, -dist*unit, 0)
                    canvas.move(agv1, -dist*unit, 0)
                elif i == 1:
                    canvas.move(AGV2, -dist*unit, 0)
                    canvas.move(agv2, -dist*unit, 0)
                elif i == 2:
                    canvas.move(AGV3, -dist*unit, 0)
                    canvas.move(agv3, -dist*unit, 0)
                elif i == 3:
                    canvas.move(AGV4, -dist*unit, 0)
                    canvas.move(agv4, -dist*unit, 0)    
            elif move == 4:
                if i == 0:
                    canvas.move(AGV1, dist*unit, 0)
                    canvas.move(agv1, dist*unit, 0)
                elif i == 1:
                    canvas.move(AGV2, dist*unit, 0)
                    canvas.move(agv2, dist*unit, 0)
                elif i == 2:
                    canvas.move(AGV3, dist*unit, 0)
                    canvas.move(agv3, dist*unit, 0)
                elif i == 3:
                    canvas.move(AGV4, dist*unit, 0)
                    canvas.move(agv4, dist*unit, 0)   
            elif move == 0:
                if i == 0:
                    canvas.move(AGV1, 0, 0)
                    canvas.move(agv1, 0, 0)
                elif i == 1:
                    canvas.move(AGV2, 0, 0)
                    canvas.move(agv2, 0, 0)
                elif i == 2:
                    canvas.move(AGV3, 0, 0)
                    canvas.move(agv3, 0, 0)
                elif i == 3:
                    canvas.move(AGV4, 0, 0)
                    canvas.move(agv4, 0, 0)
        #Run
        for t in range(1, len(Time_all)):
            canvas.delete(show)
            show = canvas.create_text(3*unit, 2*unit, text=str(round(Time_all[t]-1,1)), fill = "red", font = ("comic sans ms", '18'))
            time.sleep(tempo*(Time_all[t]-Time_all[t-1]))
            window.update()
            for i in range(0, len(path)):
                index = i
                move = -1
                if Agv_pos[i][t][1] > Agv_pos[i][t-1][1]:
                    move = 1
                    dist = Agv_pos[i][t][1] - Agv_pos[i][t-1][1]
                elif Agv_pos[i][t][1] < Agv_pos[i][t-1][1]:
                    move = 2
                    dist = Agv_pos[i][t-1][1] - Agv_pos[i][t][1]
                elif Agv_pos[i][t][0] < Agv_pos[i][t-1][0]:
                    move = 3
                    dist = Agv_pos[i][t-1][0] - Agv_pos[i][t][0]
                elif Agv_pos[i][t][0] > Agv_pos[i][t-1][0]:
                    move = 4
                    dist = Agv_pos[i][t][0] - Agv_pos[i][t-1][0]
                else:
                    move = 0
                if move == 1:
                    if i == 0:
                        canvas.move(AGV1, 0, -dist*unit)
                        canvas.move(agv1, 0, -dist*unit)
                    elif i == 1:
                        canvas.move(AGV2, 0, -dist*unit)
                        canvas.move(agv2, 0, -dist*unit)
                    elif i == 2:
                        canvas.move(AGV3, 0, -dist*unit)
                        canvas.move(agv3, 0, -dist*unit)
                    elif i == 3:
                        canvas.move(AGV4, 0, -dist*unit)
                        canvas.move(agv4, 0, -dist*unit)   
                elif move == 2:
                    if i == 0:
                        canvas.move(AGV1, 0, dist*unit)
                        canvas.move(agv1, 0, dist*unit)
                    elif i == 1:
                        canvas.move(AGV2, 0, dist*unit)
                        canvas.move(agv2, 0, dist*unit)
                    elif i == 2:
                        canvas.move(AGV3, 0, dist*unit)
                        canvas.move(agv3, 0, dist*unit)
                    elif i == 3:
                        canvas.move(AGV4, 0, dist*unit)
                        canvas.move(agv4, 0, dist*unit)    
                elif move == 3:
                    if i == 0:
                        canvas.move(AGV1, -dist*unit, 0)
                        canvas.move(agv1, -dist*unit, 0)
                    elif i == 1:
                        canvas.move(AGV2, -dist*unit, 0)
                        canvas.move(agv2, -dist*unit, 0)
                    elif i == 2:
                        canvas.move(AGV3, -dist*unit, 0)
                        canvas.move(agv3, -dist*unit, 0)
                    elif i == 3:
                        canvas.move(AGV4, -dist*unit, 0)
                        canvas.move(agv4, -dist*unit, 0)    
                elif move == 4:
                    if i == 0:
                        canvas.move(AGV1, dist*unit, 0)
                        canvas.move(agv1, dist*unit, 0)
                    elif i == 1:
                        canvas.move(AGV2, dist*unit, 0)
                        canvas.move(agv2, dist*unit, 0)
                    elif i == 2:
                        canvas.move(AGV3, dist*unit, 0)
                        canvas.move(agv3, dist*unit, 0)
                    elif i == 3:
                        canvas.move(AGV4, dist*unit, 0)
                        canvas.move(agv4, dist*unit, 0)    
                elif move == 0:
                    if i == 0:
                        canvas.move(AGV1, 0, 0)
                        canvas.move(agv1, 0, 0)
                    elif i == 1:
                        canvas.move(AGV2, 0, 0)
                        canvas.move(agv2, 0, 0)
                    elif i == 2:
                        canvas.move(AGV3, 0, 0)
                        canvas.move(agv3, 0, 0)
                    elif i == 3:
                        canvas.move(AGV4, 0, 0)
                        canvas.move(agv4, 0, 0)
    
        
    def displaySolution(self, jsonUI4Analytics, jsonOutput4UI):
        #jp = cw.jsonParserAPI()
        layout = jsonUI4Analytics
        path = jsonOutput4UI

        gridRange = []
        for record in range(len(layout)):
            if layout[record].get("Type") == "gridRange":
                gridRange.append(layout[record].get("XNumber"))
                gridRange.append(layout[record].get("YNumber"))
        gridRange = tuple(gridRange)
        unit = 22

        window = tk.Tk()
        window.title("AGV Fleet Management Solution_Analytics")
        window.geometry("1100x650")
        
        AGV_pos = []
        #tempo = 1
        
        index = -1
        move = -1
        dist = 0
        
#         #Input Speed
#         #print("Please set the simulation speed(0:slow, 1:normal, 2:fast, 3: super fast):")
        #ans = int(input())
        #while ans!=0 and ans!=1 and ans!=2 and ans!=3:
            #print("0, 1, 2, 3only!!(0:slow, 1:normal, 2:fast, 3: super fast)")
            #ans = int(input())

        descrip = tk.Canvas(window, bg="snow", height = 180, width = 1100)
        #Shelf Descrip
        descrip.create_rectangle(30, 20, 130, 40, fill="goldenrod1")
        descrip.create_text(80, 30, text = "Shelf ", font = ("comic sans ms", '12', 'bold'), fill = ('goldenrod4'))
        descrip.create_text(432, 30, text = "：Storage Space - The place where the material inventory hold.", font = ("arial", "15", "bold"))
        #Lines Descrip
        descrip.create_rectangle(30, 60, 130, 80, fill="MediumPurple1")
        descrip.create_text(80, 70, text="Line ", font=("comic sans ms", '12', 'bold'),fill=('MediumPurple4'))
        descrip.create_text(394, 70, text="：Production Line - The place where request materials.",font=("arial", "15", "bold"))
        #Charging Descrip
        descrip.create_rectangle(70, 100, 90, 120, fill="yellow green")
        descrip.create_text(80, 110, text="C", font=("comic sans ms", '12', 'bold'), fill=('dark green'))
        descrip.create_text(360, 110, text="：Parking Area - Where AGVs stay when idling.",font=("arial", "15", "bold"))
        #Wall Descrip
        descrip.create_rectangle(70, 140, 90, 160, fill="gray37")
        descrip.create_text(80, 150, text="W", font=("comic sans ms", '12', 'bold'), fill="snow")
        descrip.create_text(392, 150, text="：Wall / Pillar - Obstacles, AGVs can not walk through.", font=("arial", "15", "bold"))
        #Parking Point Descrip
        descrip.create_text(750, 30, text="P",font=("arial 14 points", '15', 'bold'), fill="red")
        descrip.create_text(850, 30, text="：Pick / Drop Point",font=("arial", "15", "bold"))
        descrip.create_text(750, 70, text="C", font=("arial 14 points", '15', 'bold'), fill="red")
        descrip.create_text(835, 70, text="：Parking Point", font=("arial", "15", "bold"))
        #AGV Descrip
        descrip.create_oval(740, 100, 760, 120, fill="midnight blue")
        descrip.create_text(750, 110, text="1", fill="snow",font=("arial", '12', 'bold'))
        descrip.create_text(926, 110, text="：Automated Guided Vehicle (AGV)", font=("arial", "15", "bold"))
        #Time Descrip
        descrip.create_text(730, 150, text="Time", fill="Red", font=("comic sans ms", '18'))
        descrip.create_text(883, 150, text="：Elapsed Time (Seconds)", font=("arial", "15", "bold"))

        descrip.pack()

        AGV_pos, canvas, AGV1, AGV2, AGV3, AGV4, agv1, agv2, agv3, agv4 = self.draw_layout(layout, window, unit)
        window.after(0, self.path_demo(path, tempo, AGV_pos, canvas, unit, window, AGV1, AGV2, AGV3, AGV4, agv1, agv2, agv3, agv4))
        window.mainloop()

 
 
 
 
 


 
 

 

 

             
         

 








def main():
    # MIT CSAIL demo scenario
    # layout = jp.getDataFromJson('UI4Analytics_MIT.json')
    # path = jp.getDataFromJson('Output4UI_MIT.json')
#     uIDisplay().displaySolution('UI4Analytics_MIT.json', 'Output4UI_MIT.json')
    
    # CIIF demo scenario
    uIDisplay().Init_user()
    #uIDisplay().displaySolution(layout, path)
    
        
if __name__ == "__main__":
    main()




