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

        # kezdeti ertkek beallitasa
        
        self.player_money = 10000
        self.bot_money = 10000
        self.bot_bet = 0
        self.player_bet = 0
        self.all_bet = 0

        # kezdeti zsetonmennyiseg beolvasasa szinenkent

        self.player_white = int(self.gui.zseton.white.cget("text"))
        self.bot_white = int(self.gui.zseton2.white.cget("text"))

        self.player_blue = int(self.gui.zseton.blue.cget("text"))
        self.bot_blue = int(self.gui.zseton2.blue.cget("text"))

        self.player_red = int(self.gui.zseton.red.cget("text"))
        self.bot_red = int(self.gui.zseton2.red.cget("text"))

        self.player_green = int(self.gui.zseton.green.cget("text"))
        self.bot_green = int(self.gui.zseton2.green.cget("text"))

        self.player_black = int(self.gui.zseton.black.cget("text"))
        self.bot_black = int(self.gui.zseton2.black.cget("text"))

        # zsetonok ertekei

        self.black_value = 100
        self.green_value = 25
        self.red_value = 10
        self.blue_value = 5
        self.white_value = 1

        # jatekmenet kovetesehez szukseges valtozok
        
        self.decision = 0
        self.end = 0
        self.throw1 = 0


    def savegame3(self, buf,player100,player_money,player_bet,bot_money,bot_bet,bet):
        """ Jatek allasanak kimentese"""
        
        file_save=open(path+"pokersave111.txt","a")
        file_save.write(buf % (player100,player_money,player_bet,bot_money,bot_bet,bet))

        file_save.close()

    def savegame2(self, info):
        """ Jatek allasanak kimentese, pl. new round"""
        file_save=open(path+"pokersave111.txt","a")
    
        for i in range(len(info)):
            file_save.write(str(info[i])+"\n")

        file_save.close()


    def savegame(self):
        """ Jatek allasanak kimentese kesobbi visszatolteshez"""
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

        file_save.write("Player_money: " + self.player_money+"\n")
        file_save.write("Bot_money: " + self.bot_money+"\n")
        file_save.write("Player_bet: " + self.player_bet+"\n")
        file_save.write("Bot_bet: " + self.bot_bet+"\n")
        file_save.write("All_bet: " + self.all_bet+"\n")   

    def opengame(self):

        """Elmentett jatek visszatoltese"""
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

                elif "Player_money" in line:

                    line = line.rstrip("\n")
                    self.player_money = int(line)

                elif "Bot_money" in line:

                    line = line.rstrip("\n")
                    self.bot_money = int(line)
                    
                elif "Player_bet" in line:

                    line = line.rstrip("\n")
                    self.player_bet = int(line)
                    
                elif "Bot_bet" in line:

                    line = line.rstrip("\n")
                    self.bot_bet = int(line)

                elif "All_bet" in line:

                    line = line.rstrip("\n")
                    self.all_bet = int(line)

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

        # uj kor jelzese a fajlban:

        self.savegame2(["New round"])

        # kezdeti ertekek visszaallitasa

        self.end = 0
        self.throw1 = 0

        self.player_white_bet = 0
        self.bot_white_bet = 0

        self.player_blue_bet = 0
        self.bot_blue_bet = 0

        self.player_red_bet = 0
        self.bot_red_bet = 0

        self.player_green_bet = 0
        self.bot_green_bet = 0

        self.player_black_bet = 0
        self.bot_black_bet = 0

        
 
        # Gui elemek atallitasa (kartyak hatoldala, gombok letiltasa?)

        self.gui.game1()
        

        self.gui.all_bet.config(text="0")
        self.gui.mycardsbutton.config(state="disabled")
        self.gui.showbutton2.config(state="disabled")
        self.putmaincards()

        # kisvak - nagyvak meghatarozasa az elozo ertek alapjan

        kisvak1 =  self.gui.kisvak.cget("text")
        nagyvak1 =  self.gui.nagyvak.cget("text")

        if kisvak1 =="player":

            self.gui.kisvak.config(text="bot")
            self.gui.nagyvak.config(text="player")

            # a nagyvak adas gombjanak feloldasa, a kisvak adas gombjanak tiltasa

            self.gui.giveButton.config(state="normal")
            self.gui.giveButton2.config(state="disabled")

            self.gui.changeText(self.gui.infolabel,self.gui.bigblind_info)


        else:

            self.gui.kisvak.config(text="player")
            self.gui.nagyvak.config(text="bot")

            self.gui.giveButton2.config(state="normal")
            self.gui.giveButton.config(state="disabled")
            self.gui.raiseButton.config(state="disabled")
            self.gui.throwButton.config(state="disabled")
            self.bot.send_to_bot("kezdes",self.player_money,self.player_bet,self.bot_money,self.bot_bet) 
            self.gui.raiseButton.config(state="normal")
            self.gui.throwButton.config(state="normal")
            self.gui.changeText(self.gui.infolabel,self.gui.smallblind_info)
            

        
    def update_player_tokens(self):
        
        self.gui.zseton.black.config(text=str(self.player_black))
        self.gui.zseton.green.config(text=str(self.player_green))
        self.gui.zseton.red.config(text=str(self.player_red))
        self.gui.zseton.blue.config(text=str(self.player_blue))
        self.gui.zseton.white.config(text=str(self.player_white))

    def update_bot_tokens(self):
        self.gui.zseton2.black.config(text=str(self.bot_black))
        self.gui.zseton2.green.config(text=str(self.bot_green))
        self.gui.zseton2.red.config(text=str(self.bot_red))
        self.gui.zseton2.blue.config(text=str(self.bot_blue))
        self.gui.zseton2.white.config(text=str(self.bot_white))

    def player_give_tokens(self):
        # zsetonok szinenkenti darabszamanak valtozasa
 
        if self.player_black >= self.player_levon/self.black_value:
            self.player_black -= self.player_levon/self.black_value
            self.player_black_bet += self.player_levon/self.black_value
            self.player_levon = 0
            
        else:
            self.player_levon = self.player_levon - self.player_black*self.black_value
            self.player_black_bet += self.player_black
            self.player_black = 0
            

        if self.player_green >= self.player_levon/self.green_value:
            self.player_green -= self.player_levon/self.green_value
            self.player_green_bet += self.player_levon/self.green_value
            self.player_levon = 0

        else:
            self.player_levon = self.player_levon - self.player_green*self.green_value
            self.player_green_bet +=self.player_green
            self.player_green = 0
            

        if self.player_red >= self.player_levon/self.red_value:
            self.player_red -= self.player_levon/self.red_value
            self.player_red_bet += self.player_levon/self.red_value
            self.player_levon = 0
        else:
            self.player_levon = self.player_levon - self.player_red*self.red_value
            self.player_red_bet += self.player_red
            self.player_red = 0

        if self.player_blue >= self.player_levon/self.blue_value:
            self.player_blue -= self.player_levon/self.blue_value
            self.player_blue_bet += self.player_levon/self.blue_value
            self.player_levon = 0
        else:
            self.player_levon = self.player_levon - self.player_blue*self.blue_value
            self.player_blue_bet += self.player_blue
            self.player_blue = 0

        if self.player_white >= self.player_levon/self.white_value:
            self.player_white -= self.player_levon/self.white_value
            self.player_white_bet += self.player_levon/self.white_value
            self.player_levon = 0
        else:
            self.player_levon = self.player_levon - self.player_white*self.white_value
            self.player_white_bet += self.player_white
            self.player_white = 0

    def bot_give_tokens(self):

        # zsetonok szinenkenti darabszamanak valtozasa

        if self.bot_black >= self.bot_levon/self.black_value:
            self.bot_black -= self.bot_levon/self.black_value
            self.bot_black_bet += self.bot_levon/self.black_value
            self.bot_levon = 0
        else:
            self.bot_levon = self.bot_levon - self.bot_black*self.black_value
            self.bot_black_bet += self.bot_black
            self.bot_black = 0

        if self.bot_green >= self.bot_levon/self.green_value:
            self.bot_green -= self.bot_levon/self.green_value
            self.bot_green_bet += self.bot_levon/self.green_value
            self.bot_levon = 0
        else:
            self.bot_levon = self.bot_levon - self.bot_green*self.green_value
            self.bot_green_bet += self.bot_green
            self.bot_green = 0

        if self.bot_red >= self.bot_levon/self.red_value:
            self.bot_red -= self.bot_levon/self.red_value
            self.bot_red_bet += self.bot_levon/self.red_value
            self.bot_levon = 0
        else:
            self.bot_levon = self.bot_levon - self.bot_red*self.red_value
            self.bot_red_bet += self.bot_red
            self.bot_red = 0

        if self.bot_blue >= self.bot_levon/self.blue_value:
            self.bot_blue -= self.bot_levon/self.blue_value
            self.bot_blue_bet += self.bot_levon/self.blue_value
            self.bot_levon = 0
        else:
            self.bot_levon = self.bot_levon - self.bot_blue*self.blue_value
            self.bot_blue_bet += self.bot_blue
            self.bot_blue = 0

        if self.bot_white >= self.bot_levon/self.white_value:
            self.bot_white -= self.bot_levon/self.white_value
            self.bot_white_bet += self.bot_levon/self.white_value
            self.bot_levon = 0
        else:
            self.bot_levon = self.bot_levon - self.bot_white*self.white_value
            self.bot_white_bet += self.bot_white
            self.bot_white = 0


    def player_get_tokens(self):

        self.player_black += self.bot_black_bet+self.player_black_bet
        self.player_green += self.bot_green_bet+self.player_green_bet
        self.player_red += self.bot_red_bet+self.player_red_bet
        self.player_blue += self.bot_blue_bet+self.player_blue_bet
        self.player_white += self.bot_white_bet+self.player_white_bet

    def bot_get_tokens(self):

        self.bot_black += self.bot_black_bet+self.player_black_bet
        self.bot_green += self.bot_green_bet+self.player_green_bet
        self.bot_red += self.bot_red_bet+self.player_red_bet
        self.bot_blue += self.bot_blue_bet+self.player_blue_bet
        self.bot_white += self.bot_white_bet+self.player_white_bet

    def both_get_tokens(self):
   

        self.bot_black += self.bot_black_bet
        self.bot_green += self.bot_green_bet
        self.bot_red += self.bot_red_bet
        self.bot_blue += self.bot_blue_bet
        self.bot_white += self.bot_white_bet
        
        self.player_black += self.player_black_bet
        self.player_green += self.player_green_bet
        self.player_red += self.player_red_bet
        self.player_blue += self.player_blue_bet
        self.player_white += self.player_white_bet
    

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


        # lapok felforditasanak hangja

        self.gui.playsound(type1="3")

        # megnezzuk, ki nyert

        bet = int(self.gui.all_bet.cget("text"))

        if case == "throw_player":

                self.throw1 = 1

                self.bot_money += self.all_bet

                self.bot_get_tokens()
                self.update_bot_tokens()

                self.gui.label_sum_bot.config(text=str(self.bot_money))
                self.gui.changeText(self.gui.infolabel,self.gui.botwin_info)

                self.savegame2(["Bot wins"])

        elif case == "throw_bot":

                self.throw1 = 1

                self.player_money += self.all_bet

                self.player_get_tokens()
                self.update_player_tokens()
                
                self.gui.label_sum.config(text=str(self.player_money))
                self.gui.changeText(self.gui.infolabel,self.gui.youwin_info)

                self.savegame2(["Player wins"])

        elif case == "evaluate":
            
            table = self.gui.othercards + self.gui.maincards + self.gui.mycards

            self.evaluate(table)

        # lenullazzuk a teteket

        self.player_bet = 0
        self.bot_bet = 0
        self.all_bet = 0

        self.gui.changeText2([self.gui.all_bet_playerlabel,self.gui.all_bet_botlabel,self.gui.all_bet],"0")


        self.update_player_tokens()
        self.update_bot_tokens()

        


        # uj kor kezdese

        self.gui.showbutton2.config(state='normal')

        # letiltjuk a megad - emel - eldob gombokat a kovetkezo korig

        self.gui.giveButton.config(state="disabled")
        self.gui.raiseButton.config(state="disabled")
        self.gui.throwButton.config(state="disabled")

        self.gui.giveButton2.config(state="disabled")
        self.gui.raiseButton2.config(state="disabled")
        self.gui.throwButton2.config(state="disabled")

    def change_values(self,who,x,all_bet):

        if who == "player":

            if self.player_money>= x:

                self.player_money -= x
                self.player_bet += x
                self.player_levon = x

            elif self.player_money<x and self.player_money>0:
                self.player_money = 0
                self.player_bet += self.player_money
                self.player_levon = self.player_money

            self.player_give_tokens()

            self.update_player_tokens()


        elif who == "bot":

            if self.bot_money>= x:

                self.bot_money -= x
                self.bot_bet += x
                self.bot_levon = x

            elif self.bot_money<x and self.bot_money>0:
                self.bot_money = 0
                self.bot_bet += self.bot_money
                self.bot_levon = self.bot_money

            self.bot_give_tokens()

            self.update_bot_tokens()

                        
        self.all_bet = self.bot_bet + self.player_bet

        



    def moneyinf(self, s,who):

        
        self.decision +=1

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

                if self.player_bet == 0 and self.bot_bet == 200:

                    self.change_values("player",100,self.all_bet)
                    self.savegame3(buf,player100,self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)

                    self.gui.mycardsbutton.config(state="normal")
                    self.gui.changeText(self.gui.infolabel,self.gui.look_info)


                else:

                    # a jatekos gombjainak tiltasa

                    self.gui.changeState([self.gui.giveButton,self.gui.raiseButton,self.gui.throwButton],"disabled")

                    # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

                    self.gui.changeState([self.gui.giveButton2,self.gui.raiseButton2,self.gui.throwButton2],"normal")

                    # ha a nagyvakot kell betenni

                    if self.player_bet == 0 and self.bot_bet == 0:
                        
                        self.gui.mycardsbutton.config(state="normal")

                        self.change_values("player",200,self.all_bet)
                        self.savegame3(buf,player200,self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)


                    elif self.player_bet == 100 and self.bot_bet == 200:

                        self.change_values("player",100,self.all_bet)
                        self.savegame3(buf,player100,self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)


                    elif self.player_bet <= self.bot_bet:

                        self.change_values("player",self.bot_bet-self.player_bet,self.all_bet)
                        self.savegame3(buf,"player_give:"+str(self.bot_bet-self.player_bet),self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)

                    if self.end == 0:
                        self.bot.send_to_bot("adas",self.player_money,self.player_bet,self.bot_money,self.bot_bet) ## TODO
                self.gui.all_bet_playerlabel.config(text=self.player_bet)
                
                
                self.continue1()

            elif who == "bot":

                # a jatekos gombjainak tiltasat feloldjuk

                self.gui.changeState([self.gui.giveButton,self.gui.raiseButton,self.gui.throwButton],"normal")


                # a bot gombjait tiltjuk (ez majd nem kell)

                self.gui.changeState([self.gui.giveButton2,self.gui.raiseButton2,self.gui.throwButton2],"disabled")

                if self.bot_bet == 0 and self.player_bet == 200:

                    self.change_values("bot",100,self.all_bet)
                    self.savegame3(buf,bot100,self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)
                    self.gui.changeState([self.gui.giveButton2,self.gui.raiseButton2,self.gui.throwButton2],"normal")
                    self.gui.changeState([self.gui.giveButton,self.gui.raiseButton,self.gui.throwButton],"disabled")
                    self.bot.send_to_bot("bot_kisvak",self.player_money,self.player_bet,self.bot_money,self.bot_bet)
                    self.bot.send_to_bot_cards(self.gui.othercards[:])

                elif self.bot_bet == 0 and self.player_bet == 0:

                    self.change_values("bot",200,self.all_bet)
                    self.savegame3(buf,bot200,self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)


                elif self.bot_bet == 100 and self.player_bet == 200:

                    self.change_values("bot",100,self.all_bet)
                    self.savegame3(buf,bot100,self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)

                elif self.bot_bet <= self.player_bet:

                    self.change_values("bot",self.player_bet-self.bot_bet,self.all_bet)
                   
                    self.savegame3(buf,"bot_give:"+str(self.player_bet-self.bot_bet),self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)

                
                self.continue1()


                self.gui.all_bet_botlabel.config(text=self.bot_bet)
            

        # emelunk

        elif(s==3):

            emel = 500

            if who == "player":

                self.change_values("player",self.bot_bet-self.player_bet+500,self.all_bet)
                self.savegame3(buf,"player_give:"+str(self.bot_bet-self.player_bet+500),self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)
                self.gui.all_bet_playerlabel.config(text=self.player_bet)

                # letiltjuk a gombokat, amig a bot kovetkezik

                self.gui.giveButton.config(state="disabled")
                self.gui.raiseButton.config(state="disabled")
                self.gui.throwButton.config(state="disabled")

                # a bot gombjainak tiltasat feloldjuk (ez majd nem kell)

                self.gui.giveButton2.config(state="normal")
                self.gui.raiseButton2.config(state="normal")
                self.gui.throwButton2.config(state="normal")

                self.bot.send_to_bot("emeles",self.player_money,self.player_bet,self.bot_money,self.bot_bet)

            elif who == "bot":

                self.change_values("bot",self.player_bet-self.bot_bet+500,self.all_bet)
                self.savegame3(buf,"bot_give:"+str(self.player_bet-self.bot_bet+500),self.player_money,self.player_bet,self.bot_money,self.bot_bet,self.all_bet)
                self.gui.all_bet_botlabel.config(text=self.bot_bet)

                # letiltjuk a gombokat, amig a jatekos kovetkezik (ez majd nem kell)

                self.gui.giveButton2.config(state="disabled")
                self.gui.raiseButton2.config(state="disabled")
                self.gui.throwButton2.config(state="disabled")

                # a jatekos gombjainak tiltasat feloldjuk

                self.gui.giveButton.config(state="normal")
                self.gui.raiseButton.config(state="normal")
                self.gui.throwButton.config(state="normal")
            
            self.continue1()

        info = self.gui.infolabel.cget("text")
        if info not in self.gui.tie_info and info not in self.gui.botwin_info and info not in self.gui.youwin_info:


            self.gui.label_sum.config(text=str(self.player_money))
            self.gui.label_sum_bot.config(text=str(self.bot_money))

##        bet = player_bet+bot_bet
##        player_bet = int(self.gui.all_bet_playerlabel.cget("text"))
##        bot_bet = int(self.gui.all_bet_botlabel.cget("text"))
        self.gui.all_bet.config(text=str(self.all_bet))

            

    def give(self, **options):

        # zsetoncsorges hangja:

        self.gui.playsound(type1="1")

        # tet meagadasa/tartasa

        self.moneyinf(2,options.get("who"))

    def continue1(self):

        if self.player_bet == self.bot_bet and self.decision>=1:

        
            # megnezzuk, hol tart a jatek

            # ha a 3. lap nincs felforditva, akkor a flop kovetkezik

            if self.gui.card[2].cget("text") == "back":
                self.showmaincards(type1="flop")

                self.savegame2([self.gui.maincards[0:3]])
                self.bot.send_to_bot_cards(self.gui.maincards[0:3])
                #send_to_bot(self.gui.maincards[0:3])

            # ha a 4. lap nincs felforditva (1-3 igen), akkor a turn kovetkezik

            elif self.gui.card[3].cget("text") == "back":
                self.showmaincards(type1="turn")

                self.bot.send_to_bot_cards(self.gui.maincards[3:4])
                #send_to_bot(self.gui.maincards[3:4])

            # ha az 5. lap nincs felforditva (1-4 igen), akkor a river kovetkezik
            elif self.gui.card[4].cget("text") == "back":
                self.showmaincards(type1="river")

                self.bot.send_to_bot_cards(self.gui.maincards[4:])
                #send_to_bot(self.gui.maincards[4:])
                self.end = 1

            # ha mindegyik fel van forditva, vege a kornek

            else:

                # ha nem tortent dobas

                if  self.throw1 ==0:
                
                    self.round_over("evaluate")
                    self.savegame2(["evaluate"])

            self.decision = 0


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

            verdict="Dontetlen!"
            self.player_money += self.player_bet
            self.bot_money += self.bot_bet

            self.both_get_tokens()
            self.update_bot_tokens()
            self.update_player_tokens()

            self.gui.changeText(self.gui.infolabel,self.gui.tie_info)
            self.savegame2(["Tie"])
            self.gui.label_sum.config(text=str(self.player_money))
            self.gui.label_sum_bot.config(text=str(self.bot_money))

        elif(finalplayerpoints<finalcomppoints):

            verdict="A gep nyert!"


            self.bot_money += self.all_bet

            self.bot_get_tokens()
            self.update_bot_tokens()
           
                        
            self.gui.label_sum_bot.config(text=str(self.bot_money))
            self.gui.changeText(self.gui.infolabel,self.gui.botwin_info)
            self.savegame2(["Bot wins"])


        else:
            verdict="Te nyertel!"

            self.player_money += self.all_bet

            self.player_get_tokens()
            self.update_player_tokens()

            self.gui.label_sum.config(text=str(self.player_money))
            self.gui.changeText(self.gui.infolabel,self.gui.youwin_info)
            self.savegame2(["Player wins"])

        return verdict
