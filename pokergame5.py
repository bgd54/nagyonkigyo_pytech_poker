import pokergui5
import tkMessageBox
import copy;
import itertools;
from random import randint
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "poker")+os.path.sep


def savegame():
    
    file_save=open(path+"pokersave.txt","w")
    file_save.write("My_first_card: "+pokergui5.mycards[0]+"\n")
    file_save.write("My_second_card: "+pokergui5.mycards[1]+"\n")

    file_save.write("Others_first_card: "+pokergui5.othercards[0]+"\n")
    file_save.write("Others_second_card: "+pokergui5.othercards[1]+"\n")
    
    file_save.write("Main1: " + pokergui5.maincards[0]+"\n")
    file_save.write("Main1_state "+pokergui5.card1.cget("text")+"\n")
   
    file_save.write("Main2: " + pokergui5.maincards[1]+"\n")
    file_save.write("Main2_state "+pokergui5.card2.cget("text")+"\n")
   
    file_save.write("Main3: " + pokergui5.maincards[2]+"\n")
    file_save.write("Main3_state "+pokergui5.card3.cget("text")+"\n")
   
    file_save.write("Main4: " + pokergui5.maincards[3]+"\n")
    file_save.write("Main4_state "+pokergui5.card4.cget("text")+"\n")
   
    file_save.write("Main5: " + pokergui5.maincards[4]+"\n")
    file_save.write("Main5_state "+pokergui5.card5.cget("text")+"\n")
   

def opengame():

    pokergui5.showbutton1.config(state="normal")
    del pokergui5.maincards[:]
    del pokergui5.othercards[:]
    del pokergui5.mycards[:]

    states = []
    
    try:
    
        file_open = open(path+"pokersave.txt","r")
        for line in file_open.readlines():
            
            if "My" in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                pokergui5.mycards.append(card)

            elif "Others" in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                pokergui5.othercards.append(card)

            elif "Main" in line and "state" not in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                pokergui5.maincards.append(card)

            elif "state" in line:

                line = line.rstrip("\n")
                state = line.split(" ")[1]
                states.append(state)
                

        pokergui5.gameopen1(pokergui5.maincards,pokergui5.mycards,pokergui5.othercards,states)
                        
    except IOError:
        tkMessageBox.showerror ("No file", "No saved game found")
        
    

def newgame():
    
    if pokergui5.language == ['english']:
        answer = tkMessageBox.askquestion("New Game", "Are You Sure?", icon="warning")
    elif pokergui5.language == ['hungarian']:
        answer = tkMessageBox.askquestion("Uj jatek", "Biztos?", icon="warning")

    if answer == "yes":

        if pokergui5.language == ['english']:
            answer2 = tkMessageBox.askquestion("Save", "Save game first?", icon="warning")
        elif pokergui5.language == ['hungarian']:
            answer2 = tkMessageBox.askquestion("Mentes", "Mentsem a jelenlegi jatekot?", icon="warning")
            
        if answer2 == "yes":
            savegame()
            pokergui5.game1()
        else:
            
            pokergui5.game1()
            

def showmaincards(**options):

    if options.get("type1") == "flop":

        pokergui5.card1.config(image=pokergui5.cardpictures2[0],text="face")
        pokergui5.card2.config(image=pokergui5.cardpictures2[1],text="face")
        pokergui5.card3.config(image=pokergui5.cardpictures2[2],text="face")
        

    elif options.get("type1") == "turn":

        pokergui5.card4.config(image=pokergui5.cardpictures2[3],text="face")

    elif options.get("type1") == "river":

        pokergui5.card5.config(image=pokergui5.cardpictures2[4],text="face")

    pokergui5.playsound(type1="3")

def showmycards():

    pokergui5.card_mine1.config(image=pokergui5.cardpictures[0])
    pokergui5.card_mine2.config(image=pokergui5.cardpictures[1])
    pokergui5.playsound(type1="3")
    pokergui5.infolabel.config(text="")

def putmaincards():

    pokergui5.cards1.lift()
    pokergui5.cards2.lift()
    pokergui5.cards3.lift()
    pokergui5.cards4.lift()
    pokergui5.cards5.lift()
    pokergui5.cards_mine.lift()
    pokergui5.cards_others.lift()

    


def round_start():

    player_money = int(pokergui5.label_sum.cget("text").split(" ")[2])
    bot_money = int(pokergui5.label_sum_bot.cget("text").split(" ")[3])
    pokergui5.game1()
    pokergui5.label_sum.config(text="You have "+str(player_money)+" tokens")
    pokergui5.label_sum_bot.config(text="The bot has "+str(bot_money)+" tokens")
     
    pokergui5.all_bet.config(text="0")
    pokergui5.mycardsbutton.config(state="disabled")
    pokergui5.showbutton2.config(state="disabled")
    putmaincards()

    # lenullazzuk a teteket

    pokergui5.all_bet_playerlabel.config(text="0")
    pokergui5.all_bet_botlabel.config(text="0")
    pokergui5.all_bet.config(text="0")
    
    kisvak1 =  pokergui5.kisvak.cget("text")
    nagyvak1 =  pokergui5.nagyvak.cget("text")
    if kisvak1 =="player":
        pokergui5.kisvak.config(text="bot")
        pokergui5.nagyvak.config(text="player")
        pokergui5.giveButton.config(state="normal")
        pokergui5.giveButton2.config(state="disabled")
        pokergui5.infolabel.config(text="You are the big blind")
        
    else:
        pokergui5.kisvak.config(text="player")
        pokergui5.nagyvak.config(text="bot")
        # give(who="bot")
        pokergui5.giveButton2.config(state="normal")
        pokergui5.giveButton.config(state="disabled")
        pokergui5.infolabel.config(text="You are the small blind")

    
    pokergui5.raiseButton.config(state="disabled")
    pokergui5.throwButton.config(state="disabled")

    
    pokergui5.raiseButton2.config(state="disabled")
    pokergui5.throwButton2.config(state="disabled")

def round_over(case):

    # vege az adott kornek

    # az osszes lapot felforditjuk, ami meg nincs felforditva (a feltetelt akar ki is lehetne hagyni)

    if pokergui5.card1.cget("text") == "back":    
        pokergui5.card1.config(image=pokergui5.cardpictures2[0],text="face")
    if pokergui5.card2.cget("text") == "back":
        pokergui5.card2.config(image=pokergui5.cardpictures2[1],text="face")
    if pokergui5.card3.cget("text") == "back":
        pokergui5.card3.config(image=pokergui5.cardpictures2[2],text="face")
    if pokergui5.card4.cget("text") == "back":
        pokergui5.card4.config(image=pokergui5.cardpictures2[3],text="face")
    if pokergui5.card5.cget("text") == "back":
        pokergui5.card5.config(image=pokergui5.cardpictures2[4],text="face")

    pokergui5.card_others1.config(image=pokergui5.cardpictures3[0])
    pokergui5.card_others2.config(image=pokergui5.cardpictures3[1])

    pokergui5.card_mine1.config(image=pokergui5.cardpictures[0])
    pokergui5.card_mine2.config(image=pokergui5.cardpictures[1])  
    
    
    # letiltjuk a megad - emel - eldob gombokat a kovetkezo korig
    
    pokergui5.giveButton.config(state="disabled")
    pokergui5.raiseButton.config(state="disabled")
    pokergui5.throwButton.config(state="disabled")

    pokergui5.giveButton2.config(state="disabled")
    pokergui5.raiseButton2.config(state="disabled")
    pokergui5.throwButton2.config(state="disabled")

    # lapok felforditasanak hangja
    
    pokergui5.playsound(type1="3")

    # megnezzuk, ki nyert

    bet = int(pokergui5.all_bet.cget("text"))

    if case == "throw_player":


            bot_money = int(pokergui5.label_sum_bot.cget("text").split(" ")[3]) + bet
            
            pokergui5.label_sum_bot.config(text="The bot has "+str(bot_money)+" tokens")
            pokergui5.infolabel.config(text="A gep nyert!")

    elif case == "throw_bot":
        
            player_money = int(pokergui5.label_sum.cget("text").split(" ")[2]) + bet
            pokergui5.label_sum.config(text="You have "+str(player_money)+" tokens")
            pokergui5.infolabel.config(text="Te nyertel!")

    elif case == "evaluate":
      

        table = pokergui5.othercards + pokergui5.maincards + pokergui5.mycards     
        
        evaluate(table)


    # uj kor kezdese

    pokergui5.showbutton2.config(state='normal')

def moneyinf(s,who):

    money1 =  pokergui5.label_sum_bot.cget("text").split(" ")
    bot_money = int(money1[3])
    money2 =  pokergui5.label_sum.cget("text").split(" ")
    player_money = int(money2[2])
    bet = int(pokergui5.all_bet.cget("text"))
    player_bet = int(pokergui5.all_bet_playerlabel.cget("text"))
    bot_bet = int(pokergui5.all_bet_botlabel.cget("text"))

    kisvak = pokergui5.kisvak.cget("text")
    nagyvak = pokergui5.nagyvak.cget("text")


    # feladjuk, a bot kapja a tetet
    
    if(s==1):

        round_over("throw_"+who)
        

    # tartjuk/megadjuk
        
    elif(s==2):
        
        if who == "player":

            # ha a kisvak tetet kell betenni
            
            if player_bet == 0 and bot_bet == 200:
                
                player_money -= 100
                player_bet += 100
                pokergui5.mycardsbutton.config(state="normal")
                pokergui5.infolabel.config(text="look at your cards")

            else:

                # a jatekos gombjainak tiltasa
                
                pokergui5.giveButton.config(state="disabled")
                pokergui5.raiseButton.config(state="disabled")
                pokergui5.throwButton.config(state="disabled")

                # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

                pokergui5.giveButton2.config(state="normal")
                pokergui5.raiseButton2.config(state="normal")
                pokergui5.throwButton2.config(state="normal")

                # ha a nagyvakot kell betenni
                
                if player_bet == 0 and bot_bet == 0:
                    player_money -= 200
                    player_bet += 200
                    pokergui5.mycardsbutton.config(state="normal")


                elif player_bet == 100 and bot_bet == 200:
                    player_money -= 100
                    player_bet += 100

                    if kisvak == who:
        
                        continue1()
                    

                elif player_bet <= bot_bet:

                    if kisvak == who:
        
                        continue1()

                    player_money -= bot_bet-player_bet
                    player_bet += bot_bet-player_bet

                
            pokergui5.all_bet_playerlabel.config(text=player_bet)

            # send_to_bot("adas",player_money,player_bet,bot_money,bot_bet)
            

        elif who == "bot":

            if bot_bet == 0 and player_bet == 200:
                bot_money -= 100
                bot_bet += 100

            else:
                
                # a jatekos gombjainak tiltasat feloldjuk

                pokergui5.giveButton.config(state="normal")
                pokergui5.raiseButton.config(state="normal")
                pokergui5.throwButton.config(state="normal")

                # a bot gombjait tiltjuk (ez majd nem kell)

                pokergui5.giveButton2.config(state="disabled")
                pokergui5.raiseButton2.config(state="disabled")
                pokergui5.throwButton2.config(state="disabled")
                                    
                if bot_bet == 0 and player_bet == 0:
                     
                    bot_money -= 200
                    bot_bet += 200

                elif bot_bet == 100 and player_bet == 200:
                    bot_money -= 100
                    bot_bet += 100

                    if kisvak == who:
        
                        continue1()

                elif bot_bet <= player_bet:
                    
                    bot_money -= player_bet-bot_bet
                    bot_bet += player_bet-bot_bet

                    if kisvak == who:
        
                        continue1()

                
            pokergui5.all_bet_botlabel.config(text=bot_bet)

            

        
    
    # emelunk
            
    elif(s==3):

        emel = 500

        if who == "player":
               
            player_money -= bot_bet-player_bet+emel
            player_bet += bot_bet-player_bet+emel
            
            pokergui5.all_bet_playerlabel.config(text=player_bet)

            # letiltjuk a gombokat, amig a bot kovetkezik

            pokergui5.giveButton.config(state="disabled")
            pokergui5.raiseButton.config(state="disabled")
            pokergui5.throwButton.config(state="disabled")

            # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

            pokergui5.giveButton2.config(state="normal")
            pokergui5.raiseButton2.config(state="normal")
            pokergui5.throwButton2.config(state="normal")

            # send_to_bot("emeles",player_money,player_bet,bot_money,bot_bet)

        elif who == "bot":

            bot_money -= player_bet-bot_bet+emel
            bot_bet += player_bet-bot_bet+emel
            
            
            pokergui5.all_bet_botlabel.config(text=bot_bet)

            # letiltjuk a gombokat, amig a jatekos kovetkezik (ez majd nem kell)

            pokergui5.giveButton2.config(state="disabled")
            pokergui5.raiseButton2.config(state="disabled")
            pokergui5.throwButton2.config(state="disabled")

            # a jatekos gombjainak tiltasat feloldjuk

            pokergui5.giveButton.config(state="normal")
            pokergui5.raiseButton.config(state="normal")
            pokergui5.throwButton.config(state="normal")


    if pokergui5.infolabel.cget("text") not in ["Dontetlen!","A gep nyert!","Te nyertel!"]:

    
        pokergui5.label_sum.config(text="You have "+str(player_money)+" tokens")
        pokergui5.label_sum_bot.config(text="The bot has "+str(bot_money)+" tokens")  

    bet = player_bet+bot_bet
    player_bet = int(pokergui5.all_bet_playerlabel.cget("text"))
    bot_bet = int(pokergui5.all_bet_botlabel.cget("text"))
    pokergui5.all_bet.config(text=str(bet))
   

def give(**options):

    # zsetoncsorges hangja:
    
    pokergui5.playsound(type1="1")

    # tet meagadasa/tartasa

    moneyinf(2,options.get("who"))

def continue1():

    
    # megnezzuk, hol tart a jatek

    # ha a 3. lap nincs felforditva, akkor a flop kovetkezik
    
    if pokergui5.card3.cget("text") == "back":
        showmaincards(type1="flop")      
        
        print pokergui5.maincards[0:3]
        #send_to_bot(pokergui5.maincards[0:3])

    # ha a 4. lap nincs felforditva (1-3 igen), akkor a turn kovetkezik
    
    elif pokergui5.card4.cget("text") == "back":
        showmaincards(type1="turn")
        
        print pokergui5.maincards[3:4]
        #send_to_bot(pokergui5.maincards[3:4])
        
    # ha az 5. lap nincs felforditva (1-4 igen), akkor a river kovetkezik
    elif pokergui5.card5.cget("text") == "back":
        showmaincards(type1="river")

        print pokergui5.maincards[4:]
        #send_to_bot(pokergui5.maincards[4:])

    # ha mindegyik fel van forditva, vege a kornek
    
    else:
        round_over("evaluate")
    

def raise1(**options):

    # zsetoncsorges hangja (ketszer)
    pokergui5.playsound(type1="2")

    # megvaltoztatjuk a tetet

    moneyinf(3,options.get("who"))


    # atadjuk a botnak az iranyitast,  3 - emeles tortent
    
    #bot_turn(3)

def throw(**options):

    moneyinf(1,options.get("who"))
    
    pokergui5.playsound(type1="3")
    round_over(options.get("who"))



# kiertekeles

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
        
                #colors.clear()
                #numbers.clear()

                del colors[:]
                del numbers[:]
                
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

    bet = int(pokergui5.all_bet.cget("text"))
    
    
    if(finalplayerpoints==finalcomppoints):
        
        pokergui5.infolabel.config(text="Dontetlen!")
        verdict="Dontetlen!"
        player_money = int(pokergui5.label_sum.cget("text").split(" ")[2]) + bet/2
        pokergui5.label_sum.config(text="You have "+str(player_money)+" tokens")
        bot_money = int(pokergui5.label_sum_bot.cget("text").split(" ")[3]) + bet/2
        pokergui5.label_sum_bot.config(text="The bot has "+str(bot_money)+" tokens")
        
    elif(finalplayerpoints<finalcomppoints):
        
        verdict="A gep nyert!"
        

        bot_money = int(pokergui5.label_sum_bot.cget("text").split(" ")[3]) + bet
        
        pokergui5.label_sum_bot.config(text="The bot has "+str(bot_money)+" tokens")
        pokergui5.infolabel.config(text="A gep nyert!")

    else:
        verdict="Te nyertel!"
        
        player_money = int(pokergui5.label_sum.cget("text").split(" ")[2]) + bet
        
        pokergui5.label_sum.config(text="You have "+str(player_money)+" tokens")
        pokergui5.infolabel.config(text="Te nyertel!")

    return verdict
    #return finalcomppoints,finalplayerpoints,verdict;
    


# a gui elemeihez hozzarendeljuk az egyes fuggvenyeket

pokergui5.mycardsbutton.config(command=showmycards)
pokergui5.showbutton2.config(command=round_start)
pokergui5.giveButton.config(command=lambda:give(who="player"))
pokergui5.raiseButton.config(command=lambda:raise1(who="player"))
pokergui5.throwButton.config(command=lambda:throw(who="player"))

pokergui5.giveButton2.config(command=lambda:give(who="bot"))
pokergui5.raiseButton2.config(command=lambda:raise1(who="bot"))
pokergui5.throwButton2.config(command=lambda:throw(who="bot"))

pokergui5.filemenu.entryconfigure(0,command=newgame)
pokergui5.filemenu.entryconfigure(1,command=opengame)
pokergui5.filemenu.entryconfigure(2,command=savegame)

# gui betoltese

pokergui5.main()
