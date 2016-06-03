import tkMessageBox
import itertools;
import os
import Tkinter as tk

from pokergui_alap import PokerGui
import bot_sample

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "poker")+os.path.sep

class Logic:
    def __init__(self, gui):
        self.gui = gui
        self.bot = bot_sample.botbeta(self) ## TODO

    def savegame3(self, buf,player100,player_money,player_bet,bot_money,bot_bet,bet):

        file_save=open(path+"pokersave111.txt","a")
        file_save.write(buf % (player100,player_money,player_bet,bot_money,bot_bet,bet))

        file_save.close()

    def savegame2(self, info):

        file_save=open(path+"pokersave111.txt","a")
    
        for i in range(len(info)):
            file_save.write(str(info[i])+"\n")

        file_save.close()


    def savegame(self):
    
        file_save=open(path+"pokersave.txt","w")
        file_save.write("My_first_card: "+self.gui.mycards[0]+"\n")
        file_save.write("My_second_card: "+self.gui.mycards[1]+"\n")

        file_save.write("Others_first_card: "+self.gui.othercards[0]+"\n")
        file_save.write("Others_second_card: "+self.gui.othercards[1]+"\n")
    
        file_save.write("Main1: " + self.gui.maincards[0]+"\n")
        file_save.write("Main1_state "+self.gui.card[0].cget("text")+"\n")
   
        file_save.write("Main2: " + self.gui.maincards[1]+"\n")
        file_save.write("Main2_state "+self.gui.card[1].cget("text")+"\n")
   
        file_save.write("Main3: " + self.gui.maincards[2]+"\n")
        file_save.write("Main3_state "+self.gui.card[2].cget("text")+"\n")
   
        file_save.write("Main4: " + self.gui.maincards[3]+"\n")
        file_save.write("Main4_state "+self.gui.card[3].cget("text")+"\n")
   
        file_save.write("Main5: " + self.gui.maincards[4]+"\n")
        file_save.write("Main5_state "+self.gui.card[4].cget("text")+"\n")
   

    def opengame(self):


        del self.gui.maincards[:]
        del self.gui.othercards[:]
        del self.gui.mycards[:]

        states = []

        try:

            file_open = open(path+"pokersave.txt","r")
            for line in file_open.readlines():

                if "My" in line:
                    line = line.rstrip("\n")
                    card = line.split(" ")[1]
                    self.gui.mycards.append(card)

                elif "Others" in line:
                    line = line.rstrip("\n")
                    card = line.split(" ")[1]
                    self.gui.othercards.append(card)

                elif "Main" in line and "state" not in line:
                    line = line.rstrip("\n")
                    card = line.split(" ")[1]
                    self.gui.maincards.append(card)

                elif "state" in line:

                    line = line.rstrip("\n")
                    state = line.split(" ")[1]
                    states.append(state)


            self.gui.gameopen1(self.gui.maincards,self.gui.mycards,self.gui.othercards,states)

        except IOError:
            tkMessageBox.showerror ("No file", "No saved game found")



    def newgame(self):

        if self.gui.language == ['english']:
            answer = tkMessageBox.askquestion("New Game", "Are You Sure?", icon="warning")
        elif self.gui.language == ['hungarian']:
            answer = tkMessageBox.askquestion("Uj jatek", "Biztos?", icon="warning")
        else: answer = no

        if answer == "yes":

            if self.gui.language == ['english']:
                answer2 = tkMessageBox.askquestion("Save", "Save game first?", icon="warning")
            elif self.gui.language == ['hungarian']:
                answer2 = tkMessageBox.askquestion("Mentes", "Mentsem a jelenlegi jatekot?", icon="warning")
            else: answer = no

            if answer2 == "yes":
                self.savegame()
                self.gui.game1()
            else:

                self.gui.game1()


    def showmaincards(self, **options):

        if options.get("type1") == "flop":

            self.gui.card[0].config(image=self.gui.cardpictures2[0],text="face")
            self.gui.card[1].config(image=self.gui.cardpictures2[1],text="face")
            self.gui.card[2].config(image=self.gui.cardpictures2[2],text="face")


        elif options.get("type1") == "turn":

            self.gui.card[3].config(image=self.gui.cardpictures2[3],text="face")

        elif options.get("type1") == "river":

            self.gui.card[4].config(image=self.gui.cardpictures2[4],text="face")

        self.gui.playsound(type1="3")

    def showmycards(self):

        self.gui.card_mine1.config(image=self.gui.cardpictures[0])
        self.gui.card_mine2.config(image=self.gui.cardpictures[1])
        self.gui.playsound(type1="3")
        self.gui.infolabel.config(text="")
        self.gui.card_mine1.config(text="face")
        self.gui.card_mine2.config(text="face")

    def putmaincards(self):

        self.gui.cards[0].lift()
        self.gui.cards[1].lift()
        self.gui.cards[2].lift()
        self.gui.cards[3].lift()
        self.gui.cards[4].lift()
        self.gui.cards_mine.lift()
        self.gui.cards_others.lift()


    def round_start(self):

        self.savegame2(["New round"])

        player_money = int(self.gui.label_sum.cget("text"))
        bot_money = int(self.gui.label_sum_bot.cget("text"))
        self.gui.game1()
        self.gui.label_sum.config(text=str(player_money))
        self.gui.label_sum_bot.config(text=str(bot_money))

        self.gui.all_bet.config(text="0")
        self.gui.mycardsbutton.config(state="disabled")
        self.gui.showbutton2.config(state="disabled")
        self.putmaincards()

        # lenullazzuk a teteket


        self.gui.changeText2([self.gui.all_bet_playerlabel,self.gui.all_bet_botlabel,self.gui.all_bet],"0")


        kisvak1 =  self.gui.kisvak.cget("text")
        nagyvak1 =  self.gui.nagyvak.cget("text")

        if kisvak1 =="player":

            self.gui.kisvak.config(text="bot")
            self.gui.nagyvak.config(text="player")

            self.gui.giveButton.config(state="normal")
            self.gui.giveButton2.config(state="disabled")

            self.gui.changeText(self.gui.infolabel,self.gui.bigblind_info)


        else:

            self.gui.kisvak.config(text="player")
            self.gui.nagyvak.config(text="bot")

            self.gui.giveButton2.config(state="normal")
            self.gui.giveButton.config(state="disabled")

            self.gui.changeText(self.gui.infolabel,self.gui.smallblind_info)




        self.gui.raiseButton.config(state="disabled")
        self.gui.throwButton.config(state="disabled")


        self.gui.raiseButton2.config(state="disabled")
        self.gui.throwButton2.config(state="disabled")

    def round_over(self, case):

        # vege az adott kornek

        # az osszes lapot felforditjuk, ami meg nincs felforditva (a feltetelt akar ki is lehetne hagyni)

        if self.gui.card[0].cget("text") == "back":
            self.gui.card[0].config(image=self.gui.cardpictures2[0],text="face")
        if self.gui.card[1].cget("text") == "back":
            self.gui.card[1].config(image=self.gui.cardpictures2[1],text="face")
        if self.gui.card[2].cget("text") == "back":
            self.gui.card[2].config(image=self.gui.cardpictures2[2],text="face")
        if self.gui.card[3].cget("text") == "back":
            self.gui.card[3].config(image=self.gui.cardpictures2[3],text="face")
        if self.gui.card[4].cget("text") == "back":
            self.gui.card[4].config(image=self.gui.cardpictures2[4],text="face")

        self.gui.card[0].config(text="ready")
        self.gui.card[1].config(text="ready")
        self.gui.card[2].config(text="ready")
        self.gui.card[3].config(text="ready")
        self.gui.card[4].config(text="ready")
        self.gui.card_others1.config(text="ready")
        self.gui.card_others2.config(text="ready")
        self.gui.card_mine1.config(text="ready")
        self.gui.card_mine2.config(text="ready")

        self.gui.card_others1.config(image=self.gui.cardpictures3[0])
        self.gui.card_others2.config(image=self.gui.cardpictures3[1])

        self.gui.card_mine1.config(image=self.gui.cardpictures[0])
        self.gui.card_mine2.config(image=self.gui.cardpictures[1])


        # letiltjuk a megad - emel - eldob gombokat a kovetkezo korig

        self.gui.giveButton.config(state="disabled")
        self.gui.raiseButton.config(state="disabled")
        self.gui.throwButton.config(state="disabled")

        self.gui.giveButton2.config(state="disabled")
        self.gui.raiseButton2.config(state="disabled")
        self.gui.throwButton2.config(state="disabled")

        # lapok felforditasanak hangja

        self.gui.playsound(type1="3")

        # megnezzuk, ki nyert

        bet = int(self.gui.all_bet.cget("text"))

        if case == "throw_player":


                bot_money = int(self.gui.label_sum_bot.cget("text")) + bet

                self.gui.label_sum_bot.config(text=str(bot_money))
                self.gui.changeText(self.gui.infolabel,self.gui.botwin_info)

                self.savegame2(["Bot wins"])

        elif case == "throw_bot":

                player_money = int(self.gui.label_sum.cget("text")) + bet
                self.gui.label_sum.config(text=str(player_money))
                self.gui.changeText(self.gui.infolabel,self.gui.youwin_info)

                self.savegame2(["Player wins"])

        elif case == "evaluate":
            print "asd"
            table = self.gui.othercards + self.gui.maincards + self.gui.mycards

            self.evaluate(table)


        # uj kor kezdese

        self.gui.showbutton2.config(state='normal')

    def moneyinf(self, s,who):

        bot_money =  int(self.gui.label_sum_bot.cget("text"))
        player_money = int(self.gui.label_sum.cget("text"))

        bet = int(self.gui.all_bet.cget("text"))
        player_bet = int(self.gui.all_bet_playerlabel.cget("text"))
        bot_bet = int(self.gui.all_bet_botlabel.cget("text"))

        kisvak = self.gui.kisvak.cget("text")
        nagyvak = self.gui.nagyvak.cget("text")

        player_levon = 0
        bot_levon = 0

        player100 = "player_give:\t100"
        player200 = "player_give:\t200"
        player500 = "player_raise:\t500"
        bot100 = "bot_give:\t100"
        bot200 = "bot_give:\t200"
        bot500 = "bot_raise:\t500"

        self.savegame2(["next"])


        buf = "%s\nplayer_has:\t%i\nplayer_bet:\t%i\nbot_has:\t%i\nbot_bet:\t%i\nall_bet:\t%i\n"

        # feladas

        if(s==1):

            self.round_over("throw_"+who)
            self.savegame2("throw_"+who)


        # tartas/megadas

        elif(s==2):

            if who == "player":

                # ha a kisvak tetet kell betenni

                if player_bet == 0 and bot_bet == 200:

                    player_money -= 100
                    player_bet += 100

                    player_levon = 100
                    bet = player_bet+bot_bet
                    self.savegame3(buf,player100,player_money,player_bet,bot_money,bot_bet,bet)

                    self.gui.mycardsbutton.config(state="normal")
                    self.gui.changeText(self.gui.infolabel,self.gui.look_info)





                else:

                    # a jatekos gombjainak tiltasa

                    self.gui.changeState([self.gui.giveButton,self.gui.raiseButton,self.gui.throwButton],"disabled")

    ##                self.gui.giveButton.config(state="disabled")
    ##                self.gui.raiseButton.config(state="disabled")
    ##                self.gui.throwButton.config(state="disabled")

                    # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

                    self.gui.changeState([self.gui.giveButton2,self.gui.raiseButton2,self.gui.throwButton2],"normal")

    ##                self.gui.giveButton2.config(state="normal")
    ##                self.gui.raiseButton2.config(state="normal")
    ##                self.gui.throwButton2.config(state="normal")

                    # ha a nagyvakot kell betenni

                    if player_bet == 0 and bot_bet == 0:
                        player_money -= 200
                        player_bet += 200
                        self.gui.mycardsbutton.config(state="normal")

                        player_levon = 200
                        bet = player_bet+bot_bet
                        self.savegame3(buf,player200,player_money,player_bet,bot_money,bot_bet,bet)


                    elif player_bet == 100 and bot_bet == 200:
                        player_money -= 100
                        player_bet += 100

                        player_levon = 100
                        bet = player_bet+bot_bet
                        self.savegame3(buf,player100,player_money,player_bet,bot_money,bot_bet,bet)

                        if kisvak == who:

                            self.continue1()


                    elif player_bet <= bot_bet:

                        if kisvak == who:

                            self.continue1()


                        player_levon = bot_bet-player_bet

                        player_money -= bot_bet-player_bet
                        player_bet += bot_bet-player_bet
                        bet = player_bet+bot_bet

                        self.savegame3(buf,"player_give:"+str(bot_bet-player_bet),player_money,player_bet,bot_money,bot_bet,bet)




                self.gui.all_bet_playerlabel.config(text=player_bet)

                self.bot.send_to_bot("adas",player_money,player_bet,bot_money,bot_bet) ## TODO


            elif who == "bot":

                if bot_bet == 0 and player_bet == 200:
                    bot_money -= 100
                    bot_bet += 100

                    bot_levon = 100
                    bet = player_bet+bot_bet
                    self.savegame3(buf,bot100,player_money,player_bet,bot_money,bot_bet,bet)


                else:

                    # a jatekos gombjainak tiltasat feloldjuk

                    self.gui.changeState([self.gui.giveButton,self.gui.raiseButton,self.gui.throwButton],"normal")

    ##                self.gui.giveButton.config(state="normal")
    ##                self.gui.raiseButton.config(state="normal")
    ##                self.gui.throwButton.config(state="normal")

                    # a bot gombjait tiltjuk (ez majd nem kell)

                    self.gui.changeState([self.gui.giveButton2,self.gui.raiseButton2,self.gui.throwButton2],"disabled")

    ##                self.gui.giveButton2.config(state="disabled")
    ##                self.gui.raiseButton2.config(state="disabled")
    ##                self.gui.throwButton2.config(state="disabled")
    ##
                    if bot_bet == 0 and player_bet == 0:

                        bot_money -= 200
                        bot_bet += 200

                        bot_levon = 200

                        bet = player_bet+bot_bet

                        #self.savegame2([bot200,"player_has: "+str(player_money),"player_bet: "+str(player_bet),"bot_has: "+str(bot_money),"bot_bet: "+str(bot_bet),"all_bet: "+str(bet)])
                        self.savegame3(buf,bot200,player_money,player_bet,bot_money,bot_bet,bet)


                    elif bot_bet == 100 and player_bet == 200:
                        bot_money -= 100
                        bot_bet += 100

                        bot_levon = 100

                        bet = player_bet+bot_bet

                        self.savegame3(buf,bot100,player_money,player_bet,bot_money,bot_bet,bet)

                        if kisvak == who:

                            self.continue1()

                    elif bot_bet <= player_bet:


                        bot_levon = player_bet-bot_bet


                        bot_money -= player_bet-bot_bet
                        bot_bet += player_bet-bot_bet
                        bet = player_bet+bot_bet

                        self.savegame3(buf,"bot_give:"+str(player_bet-bot_bet),player_money,player_bet,bot_money,bot_bet,bet)

                        if kisvak == who:

                            self.continue1()


                self.gui.all_bet_botlabel.config(text=bot_bet)





        # emelunk

        elif(s==3):

            emel = 500

            if who == "player":


                player_levon = bot_bet-player_bet+emel

                player_money -= bot_bet-player_bet+emel
                player_bet += bot_bet-player_bet+emel
                bet = player_bet+bot_bet

                self.savegame3(buf,"player_give:"+str(bot_bet-player_bet+emel),player_money,player_bet,bot_money,bot_bet,bet)

                self.gui.all_bet_playerlabel.config(text=player_bet)

                # letiltjuk a gombokat, amig a bot kovetkezik



                self.gui.giveButton.config(state="disabled")
                self.gui.raiseButton.config(state="disabled")
                self.gui.throwButton.config(state="disabled")

                # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

                self.gui.giveButton2.config(state="normal")
                self.gui.raiseButton2.config(state="normal")
                self.gui.throwButton2.config(state="normal")

                # send_to_bot("emeles",player_money,player_bet,bot_money,bot_bet)

            elif who == "bot":

                bot_levon = player_bet-bot_bet+emel

                bot_money -= player_bet-bot_bet+emel
                bot_bet += player_bet-bot_bet+emel
                bet = player_bet+bot_bet

                self.savegame3(buf,"bot_give:"+str(player_bet-bot_bet+emel),player_money,player_bet,bot_money,bot_bet,bet)

                self.gui.all_bet_botlabel.config(text=bot_bet)

                # letiltjuk a gombokat, amig a jatekos kovetkezik (ez majd nem kell)

                self.gui.giveButton2.config(state="disabled")
                self.gui.raiseButton2.config(state="disabled")
                self.gui.throwButton2.config(state="disabled")

                # a jatekos gombjainak tiltasat feloldjuk

                self.gui.giveButton.config(state="normal")
                self.gui.raiseButton.config(state="normal")
                self.gui.throwButton.config(state="normal")

        info = self.gui.infolabel.cget("text")
        if info not in self.gui.tie_info and info not in self.gui.botwin_info and info not in self.gui.youwin_info:


            self.gui.label_sum.config(text=str(player_money))
            self.gui.label_sum_bot.config(text=str(bot_money))

        bet = player_bet+bot_bet
        player_bet = int(self.gui.all_bet_playerlabel.cget("text"))
        bot_bet = int(self.gui.all_bet_botlabel.cget("text"))
        self.gui.all_bet.config(text=str(bet))


        player_white = int(self.gui.zseton.white.cget("text"))
        bot_white = int(self.gui.zseton2.white.cget("text"))

        player_blue = int(self.gui.zseton.blue.cget("text"))
        bot_blue = int(self.gui.zseton2.blue.cget("text"))

        player_red = int(self.gui.zseton.red.cget("text"))
        bot_red = int(self.gui.zseton2.red.cget("text"))

        player_green = int(self.gui.zseton.green.cget("text"))
        bot_green = int(self.gui.zseton2.green.cget("text"))

        player_black = int(self.gui.zseton.black.cget("text"))
        bot_black = int(self.gui.zseton2.black.cget("text"))

        black_value = 100
        green_value = 25
        red_value = 10
        blue_value = 5
        white = 1

        if bot_black >= bot_levon/black_value:
            self.gui.zseton2.black.config(text=str(bot_black-(bot_levon/black_value)))

        elif bot_green >= bot_levon/green_value:
            self.gui.zseton2.green.config(text=str(bot_green-(bot_levon/green_value)))

        elif bot_red >= bot_levon/red_value:
            self.gui.zseton2.red.config(text=str(bot_red-(bot_levon/red_value)))

        elif bot_blue >= bot_levon/blue_value:
            self.gui.zseton2.blue.config(text=str(bot_blue-(bot_levon/blue_value)))

        elif bot_white >= bot_levon/white_value:
            self.gui.zseton2.white.config(text=str(bot_white-(bot_levon/white_value)))

        if player_black >= player_levon/black_value:
            self.gui.zseton.black.config(text=str(player_black-(player_levon/black_value)))

        elif player_green >= player_levon/green_value:
            self.gui.zseton.green.config(text=str(player_green-(player_levon/green_value)))

        elif player_red >= player_levon/red_value:
            self.gui.zseton.red.config(text=str(player_red-(player_levon/red_value)))

        elif player_blue >= player_levon/blue_value:
            self.gui.zseton.blue.config(text=str(player_blue-(player_levon/blue_value)))

        elif player_white >= player_levon/white_value:
            self.gui.zseton.white.config(text=str(player_white-(player_levon/white_value)))


    def give(self, **options):

        # zsetoncsorges hangja:

        self.gui.playsound(type1="1")

        # tet meagadasa/tartasa

        self.moneyinf(2,options.get("who"))

    def continue1(self):


        # megnezzuk, hol tart a jatek

        # ha a 3. lap nincs felforditva, akkor a flop kovetkezik

        if self.gui.card[2].cget("text") == "back":
            self.showmaincards(type1="flop")

            self.savegame2([self.gui.maincards[0:3]])
            #send_to_bot(self.gui.maincards[0:3])

        # ha a 4. lap nincs felforditva (1-3 igen), akkor a turn kovetkezik

        elif self.gui.card[3].cget("text") == "back":
            self.showmaincards(type1="turn")

            self.savegame2([self.gui.maincards[3:4]])
            #send_to_bot(self.gui.maincards[3:4])

        # ha az 5. lap nincs felforditva (1-4 igen), akkor a river kovetkezik
        elif self.gui.card[4].cget("text") == "back":
            self.showmaincards(type1="river")

            self.savegame2([self.gui.maincards[4:]])
            #send_to_bot(self.gui.maincards[4:])

        # ha mindegyik fel van forditva, vege a kornek

        else:
            self.round_over("evaluate")
            self.savegame2(["evaluate"])


    def raise1(self, who):

        # zsetoncsorges hangja (ketszer)
        self.gui.playsound(type1="2")

        # megvaltoztatjuk a tetet
        self.moneyinf(3,who)

        # self.moneyinf(3,options.get("who"))


        # atadjuk a botnak az iranyitast,  3 - emeles tortent

        #bot_turn(3)

    def throw(self, **options):

        self.moneyinf(1,options.get("who"))

        self.gui.playsound(type1="3")
        self.round_over(options.get("who"))



    # kiertekeles

    def evaluate(self, table):

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

        bet = int(self.gui.all_bet.cget("text"))


        if(finalplayerpoints==finalcomppoints):

            self.gui.changeText(self.gui.infolabel,self.gui.tie_info)
            self.savegame2(["Tie"])

            verdict="Dontetlen!"
            player_money = int(self.gui.label_sum.cget("text")) + bet/2
            self.gui.label_sum.config(text=str(player_money))
            bot_money = int(self.gui.label_sum_bot.cget("text")) + bet/2
            self.gui.label_sum_bot.config(text=str(bot_money))

        elif(finalplayerpoints<finalcomppoints):

            verdict="A gep nyert!"


            bot_money = int(self.gui.label_sum_bot.cget("text")) + bet

            self.gui.label_sum_bot.config(text=str(bot_money))

            self.gui.changeText(self.gui.infolabel,self.gui.botwin_info)

            self.savegame2(["Bot wins"])


        else:
            verdict="Te nyertel!"

            player_money = int(self.gui.label_sum.cget("text")) + bet

            self.gui.label_sum.config(text=str(player_money))
            self.gui.changeText(self.gui.infolabel,self.gui.youwin_info)

            self.savegame2(["Player wins"])

        return verdict
        #return finalcomppoints,finalplayerpoints,verdict;

