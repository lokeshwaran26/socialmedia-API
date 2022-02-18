from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pywhatkit
import facebook as fb

import main2 as Youtube
import main3 as Insta

w = Tk()
w.geometry('1920x1080')
w.title('PYEXPO')
w.configure(bg='#ff4f5a')
w.minsize(925, 500)

#Rage Italic-autograph

#img18 = PhotoImage(file="")
#w.iconphoto(True,img18)



def socialmedia():


    signin_win = Frame(w, width=1920, height=1080, bg='white')
    signin_win.place(x=0, y=0)
    f1 = Frame(signin_win, width=350, height=400, bg='white')
    f1.place(x=480, y=100)

    global img1
    img1 = ImageTk.PhotoImage(Image.open("socila_media (1) (1).jpg"))
    Label(signin_win, image=img1, border=0, bg='white').place(x=700, y=200)

    global img2
    img2= ImageTk.PhotoImage(Image.open("Instagram_logo_140x140.png"))
    Label(signin_win, image=img2, border=0, bg='white').place(x=500, y=608)

    global img3
    img3 = ImageTk.PhotoImage(Image.open("Youtube_logo2..jpg"))
    Label(signin_win, image=img3, border=0, bg='white').place(x=750, y=616)

    global img4
    img4 = ImageTk.PhotoImage(Image.open("facebooklogo (1).jpg"))
    Label(signin_win, image=img4, border=0, bg='white').place(x=1030, y=595)

    global img5
    img5 = ImageTk.PhotoImage(Image.open("whastapplogo_140x140.png"))
    Label(signin_win, image=img5, border=0, bg='white').place(x=1280, y=608)

    global img12
    img12 = ImageTk.PhotoImage(Image.open("pyexpo_title_301x301.jpg"))
    Label(signin_win, image=img12, border=0, bg='white').place(x=50, y=50)

    b5 = Button(signin_win, width=4, pady=1 ,text='Home', border=0, bg='white', fg='#233643', ) #22D5C0
    b5.config(font=('Moon', 18,))
    b5.place(x=1100, y=80)

    b6 = Button(signin_win, width=7, pady=1, text='About us', border=0, bg='white', fg='#233643', command=aboutUs )  # 22D5C0
    b6.config(font=('Moon', 18,))
    b6.place(x=1250, y=80)

    b7 = Button(signin_win, width=8, pady=1, text='Services', border=0, bg='white', fg='#233643', command=services )  # 22D5C0
    b7.config(font=('Moon', 18,))
    b7.place(x=1450, y=80)

    b8 = Button(signin_win, width=13, pady=1, text='Contact', border=0, bg='white', fg='#233643', command=contact )  # 22D5C0
    b8.config(font=('Moon', 18,))
    b8.place(x=1650, y=80)


    b1 = Button(signin_win, width=11, pady=0 , text='-Instagram-', border=0, bg='white', fg='#bc2a8d', activebackground='#bc2a8d', command=insta)##bc2a8d
    b1.config(font=('Rockwell',10))#Tw Cen MT,**Rockwell
    b1.place(x=512, y=749)

    b2 = Button(signin_win, width=13, pady=1, text='-Youtube-', border=0, bg='white', fg='#c4302b',activebackground='#c4302b' ,command=youtube)
    b2.config(font=('Rockwell', 10))  # Tw Cen MT,**Rockwell
    b2.place(x=769, y=749)

    b3 = Button(signin_win, width=13, pady=1, text='-Facebook-', border=0, bg='white', fg='#4267B2',activebackground='#26AAEE' , command=facebook )
    b3.config(font=('Rockwell', 10))  # Tw Cen MT,**Rockwell
    b3.place(x=1040, y=749)

    b4 = Button(signin_win, width=13, pady=1, text='-Whatsapp-', border=0, bg='white', fg='#075e54',activebackground='#075e54' ,command=whatsapp )
    b4.config(font=('Rockwell', 10))  # Tw Cen MT,**Rockwell
    b4.place(x=1284, y=749)


    #l1 = Label(signin_win, text="PYEXPO", fg='black', bg='white') #075e54
    #l1.config(font=('Microsoft YaHei UI Light', 50,))
    #l1.place(x=50, y=10)


    #-----------------------------------------------------------------------------------------------------------------------


def aboutUs():
    top4 = Toplevel()
    top4.geometry('1920x1080')
    top4.title('ABOUT US')
    top4.configure(bg='white')  # bc2a8d
    top4.minsize(925, 500)

    '''signin_win5 = Frame(top4, width=1200, height=620, bg='white')
    signin_win5.place(x=340, y=180)
    f2 = Frame(signin_win5, width=430, height=430, bg='white')
    f2.place(x=580, y=100)'''

    global img15
    img15 = ImageTk.PhotoImage(Image.open("pyexpo_title_301x301(1).jpg"))
    Label(top4, image=img15, border=0, bg='white').place(x=770, y=50)

    l4 = Label(top4, text="About us:", fg='black', bg='white')
    l4.config(font=('Segoe UI', 22))
    l4.place(x=100, y=200)

    l5 = Label(top4, text="Pyexpo is a based python language event, we are the team 4 in this project our project title is uploading video/files in socialmedia", fg='black',bg='white')
    l5.config(font=('Microsoft YaHei UI', 14))
    l5.place(x=165, y=270)

    l6 = Label(top4,text="Lokeshwaran.k from CSE department has done the work in tkinter Lithikhaa.k from AI&DS department has done the work of backend",fg='black', bg='white')
    l6.config(font=('Microsoft YaHei UI', 14))
    l6.place(x=165, y=308)

    l6 = Label(top4,text="code Praveen.v from ECE department  and Manojkumar.k from AI&DS department done the work in ppt and referred some programs",fg='black', bg='white')
    l6.config(font=('Microsoft YaHei UI', 14))
    l6.place(x=165, y=342)

def services():
    top5 = Toplevel()
    top5.geometry('1920x1080')
    top5.title('SERVICES')
    top5.configure(bg='white')  # bc2a8d
    top5.minsize(925, 500)

    global img16
    img16 = ImageTk.PhotoImage(Image.open("pyexpo_title_301x301(2).jpg"))
    Label(top5, image=img16, border=0, bg='white').place(x=770, y=50)

    l4 = Label(top5, text="Services:", fg='black', bg='white')
    l4.config(font=('Segoe UI', 22))
    l4.place(x=100, y=200)

    l5 = Label(top5,text="Have a any issues in app! check the internet connection in you PC, Due to network problem the post maybe make some problem will",fg='black', bg='white')
    l5.config(font=('Microsoft YaHei UI', 14))
    l5.place(x=165, y=270)

    l6 = Label(top5,text="and please checkout your account that file is uploadedor not and there is a any problem to you contact our mail through the ",fg='black', bg='white')
    l6.config(font=('Microsoft YaHei UI', 14))
    l6.place(x=165, y=308)

    l6 = Label(top5,text="details and mail your issue to use and we will fix your problem as soon as posible",fg='black', bg='white')
    l6.config(font=('Microsoft YaHei UI', 14))
    l6.place(x=165, y=342)


def contact():
    top6 = Toplevel()
    top6.geometry('1920x1080')
    top6.title('SERVICES')
    top6.configure(bg='white')  # bc2a8d
    top6.minsize(925, 500)

    global img17
    img17 = ImageTk.PhotoImage(Image.open("pyexpo_title_301x301(3).jpg"))
    Label(top6, image=img17, border=0, bg='white').place(x=770, y=50)

    l4 = Label(top6, text="Contact:", fg='black', bg='white')
    l4.config(font=('Segoe UI', 22))
    l4.place(x=100, y=200)

    l5 = Label(top6,text="If there is a any issues like network problem, protocol issues, Uploading status, interface issue. You can contact through this emails",fg='black', bg='white')
    l5.config(font=('Microsoft YaHei UI', 14))
    l5.place(x=165, y=270)

    l6 = Label(top6,text="lithikhaa.k2021@kgkite.ac.in , lokeshwaran.k2021@kgkite.ac.in , praveenchithaparam.v2021@kgkite.ac.in , manojkumar.k2021@kgkite.ac.in",fg='black', bg='white')
    l6.config(font=('Microsoft YaHei UI', 14))
    l6.place(x=165, y=308)

    l6 = Label(top6,text=" send a mail to this email id's we will rectify you problem as soon as quickly",fg='black', bg='white')
    l6.config(font=('Microsoft YaHei UI', 14))
    l6.place(x=165, y=342)


def insta():

    top = Toplevel()
    top.geometry('1920x1080')
    top.title('INSTA')
    top.configure(bg='#8a3ab9')#bc2a8d
    top.minsize(925, 500)



    signin_win1 = Frame(top, width=1200, height=620, bg='white')
    signin_win1.place(x=340, y=180)
    f2 = Frame(signin_win1, width=430, height=430, bg='white')
    f2.place(x=580, y=100)

    global img6
    img6 = ImageTk.PhotoImage(Image.open("insta_427x427.png"))
    Label(signin_win1, image=img6, border=0, bg='white').place(x=50, y=80)

    global img13
    img13 = ImageTk.PhotoImage(Image.open("instagram_title2.png"))
    Label(signin_win1, image=img13, border=0, bg='white').place(x=535, y=20)

    def instaImage():
        global instaimage
        instaimage = filedialog.askopenfilename()
        print(instaimage)

        global username1
        username1 =e1.get()

        global password1
        password1 =e2.get()

        global caption1
        caption1 =e3.get()


    def instaUpload():

        l9.config(text='Wait a min file will be Uploaded')

        Insta.instas(username1, password1, caption1,instaimage)




    '''l2 = Label(signin_win1, text="Instagram", fg='#8a3ab9', bg='white')
    l2.config(font=('Microsoft YaHei UI Light', 23, ))
    l2.place(x=500, y=10)'''

    l3 = Label(signin_win1, text="Login:", fg='#8a3ab9', bg='white')
    l3.config(font=('Segoe UI', 13, 'bold'))
    l3.place(x=608, y=125)


    def on_leave(e):
        if e1.get() == '':
            e1.insert(0, 'Username')

    e1 = Entry(f2, width=25, fg='black', border=0, bg='white')
    e1.config(font=('Segoe UI', 13,))

    e1.bind("<FocusOut>", on_leave)
    e1.insert(0, 'Username')
    e1.place(x=30, y=66)

    Frame(f2, width=320, height=2, bg='black').place(x=25, y=97)

    # ------------------------------------------------------



    def on_leave(e):
        if e2.get() == '':
            e2.insert(0, 'Password')



    e2 = Entry(f2, width=21, fg='black', border=0, bg='white',)
    e2.config(font=('Segoe UI', 13,))

    e2.bind("<FocusOut>", on_leave)
    e2.insert(0, 'Password')
    e2.place(x=30, y=126)

    Frame(f2, width=320, height=2, bg='black').place(x=25, y=157)

    def on_leave(e):
        if e3.get() == '':
            e3.insert(0, 'Caption')

    e3 = Entry(f2, width=21, fg='black', border=0, bg='white',)
    e3.config(font=('Segoe UI', 13,))

    e3.bind("<FocusOut>", on_leave)
    e3.insert(0, 'Caption')
    e3.place(x=30, y=236)

    Frame(f2, width=320, height=2, bg='black').place(x=25, y=270)


    B2=Button(f2, width=30, pady=7, text='Image', bg='#8a3ab9', fg='white', border=0, command=instaImage)
    B2.config(font=('Rockwell',10))
    B2.place(x=35,y=189)

    B3 = Button(f2, width=15, pady=7, text='Upload', bg='#8a3ab9', fg='white', border=0, command=instaUpload)
    B3.config(font=('Rockwell', 10))
    B3.place(x=113,y=295)

    l1 = Label(f2, text="Do you want to upload in other media's?", fg="black", bg='white')
    l1.config(font=('Microsoft YaHei UI Light', 9,))
    l1.place(x=25, y=360)

    l9 = Label(signin_win1, text=" ", fg='#8a3ab9', bg='white')
    l9.config(font=('Segoe UI', 11, 'bold'))
    l9.place(x=640, y=521)

    b2 = Button(signin_win1, width=20, text='go back to prev window', border=0, bg='white', fg='#8a3ab9', command=top.destroy)
    b2.place(x=891, y=456)

#---------------------------------------------------------------------------------------------------------------------


def youtube():
    top1 = Toplevel()
    top1.geometry('1920x1080')
    top1.title('Youtube')
    top1.configure(bg='#c4302b')
    top1.minsize(925, 500)

    signin_win2 = Frame(top1, width=1250, height=670, bg='white')
    signin_win2.place(x=340, y=180)
    f3 = Frame(signin_win2, width=430, height=500, bg='white')
    f3.place(x=550, y=100)

    l4 = Label(signin_win2, text="LOGIN:", fg='#c4302b', bg='white')
    l4.config(font=('unicode', 13, 'bold'))
    l4.place(x=650, y=200)

    global img7
    img7 = ImageTk.PhotoImage(Image.open("youtubetitle3.png"))
    Label(signin_win2, image=img7, border=0, bg='white').place(x=50, y=130)

    global img14
    img14 = ImageTk.PhotoImage(Image.open("youtube_titledemo (1).png"))
    Label(signin_win2, image=img14, border=0, bg='white').place(x=500, y=10)


    '''l2 = Label(signin_win2, text="Youtube", fg='#FF0000', bg='white')
    l2.config(font=('Microsoft YaHei UI Light', 23, ))
    l2.place(x=420, y=10)'''

    l4 = Label(signin_win2, text="Instructions :" ,fg='black',bg='white')
    l4.config(font=('Segoe UI', 17))
    l4.place(x=520, y=80)

    l5 =Label(signin_win2,text="To upload the video in youtube need to select your Gmail account ",fg='black',bg='white')
    l5.config(font=('Microsoft YaHei UI Light',10))
    l5.place(x=520,y=120)

    l6 = Label(signin_win2, text="for authentication from Google api and video will be uploaded",fg='black',bg='white')
    l6.config(font=('Microsoft YaHei UI Light', 10))
    l6.place(x=520, y=147)

    def youtubeImage():
        global youtubeimage
        youtubeimage = filedialog.askopenfilename()



    def youtubeThumnail():
        global thumbnail
        thumbnail = filedialog.askopenfilename()


    def youtubeUpload():

        l9.config(text='Wait a min file will be Uploaded')

        global videotitle
        videotitle = e12.get()

        Youtube.youtube(youtubeimage, thumbnail, videotitle)

    def on_leave(e):
        if e4.get() == '':
            e4.insert(0, "Email i'd ")

    e4 = Entry(f3, width=21, fg='black', border=0, bg='white', )
    e4.config(font=('Segoe UI', 13,))

    e4.bind("<FocusOut>", on_leave)
    e4.insert(0, "Email i'd")
    e4.place(x=108, y=151)

    Frame(f3, width=325, height=2, bg='black').place(x=100, y=180)

    Frame(signin_win2, width=500, height=1.5, bg='black').place(x=525, y=176)

    def on_leave(e):
        if e5.get() == '':
            e5.insert(0, "Password")

    e5 = Entry(f3, width=21, fg='black', border=0, bg='white', )
    e5.config(font=('Segoe UI', 13,))

    e5.bind("<FocusOut>", on_leave)
    e5.insert(0, 'Password')
    e5.place(x=108, y=203)

    Frame(f3, width=325, height=2, bg='black').place(x=100, y=233)

    def on_leave(e):
        if e12.get() == '':
            e12.insert(0, "Video title")

    e12 = Entry(f3, width=21, fg='black', border=0, bg='white', )
    e12.config(font=('Bahnschrift Light', 13,))

    e12.bind("<FocusOut>", on_leave)
    e12.insert(0, 'Video title')
    e12.place(x=108, y=320)

    Frame(f3, width=325, height=2, bg='black').place(x=100, y=350)

    B1 = Button(f3, width=30, pady=6, text="Video", bg='#c4302b', fg='white', border=0, command=youtubeImage)
    B1.config(font=('Rockwell', 10))
    B1.place(x=110,y=262)

    B2 = Button(f3, width=13, pady=5, text="Upload", bg='#c4302b', fg='white', border=0,command=youtubeUpload)
    B2.config(font=('Rockwell', 10))
    B2.place(x=201, y=440)

    B3 = Button(f3, width=25, pady=6, text="Thumbnail", bg='#c4302b', fg='white', border=0, command=youtubeThumnail)
    B3.config(font=('Rockwell', 10))
    B3.place(x=138, y=373)

    l7 = Label(signin_win2, text="Want to upload in other media's?", fg="black", bg='white')
    l7.config(font=('Microsoft YaHei UI Light', 9,))
    l7.place(x=650, y=600)

    l9 = Label(signin_win2, text=" ", fg='#c4302b', bg='white')
    l9.config(font=('Segoe UI', 11, 'bold'))
    l9.place(x=150, y=596)

    b3 = Button(signin_win2, width=20, text='go back to prev window', border=0, bg='white', fg='#c4302b', command=top1.destroy ).place(x=885, y=596)


#----------------------------------------------------------------------------------------------------------------------------------------------------

def facebook():
    top2 = Toplevel()
    top2.geometry('1920x1080')
    top2.title('Facebook')
    top2.configure(bg='#26AAEE')
    top2.minsize(925, 500)

    signin_win3 = Frame(top2, width=1250, height=670, bg='white')
    signin_win3.place(x=340, y=180)
    f4 = Frame(signin_win3, width=430, height=500, bg='white')
    f4.place(x=650, y=150)

    global img8
    img8 = ImageTk.PhotoImage(Image.open("facebook_587x587.png"))
    Label(signin_win3, image=img8, border=0, bg='white').place(x=0, y=40)

    global img9
    img9 = ImageTk.PhotoImage(Image.open("Facebook_220x202.png"))
    Label(signin_win3, image=img9, border=0, bg='white').place(x=520, y=25)

    l8 = Label(signin_win3, text="Login:", fg='#245EB4', bg='white')
    l8.config(font=('Segoe UI', 15, 'bold'))
    l8.place(x=644, y=160)

    def faceImage():
        global faceimage
        faceimage = filedialog.askopenfilename()
        print(faceimage)

    def faceUpload():

        l9.config(text='Wait a min file will be Uploaded')

        access_token = "EAAJQIVZCgTSkBABb7ImTNpcbTc8KHkKZB6LdbY8e5JjenAENfVmAPhzaiIVqGriHOivDyEcRSYjExXV7lTXcngfZB8QT92i56KL5m7GqASd1w52GzjXmiB4hIZCGo04erHh4W756yQZADY9Cbtgad8jcvoPkLUkPfhTyAftAv5IZADs0QKGkoaaWHJVQL7FojrTYFLTT5wZAZBIIeHO7x9vSJk7AnACqsLW3ERcZAupJvkKlGxnVVqFj5"
        asafb = fb.GraphAPI(access_token)
        asafb.get_object("101002488055335_519844142837832")
        asafb.put_photo(open(faceimage,"rb"),message=e7.get())



    def on_leave(e):
        if e11.get() == '':
            e11.insert(0, "Username or Email I'd")

    e11 = Entry(f4, width=22, fg='black', border=0, bg='white', )
    e11.config(font=('Bahnschrift Light', 13,))

    e11.bind("<FocusOut>", on_leave)
    e11.insert(0, "Username or Email I'd")
    e11.place(x=2, y=80)

    Frame(f4, width=340, height=2, bg='black').place(x=0, y=107)

    #--------------------------------------------------------------------

    def on_leave(e):
        if e6.get() == '':
            e6.insert(0, "Password")

    e6 = Entry(f4, width=21, fg='black', border=0, bg='white', )
    e6.config(font=('Bahnschrift Light', 13,))

    e6.bind("<FocusOut>", on_leave)
    e6.insert(0, 'Password')
    e6.place(x=2, y=133)

    Frame(f4, width=340, height=2, bg='black').place(x=0, y=161)

    B1 = Button(f4, width=29, pady=9, text="Image", bg='#245EB4', fg='white', border=0, command=faceImage)
    B1.config(font=('Rockwell', 10))
    B1.place(x=20, y=184)

    def on_leave(e):
        if e7.get() == '':
            e7.insert(0, "Comments")

    e7 = Entry(f4, width=21, fg='black', border=0, bg='white', )
    e7.config(font=('Bahnschrift Light', 13,))

    e7.bind("<FocusOut>", on_leave)
    e7.insert(0, 'Comments')
    e7.place(x=2, y=243)

    Frame(f4, width=340, height=2, bg='black').place(x=0, y=271)

    B2 = Button(f4, width=15, pady=7, text="Upload", bg='#245EB4', fg='white', border=0, command=faceUpload )
    B2.config(font=('Rockwell', 10))
    B2.place(x=83, y=295)

    l8 = Label(f4, text="Want to upload in other media's?", fg="black", bg='white')
    l8.config(font=('Microsoft YaHei UI Light', 9,))
    l8.place(x=0, y=340)

    l9 = Label(signin_win3, text=" ", fg='#245EB4', bg='white')
    l9.config(font=('Segoe UI', 11, 'bold'))
    l9.place(x=700, y=521)

    b3 = Button(signin_win3, width=20, text='go back to prev window', border=0, bg='white', fg='#245EB4', command=top2.destroy ).place(x=888,y=486)


  #-----------------------------------------------------------------------------------------------------------------------------------------


def whatsapp():



    top3 = Toplevel()
    top3.geometry('1920x1080')
    top3.title('Whatsapp')
    top3.configure(bg='#259A31') #22C232
    top3.minsize(925, 500)

    signin_win4 = Frame(top3, width=1250, height=670, bg='white')
    signin_win4.place(x=340, y=180)
    f5 = Frame(signin_win4, width=430, height=400, bg='white')
    f5.place(x=650, y=150)


    global img10
    img10 = ImageTk.PhotoImage(Image.open("whatsapp_427x427.png"))
    Label(signin_win4, image=img10, border=0, bg='white').place(x=110, y=130)

    global img11
    img11 = ImageTk.PhotoImage(Image.open("whtasapp_title_240x34.jpg"))
    Label(signin_win4, image=img11, border=0, bg='white').place(x=495, y=35)


    def whatsappImage():
        global whatsappimage
        whatsappimage = filedialog.askopenfilename()
        print(whatsappimage)

    def whatsappUpload():

        l9.config(text='Wait a min file will be Uploaded')

        user =e8.get()
        Caption =e10.get()
        time =e9.get()
        Time1 = float(time)
        pywhatkit.sendwhats_image(user, whatsappimage, Caption, Time1, tab_close=False)



    def on_leave(e):
        if e8.get() == '':
            e8.insert(0, "Enter number")

    e8 = Entry(f5, width=22, fg='black', border=0, bg='white', )
    e8.config(font=('Bahnschrift Light', 13,))

    e8.bind("<FocusOut>", on_leave)
    e8.insert(0, "Enter number")
    e8.place(x=2, y=80)

    Frame(f5, width=340, height=2, bg='black').place(x=0, y=107)

    #--------------------------------------------------------------------

    def on_leave(e):
        if e9.get() == '':
            e9.insert(0, "Time to send")

    e9 = Entry(f5, width=21, fg='black', border=0, bg='white', )
    e9.config(font=('Bahnschrift Light', 13,))

    e9.bind("<FocusOut>", on_leave)
    e9.insert(0, 'Time to send')
    e9.place(x=2, y=133)

    Frame(f5, width=340, height=2, bg='black').place(x=0, y=161)

    B1 = Button(f5, width=30, pady=9, text="Image", bg='#259A31', fg='white', border=0, command=whatsappImage )
    B1.config(font=('Rockwell', 10))
    B1.place(x=20, y=184)

    def on_leave(e):
        if e10.get() == '':
            e10.insert(0, "Caption")

    e10 = Entry(f5, width=21, fg='black', border=0, bg='white', )
    e10.config(font=('Bahnschrift Light', 13,))

    e10.bind("<FocusOut>", on_leave)
    e10.insert(0, 'Caption')
    e10.place(x=2, y=243)

    Frame(f5, width=340, height=2, bg='black').place(x=0, y=271)

    B2 = Button(f5, width=15, pady=7, text="Upload", bg='#259A31', fg='white', border=0, command=whatsappUpload )
    B2.config(font=('Rockwell', 10))
    B2.place(x=83, y=290)

    l8 = Label(f5, text="Do you want to upload in other media's?", fg="black", bg='white')
    l8.config(font=('Microsoft YaHei UI Light', 9,))
    l8.place(x=0, y=335)

    l8 = Label(signin_win4, text="Send:", fg='#259A31', bg='white')
    l8.config(font=('Segoe UI', 15, 'bold'))
    l8.place(x=644, y=160)

    l9 = Label(signin_win4, text=" ", fg='#259A31', bg='white')
    l9.config(font=('Segoe UI', 11, 'bold'))
    l9.place(x=700, y=521)


    b3 = Button(signin_win4, width=20, text='go back to prev window', border=0, bg='white', fg='#259A31', command=top3.destroy ).place(x=935,y=482)




socialmedia()
w.mainloop()



