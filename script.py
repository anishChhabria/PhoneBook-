import sqlite3

import random
phoneNumber = []
stname = ['779 Euismod Av.','P.O. Box 319, 9051 Adipiscing Rd.','P.O. Box 467, 6115 Duis Rd.','919-5796 Urna. Ave','3017 Aliquet Street','P.O. Box 973, 194 Amet Road','3369 Ipsum. St.','5734 Augue Av.','967-8166 Convallis St.','292 Vel Street','P.O. Box 434, 8841 Risus. St.','Ap #282-3444 Euismod Rd.','P.O. Box 673, 8683 Ac, Street','Ap #190-6003 Ac Ave','Ap #815-6325 A, Ave','P.O. Box 168, 8018 Diam. St.','963-3660 Nulla Street',"P.O. Box 834, 266 Pede St.779 Euismod Av.",
'P.O. Box 319, 9051 Adipiscing Rd.','P.O. Box 467, 6115 Duis Rd.','919-5796 Urna. Ave','3017 Aliquet Street','P.O. Box 973, 194 Amet Road','3369 Ipsum. St.','5734 Augue Av.','967-8166 Convallis St.','292 Vel Street','P.O. Box 434, 8841 Risus. St.','Ap #282-3444 Euismod Rd.','P.O. Box 673, 8683 Ac, Street','P.O. Box 245, 560 Dui. St.','1094 Elit. Avenue','519-5777 Quis Av.','4189 Elit. Ave','P.O. Box 121, 7613 Ipsum Rd.',"Ap #837-1322 Phasellus St.",'585-3081 Aliquet St.',
'P.O. Box 704, 1577 Aenean Av.','479-6751 Libero. St.',]
city = ['Virelles',"Chetwynd",'Rimouski','Sint-Martens-Lennik','Bridgeport',"Sioux City",'El Monte','Cedar Rapids',
"Karimnagar",'Val Rezzo','Dundee','Colbún',"Comox",'Curaco de Vélez',"Carlisle","West Vancouver","Pforzheim","Chetwynd",
'Arquata del Tronto','Glendon','Kisi','Tiruvottiyur',"Gaithersburg","Kapuskasing",'Silvassa',"Thuin",'Asbestos','College','HomprŽ','Deschambault','Abbotsford',"Wallasey",'Tofield',
]
address = " "
firstName = ['John', 'Carl', 'Shawty', 'Nick', 'Johnas', 'Anish', 'Nihar', 'Jatin', 'Anshul', 'Prithvi', 'Ria', 'Hitesh', 'Aakash', 'Jay', 'Jai', 'Vandana', 'Roopa', 'Kartik', 'Shubham', 'Tanvi', 'Gayatri', 'Akashara', 'Padmaja', 'Sahil', 'Yash', 'Kunal', 'Karan', 'Aushutosh', 'Pramod', 'Tarun', 'Aricsia', 'Tejas','Mitali', 'Harshita', 'Sayali', 'Sayli', 'Tejal', 'Ankita', 'Rochna', 'Carol', 'Carl']
LastName = ['Smith', 'Wayne', 'Patel', 'Singh', 'Chhabria', 'Acharya', 'Chaudhary', 'Shinde', 'Amin', 'Bhatija', 'Abhyankar', 'Chugh', 'Mark', 'Belapurkar', 'Matai', 'Choudhary','Bhagchandani', 'Bendre', 'Darekar', 'borwankar', 'Kudchi', 'Fernandes', 'Makhija', 'Wakelkar', 'Verma', 'Natekar', 'Moghe' ]
mail = ['yahoo','gmail', 'ourkut' ]
com = ['in','com','edu']
with open('dummydata.txt','w',encoding='utf-8') as data:
    for i in range(100):
        first_Name = str(random.choice(firstName))
        Last_Name = str(random.choice(LastName))
        emailid = str(first_Name + Last_Name + str(random.randint(0, 2000))+ "@" + str(random.choice(mail))+"." + str(random.choice(com)))
        phoneNumber = str(random.randint(9000000000,9999999999))
        address = str(random.choice(stname)+"," +random.choice(city) )
        # data.write(first_Name + " "+ Last_Name+ " "+emailid +" "+ phoneNumber+" "+address+"\n")
        try:
            with sqlite3.connect('quit.db') as db:
               c = db.cursor()
            #instert into database
            insert = 'INSERT INTO contacts(Fname,Lname,Contact,Email,Address) VALUES(?,?,?,?,?)'
            c.execute(insert,[(first_Name),(Last_Name),(phoneNumber),(emailid),(address)])
            db.commit()
            print("added to DB")
        except Exception as e:
            print(e)

# with sqlite3.connect('quit.db') as db:
#     c = db.cursor()
# alter = 'ALTER TABLE contacts ADD CONSTRAINT myUniqueConstraint UNIQUE(Contact)'
# c.execute(alter)
# c.commit