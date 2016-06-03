import Tkinter as tk
from PIL import ImageTk, Image
import random
import time
import winsound
import os
import platform


class PokerGui:
    def __init__(self, master):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(BASE_DIR, "poker")+os.path.sep

        # Feliratok, nyelvek

        self.create_subs()

        self.languages = []
        self.subtitles=[]

        self.infolabels = []

        for i in range(7):
            self.infolabels.append([])
            
        self.add_language("english")
        self.add_language("hungarian")
        self.add_language("german")
        self.add_language("italien")

        # Meretek

        self.label_width1 = 15
        self.label_width2 = 5
        self.button_width = 6
        self.button_width2 = 10
        self.button_width3 = 15
        
        self.card_size = [100,250]
        self.token_size = [30,30]
        self.small_card_sizes = [70,120]
        self.sample_card_sizes = [70,120]
        
        self.table_part_size = [300,300]

        self.main_size = [1200,670]
        self.minsize = [1000,600]
        self.maincard_size=[100,160]

        #master.minsize(width=self.minsize[0], height=self.minsize[1])
        #master.geometry('1200x670')
        master.maxsize(width=self.main_size[0], height=self.main_size[1])
        #master.resizable(0,0)

        # Kepek, stilusok

        self.sample_images = []
        self.image_names = []
        
        self.get_pictures()
        
        self.rules_pic = ["rules.png","rules2.png"]

        self.cardback_samples = []
        self.cardback_smalls = []
        self.cardback_larges = []

        self.styles = []
        
        self.give_style("red","cardback.png")
        self.give_style("red2","cardback4.png")
        self.give_style("orange","cardback_orange.png")
        self.give_style("yellow","cardback_yellow.png")
        self.give_style("green","cardback_green.png")
        self.give_style("purple","cardback_purple.png")
        self.give_style("blue","cardback3.png")
        self.give_style("blue2","cardback_blue2.png")
        self.give_style("blue3","cardback_blue3.png")
        self.give_style("blue4","cardback_blue4.png")
               

        # Cimsor

        master.wm_title("Nagyonkigyo poker")
        master.tk.call("wm", "iconphoto", master._w, self.img_blue3)

        # Kilepes

        def destroy():
            self.save_settings()
            master.destroy()

        master.protocol("WM_DELETE_WINDOW", destroy)

        # Kezdeti beallitasok

        self.language = ["english"]
        self.sound = "off"
        self.style = "red"

        self.cardpictures = []
        self.cardpictures2 = []
        self.cardpictures3 = []
        self.maincards = []
        self.mycards = []
        self.othercards = []

        self.read_settings()
        self.get_style()

        vakok = tk.Frame(master)
        self.kisvak = tk.Label(vakok,text='')
        self.nagyvak = tk.Label(vakok,text='')

        # Menu

        self.menubar = tk.Menu(master)
        self.create_menu()
        master.config(menu=self.menubar)


        # Asztal hattere

        self.mainframe = tk.Label(master,height=self.main_size[1],width=self.main_size[0],image=self.table2)
        self.mainframe.place(x=0,y=0)

        # Masik jatekos (gep)
     
        self.buttons_bot = tk.Frame(master)
        self.zseton2 = tk.Frame(master)
        self.zsetonsum_bot = tk.Frame(master)
        self.cards_others = tk.Frame(master)


        self.create_bot_cards()
        self.create_bot_buttons()
            
        self.create_bot_labelsum()
        self.create_tokenlabels(self.zseton2)

        # Tetek

        self.bets = tk.Frame(master)
        self.create_bets()

        # Fo kartyak

        self.create_main_cards(master)

        # Uj kor gomb
        
        self.buttons = tk.Frame(master)
        self.create_showbutton()

        # Sajat kartyak es zsetonok

        self.cards_mine = tk.Frame(master)
        self.cards_mine2 = tk.Frame(master)
        self.zseton = tk.Frame(master)
        self.zsetonsum = tk.Frame(master)
        self.buttons2 = tk.Frame(master)

        self.create_mine_cards()

        self.create_tokenlabels(self.zseton)

        self.create_buttons()
        self.create_labelsum()

       
        self.changeState([self.giveButton,self.raiseButton,self.throwButton,self.giveButton2,self.raiseButton2,self.throwButton2],"disabled")

        # Master elemeinek elhelyezese

        self.new_separator(master,0,50,0,0)

        self.new_separator(master,300,0,1,0)
        self.zsetonsum_bot.grid(row=1,column=1)
        self.zseton2.grid(row=1,column=2)
        self.cards_others.grid(row=1,column=4)
        self.buttons_bot.grid(row=1,column=5)

        self.new_separator(master,0,10,2,0)
        
        self.bets.grid(row=3,column=0)
        # column 1-5: main cards
        self.buttons.grid(row=3,column=6)

        self.new_separator(master,0,10,4,0)
        
        self.cards_mine2.grid(row=5,column=1)
        self.cards_mine.grid(row=5,column=2)
        self.zsetonsum.grid(row=5,column=3)
        self.zseton.grid(row=5,column=4)
        self.buttons2.grid(row=5,column=5)
     
        self.new_separator(master,0,50,6,0)


        master.grid_columnconfigure(0,weight=1)
	master.grid_columnconfigure(1,weight=300)
	master.grid_columnconfigure(2,weight=1)
	master.grid_columnconfigure(3,weight=200)
	master.grid_columnconfigure(4,weight=200)
	master.grid_columnconfigure(5,weight=100)
	master.grid_columnconfigure(6,weight=100)
	master.grid_rowconfigure(0,weight=50)
	master.grid_rowconfigure(1,weight=50)
	master.grid_rowconfigure(2,weight=100)
	master.grid_rowconfigure(3,weight=100)
	master.grid_rowconfigure(4,weight=100)
	master.grid_rowconfigure(5,weight=100)

        

        
        self.update_subs()
       


        # Uj jatek betoltese

    def game1(self):

        self.changeState([self.giveButton,self.raiseButton,self.throwButton,self.giveButton2,self.raiseButton2,self.throwButton2],"disabled")  

        self.get_style()

        self.changeImages([self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]],[self.cardback_large])
        self.changeImages([self.card_others1,self.card_others2,self.card_mine1,self.card_mine2],[self.cardback_small])     

        self.hide([self.cards[0],self.cards[1],self.cards[2],self.cards[3],self.cards[4],self.cards_mine,self.cards_others])

        self.cardlist2 = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13",
                    "B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13",
                    "C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13",
                    "D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13"]
         
        del self.cardpictures[:]
        del self.cardpictures2[:]
        del self.cardpictures3[:]
        del self.maincards[:]
        del self.othercards[:]
        del self.mycards[:]

        for i in range(9):

                self.next_card = random.choice(self.cardlist2)
                del(self.cardlist2[self.cardlist2.index(self.next_card)])
                self.name = self.next_card+".png"

                if i<2:
                
                    self.mycards.append(self.next_card)
                    self.pic2 = self.load_picture(self.name,"resize",self.small_card_sizes[0],self.small_card_sizes[1])
                
                    self.cardpictures.append(self.pic2)

                elif i>=2 and i<4:

                
                    self.othercards.append(self.next_card)
                    self.pic2 = self.load_picture(self.name,"resize",self.small_card_sizes[0],self.small_card_sizes[1])
                    self.cardpictures3.append(self.pic2)

                elif i>=4:

                    self.maincards.append(self.next_card)
                    self.pic2 = self.load_picture(self.name,"resize",self.maincard_size[0],self.maincard_size[1])
                                  
                    self.cardpictures2.append(self.pic2)

        self.card[0].config(text="back")
        self.card[1].config(text="back")
        self.card[2].config(text="back")
        self.card[3].config(text="back")
        self.card[4].config(text="back")
        self.card_others1.config(text="back")
        self.card_others2.config(text="back")
        self.card_mine1.config(text="back")
        self.card_mine2.config(text="back")



    # GUI elemek

    def create_main_cards(self,master):

            self.main_card_list = [f for f in range(5)]
            self.cards = {}
            self.card = {}
            frames = []
            labels = []

            for i in self.main_card_list:
                       
                self.cards[i] = tk.Frame(master,width=self.card_size[0],height=self.card_size[1])
                self.card[i] = tk.Label(self.cards[i],image=self.cardback_large,text="back",bg="black")
                self.cards[i].grid(row=3,column=i+1)
                self.card[i].grid(row=0,column=0)
                self.cards[i].lower()
                self.card[i].bind('<Configure>', self.resize_images)

            

    def create_showbutton(self):
            self.showbutton2 = tk.Button(self.buttons,text="Start round",width=self.button_width2)
            self.showbutton2.grid(row=1)

    def create_mine_cards(self):

        self.card_mine1 = tk.Label(self.cards_mine, image=self.cardback_small)
        self.card_mine2 = tk.Label(self.cards_mine, image=self.cardback_small)

        self.card_mine1.grid(row=0,column=0)
        self.card_mine2.grid(row=0,column=1)

        self.cards_mine.lower()

        self.mycardsbutton = tk.Button(self.cards_mine2,text="Show my cards",state="disabled",width = self.button_width3)
        self.mycardsbutton.grid(row=0)

    def create_bot_cards(self):

        self.card_others1 = tk.Label(self.cards_others, image=self.cardback_small)
        self.card_others2 = tk.Label(self.cards_others, image=self.cardback_small)

        self.card_others1.grid(row=0,column=0)
        self.card_others2.grid(row=0,column=1)

        self.cards_others.lower()

    def create_tokenlabels(self,frame):

        tk.Label(frame, text="(1)").grid(row=0)
        tk.Label(frame, text="(5)").grid(row=1)
        tk.Label(frame, text="(10)").grid(row=2)
        tk.Label(frame, text="(25)").grid(row=3)
        tk.Label(frame, text="(100)").grid(row=4)

        tk.Label(frame, image=self.img_white2).grid(row=0,column=1)
        tk.Label(frame, image=self.img_red2).grid(row=1,column=1)
        tk.Label(frame, image=self.img_blue2).grid(row=2,column=1)
        tk.Label(frame, image=self.img_green2).grid(row=3,column=1)
        tk.Label(frame, image=self.img_black2).grid(row=4,column=1)

        for h in range(5):

                tk.Label(frame, text="x").grid(row=h,column=2)


        frame.white = tk.Label(frame, text="50")
        frame.blue = tk.Label(frame, text="10")
        frame.red = tk.Label(frame, text="40")
        frame.green = tk.Label(frame, text="20")
        frame.black = tk.Label(frame, text="90")

        frame.white.grid(row=0,column=3)
        frame.blue.grid(row=1,column=3)
        frame.red.grid(row=2,column=3)
        frame.green.grid(row=3,column=3)
        frame.black.grid(row=4,column=3)

        frame.grid_columnconfigure(0,weight=1)
	frame.grid_columnconfigure(1,weight=1)
	frame.grid_columnconfigure(2,weight=1)
	frame.grid_columnconfigure(3,weight=1)
	
	frame.grid_rowconfigure(0,weight=1)
	frame.grid_rowconfigure(1,weight=1)
	frame.grid_rowconfigure(2,weight=1)
	frame.grid_rowconfigure(3,weight=1)
	frame.grid_rowconfigure(4,weight=1)


    def create_buttons(self):

        self.giveButton = tk.Button(self.buttons2,text="Give",width = self.button_width)
        self.raiseButton = tk.Button(self.buttons2,text="Raise",width = self.button_width)
        self.throwButton = tk.Button(self.buttons2,text="Throw",width = self.button_width)

        self.giveButton.grid(row=0)       
        self.raiseButton.grid(row=0, column=1)       
        self.throwButton.grid(row=0, column=2)

    def create_bot_buttons(self):

        self.giveButton2 = tk.Button(self.buttons_bot,text="Give",width = self.button_width)
        self.giveButton2.grid(row=0)

        self.raiseButton2 = tk.Button(self.buttons_bot,text="Raise",width = self.button_width)
        self.raiseButton2.grid(row=0, column=1)

        self.throwButton2 = tk.Button(self.buttons_bot,text="Throw",width = self.button_width)
        self.throwButton2.grid(row=0, column=2)

    def create_labelsum(self):
        
    
        self.label_sum2 = tk.Label(self.zsetonsum,text="Your tokens:",width = self.label_width1)
        self.label_sum = tk.Label(self.zsetonsum,text="10000",width = self.label_width2)

        self.label_sum2.grid(row=0,column=0)
        self.label_sum.grid(row=0,column=1)

    def create_bot_labelsum(self):
            
        
        self.label_sum_bot2 = tk.Label(self.zsetonsum_bot,text="Bot tokens:",width = self.label_width1)
        self.label_sum_bot = tk.Label(self.zsetonsum_bot,text="10000",width = self.label_width2)

        self.label_sum_bot2.grid(row=0,column=0)
        self.label_sum_bot.grid(row=0,column=1)

    def create_bets(self):

        self.bets1 = tk.Frame(self.bets)
        self.bets2 = tk.Frame(self.bets)

        self.bet_labels_width = 16

        self.all_bet_playerlabel1 = tk.Label(self.bets1,text = "Your bet:",width=self.bet_labels_width)
        self.all_bet_playerlabel = tk.Label(self.bets1,text = "0")
        self.all_bet_botlabel1 = tk.Label(self.bets1,text = "Bot's bet:",width=self.bet_labels_width)
        self.all_bet_botlabel = tk.Label(self.bets1,text = "0")
        self.all_bet1 = tk.Label(self.bets1,text = "All bet:",width=self.bet_labels_width)
        self.all_bet = tk.Label(self.bets1,text = "0")

        self.all_bet_botlabel1.grid(row=0,column=0)
        self.all_bet1.grid(row=1,column=0)
        self.all_bet_playerlabel1.grid(row=2,column=0)

        self.all_bet_botlabel.grid(row=0,column=1)
        self.all_bet.grid(row=1,column=1)
        self.all_bet_playerlabel.grid(row=2,column=1)

        self.info_sep = tk.Label(self.bets2)
        self.infolabel = tk.Label(self.bets2,text="Welcome!")

        self.bets1.grid(row=0)
        self.bets2.grid(row=1)

        self.info_sep.grid(row=0)
        self.infolabel.grid(row=1)

    def new_separator(self,master,w,h,r,c):

        if h!=0 and w!=0:
            separator = tk.Frame(master,width=w,height=h)
        elif h==0:
            separator = tk.Frame(master,width=w)
        elif w==0:
            separator = tk.Frame(master,height=h)
        separator.grid(row=r,column=c)
        separator.lower()

    # Hangok

    def playsound(self,**options):

            if self.sound == "on":

                    if platform.system() == "Windows":


                        if options.get("type1") == "1": 
                                winsound.PlaySound(self.path+"poker1.wav",winsound.SND_FILENAME)
                        elif options.get("type1") == "2": 
                                winsound.PlaySound(self.path+"poker1.wav",winsound.SND_FILENAME)
                                winsound.PlaySound(self.path+"poker1.wav",winsound.SND_FILENAME)

                        elif options.get("type1") == "3":
                                winsound.PlaySound(self.path+"cardShove4.wav",winsound.SND_FILENAME)

                    elif platform.system() == "Linux":

                        print "linux"


    # Kepek es stilusok

    def load_picture(self,filename,type1,x,y):

            image1 = Image.open(self.path+filename)
            if type1 == "resize":
                image_resized = image1.resize((x, y),Image.ANTIALIAS)
                image2 = ImageTk.PhotoImage(image_resized)

            else:
                image2 = ImageTk.PhotoImage(image1)
            return image2

    def get_pictures(self):
            
            self.img_blue2 = self.load_picture("blue.png","resize",self.token_size[0],self.token_size[1])
            self.img_green2 = self.load_picture("green.png","resize",self.token_size[0],self.token_size[1])
            self.img_red2 = self.load_picture("red.png","resize",self.token_size[0],self.token_size[1])
            self.img_black2 = self.load_picture("black.png","resize",self.token_size[0],self.token_size[1])
            self.img_white2 = self.load_picture("white.png","resize",self.token_size[0],self.token_size[1])


            self.table2 = self.load_picture("table2.png","resize",self.main_size[0],self.main_size[1])
            self.table_part = self.load_picture("table_part2.png","resize",self.table_part_size[0],self.table_part_size[1])
            self.table_part2 = self.load_picture("table_part2.png","resize",self.token_size[0],self.token_size[1])
            
            self.img_blue3 = self.load_picture("blue1.png","resize",self.token_size[0],self.token_size[1])

    def changeImages(self,elemek,images):

        for i in range(len(elemek)):
            if len(elemek) == len(images):
                if elemek[i].cget("text") == "back" or elemek[i].cget("text") == "ready":
                    elemek[i].config(image=images[i])
            elif len(images) == 1:
                if elemek[i].cget("text") == "back" or elemek[i].cget("text") == "ready":
                    elemek[i].config(image=images[0])

    def give_style(self,style, pic_name):

            try:

                self.cardback_small = self.load_picture(pic_name,"resize",self.small_card_sizes[0],self.small_card_sizes[1])
                self.cardback_sample = self.load_picture(pic_name,"resize",self.sample_card_sizes[0],self.sample_card_sizes[1])
                self.cardback_large = self.load_picture(pic_name,"no_resize",0,0)

                self.cardback_samples.append(self.cardback_sample)
                self.cardback_smalls.append(self.cardback_small)
                self.cardback_larges.append(self.cardback_large)
                
                self.image_names.append(pic_name)
                self.styles.append(style)

            except: IOError

    def get_style(self):

        s = self.styles.index(self.style)
        self.cardback_small = self.cardback_smalls[s]
        self.cardback_large = self.cardback_larges[s]
        self.cardback_sample = self.cardback_samples[s]
        return self.cardback_small,self.cardback_large,self.cardback_sample


    def resize_images(self,event):

        new_width = event.width
	new_height = event.height

	#self.cardback_small = self.load_picture("cardback.png","resize",new_width, new_height)
##        self.cardback_large = self.load_picture("cardback.png","resize",new_width, new_height)
##        for i in self.main_card_list:
##                       
##                
##                self.card[i].config(image=self.cardback_large)


    # Szovegek

    def create_subs(self):

        self.welcome_info=[]
        self.look_info=[]
        self.tie_info=[]
        self.botwin_info=[]
        self.youwin_info=[]
        self.bigblind_info=[]
        self.smallblind_info=[]
        self.stat_info1=[]
        self.stat_info2=[]
        self.stat_info3=[]
        self.choose_lang_info=[]
        #self.lang_info=[]
        self.lang_info = [["English","Angol","Englisch"],["Hungarian","Magyar","Ungarisch"],["German","Nemet","Deutsch"]]
        self.give_info=[]
        self.raise_info=[]
        self.throw_info=[]

        self.start_info=[]
        self.mycards_info=[]

        self.player_token_info=[]
        self.bot_token_info=[]
                
        self.player_bet_info=[]
        self.bot_bet_info=[]
        self.all_bet_info=[]
        self.filemenu0_info=[]
        self.filemenu1_info=[]
        self.filemenu2_info=[]
        self.filemenu3_info=[]

        self.settingsmenu0_info=[]
        self.settingsmenu1_info=[]
        self.settingsmenu2_info=[]
        self.settingsmenu3_info=[] 
        
        self.statmenu0_info=[]
        self.statmenu1_info=[]

        self.rulesmenu0_info=[]
        self.rulesmenu1_info=[]

    def changeText(self,elem,text):

        for i in range(len(self.languages)):
            if self.language == [self.languages[i]]:
                elem.config(text=text[i])
        

    def changeText2(self,elemek,text):

        for i in range(len(elemek)):
            elemek[i].config(text=text)


    def changeMenu(self,elem,j,text):

        for i in range(len(self.languages)):
            if self.language == [self.languages[i]]:
                elem.entryconfigure(j,label=text[i])



    def update_subs(self):    
                
        self.changeText(self.showbutton2, self.start_info)
        self.changeText(self.mycardsbutton, self.mycards_info)

        self.changeText(self.giveButton,self.give_info)
        self.changeText(self.giveButton2,self.give_info)
        self.changeText(self.raiseButton,self.raise_info)
        self.changeText(self.raiseButton2,self.raise_info)
        self.changeText(self.throwButton,self.throw_info)
        self.changeText(self.throwButton2,self.throw_info)

        self.changeText(self.all_bet_playerlabel1, self.player_bet_info)
        self.changeText(self.all_bet_botlabel1, self.bot_bet_info)
        self.changeText(self.all_bet1, self.all_bet_info)
        self.changeText(self.label_sum2, self.player_token_info)
        self.changeText(self.label_sum_bot2, self.bot_token_info)

        self.changeMenu(self.menubar,1,self.filemenu0_info)
        self.changeMenu(self.menubar,2,self.statmenu0_info)
        self.changeMenu(self.menubar,3,self.settingsmenu0_info)
        self.changeMenu(self.menubar,4,self.rulesmenu0_info)

        self.changeMenu(self.filemenu,0,self.filemenu1_info)
        self.changeMenu(self.filemenu,1,self.filemenu2_info)
        self.changeMenu(self.filemenu,2,self.filemenu3_info)

        self.changeMenu(self.settingsmenu,0,self.settingsmenu1_info)
        self.changeMenu(self.settingsmenu,1,self.settingsmenu2_info)
        self.changeMenu(self.settingsmenu,2,self.settingsmenu3_info)

        self.changeMenu(self.statmenu,1,self.statmenu1_info)
        self.changeMenu(self.rulesmenu,1,self.rulesmenu1_info)

        index1 = self.languages.index(self.language[0])

        for i in range(len(self.infolabels)):
            for j in range(len(self.languages)):
                if self.infolabel.cget("text") == self.infolabels[i][j]:
                        self.infolabel.config(text=self.infolabels[i][index1])
                        




    # Allapotok

    def changeState(self,elemek,state):

        for i in range(len(elemek)):
            elemek[i].config(state=state)

    def hide(self,elemek):
        for i in range(len(elemek)):
            elemek[i].lower()

    # Alap beallitasok: nyelv, hang, stilus

    def save_settings(self):
            settings_save=open(self.path+"pokersettings.txt","w")
            settings_save.write("Language: "+self.language[0]+"\n")
            settings_save.write("Sound: "+self.sound+"\n")
            settings_save.write("Style: "+self.style+"\n")
            settings_save.close()

    def read_settings(self):
            try:
                settings_read=open(self.path+"pokersettings.txt","r")
                for line in settings_read.readlines():
                    if "Language" in line:
                        line = line.rstrip("\n")
                        language = str(line.split(": ")[1])
                        if language in self.languages:
                            del self.language[0]
                            self.language.append(language)

                    elif "Sound" in line:
                        line = line.rstrip("\n")
                        
                        self.sound = str(line.split(": ")[1])

                    elif "Style" in line and "state" not in line:
                        line = line.rstrip("\n")
                        if str(line.split(": ")[1]) in  self.styles:
                            self.style = str(line.split(": ")[1])

                settings_read.close()

            except IOError:
                pass

    def add_language(self,language):
            success = self.read_language_subs(language)
            if success:
                self.languages.append(language)

##            self.lang_info.append([])
##            for j in range(len(self.lang_info)):
##                    self.lang_info[j].append(language)

    def read_language_subs(self,language):
            
        try:
            file_lang = open(self.path+"sub_"+str(language)+".txt","r")
            del self.subtitles[:]
            for line in file_lang.readlines():
                
                line = line.rstrip("\n")
                self.subtitles.append(str(line))

            self.welcome_info.append(self.subtitles[0])
            self.look_info.append(self.subtitles[1])
            self.tie_info.append(self.subtitles[2])
            self.botwin_info.append(self.subtitles[3])
            self.youwin_info.append(self.subtitles[4])
            self.bigblind_info.append(self.subtitles[5])
            self.smallblind_info.append(self.subtitles[6])

            self.infolabels[0].append(self.subtitles[0])
            self.infolabels[1].append(self.subtitles[1])
            self.infolabels[2].append(self.subtitles[2])
            self.infolabels[3].append(self.subtitles[3])
            self.infolabels[4].append(self.subtitles[4])
            self.infolabels[5].append(self.subtitles[5])
            self.infolabels[6].append(self.subtitles[6])
            
            self.stat_info1.append(self.subtitles[7])
            self.stat_info2.append(self.subtitles[8])
            self.stat_info3.append(self.subtitles[9])
            self.choose_lang_info.append(self.subtitles[10])
            
            self.give_info.append(self.subtitles[11])
            self.raise_info.append(self.subtitles[12])
            self.throw_info.append(self.subtitles[13])

            self.start_info.append(self.subtitles[14])
            self.mycards_info.append(self.subtitles[15])

            self.player_token_info.append(self.subtitles[16])
            self.bot_token_info.append(self.subtitles[17])
            
            self.player_bet_info.append(self.subtitles[18])
            self.bot_bet_info.append(self.subtitles[19])
            self.all_bet_info.append(self.subtitles[20])

            self.filemenu0_info.append(self.subtitles[21])
            self.filemenu1_info.append(self.subtitles[22])
            self.filemenu2_info.append(self.subtitles[23])
            self.filemenu3_info.append(self.subtitles[24])

            self.settingsmenu0_info.append(self.subtitles[25])
            self.settingsmenu1_info.append(self.subtitles[26])
            self.settingsmenu2_info.append(self.subtitles[27])
            self.settingsmenu3_info.append(self.subtitles[28]) 
            
            self.statmenu0_info.append(self.subtitles[29])
            self.statmenu1_info.append(self.subtitles[30])

            self.rulesmenu0_info.append(self.subtitles[31])
            self.rulesmenu1_info.append(self.subtitles[32])


            file_lang.close()
            return True
        except IOError:
            return False
            pass


    def create_menu(self):

        # Fajl menu
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")

        # Statisztika menu

        self.statmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Statistics", menu=self.statmenu)
        self.statmenu.add_command(label="Game stat",command=self.statistics)

        # Beallitasok menu

        self.settingsmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Settings", menu=self.settingsmenu)
        self.settingsmenu.add_command(label="Language",command=self.languageset)
        self.settingsmenu.add_command(label="Sounds",command=self.set_sound)
        self.settingsmenu.add_command(label="Card types",command=self.card_type)

        # Szabalyok menu

        self.rulesmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Rules", menu=self.rulesmenu)
        self.rulesmenu.add_command(label="Rankings",command=self.ranking)


    # Statisztika, jatekok szama

    def statistics(self):

        stat = tk.Toplevel()
        #stat.resizable(0,0)
        #stat.tk.call("wm", "iconphoto", master._w, self.img_blue3)

        label = tk.Label(stat,text="All games: ")
        label2 = tk.Label(stat,text="Lost: ")
        label1 = tk.Label(stat,text="Win: ")

        
        self.changeText(label,self.stat_info1)
        self.changeText(label2,self.stat_info2)
        self.changeText(label1,self.stat_info3)
            
        label.pack()
        label1.pack()
        label2.pack()
        stat.mainloop()


     # Beallitasok, nyelv valasztasa

    def languageset(self):
          
        settings = tk.Toplevel()
        settings.resizable(0,0)

        def update_self():
            self.changeText(label,self.choose_lang_info)
            for i in range(len(frame1.buttons)):
                self.changeText(frame1.buttons[i],self.lang_info[i])

        def set_language(language):

            del self.language[0]
            
            self.language.append(language)


            update_self()
            self.update_subs()

            

        frame = tk.Frame(settings,width = 600)
        frame1 = tk.Frame(settings,width = 600)

        label = tk.Label(frame,text="Choose language")
        label.pack()

        if len(self.languages) <=4:

            button_list = [f for f in range(len(self.languages))]
            frame1.buttons = {}
            buttons = []

            for num in button_list:

                                      
                frame1.buttons[num] = tk.Button(frame1,text=self.languages[num],command=lambda f=self.languages[num]:set_language(f))
                frame1.buttons[num].pack(side=tk.LEFT)                        
            

        frame.pack()
        frame1.pack()

        settings.mainloop()


    # Hang menu
    
    def set_sound(self):

        sound_settings = tk.Toplevel()
        sound_settings.resizable(0,0)

        frame = tk.Frame(sound_settings,width = 600)
        frame1 = tk.Frame(sound_settings,width = 600)

        label = tk.Label(frame,text="Sound")
        label.pack()

        def change_sound(**options):
                
            self.sound = options.get("type1")
        
        on_button = tk.Radiobutton(frame1, variable=self.sound,value="on",text="On", command=lambda:change_sound(type1="on"))
        off_button = tk.Radiobutton(frame1, variable=self.sound,value="off",text="Off",command=lambda:change_sound(type1="off"))

        if self.sound == "on":
                on_button.select()
                off_button.deselect()
        elif self.sound == "off":
                off_button.select()
                on_button.deselect()

        on_button.pack()
        off_button.pack()
        
        frame.pack()
        frame1.pack()

        sound_settings.mainloop()


    def card_type(self):

        card_types = tk.Toplevel()
        card_types.resizable(0,0)

        frame = tk.Frame(card_types,width = 600)

        label = tk.Label(frame,text="Choose")
        label.pack()
        frame.pack()


        if len(self.styles) <= 6:
            sor = 1
            column = len(self.styles)

        else:
            if len(self.styles)%6 ==0:
                sor = len(self.styles)/6
                column = 6
            else:
                sor = len(self.styles)/6+1
                column = 6              

        cardtypes_frame = tk.Frame(card_types)
        alapframes = [f for f in range(sor)]
        cardtypes_frame.frames = {}
        frames = []

        columns = [i for i in range(column)]

        labels = []

        select = lambda z, event: (lambda u: select_style(frame = z,num=event))

        for frame in alapframes:
                
                cardtypes_frame.frames[frame] = tk.Frame(cardtypes_frame)
                cardtypes_frame.frames[frame].grid(row=frame,column=0)
                cardtypes_frame.frames[frame].labels = {}

                for col in columns:

                        try:

                            cardtypes_frame.frames[frame].labels[col]= tk.Label(cardtypes_frame.frames[frame],image=self.cardback_samples[frame*6+col])
                            cardtypes_frame.frames[frame].labels[col].bind("<Button-1>",select(frame,col))
                            cardtypes_frame.frames[frame].labels[col].grid(row=0,column=col)
                            
                        except: IndexError

##                                cardtypes_frame.frames[frame].labels[ures]= tk.Label(cardtypes_frame.frames[frame],width=self.small_card_sizes[0])
##                        
##                                cardtypes_frame.frames[frame].labels[ures].grid(row=0,column=ures)

                        

        cardtypes_frame.pack()

        def select_style(**options):
             
            s = options.get("num")
            f = options.get("frame")

            for i in range(len(cardtypes_frame.frames)):

                for j in range(len(cardtypes_frame.frames[i].labels)):

                    cardtypes_frame.frames[i].labels[j].configure(bd=0)
               
            cardtypes_frame.frames[f].labels[s].config(bd=2,bg="green")

            self.cardback_small = self.cardback_smalls[f*6+s]
            self.cardback_large = self.cardback_larges[f*6+s]

            self.changeImages([self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]],[self.cardback_large])
            self.changeImages([self.card_others1,self.card_others2,self.card_mine1,self.card_mine2],[self.cardback_small])

            self.style = self.styles[f*6+s]

        card_types.mainloop()

     # Szabalyok
            
    def ranking(self):

        rank = tk.Toplevel()
        rank.resizable(0,0)
        
        index1 = self.languages.index(self.language[0])
        img_rank2 = self.load_picture(self.rules_pic[index1],"resize",210,390)

        label = tk.Label(rank,image=img_rank2)
        label.pack()

        rank.mainloop()
