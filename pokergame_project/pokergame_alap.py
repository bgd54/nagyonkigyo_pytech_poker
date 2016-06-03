import pokergui_alap
import bot_sample
import tkMessageBox
import copy;
import itertools;
from random import randint
import os
import Tkinter as tk


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "poker")+os.path.sep

# gui betoltese

master = tk.Tk()
gui = pokergui_alap.PokerGui(master)


def savegame3(buf,player100,player_money,player_bet,bot_money,bot_bet,bet):

    file_save=open(path+"pokersave111.txt","a")
    
    file_save.write(buf % (player100,player_money,player_bet,bot_money,bot_bet,bet))

    file_save.close()

def savegame2(info):

    file_save=open(path+"pokersave111.txt","a")
    
    for i in range(len(info)):   
        file_save.write(str(info[i])+"\n")

    file_save.close()


def savegame():
    
    file_save=open(path+"pokersave.txt","w")
    file_save.write("My_first_card: "+gui.mycards[0]+"\n")
    file_save.write("My_second_card: "+gui.mycards[1]+"\n")

    file_save.write("Others_first_card: "+gui.othercards[0]+"\n")
    file_save.write("Others_second_card: "+gui.othercards[1]+"\n")
    
    file_save.write("Main1: " + gui.maincards[0]+"\n")
    file_save.write("Main1_state "+gui.card[0].cget("text")+"\n")
   
    file_save.write("Main2: " + gui.maincards[1]+"\n")
    file_save.write("Main2_state "+gui.card[1].cget("text")+"\n")
   
    file_save.write("Main3: " + gui.maincards[2]+"\n")
    file_save.write("Main3_state "+gui.card[2].cget("text")+"\n")
   
    file_save.write("Main4: " + gui.maincards[3]+"\n")
    file_save.write("Main4_state "+gui.card[3].cget("text")+"\n")
   
    file_save.write("Main5: " + gui.maincards[4]+"\n")
    file_save.write("Main5_state "+gui.card[4].cget("text")+"\n")
   

def opengame():

    
    del gui.maincards[:]
    del gui.othercards[:]
    del gui.mycards[:]

    states = []
    
    try:
    
        file_open = open(path+"pokersave.txt","r")
        for line in file_open.readlines():
            
            if "My" in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                gui.mycards.append(card)

            elif "Others" in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                gui.othercards.append(card)

            elif "Main" in line and "state" not in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                gui.maincards.append(card)

            elif "state" in line:

                line = line.rstrip("\n")
                state = line.split(" ")[1]
                states.append(state)
                

        gui.gameopen1(gui.maincards,gui.mycards,gui.othercards,states)
                        
    except IOError:
        tkMessageBox.showerror ("No file", "No saved game found")
        
    

def newgame():
    
    if gui.language == ['english']:
        answer = tkMessageBox.askquestion("New Game", "Are You Sure?", icon="warning")
    elif gui.language == ['hungarian']:
        answer = tkMessageBox.askquestion("Uj jatek", "Biztos?", icon="warning")
    else: answer = no

    if answer == "yes":

        if gui.language == ['english']:
            answer2 = tkMessageBox.askquestion("Save", "Save game first?", icon="warning")
        elif gui.language == ['hungarian']:
            answer2 = tkMessageBox.askquestion("Mentes", "Mentsem a jelenlegi jatekot?", icon="warning")
        else: answer = no
            
        if answer2 == "yes":
            savegame()
            gui.game1()
        else:
            
            gui.game1()
            

def showmaincards(**options):

    if options.get("type1") == "flop":

        gui.card[0].config(image=gui.cardpictures2[0],text="face")
        gui.card[1].config(image=gui.cardpictures2[1],text="face")
        gui.card[2].config(image=gui.cardpictures2[2],text="face")
        

    elif options.get("type1") == "turn":

        gui.card[3].config(image=gui.cardpictures2[3],text="face")

    elif options.get("type1") == "river":

        gui.card[4].config(image=gui.cardpictures2[4],text="face")

    gui.playsound(type1="3")

def showmycards():

    gui.card_mine1.config(image=gui.cardpictures[0])
    gui.card_mine2.config(image=gui.cardpictures[1])
    gui.playsound(type1="3")
    gui.infolabel.config(text="")
    gui.card_mine1.config(text="face")
    gui.card_mine2.config(text="face")

def putmaincards():

    gui.cards[0].lift()
    gui.cards[1].lift()
    gui.cards[2].lift()
    gui.cards[3].lift()
    gui.cards[4].lift()
    gui.cards_mine.lift()
    gui.cards_others.lift()    


def round_start():

    savegame2(["New round"])

    player_money = int(gui.label_sum.cget("text"))
    bot_money = int(gui.label_sum_bot.cget("text"))
    gui.game1()
    gui.label_sum.config(text=str(player_money))
    gui.label_sum_bot.config(text=str(bot_money))
     
    gui.all_bet.config(text="0")
    gui.mycardsbutton.config(state="disabled")
    gui.showbutton2.config(state="disabled")
    putmaincards()

    # lenullazzuk a teteket


    gui.changeText2([gui.all_bet_playerlabel,gui.all_bet_botlabel,gui.all_bet],"0")
 
    
    kisvak1 =  gui.kisvak.cget("text")
    nagyvak1 =  gui.nagyvak.cget("text")

    if kisvak1 =="player":

        gui.kisvak.config(text="bot")
        gui.nagyvak.config(text="player")
        
        gui.giveButton.config(state="normal")
        gui.giveButton2.config(state="disabled")
        
        gui.changeText(gui.infolabel,gui.bigblind_info)

        
    else:

        gui.kisvak.config(text="player")
        gui.nagyvak.config(text="bot")
        
        gui.giveButton2.config(state="normal")
        gui.giveButton.config(state="disabled")

        gui.changeText(gui.infolabel,gui.smallblind_info)
        
        

    
    gui.raiseButton.config(state="disabled")
    gui.throwButton.config(state="disabled")

    
    gui.raiseButton2.config(state="disabled")
    gui.throwButton2.config(state="disabled")

def round_over(case):

    # vege az adott kornek

    # az osszes lapot felforditjuk, ami meg nincs felforditva (a feltetelt akar ki is lehetne hagyni)

    if gui.card[0].cget("text") == "back":    
        gui.card[0].config(image=gui.cardpictures2[0],text="face")
    if gui.card[1].cget("text") == "back":
        gui.card[1].config(image=gui.cardpictures2[1],text="face")
    if gui.card[2].cget("text") == "back":
        gui.card[2].config(image=gui.cardpictures2[2],text="face")
    if gui.card[3].cget("text") == "back":
        gui.card[3].config(image=gui.cardpictures2[3],text="face")
    if gui.card[4].cget("text") == "back":
        gui.card[4].config(image=gui.cardpictures2[4],text="face")

    gui.card[0].config(text="ready")
    gui.card[1].config(text="ready")
    gui.card[2].config(text="ready")
    gui.card[3].config(text="ready")
    gui.card[4].config(text="ready")
    gui.card_others1.config(text="ready")
    gui.card_others2.config(text="ready")
    gui.card_mine1.config(text="ready")
    gui.card_mine2.config(text="ready")

    gui.card_others1.config(image=gui.cardpictures3[0])
    gui.card_others2.config(image=gui.cardpictures3[1])

    gui.card_mine1.config(image=gui.cardpictures[0])
    gui.card_mine2.config(image=gui.cardpictures[1])  
    
    
    # letiltjuk a megad - emel - eldob gombokat a kovetkezo korig
    
    gui.giveButton.config(state="disabled")
    gui.raiseButton.config(state="disabled")
    gui.throwButton.config(state="disabled")

    gui.giveButton2.config(state="disabled")
    gui.raiseButton2.config(state="disabled")
    gui.throwButton2.config(state="disabled")

    # lapok felforditasanak hangja
    
    gui.playsound(type1="3")

    # megnezzuk, ki nyert

    bet = int(gui.all_bet.cget("text"))

    if case == "throw_player":


            bot_money = int(gui.label_sum_bot.cget("text")) + bet
            
            gui.label_sum_bot.config(text=str(bot_money))
            gui.changeText(gui.infolabel,gui.botwin_info)

            savegame2(["Bot wins"])

    elif case == "throw_bot":
        
            player_money = int(gui.label_sum.cget("text")) + bet
            gui.label_sum.config(text=str(player_money))
            gui.changeText(gui.infolabel,gui.youwin_info)

            savegame2(["Player wins"])

    elif case == "evaluate":
      
        table = gui.othercards + gui.maincards + gui.mycards     
        
        evaluate(table)


    # uj kor kezdese

    gui.showbutton2.config(state='normal')

def moneyinf(s,who):

    bot_money =  int(gui.label_sum_bot.cget("text"))
    player_money = int(gui.label_sum.cget("text"))
    
    bet = int(gui.all_bet.cget("text"))
    player_bet = int(gui.all_bet_playerlabel.cget("text"))
    bot_bet = int(gui.all_bet_botlabel.cget("text"))

    kisvak = gui.kisvak.cget("text")
    nagyvak = gui.nagyvak.cget("text")

    player_levon = 0
    bot_levon = 0

    player100 = "player_give:\t100"
    player200 = "player_give:\t200"
    player500 = "player_raise:\t500"
    bot100 = "bot_give:\t100"
    bot200 = "bot_give:\t200"
    bot500 = "bot_raise:\t500"
    
    savegame2(["next"])


    buf = "%s\nplayer_has:\t%i\nplayer_bet:\t%i\nbot_has:\t%i\nbot_bet:\t%i\nall_bet:\t%i\n"

    # feladas
    
    if(s==1):

        round_over("throw_"+who)
        savegame2("throw_"+who)
        

    # tartas/megadas
        
    elif(s==2):
        
        if who == "player":

            # ha a kisvak tetet kell betenni
            
            if player_bet == 0 and bot_bet == 200:
                
                player_money -= 100
                player_bet += 100

                player_levon = 100
                bet = player_bet+bot_bet
                savegame3(buf,player100,player_money,player_bet,bot_money,bot_bet,bet)
                
                gui.mycardsbutton.config(state="normal")
                gui.changeText(gui.infolabel,gui.look_info)
                

                    
                

            else:

                # a jatekos gombjainak tiltasa

                gui.changeState([gui.giveButton,gui.raiseButton,gui.throwButton],"disabled")
                
##                gui.giveButton.config(state="disabled")
##                gui.raiseButton.config(state="disabled")
##                gui.throwButton.config(state="disabled")

                # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

                gui.changeState([gui.giveButton2,gui.raiseButton2,gui.throwButton2],"normal")

##                gui.giveButton2.config(state="normal")
##                gui.raiseButton2.config(state="normal")
##                gui.throwButton2.config(state="normal")

                # ha a nagyvakot kell betenni
                
                if player_bet == 0 and bot_bet == 0:
                    player_money -= 200
                    player_bet += 200
                    gui.mycardsbutton.config(state="normal")

                    player_levon = 200
                    bet = player_bet+bot_bet
                    savegame3(buf,player200,player_money,player_bet,bot_money,bot_bet,bet)


                elif player_bet == 100 and bot_bet == 200:
                    player_money -= 100
                    player_bet += 100

                    player_levon = 100
                    bet = player_bet+bot_bet
                    savegame3(buf,player100,player_money,player_bet,bot_money,bot_bet,bet)

                    if kisvak == who:
        
                        continue1()
                    

                elif player_bet <= bot_bet:

                    if kisvak == who:
        
                        continue1()

                    
                    player_levon = bot_bet-player_bet

                    player_money -= bot_bet-player_bet
                    player_bet += bot_bet-player_bet
                    bet = player_bet+bot_bet

                    savegame3(buf,"player_give:"+str(bot_bet-player_bet),player_money,player_bet,bot_money,bot_bet,bet)

                    

                
            gui.all_bet_playerlabel.config(text=player_bet)

            bot_sample.send_to_bot("adas",player_money,player_bet,bot_money,bot_bet)
            

        elif who == "bot":

            if bot_bet == 0 and player_bet == 200:
                bot_money -= 100
                bot_bet += 100

                bot_levon = 100
                bet = player_bet+bot_bet
                savegame3(buf,bot100,player_money,player_bet,bot_money,bot_bet,bet)
                

            else:
                
                # a jatekos gombjainak tiltasat feloldjuk

                gui.changeState([gui.giveButton,gui.raiseButton,gui.throwButton],"normal")

##                gui.giveButton.config(state="normal")
##                gui.raiseButton.config(state="normal")
##                gui.throwButton.config(state="normal")

                # a bot gombjait tiltjuk (ez majd nem kell)

                gui.changeState([gui.giveButton2,gui.raiseButton2,gui.throwButton2],"disabled")

##                gui.giveButton2.config(state="disabled")
##                gui.raiseButton2.config(state="disabled")
##                gui.throwButton2.config(state="disabled")
##                                    
                if bot_bet == 0 and player_bet == 0:
                     
                    bot_money -= 200
                    bot_bet += 200

                    bot_levon = 200

                    bet = player_bet+bot_bet
                    
                    #savegame2([bot200,"player_has: "+str(player_money),"player_bet: "+str(player_bet),"bot_has: "+str(bot_money),"bot_bet: "+str(bot_bet),"all_bet: "+str(bet)])
                    savegame3(buf,bot200,player_money,player_bet,bot_money,bot_bet,bet)


                elif bot_bet == 100 and player_bet == 200:
                    bot_money -= 100
                    bot_bet += 100

                    bot_levon = 100

                    bet = player_bet+bot_bet
                    
                    savegame3(buf,bot100,player_money,player_bet,bot_money,bot_bet,bet)

                    if kisvak == who:
        
                        continue1()

                elif bot_bet <= player_bet:


                    bot_levon = player_bet-bot_bet
                    
                    
                    bot_money -= player_bet-bot_bet
                    bot_bet += player_bet-bot_bet
                    bet = player_bet+bot_bet

                    savegame3(buf,"bot_give:"+str(player_bet-bot_bet),player_money,player_bet,bot_money,bot_bet,bet)

                    if kisvak == who:
        
                        continue1()

                
            gui.all_bet_botlabel.config(text=bot_bet)

            

        
    
    # emelunk
            
    elif(s==3):

        emel = 500

        if who == "player":


            player_levon = bot_bet-player_bet+emel
               
            player_money -= bot_bet-player_bet+emel
            player_bet += bot_bet-player_bet+emel
            bet = player_bet+bot_bet

            savegame3(buf,"player_give:"+str(bot_bet-player_bet+emel),player_money,player_bet,bot_money,bot_bet,bet)

            gui.all_bet_playerlabel.config(text=player_bet)

            # letiltjuk a gombokat, amig a bot kovetkezik

            

            gui.giveButton.config(state="disabled")
            gui.raiseButton.config(state="disabled")
            gui.throwButton.config(state="disabled")

            # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

            gui.giveButton2.config(state="normal")
            gui.raiseButton2.config(state="normal")
            gui.throwButton2.config(state="normal")

            # send_to_bot("emeles",player_money,player_bet,bot_money,bot_bet)

        elif who == "bot":

            bot_levon = player_bet-bot_bet+emel

            bot_money -= player_bet-bot_bet+emel
            bot_bet += player_bet-bot_bet+emel
            bet = player_bet+bot_bet

            savegame3(buf,"bot_give:"+str(player_bet-bot_bet+emel),player_money,player_bet,bot_money,bot_bet,bet)
            
            gui.all_bet_botlabel.config(text=bot_bet)

            # letiltjuk a gombokat, amig a jatekos kovetkezik (ez majd nem kell)

            gui.giveButton2.config(state="disabled")
            gui.raiseButton2.config(state="disabled")
            gui.throwButton2.config(state="disabled")

            # a jatekos gombjainak tiltasat feloldjuk

            gui.giveButton.config(state="normal")
            gui.raiseButton.config(state="normal")
            gui.throwButton.config(state="normal")

    info = gui.infolabel.cget("text")                        
    if info not in gui.tie_info and info not in gui.botwin_info and info not in gui.youwin_info:

    
        gui.label_sum.config(text=str(player_money))
        gui.label_sum_bot.config(text=str(bot_money))  

    bet = player_bet+bot_bet
    player_bet = int(gui.all_bet_playerlabel.cget("text"))
    bot_bet = int(gui.all_bet_botlabel.cget("text"))
    gui.all_bet.config(text=str(bet))


    player_white = int(gui.zseton.white.cget("text"))
    bot_white = int(gui.zseton2.white.cget("text"))

    player_blue = int(gui.zseton.blue.cget("text"))
    bot_blue = int(gui.zseton2.blue.cget("text"))

    player_red = int(gui.zseton.red.cget("text"))
    bot_red = int(gui.zseton2.red.cget("text"))

    player_green = int(gui.zseton.green.cget("text"))
    bot_green = int(gui.zseton2.green.cget("text"))

    player_black = int(gui.zseton.black.cget("text"))
    bot_black = int(gui.zseton2.black.cget("text"))

    black_value = 100
    green_value = 25
    red_value = 10
    blue_value = 5
    white = 1

    if bot_black >= bot_levon/black_value:
        gui.zseton2.black.config(text=str(bot_black-(bot_levon/black_value)))

    elif bot_green >= bot_levon/green_value:
        gui.zseton2.green.config(text=str(bot_green-(bot_levon/green_value)))

    elif bot_red >= bot_levon/red_value:
        gui.zseton2.red.config(text=str(bot_red-(bot_levon/red_value)))

    elif bot_blue >= bot_levon/blue_value:
        gui.zseton2.blue.config(text=str(bot_blue-(bot_levon/blue_value)))

    elif bot_white >= bot_levon/white_value:
        gui.zseton2.white.config(text=str(bot_white-(bot_levon/white_value)))

    if player_black >= player_levon/black_value:
        gui.zseton.black.config(text=str(player_black-(player_levon/black_value)))

    elif player_green >= player_levon/green_value:
        gui.zseton.green.config(text=str(player_green-(player_levon/green_value)))

    elif player_red >= player_levon/red_value:
        gui.zseton.red.config(text=str(player_red-(player_levon/red_value)))

    elif player_blue >= player_levon/blue_value:
        gui.zseton.blue.config(text=str(player_blue-(player_levon/blue_value)))

    elif player_white >= player_levon/white_value:
        gui.zseton.white.config(text=str(player_white-(player_levon/white_value)))
   

def give(**options):

    # zsetoncsorges hangja:
    
    gui.playsound(type1="1")

    # tet meagadasa/tartasa

    moneyinf(2,options.get("who"))

def continue1():

    
    # megnezzuk, hol tart a jatek

    # ha a 3. lap nincs felforditva, akkor a flop kovetkezik
    
    if gui.card[2].cget("text") == "back":
        showmaincards(type1="flop")      
        
        savegame2([gui.maincards[0:3]])
        #send_to_bot(gui.maincards[0:3])

    # ha a 4. lap nincs felforditva (1-3 igen), akkor a turn kovetkezik
    
    elif gui.card[3].cget("text") == "back":
        showmaincards(type1="turn")
        
        savegame2([gui.maincards[3:4]])
        #send_to_bot(gui.maincards[3:4])
        
    # ha az 5. lap nincs felforditva (1-4 igen), akkor a river kovetkezik
    elif gui.card[4].cget("text") == "back":
        showmaincards(type1="river")

        savegame2([gui.maincards[4:]])
        #send_to_bot(gui.maincards[4:])

    # ha mindegyik fel van forditva, vege a kornek
    
    else:
        round_over("evaluate")
        savegame2(["evaluate"])
    

def raise1(**options):

    # zsetoncsorges hangja (ketszer)
    gui.playsound(type1="2")

    # megvaltoztatjuk a tetet

    moneyinf(3,options.get("who"))


    # atadjuk a botnak az iranyitast,  3 - emeles tortent
    
    #bot_turn(3)

def throw(**options):

    moneyinf(1,options.get("who"))
    
    gui.playsound(type1="3")
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

    bet = int(gui.all_bet.cget("text"))
    
    
    if(finalplayerpoints==finalcomppoints):

        gui.changeText(gui.infolabel,gui.tie_info)
        savegame2(["Tie"])
        
        verdict="Dontetlen!"
        player_money = int(gui.label_sum.cget("text")) + bet/2
        gui.label_sum.config(text=str(player_money))
        bot_money = int(gui.label_sum_bot.cget("text")) + bet/2
        gui.label_sum_bot.config(text=str(bot_money))
        
    elif(finalplayerpoints<finalcomppoints):
        
        verdict="A gep nyert!"
        

        bot_money = int(gui.label_sum_bot.cget("text")) + bet
        
        gui.label_sum_bot.config(text=str(bot_money))
        
        gui.changeText(gui.infolabel,gui.botwin_info)

        savegame2(["Bot wins"])


    else:
        verdict="Te nyertel!"
        
        player_money = int(gui.label_sum.cget("text")) + bet
        
        gui.label_sum.config(text=str(player_money))
        gui.changeText(gui.infolabel,gui.youwin_info)

        savegame2(["Player wins"])

    return verdict
    #return finalcomppoints,finalplayerpoints,verdict;
    


# a gui elemeihez hozzarendeljuk az egyes fuggvenyeket

gui.mycardsbutton.config(command=showmycards)
gui.showbutton2.config(command=round_start)
gui.giveButton.config(command=lambda:give(who="player"))
gui.raiseButton.config(command=lambda:raise1(who="player"))
gui.throwButton.config(command=lambda:throw(who="player"))
##
gui.giveButton2.config(command=lambda:give(who="bot"))
gui.raiseButton2.config(command=lambda:raise1(who="bot"))
gui.throwButton2.config(command=lambda:throw(who="bot"))
##
gui.filemenu.entryconfigure(0,command=newgame)
gui.filemenu.entryconfigure(1,command=opengame)
gui.filemenu.entryconfigure(2,command=savegame)


#master.mainloop()
