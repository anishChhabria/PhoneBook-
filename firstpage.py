import tkinter as tk
from PIL import Image,ImageTk

#### intro page

#### main body
def work():
    try:
        import login
    except Exception as e:
        pass

#### window
w = tk.Tk()
w.title('KnowTheDialer')
w.geometry('600x600')
w.configure(bg='light sky blue')

#### check box variable
var1 = tk.IntVar()
img1 = ImageTk.PhotoImage(file = r".\\p1.gif")
img2 = ImageTk.PhotoImage(file = r".\\p3.gif")

#### home screen label
f1 = tk.Frame(w,height=400,width=600,background='light sky blue')
f1.pack_propagate(0) # don't shrink
f1.place(x=0, y=60)
home_lbl1 = tk.Label(f1, image=img1, bg='light sky blue')
home_lbl1.pack(fill=tk.BOTH, expand=1)

#### lets start label
f2 = tk.Frame(w,height=100,width=400,bg='light sky blue')
f2.pack_propagate(0) # don't shrink
f2.place(x=100, y=400)
home = tk.Label(f2,text="Let's Get Started..!!",bg='light sky blue')
home.pack(fill=tk.BOTH, expand=1)
home.config(font=("Courier", 20))

#### papragraph
# para_1 = "helloawfwagedhdrfhsfeHSGSEDjgieOSJG\n\n\n\n\n\nawfAWFuaghuisehGueHGisehg"
para_2 = "TERMS AND CONDITION:\nIt is advisable to the user to read throughly,\nthe contents if the End User License Agreement and \nall the clauses listed herewith."
para_3 = "\n1) The makers of this application do not give, or intend to give in any \nshape or form, rights to use, copy or reproduce any part of the code \nin disk, printed media or any other means of mass production.\n2) As this is a demo application, no advanced security algorithms have \nbeen used. Users are at their own risk when storing data into the database.\n3) In the event of proprietary loss of data into the user machine,\nthe user may in any legal way, hold the makers of this application\nresponsible, as the threats of said application have been discussed in point 2 above.\n4) Reverse engineering to develop other third party applications is strictly\nprohibited, the user is warned against the same.\n5) Devs:- Nihar, Jatin, Anshul, Anish, copyright April 2019"

#### end the poped label
def temp_terminate():
   f_temp.destroy()
   next_H3.config(state = 'normal')
   chk1.config(state = 'normal')

#### 3rd accept
def next_do3():
   if var1.get() == 0:
       next_H3.config(state = 'disable')
       chk1.config(state = 'disable')
       global f_temp
       f_temp = tk.Frame(w,height=300,width=300,bg="light gray")
       f_temp.pack_propagate(0) # don't shrink
       f_temp.place(x=150, y=150)
       temp_lbl1 = tk.Label(f_temp,text = 'Warning!',font = ("Courier", 20),bg = "light gray")
       temp_lbl2 = tk.Label(f_temp,text = 'Please select the check box if you wish to continue',bg = "light gray")
       temp_lbl1.pack(fill = tk.BOTH, expand=1)
       temp_lbl2.pack(fill = tk.BOTH, expand=1)
       temp_but = tk.Button(f_temp,text='OK', width=5, command=temp_terminate)
       temp_but.pack()

   if var1.get() == 1:
       global w1
       f1.destroy()
       f2.destroy()
       f3.destroy()
       next_H3.destroy()
       w.destroy()
       work()

#### 2nd next
def next_do2():
   home_lbl1.destroy()
   home.destroy()
   # 1st click home screen
   global home_lbl3
   global next_H3
   global chk1,f2,f3
   #label
   home_lbl3 = tk.Label(f1,text=para_2+para_3,justify ='left',background='light sky blue')
   home_lbl3.pack()
   home_lbl3.config(font=(13))
   #old button forget
   # next_H2.destroy()
   #new button
   next_H3 = tk.Button(w,bg = 'sky blue',fg = 'black', text='Agree', width=5,command = next_do3)
   next_H3.place(x=280, y=500)
   next_H3.config(font=("Courier", 14))
   #check box
   f2 = tk.Frame(w,height=50,width=150,background='light sky blue')
   f2.pack_propagate(0) # don't shrink
   f2.place(x=20, y=400)
   # image
   f3 = tk.Frame(w,height=100,width=100,background='light sky blue')
   f3.pack_propagate(0) # don't shrink
   f3.place(x=500, y=0)
   img_lbl = tk.Label(f3, image=img2, bg='light sky blue')
   img_lbl.pack(fill=tk.BOTH, expand=1)
   chk1 = tk.Checkbutton(f2,text = "I, agree the T&C",variable = var1,bg= 'light sky blue',font=(12))
   chk1.pack(side='left', fill=tk.BOTH, expand=1)

#### 1st Start

#### home screen button
next_H1 = tk.Button(w,bg = 'sky blue',fg = 'black', text='Start', width=5,command = next_do2)
next_H1.place(x=280, y=500)
next_H1.config(font=("Courier", 14))

w.mainloop() 




