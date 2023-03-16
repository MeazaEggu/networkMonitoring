import subprocess
import mysql.connector as con
from datetime import datetime
db = con.connect(
                 host="172.16.0.56",
                 user="root",
                 passwd="Act@1234",
                 db="test2")

mycursor = db.cursor()
mycursor.execute("SELECT ip FROM ip")
myresult = mycursor.fetchall()
ipList=[]
for x in myresult:
  x=str(x)[2:-3]
  ipList.append(x)
def pinger():
    return subprocess.Popen(
        ["ping" ,"-s",tt, "-c", "4", host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
lisByte = ["56","1016","504","1992"]
for host in ipList:
    for tt in lisByte:
        out = pinger().communicate()[0].decode()
        pingList = out.splitlines()
        ls=[]
        for i in range(1, len(pingList)-4):
            x=pingList[i].split(" ")
            ls.append(x)
        for i in range(len(ls)):
            bb=ls[i][4].split("=")
            bc=ls[i][5].split("=")
            bm=ls[i][6].split("=")
            timeUnit=ls[i][7]
            bytes=ls[i][0]
            ip=ls[i][3][:-1]
            icmp_seq=bb[1]
            ttl=bc[1]
            time=bm[1]
    
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
            print(icmp_seq,bytes)
            
        cursor = db.cursor()
            
        query = "INSERT INTO ping_info (bytes,ip,icmp_seq,ttl,time,ts)VALUES(%s, %s,%s, %s,%s,%s)"
        values=bytes,ip,icmp_seq,ttl,time,timestamp
        cursor.execute(query,values)
        db.commit()

        print(cursor)
        print("create")
            





                