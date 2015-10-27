from graphics import *
import random
x=input('enter grid lenth:')
def kanu(o):
        filled=0
        list4=[[0 for q in range(x)] for w in range(x)]
        list5=[[0 for p in range(x)] for l in range(x)]
        win = GraphWin("2048 Game", 100*(x+2), 100*(x+3))
        di=Text(Point((50*x+100),10),"!!!! Welcome to 2048 !!!!")
        di.draw(win)
        di.setStyle('bold italic')
        di.setTextColor("purple")
        def main(i,j):
            ci = Rectangle(Point(100*i,100*j), Point((100*i)+100,(100*j)+100))
            ci.draw(win)
            ci.setWidth("4")
            ci.setOutline("blue")
            ci.setFill("red2")
        def grid(i,j):
            while j!=x+1:
                while i!=x+1:
                    main(i,j)
                    i=i+1
                i=1
                j=j+1
        grid(1,1)
        d1=Text(Point((50*x+100),100*(x+2)-10),"")
        d1.draw(win)
        d1.setStyle('bold italic')
        d1.setTextColor("red")
        def write(number,column,row):
            writing=Text(Point((100*(column+1)+50),(100*(row+2)-50)),number)
            writing.draw(win)
            writing.setStyle('bold')
            writing.setTextColor("white")
            writing.setSize(36)
        def update(boardsize,list4,list1):
            xaxis=0
            while xaxis<x:
                yaxis=0
                while yaxis<x:
                    if list4[yaxis][xaxis]!=list1[yaxis][xaxis]:
                        if list4[yaxis][xaxis]!=0:
                                main(xaxis+1,yaxis+1)
                                write(list4[yaxis][xaxis],xaxis,yaxis)
                        else:
                                main(xaxis+1,yaxis+1)
                    yaxis=yaxis+1
                xaxis=xaxis+1
            
        def bubble(listx,direction,x):
                if direction == "left":
                        vertical=0
                        while vertical<x:
                                limit = x
                                horizontal=0
                                while horizontal<limit:
                                        if listx[vertical][horizontal]==0:
                                                temp=listx[vertical].pop(horizontal)
                                                listx[vertical].append(temp)
                                                limit=limit-1
                                        else:
                                                horizontal=horizontal+1
                                vertical=vertical+1
                elif direction == "right":
                        vertical=0
                        while vertical<x:
                                limit = 0
                                horizontal=x-1
                                while horizontal>=limit:
                                        if listx[vertical][horizontal]==0:
                                                temp=listx[vertical].pop(horizontal)
                                                listx[vertical].insert(0,temp)
                                                limit = limit+1
                                        else:
                                                horizontal=horizontal-1
                                vertical=vertical+1
                elif direction == "up":
                        horizontal=0
                        while horizontal<x:
                                copy=0
                                templist=[0]*x
                                while copy<x:
                                        templist[copy]=listx[copy][horizontal]
                                        copy=copy+1
                                limit = x
                                vertical=0
                                while vertical<limit:
                                        if templist[vertical]==0:
                                                temp=templist.pop(vertical)
                                                templist.append(temp)
                                                limit = limit-1
                                        else:
                                                vertical=vertical+1
                                copy=0
                                while copy<x:
                                        listx[copy][horizontal]=templist[copy]
                                        copy=copy+1
                                horizontal=horizontal+1
                elif direction == "down":
                        horizontal=0
                        while horizontal<x:
                                copy=0
                                templist=[0]*x
                                while copy<x:
                                        templist[copy]=listx[copy][horizontal]
                                        copy=copy+1
                                limit = 0
                                vertical=x-1
                                while vertical>=limit:
                                        if templist[vertical]==0:
                                                temp=templist.pop(vertical)
                                                templist.insert(0,temp)
                                                limit = limit+1
                                        else:
                                                vertical=vertical-1
                                copy=0
                                while copy<x:
                                        listx[copy][horizontal]=templist[copy]
                                        copy=copy+1
                                horizontal=horizontal+1
        
        def replay(i):
                ci = Rectangle(Point(100*(x),100*(x+2)-60), Point(100*x+100,100*(x+2)-10))
                ci.draw(win)
                ci.setWidth("3")
                ci.setOutline("blue")
                d=Text(Point(100*x+50,100*(x+2)-40),"exit")
                d.draw(win)
                d.setStyle('bold italic')
                d.setTextColor("red")
                ci = Rectangle(Point(100,100*(x+2)-60), Point(200,100*(x+2)-10))
                ci.draw(win)
                ci.setWidth("3")
                ci.setOutline("blue")
                d=Text(Point(150,100*(x+2)-40),"replay")
                d.draw(win)
                d.setStyle('bold italic')
                d.setTextColor("red")
                m=win.getMouse()
                if 100*x<=m.x<=100*(x+1) and 100*(x+2)-60<=m.y<=100*(x+2)-20:
                        win.close()
                elif 100<=m.x<=200 and 100*(x+2)-60<=m.y<=100*(x+2)-0:
                        win.close()
                        kanu(o+1)
                else:
                        e = GraphWin("ERROR!", 500, 50)
                        d=Text(Point(250,10),"Pls. choose apropriate option")
                        d.draw(e)
                        d.setStyle('bold italic')
                        d.setTextColor("red")
                        e.getMouse()
                        e.close()
                        replay(i)
        def play(playno,filled):
            xaxs=0
            while xaxs<x:
                    yaxs=0
                    while yaxs<x:
                            list5[yaxs][xaxs]=list4[yaxs][xaxs]
                            yaxs+=1
                    xaxs+=1
            move=input()
            if move == 8:
                
                bubble(list4,"up",x)

                horizontalx=0    
                while(horizontalx!=x):
                    verticaly=0
                    while(verticaly<x-1):
                        if list4[verticaly][horizontalx]!=0 and list4[verticaly][horizontalx]==list4[verticaly+1][horizontalx]:
                            list4[verticaly][horizontalx]=2*list4[verticaly][horizontalx]
                            list4[verticaly+1][horizontalx]=0
                            verticaly=verticaly+2
                            filled=filled-1
                            print "decreasing 1",filled
                        else:
                            verticaly=verticaly+1
                    horizontalx=horizontalx+1
                    
                bubble(list4,"up",x)

            elif move == 6:
                bubble(list4,"right",x)

                verticaly=0
                while(verticaly!=x):
                    horizontalx=x-1
                    while(horizontalx>0):
                        if list4[verticaly][horizontalx]!=0 and list4[verticaly][horizontalx]==list4[verticaly][horizontalx-1]:
                            list4[verticaly][horizontalx]=2*list4[verticaly][horizontalx]
                            list4[verticaly][horizontalx-1]=0
                            horizontalx=horizontalx-2
                            filled=filled-1
                            print "decreasing 1",filled
                        else:
                            horizontalx=horizontalx-1
                    verticaly=verticaly+1

                bubble(list4,"right",x)

            elif move == 4:
                bubble(list4,"left",x)
                    
                verticaly=0
                while(verticaly!=x):
                    horizontalx=0
                    while(horizontalx<x-1):
                        if list4[verticaly][horizontalx]!=0 and list4[verticaly][horizontalx]==list4[verticaly][horizontalx+1]:
                            list4[verticaly][horizontalx]=2*list4[verticaly][horizontalx]
                            list4[verticaly][horizontalx+1]=0
                            horizontalx=horizontalx+2 
                            filled=filled-1
                            print "decreasing 1",filled
                        else:
                            horizontalx=horizontalx+1
                    verticaly=verticaly+1
                    
                bubble(list4,"left",x)
                
            elif move == 2:
                bubble(list4,"down",x)
                    
                horizontalx=0
                while(horizontalx!=x):
                    verticaly=x-1
                    while(verticaly>0):
                        if list4[verticaly][horizontalx]!=0 and list4[verticaly][horizontalx]==list4[verticaly-1][horizontalx]:
                            list4[verticaly][horizontalx]=2*list4[verticaly][horizontalx]
                            list4[verticaly-1][horizontalx]=0
                            verticaly=verticaly-2
                            filled=filled-1
                            print "decreasing 1",filled
                        else:
                            verticaly=verticaly-1
                    horizontalx=horizontalx+1
                    
                bubble(list4,"down",x)
                
            else:
                  play(o+1,filled)  
                    
            i=random.randint(0,len(list4)-1)
            j=random.randint(0,len(list4)-1)
            filled=filled+1
            if filled>x*x:
                    replay(0)
            while list4[j][i]!=0:
                i=random.randint(0,len(list4)-1)
                j=random.randint(0,len(list4)-1)
            initialnumber = random.choice((4,2))
            list4[j][i]=initialnumber
            print "adding 1",filled
            update(x,list4,list5)
            play(o+1,filled)

        i=random.randint(0,len(list4)-1)
        j=random.randint(0,len(list4)-1)
        while list4[i][j]!=0:
            i=random.randint(0,len(list4)-1)
            j=random.randint(0,len(list4)-1)
        initialnumber = random.choice((4,2))
        list4[i][j]=initialnumber
        i=random.randint(0,len(list4)-1)
        j=random.randint(0,len(list4)-1)
        while list4[i][j]!=0:
            i=random.randint(0,len(list4)-1)
            j=random.randint(0,len(list4)-1)
        initialnumber = random.choice((2,4))
        list4[i][j]=initialnumber
        filled=filled+2
        print "should",filled
        update(x,list4,list5)

        play(o+1,filled)
        
        replay(1)
kanu(1)
