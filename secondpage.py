import tkinter as tk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox as ms
# from TkTreectrl import *

with sqlite3.connect('quit.db') as db:
   c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS contacts (Fname TEXT NOT NULL ,Lname TEXT NOT NULL, Contact INTEGER  NOT NULL, Email TEXT NOT NULL, Address CHAR(50) NOT NULL  );')
db.commit()
db.close()

#### top right icon
def icon(w):
    f1 = tk.Frame(w,height=100,width=100,background='light sky blue')
    f1.pack_propagate(0) # don't shrink
    f1.place(x=500, y=0)
    img_lbl = tk.Label(f1, image=img2, bg='light sky blue')
    img_lbl.pack(fill=tk.BOTH, expand=1)
#### frame function
def mk_frame(root,name,h,w,color,x,y):
    name = tk.Frame(root,height=h,width=w,background=color)
    name.pack_propagate(0) # don't shrink
    name.place(x=x, y=y) 
    return name
#### label function
def mk_label(root,name,txt,color,x,y,w):
    name = tk.Label(root,text=txt,bg=color,font=("Courier", 12),width=w,height=2)
    name.pack_propagate(0)
    name.place(x=x,y=y)
    return name
#### text box function
def mk_txt(root,name,color,x,y,w):
    name = tk.Text(root,bg=color,font=("Courier", 12),width=w,height=2)
    name.pack_propagate(0)
    name.place(x=x,y=y)
    return name


#### view
#frame vode
def view_fun():
    try:
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        c.execute('Select Fname,Lname,Contact FROM contacts')
        db.commit()
        rows = c.fetchall() 
        # print(c.fetchall())
    except Exception as e :
        print(e)

    
    

    f_v= tk.Frame()
    f_v = mk_frame(w,f_v,200,500,'light sky blue',0,10)

    listNodes = tk.Listbox(f_v,width = 56, font=("Helvetica", 12))#
    listNodes.place(x = 0,y = 0)

    scrollbar = tk.Scrollbar(f_v, orient="vertical")
    scrollbar.config(command=listNodes.yview)
    scrollbar.pack(side="right", fill="y")

    listNodes.config(yscrollcommand=scrollbar.set)

    for x in rows:
        lvfname = str(x[0][0:])
        lvlname = str(x[1][0:])
        # lvcname = str(x[2])
        string = lvfname+"      "+lvlname   
        # mlb.insert('end',*map(unicode,row))
        listNodes.insert(tk.END,string )
        # print(x[3])
#click
def view():
    global f_view,b_v
    f_view = tk.Frame(w,height=540,width=600,background='light sky blue')
    f_view.pack_propagate(0) # don't shrink
    f_view.place(x=0, y=0)
    #back
    icon(f_view)
    view_fun()


#### add
#add in DB
def add_db():
    # a --> add
    Id = 0
    aFname = ta_n.get('1.0','2.0')
    aLname = ta_l.get('1.0','2.0')
    aContact = ta_c.get('1.0','2.0')
    aEmail = ta_e.get('1.0','2.0')
    aAddress = ta_a.get('1.0','2.0')
    Id += 1 
    # print(aFname)
    try:
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        #instert into database
        insert = 'INSERT INTO contacts(Fname,Lname,Contact,Email,Address) VALUES(?,?,?,?,?)'
        c.execute(insert,[(aFname),(aLname),(aContact),(aEmail),(aAddress)])
        db.commit()
        print("Committed to db")

    except Exception as e:
        print("ERROR !!!")
        print(e)


#frame code
def add_fun():
    global f1,ta_a,ta_c,ta_e,ta_l,ta_n
    f1 = tk.Frame()
    f1=mk_frame(f_add,f1,540,500,'light sky blue',0,0)#
    b1_add = tk.Button(f1,text='Add',bg='sky blue',width=10,font=("Courier"),command = add_db)
    b1_add.place(x=150,y=390)
    l1=tk.Label()
    l1=mk_label(f1,l1,'First Name','sky blue',10,50,10)
    l2=tk.Label()
    l2=mk_label(f1,l2,'Last Name','sky blue',10,110,10)
    l3=tk.Label()
    l3=mk_label(f1,l3,'Contact','sky blue',10,170,10)
    l4=tk.Label()
    l4=mk_label(f1,l4,'Email','sky blue',10,230,10)
    l5=tk.Label()
    l5=mk_label(f1,l5,'Address','sky blue',10,290,10)
    ta_n=tk.Text()
    ta_n=mk_txt(f1,ta_n,'white',130,50,20)
    ta_l=tk.Text()
    ta_l=mk_txt(f1,ta_l,'white',130,110,20)
    ta_c=tk.Text()
    ta_c=mk_txt(f1,ta_c,'white',130,170,20)
    ta_e=tk.Text()
    ta_e=mk_txt(f1,ta_e,'white',130,230,20)
    ta_a=tk.Text()
    ta_a=mk_txt(f1,ta_a,'white',130,290,20) 
#click
def add():
    global f_add,b_a
    f_add = tk.Frame(w,height=540,width=500,background='light sky blue')
    f_add.pack_propagate(0) # don't shrink
    f_add.place(x=0, y=0)
    #back
    icon(f_add)
    add_fun()


#### edit
def fetchdata():
        global tefname,telname,tecontact,teemail,teaddress
        efname,elname = te.get("1.0",'end-1c').split(" ") 
        # print(te.get("1.0","end-1c"))
        # print(efname+" \n "+elname)
        efname = efname.strip()
        elname = elname.strip()
        try:
            with sqlite3.connect('quit.db') as db:
                c = db.cursor()      
            find_contact = ('SELECT Fname,Lname,Contact,Email,Address FROM contacts WHERE Fname = ? and Lname = ?')
            c.execute(find_contact,[(efname),(elname)])  
            rawdatas = c.fetchall()
            if rawdatas:
                for p1 in rawdatas:
                    # print(raw[0])
                    tefname = p1[0]
                    telname = p1[1]
                    tecontact = p1[2]
                    teemail = p1[3]
                    teaddress = p1[4]
                    te_n.insert(tk.END,tefname)
                    te_l.insert(tk.END,telname)
                    te_c.insert(tk.END,tecontact)
                    te_e.insert(tk.END,teemail)
                    te_a.insert(tk.END,teaddress)
                    

            else:
                ms.showerror('Error!','Not Found ')
        except Exception as e:
            print(e)

        
def saveEditedData(): 
    try:
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        #instert into database
        insert = 'INSERT INTO contacts(Fname,Lname,Contact,Email,Address) VALUES(?,?,?,?,?)'
        c.execute(insert,[(te_n.get('1.0','2.0')),(te_l.get('1.0','2.0')),(te_c.get('1.0','2.0')),(te_e.get('1.0','2.0')),(te_a.get('1.0','2.0'))])
        
        db.commit()

        print("Committed to db")
        deletedata()
    except Exception as e:
        print("ERROR !!!")
        print(e)   

def deletedata():
    try:
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        delete_contact = ('DELETE FROM contacts WHERE Fname = ? and Lname = ?')
        c.execute(delete_contact,[(tefname),(telname.strip())])
        db.commit()

        print("Committed to db")
    except Exception as e:
        print("ERROR !!!")
        print(e)   

#frame code
def edit_fun():
    global f2,te,te_n,te_l,te_a,te_c,te_e
    f2 = tk.Frame()
    f2=mk_frame(f_edit,f2,540,500,'light sky blue',0,0)
    b1 = tk.Button(f2,text='Save',bg='sky blue',width=10,font=("Courier"),command = saveEditedData)
    b1.place(x=150,y=460)
    b2 = tk.Button(f2,text='edit',bg='sky blue',width=10,font=("Courier"),command = fetchdata)
    b2.place(x=150,y=110)
    l=tk.Label()
    l=mk_label(f2,l,'Saved name','sky blue',10,50,10)
    l1=tk.Label()
    l1=mk_label(f2,l1,'First Name','sky blue',10,160,10)
    l2=tk.Label()
    l2=mk_label(f2,l2,'Last Name','sky blue',10,220,10)
    l3=tk.Label()
    l3=mk_label(f2,l3,'Contact','sky blue',10,280,10)
    l4=tk.Label()
    l4=mk_label(f2,l4,'Email','sky blue',10,340,10)
    l5=tk.Label()
    l5=mk_label(f2,l5,'Address','sky blue',10,400,10)
    te=tk.Text()
    te=mk_txt(f2,te,'white',130,50,20)
    te_n=tk.Text()
    te_n=mk_txt(f2,te_n,'white',130,160,20)
    te_l=tk.Text()
    te_l=mk_txt(f2,te_l,'white',130,220,20)
    te_c=tk.Text()
    te_c=mk_txt(f2,te_c,'white',130,280,20)
    te_e=tk.Text()
    te_e=mk_txt(f2,te_e,'white',130,340,20)
    te_a=tk.Text()
    te_a=mk_txt(f2,te_a,'white',130,400,20)
    
#click
def edit():
    global f_edit,b_e
    f_edit = tk.Frame(w,height=540,width=600,background='light sky blue')
    f_edit.pack_propagate(0) # don't shrink
    f_edit.place(x=0, y=0)
    icon(f_edit)
    edit_fun()


#### search
def searchdatabyname():
        global tefname,telname,tecontact,teemail,teaddress
        efname,elname = ts_d.get("1.0",'end-1c').split(" ")
        # print(te.get("1.0","end-1c"))
        # print(efname+" \n "+elname)
        efname = efname.strip()
        elname = elname.strip()
        try:
            with sqlite3.connect('quit.db') as db:
                c = db.cursor()      
            find_contact = ('SELECT Fname,Lname,Contact,Email,Address FROM contacts WHERE Fname = ? and Lname = ?')
            c.execute(find_contact,[(efname),(elname)])  
            rawdatas = c.fetchall()
            if rawdatas:
                for p1 in rawdatas:
                    # print(raw[0])
                    tefname = p1[0]
                    telname = p1[1]
                    tecontact = p1[2]
                    teemail = p1[3]
                    teaddress = p1[4]
                    ts_n.insert(tk.END,tefname)
                    ts_l.insert(tk.END,telname)
                    ts_c.insert(tk.END,tecontact)
                    ts_e.insert(tk.END,teemail)
                    ts_a.insert(tk.END,teaddress)
                    

            else:
                ms.showerror('Error!','Not Found ')
        except Exception as e:
            print(e)

def searchdatabyphonenumber():
        global tefname,telname,tecontact,teemail,teaddress
        tsnum = ts_dn.get("1.0",'end-1c')
        # print(te.get("1.0","end-1c"))
        # print(efname+" \n "+elname)
        
        tsnum = tsnum.strip()
        try:
            with sqlite3.connect('quit.db') as db:
                c = db.cursor()      
            find_contact = ('SELECT Fname,Lname,Contact,Email,Address FROM contacts WHERE Contact = ?')
            c.execute(find_contact,[(tsnum)])  
            rawdatas = c.fetchall()
            if rawdatas:
                for p1 in rawdatas:
                    # print(raw[0])
                    tefname = p1[0]
                    telname = p1[1]
                    tecontact = p1[2]
                    teemail = p1[3]
                    teaddress = p1[4]
                    ts_n.insert(tk.END,tefname)
                    ts_l.insert(tk.END,telname)
                    ts_c.insert(tk.END,tecontact)
                    ts_e.insert(tk.END,teemail)
                    ts_a.insert(tk.END,teaddress)
                    

            else:
                ms.showerror('Error!','Not Found ')
        except Exception as e:
            print(e)

def search_data():
    global f_data,ts_n,ts_l,ts_c,ts_e,ts_a
    f_data = tk.Frame()
    f_data=mk_frame(f_search,f_data,420,500,'light sky blue',100,110)
    l1=tk.Label()
    l1=mk_label(f_data,l1,'First Name','sky blue',10,70,10)
    l2=tk.Label()
    l2=mk_label(f_data,l2,'Last Name','sky blue',10,130,10)
    l3=tk.Label()
    l3=mk_label(f_data,l3,'Contact','sky blue',10,190,10)
    l4=tk.Label()
    l4=mk_label(f_data,l4,'Email','sky blue',10,250,10)
    l5=tk.Label()
    l5=mk_label(f_data,l5,'Address','sky blue',10,310,10)
    ts_n=tk.Text()
    ts_n=mk_txt(f_data,ts_n,'white',130,70,20)
    ts_l=tk.Text()
    ts_l=mk_txt(f_data,ts_l,'white',130,130,20)
    ts_c=tk.Text()
    ts_c=mk_txt(f_data,ts_c,'white',130,190,20)
    ts_e=tk.Text()
    ts_e=mk_txt(f_data,ts_e,'white',130,250,20)
    ts_a=tk.Text()
    ts_a=mk_txt(f_data,ts_a,'white',130,310,20)
# to search by name
def s_name():
    global ts_d
    f_name=tk.Frame()
    f_name=mk_frame(f_search,f_name,40,500,'light sky blue',0,70)
    l_name=tk.Label()
    l_name=mk_label(f_name,l_name,'Enter name','sky blue',20,0,10)
    ts_d=tk.Text()
    ts_d=mk_txt(f_name,ts_d,'white',150,0,20)
    search_data()
    b_n = tk.Button(f_search,bg = 'sky blue',fg = 'black', text='search', width=10,command = searchdatabyname)
    b_n.place(x=200,y=120)
    
#to search by number
def s_number():
    global ts_dn
    f_no=tk.Frame()
    f_no=mk_frame(f_search,f_no,40,500,'light sky blue',0,70)
    l_n = tk.Label()
    l_n=mk_label(f_no,l_n,'Enter no.','sky blue',20,0,10)
    ts_dn=tk.Text()
    ts_dn=mk_txt(f_no,ts_dn,'white',150,0,20)
    search_data()
    b_n = tk.Button(f_search,bg = 'sky blue',fg = 'black', text='search', width=10,command = searchdatabyphonenumber)
    b_n.place(x=200,y=120)
    

# search "next command"
def srch():
    var = var_s.get()
    if var == 1:
        s_name()
    if var == 2:
        s_number()
# frame code
def search_fun():
    global var_s
    var_s = tk.IntVar()
    r1=tk.Radiobutton(f_search,text='Search by name\t',value = 1,variable = var_s,bg='sky blue',width = 15)
    r1.place(x=5,y=10)
    r2=tk.Radiobutton(f_search,text='Search by number',value = 2,variable = var_s,bg='sky blue',width = 15)
    r2.place(x=5,y=40)
    b_search = tk.Button(f_search,bg = 'sky blue',fg = 'black', text='Next', width=10, command = srch)#
    b_search.place(x=150,y=25)
#click   
def search():
    global f_search,b_s,var_s
    f_search= tk.Frame(w,height=540,width=500,background='light sky blue')
    f_search.pack_propagate(0) # don't shrink
    f_search.place(x=0, y=0)
    icon(f_search)
    search_fun()

####delete
def searchdatabynamedelcontact():
        global tdfname,tdlname,tdcontact,tdemail,tdaddress,dlname,dfname
        dfname,dlname = td.get("1.0",'end-1c').split(" ")
        # print(te.get("1.0","end-1c"))
        # print(dfname+" \n "+dlname)
        dfname = dfname.strip()
        dlname = dlname.strip()
        # print(dfname+"\n"+dlname)
        try:
            with sqlite3.connect('quit.db') as db:
                c = db.cursor()      
            find_contact = ('SELECT Fname,Lname,Contact,Email,Address FROM contacts WHERE Fname = ? and Lname = ?')
            c.execute(find_contact,[(dfname),(dlname)])  
            rawdatas = c.fetchall()
            if rawdatas:
                for p1 in rawdatas:
                    # print(raw[0])
                    tdfname = p1[0]
                    tdlname = p1[1]
                    tdcontact = p1[2]
                    tdemail = p1[3]
                    tdaddress = p1[4]
                    td_n.insert(tk.END,tdfname)
                    td_l.insert(tk.END,tdlname)
                    td_c.insert(tk.END,tdcontact)
                    td_e.insert(tk.END,tdemail)
                    td_a.insert(tk.END,tdaddress) 
                    

            else:
                ms.showerror('Error!','Not Found ')
        except Exception as e:
            print(e)

def deletedatadelcontact():
    try:
        # print(dfname+"\n"+dlname.strip())
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        delete_contact = ('DELETE FROM contacts WHERE Fname = ? and Lname = ?')
        c.execute(delete_contact,[(dfname),(dlname.strip())])
        db.commit()


        print("Committed to db")
    except Exception as e:
        print("ERROR !!!")
        print(e)   

#frame code
def delete_fun():
    global f2,td,td_n,td_e,td_l,td_c,td_a
    f2 = tk.Frame()
    f2=mk_frame(f_delete,f2,540,500,'light sky blue',0,0)
    b1 = tk.Button(f2,text='Delete',bg='sky blue',width=10,font=("Courier"),command = deletedatadelcontact)
    b1.place(x=150,y=460)
    b2 = tk.Button(f2,text='Next',bg='sky blue',width=10,font=("Courier"),command = searchdatabynamedelcontact)
    b2.place(x=150,y=110)
    l=tk.Label()
    l=mk_label(f2,l,'Saved name','sky blue',10,50,10)
    l1=tk.Label()
    l1=mk_label(f2,l1,'First Name','sky blue',10,160,10)
    l2=tk.Label()
    l2=mk_label(f2,l2,'Last Name','sky blue',10,220,10)
    l3=tk.Label()
    l3=mk_label(f2,l3,'Contact','sky blue',10,280,10)
    l4=tk.Label()
    l4=mk_label(f2,l4,'Email','sky blue',10,340,10)
    l5=tk.Label()
    l5=mk_label(f2,l5,'Address','sky blue',10,400,10)
    td=tk.Text()
    td=mk_txt(f2,td,'white',130,50,20)
    td_n=tk.Text()
    td_n=mk_txt(f2,td_n,'white',130,160,20)
    td_l=tk.Text()
    td_l=mk_txt(f2,td_l,'white',130,220,20)
    td_c=tk.Text()
    td_c=mk_txt(f2,td_c,'white',130,280,20)
    td_e=tk.Text()
    td_e=mk_txt(f2,td_e,'white',130,340,20)
    td_a=tk.Text()
    td_a=mk_txt(f2,td_a,'white',130,400,20)
#click
def delete():
    global f_delete
    f_delete = tk.Frame(w,height=540,width=600,background='light sky blue')
    f_delete.pack_propagate(0) # don't shrink
    f_delete.place(x=0, y=0)
    icon(f_delete)
    delete_fun()



#### home screen
def home():
    #### home icon
    icon(w)
    ####home screen canvas
    canvas = tk.Canvas(w,height=290,width=400,bg='light blue')
    canvas.pack_propagate()
    canvas.place(x=90,y=100)
    canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW)
    test_string = "FUNCTIONALITY\n\n* You can add new contact\n* You can view existing contacts\n* You can edit existing contacts\n* Search for contact\n* Block contact\n* Get user details of any contact"
    #Time delay between chars, in milliseconds
    delta = 10
    delay = 0
    for i in range(len(test_string) + 1):
        s = test_string[:i]
        update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s,font = ('courier',14))
        canvas.after(delay, update_text)
        delay += delta  
    f = tk.Frame(canvas,height=30,width=397,background='light blue')
    f.pack_propagate(0)
    f.place(x=3, y=260)
    lbl_home = tk.Label(f,bg = 'light blue', text='-Drop your suggestion ',font =('courier',12))
    lbl_home.pack(side = "right")
    #### button frame
    f_b = tk.Frame(w,height=100,width=600,background='light sky blue')
    f_b.pack_propagate(0) # don't shrink
    f_b.place(x=0, y=540)
    #### view button
    b1 = tk.Button(f_b,bg = 'sky blue',fg = 'black', text='View\nContact', width=10, command = view)
    b1.config(font=("Courier", 14))
    b1.place(x=0,y=0)
    #### add button
    b2 = tk.Button(f_b,bg = 'sky blue',fg = 'black', text='Add\nContact', width=10,command = add)
    b2.config(font=("Courier", 14))
    b2.place(x=120,y=0)
    #### edit button
    b3 = tk.Button(f_b,bg = 'sky blue',fg = 'black', text='Edit\nContact', width=10,command = edit)
    b3.config(font=("Courier", 14))
    b3.place(x=240,y=0)
    #### search button
    b4 = tk.Button(f_b,bg = 'sky blue',fg = 'black', text='Search\nContact', width=10,height=2,command = search)
    b4.config(font=("Courier", 14))
    b4.place(x=360,y=0)
    #### block button
    b5 = tk.Button(f_b,bg = 'sky blue',fg = 'black', text='Delete\nContact', width=10,height=2,command = delete)
    b5.config(font=("Courier", 14))
    b5.place(x=480,y=0)

def main():
    ####window
    global w,img2
    w = tk.Tk()
    w.geometry('600x600')
    w.title('KnowTheDialer') 
    w.configure(bg='light sky blue')
    img2 = ImageTk.PhotoImage(file = r".\\p3.gif")
    home()
    w.mainloop()



main()