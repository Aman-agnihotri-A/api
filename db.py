import sqlite3

def display():
    con = sqlite3.connect("aman.db")
    cur = con.cursor()
    #cur.execute("Create table aman(P_ID TEXT,Name TEXT,PH_NO INTEGER)")
    #cur.execute("Insert into aman values ")
    #res = cur.execute("SELECT name FROM sqlite_master")
    #print(res.fetchone())
    #cur.execute("insert into aman values(2,'fang',8294342323),(3,'shani',57843783)")
    #con.commit()

    r=cur.execute("select * from aman")
    #print(r.fetchall())
    return r.fetchall()
#display()