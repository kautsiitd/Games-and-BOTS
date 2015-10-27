from graphics import *
import random
x=input('enter grid lenth:')
y=input('win lenth:')
def kanu(o):
        list4=[[[0 for q in range(x)] for w in range(x)],[[0 for q in range(x)] for w in range(x)]]
        win = GraphWin("Tic Tac Toe", 50*(x+2), 50*(x+3))
        di=Text(Point((25*x+50),10),"!!!! Welcome to TIC TAC TOE !!!!")
        di.draw(win)
        di.setStyle('bold italic')
        di.setTextColor("purple")
        def main(i,j):
            ci = Rectangle(Point(50*i,50*j), Point((50*i)+50,(50*j)+50))
            ci.draw(win)
            ci.setWidth("3")
            ci.setOutline("blue")
        def grid(i,j):
            while j!=x+1:
                while i!=x+1:
                    main(i,j)
                    i=i+1
                i=1
                j=j+1
        grid(1,1)
        d1=Text(Point((25*x+50),50*(x+2)-10),"")
        d1.draw(win)
        d1.setStyle('bold italic')
        d1.setTextColor("red")
        def computer(first,list2,list3,list4,lastmovex,lastmovey,commovex,commovey):
                            a=canbewin(0,0,list2)
                            b=havetostop(0,0,list3)
                            chance_to_win=minimum(list2)
                            chance_to_stop=minimum(list3)
                            if perfectwin(0,0)!= False:
                                print '1'
                                (alongno,along)=perfectwin(0,0)
                                return (findempty(list4[1],alongno,along))
                            if a!= 'no' or b!= 'no':
                                if list2==[[x,x,x]]*(2*x+2):
                                        print '2'
                                        return findempty(list4[1],chance_to_stop[0],chance_to_stop[1])
                                elif list3==[[x,x,x,]]*(2*x+2):
                                        print '3'
                                        return findempty(list4[1],chance_to_win[0],chance_to_win[1])
                                elif chance_to_stop[2]<chance_to_win[2]:
                                        print '4'
                                        return findempty(list4[1],chance_to_stop[0],chance_to_stop[1])
                                else:
                                        print '5'
                                        return findempty(list4[1],chance_to_win[0],chance_to_win[1])
                            if makedoublecross(list4[1],commovex,commovey)!= False:
                                print '6'
                                return makedoublecross(list4[1],commovex,commovey)
                            if doublecross(lastmovex,lastmovey)!= False:
                                print '7'
                                return doublecross(lastmovex,lastmovey)
                            if triplewin(list4,commovex,commovey)!= 'no':
                                print '8'
                                return triplewin(list4,commovex,commovey)
                            if stoptriplewin(first,list4,lastmovex,lastmovey)!= 'no':
                                print '9'
                                return stoptriplewin(first,list4,lastmovex,lastmovey)
                            else:
                                print '10'
                                return (findcorner())
        def stoptriplewin(first,list4,lastmovex,lastmovey):
                            holes=calculate(list4[1],0,lastmovey-1,'row')
                            cross=calculate(list4[1],'cross',lastmovey-1,'row')
                            i=0
                            if lastmovex==-1 or first-o==2:
                                    return 'no'
                            if cross+2+(holes-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][lastmovey-1][i]==0:
                                                    list4[1][lastmovey-1][i]='cross'
                                                    if doublecross(i+1,lastmovey)!= False:
                                                            list4[1][lastmovey-1][i]=0
                                                            return lastmovey-1,i
                                                    else:
                                                            list4[1][lastmovey-1][i]=0
                                                            i=i+1
                                            else:
                                                    i=i+1
                            holesvertical=calculate(list4[1],0,lastmovex-1,'column')
                            crossvertical=calculate(list4[1],'cross',lastmovex-1,'column')
                            i=0
                            if crossvertical+2+(holesvertical-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][i][lastmovex-1]==0:
                                                    list4[1][i][lastmovex-1]='cross'
                                                    if doublecross(lastmovex,i+1)!= False:
                                                            list4[1][i][lastmovex-1]=0
                                                            return i,lastmovex-1
                                                    else:
                                                            list4[1][i][lastmovex-1]=0
                                                            i=i+1
                                            else:
                                                    i=i+1
                            holesdiagonal=calculate(list4[1],0,0,'d1')
                            crossdiagonal=calculate(list4[1],'cross',0,'d1')
                            i=0
                            j=0
                            if lastmovex==lastmovey and crossdiagonal+2+(holesdiagonal-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][i][j]==0:
                                                    list4[1][i][j]='cross'
                                                    if doublecross(j+1,i+1)!= False:
                                                            list4[1][i][j]=0
                                                            return i,j
                                                    else:
                                                            list4[1][i][j]=0
                                                            i=i+1
                                                            j=j+1
                                            else:
                                                    i=i+1
                                                    j=j+1
                            holesdiagonal2=calculate(list4[1],0,0,'d2')
                            crossdiagonal2=calculate(list4[1],'cross',0,'d2')
                            i=0
                            j=x-1
                            if lastmovex+lastmovey-1==x and crossdiagonal2+2+(holesdiagonal2-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][i][j]==0:
                                                    list4[1][i][j]='cross'
                                                    if doublecross(j+1,i+1)!= False:
                                                            list4[1][i][j]=0
                                                            return i,j
                                                    else:
                                                            list4[1][i][j]=0
                                                            i=i+1
                                                            j=j-1
                                            else:
                                                    i=i+1
                                                    j=j-1
                            return 'no'
        def triplewin(list4,commovex,commovey):
                            holes=calculate(list4[1],0,commovey-1,'row')
                            cross=calculate(list4[1],'circle',commovey-1,'row')
                            i=0
                            if commovex==-1:
                                    return 'no'
                            if cross+2+(holes-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][commovey-1][i]==0:
                                                    list4[1][commovey-1][i]='circle'
                                                    if makedoublecross(list4[1],i+1,commovey)!= False:
                                                            list4[1][commovey-1][i]=0
                                                            return commovey-1,i
                                                    else:
                                                            list4[1][commovey-1][i]=0
                                                            i=i+1
                                            else:
                                                    i=i+1
                                    
                            holesvertical=calculate(list4[1],0,commovex-1,'column')
                            crossvertical=calculate(list4[1],'circle',commovex-1,'column')
                            i=0
                            if crossvertical+2+(holesvertical-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][i][commovex-1]==0:
                                                    list4[1][i][commovex-1]='circle'
                                                    if makedoublecross(list4[1],commovex,i+1)!= False:
                                                            list4[1][i][commovex-1]=0
                                                            return i,commovex-1
                                                    else:
                                                            list4[1][i][commovex-1]=0
                                                            i=i+1
                                            else:
                                                    i=i+1
                            holesdiagonal=calculate(list4[1],0,0,'d1')
                            crossdiagonal=calculate(list4[1],'circle',0,'d1')
                            i=0
                            j=0
                            if commovex==commovey and crossdiagonal+2+(holesdiagonal-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][i][j]==0:
                                                    list4[1][i][j]='circle'
                                                    if makedoublecross(list4[1],j+1,i+1)!= False:
                                                            list4[1][i][j]=0
                                                            return i,j
                                                    else:
                                                            list4[1][i][j]=0
                                                            i=i+1
                                                            j=j+1
                                            else:
                                                    i=i+1
                                                    j=j+1
                            holesdiagonal2=calculate(list4[1],0,0,'d2')
                            crossdiagonal2=calculate(list4[1],'circle',0,'d2')
                            i=0
                            j=x-1
                            if commovex+commovey-1==x and crossdiagonal2+2+(holesdiagonal2-2)/2>=y:
                                    while i<len(list4[1]):
                                            if list4[1][i][j]==0:
                                                    list4[1][i][j]='circle'
                                                    if makedoublecross(list4[1],j+1,i+1)!= False:
                                                            list4[1][i][j]=0
                                                            return i,j
                                                    else:
                                                            list4[1][i][j]=0
                                                            i=i+1
                                                            j=j-1
                                            else:
                                                    i=i+1
                                                    j=j-1
                            return 'no'
        def makedoublecross(listx,commovex,commovey):
                            horizontalholes=calculate(listx,0,commovey-1,'row')
                            horizontalcross=calculate(listx,'circle',commovey-1,'row')
                            verticalholes=calculate(listx,0,commovex-1,'column')
                            verticalcross=calculate(listx,'circle',commovex-1,'column')
                            if commovex==-1 and commovey==-1:
                                    return False
                            if horizontalcross+2+(horizontalholes-2)/2==y:
                                    i=0
                                    k=0
                                    while i!=x:
                                            if listx[commovey-1][i]!=0:
                                                    i=i+1
                                                    continue
                                            elif i==commovey-1 and k==0:
                                                    d1holes=calculate(listx,0,0,'d1')
                                                    d1cross=calculate(listx,'circle',0,'d1')
                                                    if d1cross+2+(d1holes-2)/2==y:
                                                            return commovey-1,i
                                                    k=k+1
                                                    i=i
                                            elif commovey+i==x and (k==1 or k==0):
                                                    d2holes=calculate(listx,0,0,'d2')
                                                    d2cross=calculate(listx,'circle',0,'d2')
                                                    if d2cross+2+(d2holes-2)/2==y:
                                                            return commovey-1,i
                                                    k=k+1
                                                    i=i
                                            else:
                                                    crossholes=calculate(listx,0,i,'column')
                                                    crosscross=calculate(listx,'circle',i,'column')
                                                    if crosscross+2+(crossholes-2)/2==y:
                                                            return commovey-1,i
                                                    else:
                                                            i=i+1
                            if verticalcross+2+(verticalholes-2)/2==y:
                                    j=0
                                    k=0
                                    while j!=x:
                                            if listx[j][commovex-1]!=0:
                                                    j=j+1
                                                    continue
                                            elif j==commovex-1 and k==0:
                                                    d1holes=calculate(listx,0,0,'d1')
                                                    d1cross=calculate(listx,'circle',0,'d1')
                                                    if d1cross+2+(d1holes-2)/2==y:
                                                            return j,commovex-1
                                                    k=k+1
                                                    j=j
                                            elif commovex+j==x and (k==1 or k==0):
                                                    d2holes=calculate(listx,0,0,'d2')
                                                    d2cross=calculate(listx,'circle',0,'d2')
                                                    if d2cross+2+(d2holes-2)/2==y:
                                                            return j,commovex-1
                                                    k=k+1
                                                    j=j
                                            else: 
                                                    crossholes=calculate(listx,0,j,'row')
                                                    crosscross=calculate(listx,'circle',j,'row')
                                                    if crosscross+2+(crossholes-2)/2==y:
                                                            return j,commovex-1
                                                    else:
                                                            j=j+1
                            if commovex+commovey-1==x:
                                    d2holes=calculate(listx,0,0,'d2')
                                    d2cross=calculate(listx,'circle',0,'d2')
                                    if d2cross+2+(d2holes-2)/2==y:
                                            i=x-1
                                            j=0
                                            while i!=-1:
                                                    doublecrosshorizontalholes=calculate(listx,0,j,'row')
                                                    doublecrosshorizontalcross=calculate(listx,'circle',j,'row')
                                                    doublecrossverticalholes=calculate(listx,0,i,'column')
                                                    doublecrossverticalcross=calculate(listx,'circle',i,'column')
                                                    if doublecrosshorizontalcross+2+(doublecrosshorizontalholes-2)/2==y and list4[1][j][i]==0:
                                                            if listx[j][i]==0:
                                                                    return j,i
                                                    if doublecrossverticalcross+2+(doublecrossverticalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    else:
                                                            i=i-1
                                                            j=j+1
                            if commovex==commovey:
                                    d1holes=calculate(listx,0,0,'d1')
                                    d1cross=calculate(listx,'circle',0,'d1')
                                    if d1cross+2+(d1holes-2)/2==y:
                                            i=x-1
                                            j=x-1
                                            while i!=-1:
                                                    doublecrosshorizontalholes=calculate(listx,0,j,'row')
                                                    doublecrosshorizontalcross=calculate(listx,'circle',j,'row')
                                                    doublecrossverticalholes=calculate(listx,0,i,'column')
                                                    doublecrossverticalcross=calculate(listx,'circle',i,'column')
                                                    if doublecrosshorizontalcross+2+(doublecrosshorizontalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    if doublecrossverticalcross+2+(doublecrossverticalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    else:
                                                            i=i-1
                                                            j=j-1
                            return False
        def doublecross(lastmovex,lastmovey):
                            horizontalholes=calculate(list4[1],0,lastmovey-1,'row')
                            horizontalcross=calculate(list4[1],'cross',lastmovey-1,'row')
                            verticalholes=calculate(list4[1],0,lastmovex-1,'column')
                            verticalcross=calculate(list4[1],'cross',lastmovex-1,'column')
                            if lastmovex==-1 and lastmovey==-1:
                                    return False
                            if horizontalcross+2+(horizontalholes-2)/2==y:
                                    i=0
                                    k=0
                                    while i!=x:
                                            if list4[1][lastmovey-1][i]!=0:
                                                    i=i+1
                                                    continue
                                            elif i==lastmovey-1 and k==0:
                                                    d1holes=calculate(list4[1],0,0,'d1')
                                                    d1cross=calculate(list4[1],'cross',0,'d1')
                                                    if d1cross+2+(d1holes-2)/2==y:
                                                            return lastmovey-1,i
                                                    k=k+1
                                                    i=i
                                            elif lastmovey+i==x and (k==1 or k==0):
                                                    d2holes=calculate(list4[1],0,0,'d2')
                                                    d2cross=calculate(list4[1],'cross',0,'d2')
                                                    if d2cross+2+(d2holes-2)/2==y:
                                                            return lastmovey-1,i
                                                    k=k+1
                                                    i=i
                                            else:
                                                    crossholes=calculate(list4[1],0,i,'column')
                                                    crosscross=calculate(list4[1],'cross',i,'column')
                                                    if crosscross+2+(crossholes-2)/2==y:
                                                            return lastmovey-1,i
                                                    else:
                                                            i=i+1
                            if verticalcross+2+(verticalholes-2)/2==y:
                                    j=0
                                    k=0
                                    while j!=x:
                                            if list4[1][j][lastmovex-1]!=0:
                                                    j=j+1
                                                    continue
                                            elif j==lastmovex-1 and k==0:
                                                    d1holes=calculate(list4[1],0,0,'d1')
                                                    d1cross=calculate(list4[1],'cross',0,'d1')
                                                    if d1cross+2+(d1holes-2)/2==y:
                                                            return j,lastmovex-1
                                                    k=k+1
                                                    j=j
                                            elif lastmovex+j==x and (k==1 or k==0):
                                                    d2holes=calculate(list4[1],0,0,'d2')
                                                    d2cross=calculate(list4[1],'cross',0,'d2')
                                                    if d2cross+2+(d2holes-2)/2==y:
                                                            return j,lastmovex-1
                                                    k=k+1
                                                    j=j
                                            else: 
                                                    crossholes=calculate(list4[1],0,j,'row')
                                                    crosscross=calculate(list4[1],'cross',j,'row')
                                                    if crosscross+2+(crossholes-2)/2==y:
                                                            return j,lastmovex-1
                                                    else:
                                                            j=j+1
                            if lastmovex+lastmovey-1==x:
                                    d2holes=calculate(list4[1],0,0,'d2')
                                    d2cross=calculate(list4[1],'cross',0,'d2')
                                    if d2cross+2+(d2holes-2)/2==y:
                                            i=x-1
                                            j=0
                                            while i!=-1:
                                                    doublecrosshorizontalholes=calculate(list4[1],0,j,'row')
                                                    doublecrosshorizontalcross=calculate(list4[1],'cross',j,'row')
                                                    doublecrossverticalholes=calculate(list4[1],0,i,'column')
                                                    doublecrossverticalcross=calculate(list4[1],'cross',i,'column')
                                                    if doublecrosshorizontalcross+2+(doublecrosshorizontalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    elif doublecrossverticalcross+2+(doublecrossverticalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    else:
                                                            i=i-1
                                                            j=j+1
                            if lastmovex==lastmovey:
                                    d1holes=calculate(list4[1],0,0,'d1')
                                    d1cross=calculate(list4[1],'cross',0,'d1')
                                    if d1cross+2+(d1holes-2)/2==y:
                                            i=x-1
                                            j=x-1
                                            while i!=-1:
                                                    doublecrosshorizontalholes=calculate(list4[1],0,j,'row')
                                                    doublecrosshorizontalcross=calculate(list4[1],'cross',j,'row')
                                                    doublecrossverticalholes=calculate(list4[1],0,i,'column')
                                                    doublecrossverticalcross=calculate(list4[1],'cross',i,'column')
                                                    if doublecrosshorizontalcross+2+(doublecrosshorizontalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    elif doublecrossverticalcross+2+(doublecrossverticalholes-2)/2==y and list4[1][j][i]==0:
                                                                    return j,i
                                                    else:
                                                            i=i-1
                                                            j=j-1
                            return False
        def minimum(alist):
                            i=0
                            n=[x,x,x]
                            while i!=2*x+2:
                                if alist[i][2]<n[2]:
                                        n=alist[i]
                                        i=i+1
                                else:
                                        i=i+1
                            return n
        def perfectwin(i,j):
                            while j!=len(list4[1]):
                                holes=calculate(list4[1],0,j,'row')
                                cross=calculate(list4[1],'circle',j,'row')
                                if cross>=y-1 and holes>=1:
                                    return (j,'row')
                                else:
                                    j=j+1
                            while i!=len(list4[1]):
                                holes=calculate(list4[1],0,i,'column')
                                cross=calculate(list4[1],'circle',i,'column')
                                if cross>=y-1 and holes>=1:
                                    return (i,'column')
                                else:
                                    i=i+1
                            holes=calculate(list4[1],0,0,'d1')
                            cross=calculate(list4[1],'circle',0,'d1')
                            if cross>=y-1 and holes>=1:
                                return (0,'d1')
                            holes=calculate(list4[1],0,0,'d2')
                            cross=calculate(list4[1],'circle',0,'d2')
                            if cross>=y-1 and holes>=1:
                                return (0,'d2')
                            return False
        def canbewin(i,j,list2):
                            operate=0
                            while j!=len(list4[1]):
                                holes=calculate(list4[1],0,j,'row')
                                cross=calculate(list4[1],'circle',j,'row')
                                if cross+1+(holes-1)/2>=y:
                                    list2[j]=[j,'row',(holes-1)/2]
                                    operate=operate+1
                                    j=j+1
                                if cross+1+(holes-1)/2<y:
                                    j=j+1
                            while i!=len(list4[1]):
                                holes=calculate(list4[1],0,i,'column')
                                cross=calculate(list4[1],'circle',i,'column')
                                if cross+1+(holes-1)/2>=y:
                                    list2[i+x]=[i,'column',(holes-1)/2]
                                    operate=operate+1
                                    i=i+1
                                if cross+1+(holes-1)/2<y:
                                    i=i+1
                            holes=calculate(list4[1],0,0,'d1')
                            cross=calculate(list4[1],'circle',0,'d1')
                            if cross+1+(holes-1)/2>=y:
                                list2[2*x]=[0,'d1',(holes-1)/2]
                                operate=operate+1
                            holes=calculate(list4[1],0,0,'d2')
                            cross=calculate(list4[1],'circle',0,'d2')
                            if cross+1+(holes-1)/2>=y:
                                list2[2*x+1]=[0,'d2',(holes-1)/2]
                                operate=operate+1
                            if operate==0:
                                return 'no'
        def findempty(listx,alongno,along):
                            if along == 'row':
                                i=0
                                while i!=len(listx):
                                    if listx[alongno][i]==0:
                                        return alongno,i
                                    else:
                                        i=i+1
                            elif along == 'column':
                                j=0
                                n=0
                                while j!=len(listx):
                                    if listx[j][alongno]==0:
                                        return j,alongno
                                    else:
                                        j=j+1
                                return n
                            elif along == 'd1':
                                i=0
                                j=0
                                n=0
                                while i!=len(listx):
                                    if listx[j][i]==0:
                                        return j,i
                                    else:
                                        j=j+1
                                        i=i+1
                                return n
                            else:
                                i=0
                                j=len(listx)-1
                                n=0
                                while i!=len(listx):
                                    if listx[j][i]==0:
                                        return j,i
                                    else:
                                        j=j-1
                                        i=i+1
                                return n
        def havetostop(i,j,list3):
                                operating=0
                                while j!=len(list4[1]):
                                    holes=calculate(list4[1],0,j,'row')
                                    cross=calculate(list4[1],'cross',j,'row')
                                    if cross+1+(holes-1)/2>=y:
                                        list3[j]=[j,'row',(holes-1)/2]
                                        operating=operating+1
                                        j=j+1
                                    if cross+1+(holes-1)/2<y:
                                        j=j+1
                                while i!=len(list4[1]):
                                    holes=calculate(list4[1],0,i,'column')
                                    cross=calculate(list4[1],'cross',i,'column')
                                    if cross+1+(holes-1)/2>=y:
                                        list3[i+x]=[i,'column',(holes-1)/2]
                                        operating=operating+1
                                        i=i+1
                                    if cross+1+(holes-1)/2<y:
                                        i=i+1
                                holes=calculate(list4[1],0,0,'d1')
                                cross=calculate(list4[1],'cross',0,'d1')
                                if cross+1+(holes-1)/2>=y:
                                    list3[2*x]=[0,'d1',(holes-1)/2]
                                    operating=operating+1
                                holes=calculate(list4[1],0,0,'d2')
                                cross=calculate(list4[1],'cross',0,'d2')
                                if cross+1+(holes-1)/2>=y:
                                    list3[2*x+1]=[0,'d2',(holes-1)/2]
                                    operating=operating+1
                                holes=calculate(list4[1],0,0,'d1')
                                cross=calculate(list4[1],'cross',0,'d1')
                                if operating==0:
                                    return 'no'
        def findcorner():
                            if o%2==1 and x%2==1 and list4[1][(x)/2][(x)/2]==0:
                                return (x)/2,(x)/2
                            elif list4[1][0][0]==0:
                                return 0,0
                            elif list4[1][len(list4[1])-1][0]==0:
                                return len(list4[1])-1,0
                            elif list4[1][len(list4[1])-1][len(list4[1])-1]==0:
                                return len(list4[1])-1,len(list4[1])-1
                            elif list4[1][0][len(list4[1])-1]==0:
                                return 0,len(list4[1])-1
                            else:
                                j=random.randint(0,len(list4[1])-1)
                                i=random.randint(0,len(list4[1])-1)
                                if list4[1][j][i]==0:
                                        return j,i
                                else:
                                        return findcorner()
        def calculate(listx,element,alongno,along):
                            if along == 'row':
                                i=0
                                n=0
                                while i!=len(listx):
                                    if listx[alongno][i]==element:
                                        n=n+1
                                        i=i+1
                                    else:
                                        i=i+1
                                return n
                            elif along == 'column':
                                j=0
                                n=0
                                while j!=len(listx):
                                    if listx[j][alongno]==element:
                                        n=n+1
                                        j=j+1
                                    else:
                                        j=j+1
                                return n
                            elif along == 'd1':
                                i=0
                                j=0
                                n=0
                                while i!=len(listx):
                                    if listx[j][i]==element:
                                        n=n+1
                                        j=j+1
                                        i=i+1
                                    else:
                                        j=j+1
                                        i=i+1
                                return n
                            else:
                                i=0
                                j=len(listx)-1
                                n=0
                                while i!=len(listx):
                                    if listx[j][i]==element:
                                        n=n+1
                                        j=j-1
                                        i=i+1
                                    else:
                                        j=j-1
                                        i=i+1
                                return n

        def play(i,lastmovex,lastmovey,commovex,commovey):
            if i%2==0:
                d1.setText("your move")
            if i%2==1:
                d1.setText("computer is thinking")
            if i%2==0:
                    m=win.getMouse()
                    column_no=(m.x)/50
                    row_no=(m.y)/50
                    if 50<=m.x<=50*(x+1) and 50<=m.y<=50*(x+1):
                        if list4[1][row_no-1][column_no-1]=='circle' or list4[1][row_no-1][column_no-1]=='cross':
                            e = GraphWin("ERROR!", 500, 50)
                            d=Text(Point(250,10),"This place is already occupied, pls. try again")
                            d.draw(e)
                            d.setStyle('bold italic')
                            d.setTextColor("red")
                            e.getMouse()
                            e.close()
                            print 'This place is already occupied, pls. try again'
                            play(i,lastmovex,lastmovey,commovex,commovey)
                        else:
                            l = Line(Point(50*column_no+10,50*row_no+10),Point(50*(column_no+1)-10,50*(row_no+1)-10))
                            l.draw(win)
                            l.setWidth("5")
                            l.setOutline("red")
                            k=Line(Point(50*(column_no+1)-10,50*row_no+10),Point(50*(column_no)+10,50*(row_no+1)-10))
                            k.draw(win)
                            k.setWidth("5")
                            k.setOutline("red")
                            list4[1][row_no-1][column_no-1]='cross'
                            list4[0][row_no-1][column_no-1]='cross'
                            if result('cross','circle',column_no,row_no)==1:
                                d=Text(Point((25*x+50),50*(x+3)-10),"!!!! Congrats, You Win !!!!")
                                d.draw(win)
                                d.setStyle('bold italic')
                                d.setTextColor("purple")
                                d1.setText("!!!! Congrats, You Win !!!!")
                                print 'cross win'
                            elif i-o==x*x:
                                d=Text(Point((25*x+50),50*(x+3)-10),"!!!! Game Is Tie !!!!")
                                d.draw(win)
                                d.setStyle('bold italic')
                                d.setTextColor("purple")
                                d1.setText("")
                                print 'game is tie'
                            else:
                                play(i+1,column_no,row_no,commovex,commovey)
                    else:
                        e = GraphWin("ERROR!", 500, 50)
                        d=Text(Point(250,10),"Out of board, pls. try again")
                        d.draw(e)
                        d.setStyle('bold italic')
                        d.setTextColor("red")
                        e.getMouse()
                        e.close()
                        d1.setText("click on screen in error window")
                        print 'Out of board, pls. try again'
                        play(i,lastmovex,lastmovey,commovex,commovey)
            else :
                        time.sleep(.5)
                        list4[0]=list4[1][ :len(list4[1])]
                        list2=[[x,x,x]]*(2*x+2)
                        list3=[[x,x,x]]*(2*x+2)
                        (row_nox,column_nox) = computer(i,list2,list3,list4,lastmovex,lastmovey,commovex,commovey)
                        c = Circle(Point((50*(column_nox+1)+25),(50*(row_nox+1)+25)), 15)
                        c.draw(win)
                        c.setWidth("5")
                        c.setOutline("orange")
                        list4[1][row_nox][column_nox]='circle'
                        list4[0][row_nox][column_nox]='circle'
                        if result('circle','cross',column_nox+1,row_nox+1)==1:
                                d=Text(Point((25*x+50),50*(x+3)-10),"!!!! Oops, You Loss !!!!")
                                d.draw(win)
                                d.setStyle('bold italic')
                                d.setTextColor("purple")
                                d1.setText("")
                                print 'circle win'
                        elif i-o==x*x:
                                d=Text(Point((25*x+50),50*(x+3)-10),"!!!! Game Is Tie !!!!")
                                d.draw(win)
                                d.setStyle('bold italic')
                                d.setTextColor("purple")
                                d1.setText("")
                                print 'game is tie'
                        else:
                                play(i+1,0,0,column_nox+1,row_nox+1)
        def along_x(r,i,row_no):
            n=0
            while i!=x:
                if list4[1][row_no-1][i]==r:
                        n=n+1
                        if n==y:
                                d=0
                                while d!=x:
                                        if list4[1][row_no-1][d]==r:
                                                c = Rectangle(Point(50*(d+1),50*(row_no)), Point((50*(d+1))+50,(50*(row_no))+50))
                                                c.draw(win)
                                                c.setFill("green")
                                                c.setWidth("3")
                                                c.setOutline("blue")
                                                if r=='circle':
                                                        g = Circle(Point((50*(d+1)+25),(50*row_no+25)), 15)
                                                        g.draw(win)
                                                        g.setWidth("5")
                                                        g.setOutline("orange")
                                                else:
                                                        l = Line(Point(50*(d+1)+10,50*row_no+10),Point(50*(d+2)-10,50*(row_no+1)-10))
                                                        l.draw(win)
                                                        l.setWidth("5")
                                                        l.setOutline("red")
                                                        k=Line(Point(50*(d+2)-10,50*row_no+10),Point(50*(d+1)+10,50*(row_no+1)-10))
                                                        k.draw(win)
                                                        k.setWidth("5")
                                                        k.setOutline("red")
                                                d=d+1
                                        else:
                                                d=d+1
                                return 'yes'
                        else:
                                i=i+1
                else:
                        i=i+1
        def along_y(r,i,column_no):
            n=0
            while i!=x:
                if list4[1][i][column_no-1]==r:
                        n=n+1
                        if n==y:
                                d=0
                                while d!=x:
                                        if list4[1][d][column_no-1]==r:
                                                c = Rectangle(Point(50*(column_no),50*(d+1)), Point((50*(column_no))+50,(50*(d+1))+50))
                                                c.draw(win)
                                                c.setFill("green")
                                                c.setWidth("3")
                                                c.setOutline("blue")
                                                if r=='circle':
                                                        g = Circle(Point((50*(column_no)+25),(50*(d+1)+25)), 15)
                                                        g.draw(win)
                                                        g.setWidth("5")
                                                        g.setOutline("orange")
                                                else:
                                                        l = Line(Point(50*(column_no)+10,50*(d+1)+10),Point(50*(column_no+1)-10,50*(d+2)-10))
                                                        l.draw(win)
                                                        l.setWidth("5")
                                                        l.setOutline("red")
                                                        k=Line(Point(50*(column_no+1)-10,50*(d+1)+10),Point(50*(column_no)+10,50*(d+2)-10))
                                                        k.draw(win)
                                                        k.setWidth("5")
                                                        k.setOutline("red")
                                                d=d+1
                                        else:
                                                d=d+1
                                return 'yes'
                        else:
                                i=i+1
                else:
                        i=i+1
        def along_d1(r,i):
            n=0
            while i!=x:
                if list4[1][i][i]==r:
                        n=n+1
                        if n==y:
                                d=0
                                while d!=x:
                                        if list4[1][d][d]==r:
                                                c = Rectangle(Point(50*(d+1),50*(d+1)), Point((50*(d+1))+50,(50*(d+1))+50))
                                                c.draw(win)
                                                c.setFill("green")
                                                c.setWidth("3")
                                                c.setOutline("blue")
                                                if r=='circle':
                                                        g = Circle(Point((50*(d+1)+25),(50*(d+1)+25)), 15)
                                                        g.draw(win)
                                                        g.setWidth("5")
                                                        g.setOutline("orange")
                                                else:
                                                        l = Line(Point(50*(d+1)+10,50*(d+1)+10),Point(50*(d+2)-10,50*(d+2)-10))
                                                        l.draw(win)
                                                        l.setWidth("5")
                                                        l.setOutline("red")
                                                        k=Line(Point(50*(d+2)-10,50*(d+1)+10),Point(50*(d+1)+10,50*(d+2)-10))
                                                        k.draw(win)
                                                        k.setWidth("5")
                                                        k.setOutline("red")
                                                d=d+1
                                        else:
                                                d=d+1
                                return 'yes'
                        else:
                                i=i+1
                else:
                        i=i+1
        def along_d2(r,i):
            n=0
            while i!=x:
                if list4[1][i][x-1-i]==r:
                        n=n+1
                        if n==y:
                                d=0
                                while d!=x:
                                        if list4[1][d][x-d-1]==r:
                                                c = Rectangle(Point(50*(x-d),50*(d+1)), Point((50*(x-d))+50,(50*(d+1))+50))
                                                c.draw(win)
                                                c.setFill("green")
                                                c.setWidth("3")
                                                c.setOutline("blue")
                                                if r=='circle':
                                                        g = Circle(Point((50*(x-d)+25),(50*(d+1)+25)), 15)
                                                        g.draw(win)
                                                        g.setWidth("5")
                                                        g.setOutline("orange")
                                                else:
                                                        l = Line(Point(50*(x-d)+10,50*(d+1)+10),Point(50*(x-d+1)-10,50*(d+2)-10))
                                                        l.draw(win)
                                                        l.setWidth("5")
                                                        l.setOutline("red")
                                                        k=Line(Point(50*(x-d+1)-10,50*(d+1)+10),Point(50*(x-d)+10,50*(d+2)-10))
                                                        k.draw(win)
                                                        k.setWidth("5")
                                                        k.setOutline("red")
                                                d=d+1
                                        else:
                                                d=d+1
                                return 'yes'
                        else:
                                i=i+1
                else:
                        i=i+1
        def result(r,j,column_no,row_no):
            if along_x(r,0,row_no) == 'yes' or along_y(r,0,column_no) == 'yes' or along_d1(r,0)=='yes' or along_d2(r,0)=='yes':
                return 1
            else:
                return 0
        play(o+1,-1,-1,-1,-1)
        def replay(i):
                ci = Rectangle(Point(50*(x),50*(x+2)-30), Point(50*x+50,50*(x+2)-10))
                ci.draw(win)
                ci.setWidth("3")
                ci.setOutline("blue")
                d=Text(Point(50*x+25,50*(x+2)-20),"exit")
                d.draw(win)
                d.setStyle('bold italic')
                d.setTextColor("red")
                ci = Rectangle(Point(50,50*(x+2)-30), Point(100,50*(x+2)-10))
                ci.draw(win)
                ci.setWidth("3")
                ci.setOutline("blue")
                d=Text(Point(75,50*(x+2)-20),"replay")
                d.draw(win)
                d.setStyle('bold italic')
                d.setTextColor("red")
                m=win.getMouse()
                if 50*x<=m.x<=50*(x+1) and 50*(x+2)-30<=m.y<=50*(x+2)-10:
                        win.close()
                elif 50<=m.x<=100 and 50*(x+2)-30<=m.y<=50*(x+2)-10:
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
        replay(1)
kanu(1)

