'''
Created on 2016. apr. 2.

@author: Zsiraf
'''
import CardsClass;
import copy;
import itertools;
from random import randint

def menu():
    print("1-es gomb jatek")
    print("2-es gomb kilepes")
    x=input()
    x=int(x);
    return x;

def game(table):
    print("\n")
    print(table[0]+"   "+table[1])
    print(table[2]+"   "+table[3]+"   "+table[4]+"   "+table[5]+"   "+table[6])
    print(table[7]+"   "+table[8])

    
def moneyinf(playermoney,computermoney,bet,isfirst,k):
    emel=500;
    conti="";
    print("A te penzed: "+str(playermoney))
    print("A gep penze: "+str(computermoney))
    print("A tet: "+str(bet))
    if(k%2==1):
        if(isfirst==1):
            print("A gep megadja!")
            computermoney=computermoney-sblind;
            bet=bet+sblind;
        print("1 - dobas \n2 - megadas \n3 - emeles " +str(emel)+"-al")
        s=input();
        s=int(s);
        if(s==1):
            computermoney=computermoney+bet;
            print("A gep nyert!");
            conti="continue";
        elif(s==2):
            pass
        elif(s==3):
            playermoney=playermoney-emel;
            bet=bet+emel;
            print("A gep tartja!")
            computermoney=computermoney-emel;
            bet=bet+emel;
            
            
    else:
        print("1 - dobas \n2 - megadas \n3 - emeles " +str(emel)+"-al")
        s=input();
        s=int(s);
        if(s==1):
            computermoney=computermoney+bet;
            print("A gep nyert!");
            conti="continue";
        elif(s==2):
            if(isfirst==1):
                playermoney=playermoney-sblind;
                bet=bet+sblind;
            else:
                pass
            print("A gep nem emel!")
        elif(s==3):
            if(isfirst==1):
                playermoney=playermoney-emel-sblind;
                bet=bet+sblind+emel;
            else:
                playermoney=playermoney-emel;
                bet=bet+emel;
            print("A gep tartja!")
            computermoney=computermoney-emel;
            bet=bet+emel;

    return playermoney,computermoney,bet,conti;
def evaluate(table):
    comppoints=0;
    finalcomppoints=0;
    finalplayerpoints=0;
    colors=[]
    numbers=[]

    for k in range(0,2):
    
        if(k==0):
            a0=table[0][:1]
            b0=int(table[0][1:])
            a1=table[1][:1]
            b1=int(table[1][1:])
        else:
            a0=table[7][:1]
            b0=int(table[7][1:])
            a1=table[8][:1]
            b1=int(table[8][1:])
        a2=table[2][:1]
        b2=int(table[2][1:])
        a3=table[3][:1]
        b3=int(table[3][1:])
        a4=table[4][:1]
        b4=int(table[4][1:])
        a5=table[5][:1]
        b5=int(table[5][1:])
        a6=table[6][:1]
        b6=int(table[6][1:])
        y=10;
        for j in range(0,3):
            if(j==0):
                iterlist=[(a2,b2),(a3,b3),(a4,b4),(a5,b5),(a6,b6)]
                iterlist=list(itertools.combinations(iterlist,3))
            else:
                y=5;
                iterlist=[(a2,b2),(a3,b3),(a4,b4),(a5,b5),(a6,b6)]
                iterlist=list(itertools.combinations(iterlist,4))
            for i in range(0,y):
        
                colors.clear()
                numbers.clear()
                
                if (j==0):
                    colors.append(a1)
                    colors.append(a0)
                elif(j==1):
                    colors.append(a0)
                    colors.append(iterlist[i][3][0])
                elif(j==2):
                    colors.append(a1)
                    colors.append(iterlist[i][3][0])
                colors.append(iterlist[i][0][0])
                colors.append(iterlist[i][1][0])
                colors.append(iterlist[i][2][0])
                #colors.append(a5)
                #colors.append(a6)
    
                if(j==0):
                    numbers.append(b0)
                    numbers.append(b1)
                elif(j==1):
                    numbers.append(iterlist[i][3][1])
                    numbers.append(b1)
                elif(j==2):
                    numbers.append(b0)
                    numbers.append(iterlist[i][3][1])
                numbers.append(iterlist[i][0][1])
                numbers.append(iterlist[i][1][1])
                numbers.append(iterlist[i][2][1])
                #numbers.append(b5)
                #numbers.append(b6)
                numbers.sort();
                #if all(x >= 2 for x in (A, B, C, D)):
                if (all(x in numbers for x in [1,10,11,12,13])) and (colors[0]==colors[1]==colors[2]==colors[3]==colors[4]):
                    comppoints=9;# royal flush
                elif colors[0]==colors[1]==colors[2]==colors[3]==colors[4] and numbers[0]+1==numbers[1] and numbers[1]+1==numbers[2] and numbers[2]+1==numbers[3] and numbers[3]+1==numbers[4]:
                    comppoints=8;#szinsor
                elif numbers.count(numbers[0])==4 or numbers.count(numbers[1])==4 or numbers.count(numbers[2])==4 or numbers.count(numbers[3])==4 or numbers.count(numbers[4])==4:
                    comppoints=7;#poker
                elif (numbers.count(numbers[0])==3 or numbers.count(numbers[1])==3 or numbers.count(numbers[2])==3 or numbers.count(numbers[3])==3 or numbers.count(numbers[4])==3) and (numbers.count(numbers[0])==2 or numbers.count(numbers[1])==2 or numbers.count(numbers[2])==2 or numbers.count(numbers[3])==2 or numbers.count(numbers[4])==2):
                    comppoints=6;#full house
                elif colors[0]==colors[1]==colors[2]==colors[3]==colors[4]:
                    comppoints=5;#flush
                elif (numbers[0]+1==numbers[1] and numbers[1]+1==numbers[2] and numbers[2]+1==numbers[3] and numbers[3]+1==numbers[4]) or (numbers==[1,10,11,12,13]):
                    comppoints=4;#sor
                elif numbers.count(numbers[0])==3 or numbers.count(numbers[1])==3 or numbers.count(numbers[2])==3 or numbers.count(numbers[3])==3 or numbers.count(numbers[4])==3:
                    comppoints=3;#drill
                elif (numbers[0]==numbers[1] and (numbers[2]==numbers[3] or numbers[3]==numbers[4])) or (numbers[1]==numbers[2] and numbers[3]==numbers[4]):
                    comppoints=2;#dupla par
                elif numbers.count(numbers[0])==2 or numbers.count(numbers[1])==2 or numbers.count(numbers[2])==2 or numbers.count(numbers[3])==2 or numbers.count(numbers[4])==2:
                    comppoints=1;#par
                else:
                    comppoints=0;#magas lap
                if(finalcomppoints<comppoints and k==0):
                    finalcomppoints=comppoints;
                elif(finalplayerpoints<comppoints and k!=0):
                    finalplayerpoints=comppoints;
    if(finalplayerpoints==finalcomppoints):
        verdict="Dontetlen!";
    elif(finalplayerpoints<finalcomppoints):
        verdict="A gep nyert!";
    else:
        verdict="Te nyertel!";
    return finalcomppoints,finalplayerpoints,verdict;


deck=[];
color="a";
num=0;
backupdeck=[]; 

'''
if (all(x in backupdeck for x in [1,10,11,12,13])) and (deck[0]==deck[1]==deck[2]==deck[3]==deck[4]):
        
    print("flush bazeg");

input(color);
'''

for i in range(0,52):
    if i==13:
        color="b";
        num=0
    elif i==26:
        color="c";
        num=0
    elif i==39:
        color="d"
        num=0;
    num=num+1;
    value="%s%i" %(color,num)
    x=CardsClass.Card(value)
    deck.append(x)


backupdeck=copy.deepcopy(deck);
    
# ez itt nem szukseges csak megadja melyik tomb elem minek felel meg a tablan
player1,player2,table1,table2,table3,table4,table5,comp1,comp2=("",)*9;
table=[];
table.append(comp1)
table.append(comp2)
table.append(table1)
table.append(table2)
table.append(table3)
table.append(table4)
table.append(table5)
table.append(player1)
table.append(player2)
'''
for i in range(0,52):
    print(deck[i].value)
'''
#a jatek
i=0;
s="";
k=0;
while(1):
    playermoney=10000;
    computermoney=10000;
    sblind=100;
    bblind=200;
    
    menudec=menu()
    if menudec==2:
        break
    elif menudec==1:
        print("A jatek indul!")
        while(k!=-1):
            k=k+1;
            i=0;
            bet=0;
            conti="";
            print("A te penzed: "+str(playermoney))
            print("A gep penze: "+str(computermoney))
            deck=copy.deepcopy(backupdeck);
            if(k%2==1):
                print("A gep az oszto!")
            else:
                print("Te vagy az oszto!")
            randtmp=51;
            
            
            #elso kor
            #osztas gepnek
            x=randint(0,randtmp)
            table[0]=deck[x].value;
            deck.pop(x);
            randtmp=randtmp-1
            
            x=randint(0,randtmp)
            table[1]=deck[x].value;
            deck.pop(x);
            randtmp=randtmp-1
            #osztas jatekosnak
            x=randint(0,randtmp)
            table[7]=deck[x].value;
            deck.pop(x);
            randtmp=randtmp-1
            
            x=randint(0,randtmp)
            table[8]=deck[x].value;
            deck.pop(x);
            randtmp=randtmp-1
            
            game(table);
            if(k%2==1):
                print("Te vagy a nagy vak -> "+str(bblind))
                print("A gep a kis vak -> "+str(sblind))
                playermoney=playermoney-bblind;
                computermoney=computermoney-sblind;
                bet=sblind+bblind;
            else:
                print("Te vagy a kis vak -> "+str(sblind))
                print("A gep a nagy vak -> "+str(bblind))
                playermoney=playermoney-sblind;
                computermoney=computermoney-bblind;
                bet=sblind+bblind;
                
            monreturn=moneyinf(playermoney, computermoney, bet,1,k)
            playermoney=monreturn[0]
            computermoney=monreturn[1]
            bet=monreturn[2]
            if(monreturn[3]=="continue"):
                continue
            
            
            #masodik kor
            #osztas kozepre
            
            while(i<3):
                x=randint(0,randtmp)
                table[i+2]=deck[x].value;
                deck.pop(x);
                randtmp=randtmp-1
                i=i+1;
                
            game(table);
            monreturn=moneyinf(playermoney, computermoney, bet,0,k)
            playermoney=monreturn[0]
            computermoney=monreturn[1]
            bet=monreturn[2]
            if(monreturn[3]=="continue"):
                continue


            
            x=randint(0,randtmp)
            table[5]=deck[x].value;
            deck.pop(x);
            randtmp=randtmp-1
            game(table);
            monreturn=moneyinf(playermoney, computermoney, bet,0,k)
            playermoney=monreturn[0]
            computermoney=monreturn[1]
            bet=monreturn[2]
            if(monreturn[3]=="continue"):
                continue
            
            x=randint(0,randtmp)
            table[6]=deck[x].value;
            deck.pop(x);
            game(table);
            monreturn=moneyinf(playermoney, computermoney, bet,0,k)
            playermoney=monreturn[0]
            computermoney=monreturn[1]
            bet=monreturn[2]
            if(monreturn[3]=="continue"):
                continue
            
            print("A szamitogep pontja: "+str(evaluate(table)[0]));
            print("A te pontod: "+str(evaluate(table)[1]));
            print(evaluate(table)[2]);
            if(evaluate(table)[2]=="Dontetlen!"):
                playermoney=playermoney+bet/2
                computermoney=computermoney+bet/2
            elif(evaluate(table)[2]=="A gep nyert!"):
                computermoney=computermoney+bet;
            elif(evaluate(table)[2]=="Te nyertel!"):
                playermoney=playermoney+bet;
            print("Kor vege! Kovetkezo kor indul!")
            for j in range(0,9):
                table[j]="";
            
            input()
    else:
        print("A megadott ertek nem ertelmezheto!")
