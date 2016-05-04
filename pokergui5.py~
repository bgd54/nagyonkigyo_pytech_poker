import Tkinter as tk
from PIL import ImageTk, Image
import random
import time
import winsound
import os

master = tk.Tk()

# Kepek

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "poker")+os.path.sep

img_blue = Image.open(path+"blue.png")
img_blue1 = Image.open(path+"blue1.png")
img_blue_resized = img_blue.resize((30, 30),Image.ANTIALIAS)
img_blue_resized2 = img_blue1.resize((30, 30),Image.ANTIALIAS)
img_blue2 = ImageTk.PhotoImage(img_blue_resized)
img_blue3 = ImageTk.PhotoImage(img_blue_resized2)

img_green = Image.open(path+"green.png")
img_green_resized = img_green.resize((30, 30),Image.ANTIALIAS)                        
img_green2 = ImageTk.PhotoImage(img_green_resized)

img_red = Image.open(path+"red.png")
img_red_resized = img_red.resize((30, 30),Image.ANTIALIAS)                        
img_red2 = ImageTk.PhotoImage(img_red_resized)

img_white = Image.open(path+"white.png")
img_white_resized = img_white.resize((30, 30),Image.ANTIALIAS)                        
img_white2 = ImageTk.PhotoImage(img_white_resized)

img_black = Image.open(path+"black.png")
img_black_resized = img_black.resize((30, 30),Image.ANTIALIAS)                        
img_black2 = ImageTk.PhotoImage(img_black_resized)

cardback = Image.open(path+"cardback.png")
cardback_resized = cardback.resize((60, 120),Image.ANTIALIAS)                        
cardback2 = ImageTk.PhotoImage(cardback)
cardback_small = ImageTk.PhotoImage(cardback_resized)

table = Image.open(path+"table2.png")
table_resized = table.resize((1200, 670),Image.ANTIALIAS)                        
table2 = ImageTk.PhotoImage(table_resized)

table_1 = Image.open(path+"table_part2.png")
table_resized2 = table_1.resize((300, 300),Image.ANTIALIAS)         
table_part = ImageTk.PhotoImage(table_resized2)

table_2 = Image.open(path+"table_part2.png")
table_resized3 = table_2.resize((30, 30),Image.ANTIALIAS)         
table_part2 = ImageTk.PhotoImage(table_resized3)

# Hangok

def playsound(**options):
        

        if options.get("type1") == "1": 
                winsound.PlaySound(path+"poker1.wav",winsound.SND_FILENAME)
        elif options.get("type1") == "2": 
                winsound.PlaySound(path+"poker1.wav",winsound.SND_FILENAME)
                winsound.PlaySound(path+"poker1.wav",winsound.SND_FILENAME)

        elif options.get("type1") == "3":
                winsound.PlaySound(path+"cardShove4.wav",winsound.SND_FILENAME)


language = ['english']

# Menu

# Fajl menu


menubar = tk.Menu(master)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")


# Statisztika, jatekok szama

def statistics():

    
    stat = tk.Toplevel()
    stat.resizable(0,0)
    if language == ['english']:
            label = tk.Label(stat,text="All games: ")
            label2 = tk.Label(stat,text="Lost: ")
            label1 = tk.Label(stat,text="Win: ")
    elif language == ['hungarian']:
            label = tk.Label(stat,text="Osszes jatek: ")
            label2 = tk.Label(stat,text="Elvesztett: ")
            label1 = tk.Label(stat,text="Nyert: ")
    label.pack()
    label1.pack()
    label2.pack()
    stat.mainloop()

  

statmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Statistics", menu=statmenu)
statmenu.add_command(label="Game stat",command=statistics)


# Beallitasok, nyelv valasztasa (meg nem a legjobb megoldas)

def languageset():
      
    settings = tk.Toplevel()
    settings.resizable(0,0)

    def english():
        language.append('english')
        del language[0]
        label.config(text="Choose language")
        button.config(text="english")
        button2.config(text="hungarian")
        mycardsbutton.config(text="Show my cards")
        giveButton.config(text="Give")
        raiseButton.config(text="Raise")
        throwButton.config(text="Throw")
        showbutton1.config(text="Show next card")
        showbutton2.config(text="Put cards")
        label_sum.config(text="You have 1410 tokens")
        
      

    def hungarian():
        language.append('hungarian')
        del language[0]
        label.config(text="Valaszd ki a nyelvet")
        button.config(text="angol")
        button2.config(text="magyar")
        mycardsbutton.config(text="Mutasd a kartyaim")
        giveButton.config(text="Megad")
        raiseButton.config(text="Emel")
        throwButton.config(text="Eldob")
        showbutton1.config(text="Mutasd a kovetkezot")
        showbutton2.config(text="Lapok kiosztasa")
        label_sum.config(text="Zsetonjaid szama: 10000")
        menubar.entryconfigure(1,label="Fajl")
        menubar.entryconfigure(2,label="Statisztika")
        menubar.entryconfigure(3,label="Beallitasok")
        menubar.entryconfigure(4,label="Szabalyok")
        settingsmenu.entryconfigure(1,label="Nyelv")
        statmenu.entryconfigure(1,label="Jatek statisztika")
        rulesmenu.entryconfigure(1,label="Lap ertekek")
        filemenu.entryconfigure(0,label="Uj")
        filemenu.entryconfigure(1,label="Megnyitas")
        filemenu.entryconfigure(2,label="Mentes")

    frame = tk.Frame(settings,width = 600)
    frame1 = tk.Frame(settings,width = 600)

    label = tk.Label(frame,text="language")
    button = tk.Button(frame1,text="english",command=english)
    button2 = tk.Button(frame1,text="hungarian",command=hungarian)

    label.pack()
    button.pack(side=tk.RIGHT)
    button2.pack(side=tk.LEFT)

    frame.pack()
    frame1.pack()

    settings.mainloop()

settingsmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=settingsmenu)
settingsmenu.add_command(label="Language",command=languageset)


# Szabalyok
    
def ranking():

    rank = tk.Toplevel()
    rank.resizable(0,0)
    img_rank = Image.open(path+"rules.png")
    img_rank_resized = img_rank.resize((210, 390),Image.ANTIALIAS) 
    img_rank2 = ImageTk.PhotoImage(img_rank_resized)
    label = tk.Label(rank,image=img_rank2)
    label.pack()

    rank.mainloop()

rulesmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Rules", menu=rulesmenu)
rulesmenu.add_command(label="Rankings",command=ranking)

master.config(menu=menubar)




# Asztal hattere

mainframe = tk.Label(master,height=670,width=1200,image=table2)
mainframe.place(x=0,y=0)

# Zsetonok:

def make_tokenlabels(self):

        tk.Label(self, text="(1)").grid(row=0)
        tk.Label(self, text="(5)").grid(row=1)
        tk.Label(self, text="(10)").grid(row=2)
        tk.Label(self, text="(25)").grid(row=3)
        tk.Label(self, text="(100)").grid(row=4)

        tk.Label(self, image=img_white2).grid(row=0,column=1)
        tk.Label(self, image=img_red2).grid(row=1,column=1)
        tk.Label(self, image=img_blue2).grid(row=2,column=1)
        tk.Label(self, image=img_green2).grid(row=3,column=1)
        tk.Label(self, image=img_black2).grid(row=4,column=1)

        for h in range(5):

                tk.Label(self, text="x").grid(row=h,column=2)


        self.white = tk.Label(self, text="10")
        self.blue = tk.Label(self, text="10")
        self.red = tk.Label(self, text="10")
        self.green = tk.Label(self, text="10")
        self.black = tk.Label(self, text="10")


        self.white.grid(row=0,column=3)
        self.blue.grid(row=1,column=3)
        self.red.grid(row=2,column=3)
        self.green.grid(row=3,column=3)
        self.black.grid(row=4,column=3)


# Masik jatekos (gep)

separator1 = tk.Frame(master,height=50,padx=0,pady=0,bd=0)
separator1.grid(row=0)
separator1.lower()

vakok = tk.Frame(master)
kisvak = tk.Label(vakok,text='')
nagyvak = tk.Label(vakok,text='')

zseton2 = tk.Frame(master)
zseton2.grid(row=1,column=2)

zsetonsum_bot = tk.Frame(master)
zsetonsum_bot.grid(row=1,column=1)

label_sum_bot = tk.Label(zsetonsum_bot,text="The bot has 10000 tokens")
label_sum_bot.grid(row=0)


make_tokenlabels(zseton2)

cards_others = tk.Frame(master)

card_others1 = tk.Label(cards_others, image=cardback_small)
card_others2 = tk.Label(cards_others, image=cardback_small)

cards_others.grid(row=1,column=4)

card_others1.grid(row=0,column=0)
card_others2.grid(row=0,column=1)

cards_others.lower()

buttons_bot = tk.Frame(master)
buttons_bot.grid(row=1,column=5)
        
giveButton2 = tk.Button(buttons_bot,text="Give")
giveButton2.grid(row=0)

raiseButton2 = tk.Button(buttons_bot,text="Raise")
raiseButton2.grid(row=0, column=1)

throwButton2 = tk.Button(buttons_bot,text="Throw")
throwButton2.grid(row=0, column=2)

separator4 = tk.Frame(master,height=10)
separator4.grid(row=2)
separator4.lower()


# Tetek

bets = tk.Frame(master)
bets.grid(row=3,column=0)

bets1 = tk.Frame(bets)
bets2 = tk.Frame(bets)

all_bet_playerlabel1 = tk.Label(bets1,text = "Your bet:")
all_bet_playerlabel = tk.Label(bets1,text = "0")
all_bet_botlabel1 = tk.Label(bets1,text = "Bot's bet:")
all_bet_botlabel = tk.Label(bets1,text = "0")
all_bet1 = tk.Label(bets1,text = "All bet:")
all_bet = tk.Label(bets1,text = "0")

all_bet_botlabel1.grid(row=0,column=0)
all_bet1.grid(row=1,column=0)
all_bet_playerlabel1.grid(row=2,column=0)

all_bet_botlabel.grid(row=0,column=1)
all_bet.grid(row=1,column=1)
all_bet_playerlabel.grid(row=2,column=1)

info_sep = tk.Label(bets2)
infolabel = tk.Label(bets2,text="Welcome")

bets1.grid(row=0)
bets2.grid(row=1)

info_sep.grid(row=0)
infolabel.grid(row=1)


# Fo kartyak

separator3 = tk.Frame(master,width=300,bd=0,padx=0,pady=0,bg="blue")
separator3.grid(row=1,column=0)
separator3.lower()

cards1 = tk.Frame(master,width=100,height=250)
cards2 = tk.Frame(master,width=100,height=250)
cards3 = tk.Frame(master,width=100,height=250)
cards4 = tk.Frame(master,width=100,height=250)
cards5 = tk.Frame(master,width=100,height=250)

card1 = tk.Label(cards1, image=cardback2,text="back",bg="black")
card2 = tk.Label(cards2, image=cardback2,text="back",bg="black")
card3 = tk.Label(cards3, image=cardback2,text="back",bg="black")
card4 = tk.Label(cards4, image=cardback2,text="back",bg="black")
card5 = tk.Label(cards5, image=cardback2,text="back",bg="black")

cards1.grid(row=3,column=1)
cards2.grid(row=3,column=2)
cards3.grid(row=3,column=3)
cards4.grid(row=3,column=4)
cards5.grid(row=3,column=5)

card1.grid(row=0,column=0)
card2.grid(row=0,column=0)
card3.grid(row=0,column=0)
card4.grid(row=0,column=0)
card5.grid(row=0,column=0)


cards1.lower()
cards2.lower()
cards3.lower()
cards4.lower()
cards5.lower()

buttons = tk.Frame(master)
buttons.grid(row=3,column=6)
showbutton1 = tk.Button(buttons,text="Show next card",state="disabled")

showbutton2 = tk.Button(buttons,text="Start round")
showbutton2.grid(row=1)


separator4 = tk.Frame(master,height=10)
separator4.grid(row=4)
separator4.lower()


# Sajat kartyak es zsetonok

cards_mine = tk.Frame(master)
cards_mine2 = tk.Frame(master)
card_mine1 = tk.Label(cards_mine, image=cardback_small)
card_mine2 = tk.Label(cards_mine, image=cardback_small)

cards_mine.grid(row=5,column=2)
cards_mine2.grid(row=5,column=1)
card_mine1.grid(row=0,column=0)
card_mine2.grid(row=0,column=1)

cards_mine.lower()

mycardsbutton = tk.Button(cards_mine2,text="Show my cards",state="disabled")
mycardsbutton.grid(row=0)


zseton = tk.Frame(master)
zseton.grid(row=5,column=4)

make_tokenlabels(zseton)

zsetonsum = tk.Frame(master)
zsetonsum.grid(row=5,column=3)

label_sum = tk.Label(zsetonsum,text="You have 10000 tokens")
label_sum.grid(row=0)
                

buttons = tk.Frame(master)
buttons.grid(row=5,column=5)
        
giveButton = tk.Button(buttons,text="Give")
giveButton.grid(row=0)

raiseButton = tk.Button(buttons,text="Raise")
raiseButton.grid(row=0, column=1)

throwButton = tk.Button(buttons,text="Throw")
throwButton.grid(row=0, column=2)

separator5 = tk.Frame(master,height=50)
separator5.grid(row=7)
separator5.lower()


cardpictures = []
cardpictures2 = []
cardpictures3 = []
maincards = []
mycards = []
othercards = []


# Uj jatek betoltese

def game1():

    giveButton.config(state="disabled")
    raiseButton.config(state="disabled")
    throwButton.config(state="disabled")

    giveButton2.config(state="disabled")
    raiseButton2.config(state="disabled")
    throwButton2.config(state="disabled")
    
    cards_mine.lower()
    cards_others.lower()
    card1.config(image=cardback2)
    card2.config(image=cardback2)
    card3.config(image=cardback2)
    card4.config(image=cardback2)
    card5.config(image=cardback2)
    card_others1.config(image=cardback_small)
    card_others2.config(image=cardback_small)
    card_mine1.config(image=cardback_small)
    card_mine2.config(image=cardback_small)
    
    cards1.lower()
    cards2.lower()
    cards3.lower()
    cards4.lower()
    cards5.lower()

    cardlist2 = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13",
                "B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13",
                "C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13",
                "D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13"]
     
    del cardpictures[:]
    del cardpictures2[:]
    del cardpictures3[:]
    del maincards[:]
    del othercards[:]
    del mycards[:]

    

    for i in range(2):
            mine = random.choice(cardlist2)
            mycards.append(mine)
            del(cardlist2[cardlist2.index(mine)])
            name = path+mine+".png"
            pic = Image.open(name,"r")
            pic_resized = pic.resize((60, 120),Image.ANTIALIAS)
            pic2 = ImageTk.PhotoImage(pic_resized)
            cardpictures.append(pic2)

    for l in range(2):

            other = random.choice(cardlist2)
            othercards.append(other)
            del(cardlist2[cardlist2.index(other)])
            name = path+other+".png"
            pic = Image.open(name,"r")
            pic_resized = pic.resize((60, 120),Image.ANTIALIAS)
            pic2 = ImageTk.PhotoImage(pic_resized)
            cardpictures3.append(pic2)

    for p in range(5):

            maincard = random.choice(cardlist2)
            maincards.append(maincard)
            del(cardlist2[cardlist2.index(maincard)])
            name = path+maincard+".png"
            pic = Image.open(name,"r")
            pic_resized2 = pic.resize((100, 160),Image.ANTIALIAS)
            pic3 = ImageTk.PhotoImage(pic_resized2)
                
            cardpictures2.append(pic3)

    card1.config(image=cardback2,text="back")
    card2.config(image=cardback2,text="back")
    card3.config(image=cardback2,text="back")
    card4.config(image=cardback2,text="back")
    card5.config(image=cardback2,text="back")

    card_mine1.config(image=cardback_small)
    card_mine2.config(image=cardback_small)

    card_others1.config(image=cardback_small)
    card_others2.config(image=cardback_small)


# Mentett jatek megnyitasa a pokergame modulbol

def gameopen1(maincards,mycards,othercards,states):

        del cardpictures[:]
        del cardpictures2[:]
        del cardpictures3[:]


        for i in range(len(mycards)):
                name = path+mycards[i]+".png"
                pic = Image.open(name,"r")
                pic_resized = pic.resize((60, 120),Image.ANTIALIAS)
                pic2 = ImageTk.PhotoImage(pic_resized)
                cardpictures.append(pic2)

        card_mine1.config(image=cardpictures[0])
        card_mine2.config(image=cardpictures[1])

        for i in range(len(othercards)):
                name = path+othercards[i]+".png"
                pic = Image.open(name,"r")
                pic_resized = pic.resize((60, 120),Image.ANTIALIAS)
                pic2 = ImageTk.PhotoImage(pic_resized)
                cardpictures3.append(pic2)
      
        for p in range(len(maincards)):

                
                name = path+maincards[p]+".png"
                pic = Image.open(name,"r")
                pic_resized2 = pic.resize((100, 160),Image.ANTIALIAS)
                pic3 = ImageTk.PhotoImage(pic_resized2)
                
                cardpictures2.append(pic3)

        card_others1.config(image=cardback_small)
        card_others2.config(image=cardback_small)
        
        
        if states[0] == "back":
                card1.config(image=cardback2,text="back")
        else:
                card1.config(image=cardpictures2[0],text="face")

        if states[1] == "back":
                card2.config(image=cardback2,text="back")
        else:
                card2.config(image=cardpictures2[1],text="face")

        if states[2] == "back":
                card3.config(image=cardback2,text="back")
        else:
                card3.config(image=cardpictures2[2],text="face")

        if states[3] == "back":
                card4.config(image=cardback2,text="back")
        else:
                card4.config(image=cardpictures2[3],text="face")

        if states[4] == "back":
                card5.config(image=cardback2,text="back")
        else:
                card5.config(image=cardpictures2[4],text="face")
                card_others1.config(image=cardpictures3[0])
                card_others2.config(image=cardpictures3[1])
                showbutton1.config(state="disabled")



game1()

master.minsize(width=1200, height=670)
master.maxsize(width=1200, height=670)
master.resizable(0,0)
master.wm_title("Nagyonkigyo poker")
master.tk.call("wm", "iconphoto", master._w, img_blue3)

def main():
        master.mainloop()
