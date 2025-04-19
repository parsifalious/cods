import psycopg2
import random
import string
from tabulate import tabulate
try:
    connection=psycopg2.connect(
        dbname="phonebook",
        host="localhost",
        user="postgres",
        password="1234"
    )
    connection.autocommit=True
    # with connection.cursor() as cur:
    #     cur.execute("SELECT version();")
    # with connection.cursor() as cur:
    #     cur.execute("""create table users(
    #                 id bigserial not null primary key,
    #                 first_name varchar(50) not null,
    #                 last_name varchar(50) not null,
    #                 phone varchar(12) not null,
    #                 password varchar(10) not null,
    #                 CHECK(char_length(password) BETWEEN 4 AND 10));
    #                 """)
    #     print("table created")
    # with connection.cursor() as cur:
    #     cur.execute("""INSERT INTO users(first_name,last_name,phone,password) values('Ryba','Ezh','87773676398','5555')""")
    #     print("inserted")
    operators={
        "figma":"78952",
        "A4":"etolamba"
    }
    aus="Jele"
    apa="crecker7456"
    with connection.cursor() as cur:
        cur.execute('select * from "users";')
        mas=cur.fetchall()
    act=None
    act=int(input("1 to insert, 2 to update,3 to Querying,4 to drop data:"))
    while act!=1 and act!=2 and act!=3 and act!=4:
        act=int(input("try again: "))
    insert=False
    updat=False
    if act==1:
        numu=input("o-one user,m-many users: ")
        while numu!='o' and numu!='m':
            numu=input("try again: ")
        if numu=='m':
            nu=int(input("num of users: "))
            characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]}{|;:,.<>?/"
            pepe=[]
            for i in range(nu):
                fname=input("first name: ")
                lname=input("last name: ")
                phone=input("phone: ").replace(" ", "")
                lenn=random.randint(4,10)
                password=''.join(random.choices(characters, k=lenn))
                pepe.append([fname,lname,phone,password])
            wpepe=[]
            kk=0
            for i in range(nu):
                if (pepe[i][2][0]!='8' or len(pepe[i][2])!=11) and (pepe[i][2][0]!='+' or pepe[i][2][1]!='7' or len(pepe[i][2])!=12):
                    kk+=1
                    if kk==1:
                        print("users with wrong phone: ")
                    print(pepe[i],"phone:",pepe[i][2],sep=" ")
                    wpepe.append(i)
            for x in sorted(wpepe, reverse=True):
                del pepe[x]
            
                

        if numu=='o':
            fname=input("first name: ")
            lname=input("last name: ")

            bb=True
            for x in mas:
                if fname==x[1] and lname==x[2]:
                    bb=False
                    break
            if bb==False:
                print("user already exist")
                iou=input("p-change phone, i-insert new: ")
                if iou=='p':
                    
                    while updat==False:
                        password=input("enter password: ")
                        bb=True
                        updat=False
                        for x in mas:
                            if fname==x[1] and lname==x[2] and password==x[4]:
                                updat=True
                    phone=input("new phone(begin from 8 or +7 and digits=11): ").replace(" ", "")
                    while (phone[0]!='8' or len(phone)!=11) and (phone[0]!='+' or phone[1]!='7' or len(phone)!=12):
                        phone=input("new phone(begin from 8 or +7 and digits=11): ").replace(" ", "")
                    act=0

                elif iou=='i':
                    bbb=False
                    while bbb==False:
                        print("enter user again")
                        fname=input("first name: ")
                        lname=input("last name: ")
                        temp=True
                        for x in mas:
                            if fname==x[1] and lname==x[2]:
                                temp=False
                                break
                        if temp==True:
                            bbb=True
            if updat==False:
                phone=input("your phone(begin from 8 or +7 and digits=11): ").replace(" ", "")
                while (phone[0]!='8' or len(phone)!=11) and (phone[0]!='+' or phone[1]!='7' or len(phone)!=12):
                    phone=input("your phone(begin from 8 or +7 and digits=11): ").replace(" ", "")
                password=input("install password(from 4 to 10 chars): ")
                passcheck=input("confirm your password: ")
                while password!=passcheck or len(password)<4 or len(password)>10:
                    print("it didnt confirm or conditions didnt met, try again")
                    password=input("install password(from 4 to 10 chars): ")
                    passcheck=input("confirm your password: ")
                insert=True
    elif act==2:
        conf=False 
        fname=input("first name: ")
        lname=input("last name: ")
        for x in mas:
            if x[1]==fname and x[2]==lname:
                conf=True
                break
        while conf==False:
            print("try again")
            fname=input("first name: ")
            lname=input("last name: ")
            for x in mas:
                if x[1]==fname and x[2]==lname:
                    conf=True
                    break
        if conf==True:
            conf2=False
            password=input("enter password: ")
            for x in mas:
                if x[4]==password:
                    phone=x[3]
                    conf2=True
            while conf2==False:
                print("try again")
                password=input()
                for x in mas:
                    if x[4]==password:
                        phone=x[3]
                        conf2=True
                        break
        if conf==True and conf2==True:
            cha=None
            p=[fname,lname,phone,password]
            while cha!='n':
                cha=input("what do you want change?(1-first name, 2-last name, 3-phone, 4-password, n-nothing else):")
                if cha=='1':
                    f=True
                    k=0
                    while f==True:
                        temp=False
                        if k==1:
                            print("again")
                        k=1
                        fname=input("first name: ")
                        for x in mas:
                            if fname==x[1]:
                                temp=True
                                break
                        if temp==False:
                            f=False         
                elif cha=='2':
                    f=True
                    k=0
                    while f==True:
                        temp=False
                        if k==1:
                            print("again")
                        k=1
                        lname=input("last name: ")
                        for x in mas:
                            if lname==x[2]:
                                temp=True
                                break
                        if temp==False:
                            f=False     
                elif cha=='3':
                    f=True
                    k=0
                    while f==True:
                        temp=False
                        if k==1:
                            print("again")
                        k=1
                        phone=input("phone(begin from 8 or +7 and digits=11): ").replace(" ","")
                        while (phone[0]!='8' or len(phone)!=11) and (phone[0]!='+' or phone[1]!='7' or len(phone)!=12):
                            phone=input("phone(begin from 8 or +7 and digits=11): ").replace(" ","")
                        for x in mas:
                            if phone==x[3]:
                                temp=True
                                break
                        if temp==False:
                            f=False  
                elif cha=='4':
                    password=input("install password(from 4 to 10 chars): ")
                    passcheck=input("confirm your password: ")
                    while password!=passcheck or len(password)<4 or len(password)>10:
                        print("it didnt confirm, try again")
                        password=input("install password(from 4 to 10 chars): ")
                        passcheck=input("confirm your password: ")
    elif act==3:
        quer=input("who are you?(u-user,o-operator,a-admin): ")
        while quer!='u' and quer!='o' and quer!='a':
            quer=input('try again: ')
        q1=input("o-one user info,a-all users info: ")
        while q1!='o' and q1!='a':
            q1=input('try again: ')
        
        if q1=='o':
            q2=input("n-name,p-phone,s-password: ")
            while q2!='n' and q2!='p' and q2!='s':
                q2=input("try again:")
            if q2=='n':
                qp=False
                phone=input("enter users phone: ")
                for x in mas:
                    if phone==x[3]:
                        qp=True
                        break
                while qp==False:
                    phone=input("this phone dont exist,try again: ")
                    for x in mas:
                        if phone==x[3]:
                            qp=True
                            break
            if q2=='p':
                qn=False
                fname=input("first name: ")
                lname=input("last name:")
                for x in mas:
                    if fname==x[1] and lname==x[2]:
                        qn=True
                        break
                while qn==False:
                    print("this name dont exist")
                    fname=input("first name: ")
                    lname=input("last name:")
                    for x in mas:
                        if fname==x[1] and lname==x[2]:
                            qn=True
                            break
                
            if q2=='s':
                if quer=='a':
                    qa=False
                    au=input("admins username: ")
                    ap=input("admins password: ")
                    if au==aus and ap==apa:
                        qa=True
                    while qa==False:
                        print("try again: ")
                        au=input("admins username: ")
                        ap=input("admins password: ")
                        if au==aus and ap==apa:
                            qa=True
                    qn=False
                    fname=input("first name: ")
                    lname=input("last name:")
                    for x in mas:
                        if fname==x[1] and lname==x[2]:
                            qn=True
                            break
                    while qn==False:
                        print("this name dont exist")
                        fname=input("first name: ")
                        lname=input("last name:")
                        for x in mas:
                            if fname==x[1] and lname==x[2]:
                                qn=True
                                break
                else:
                    print("you are not admin")
                    act=-1
        elif q1=='a':
            q2=input("""n-only names(allowed for all)
p-names and phones(only for operators and admin)
ps-names,phones,passwords(only for admin):
""")
            while q2!='n' and q2!='p' and q2!='ps':
                q2=input("try again:")
            if q2=='p':
                if quer=='a':
                    qa=False
                    au=input("admins username: ")
                    ap=input("admins password: ")
                    if au==aus and ap==apa:
                        qa=True
                    while qa==False:
                        print("try again: ")
                        au=input("admins username: ")
                        ap=input("admins password: ")
                        if au==aus and ap==apa:
                            qa=True
                elif quer=='o':
                    qa=False
                    ou=input("operators username: ")
                    op=input("operators password: ")
                    if ou in operators:
                        if operators[ou]==op:
                            qa=True
                    while qa==False:
                        print("try again")
                        ou=input("operators username: ")
                        op=input("operators password: ")
                        if ou in operators:
                            if operators[ou]==op:
                                qa=True
                else:
                    qa=False
                    print("you have not access")
                
            elif q2=='ps':
                if quer=='a':
                    qps=False
                    au=input("admins username: ")
                    ap=input("admins password: ")
                    if au==aus and ap==apa:
                        qps=True
                    while qps==False:
                        print("try again: ")
                        au=input("admins username: ")
                        ap=input("admins password: ")
                        if au==aus and ap==apa:
                            qps=True
                else:
                    qps=False
                    print("you have not access")
    elif act==4:
        quer=input("who are you?(u-user,o-operator,a-admin): ")
        while quer!='u' and quer!='o' and quer!='a':
            quer=input('try again: ')
        if quer=='u':
            qn=False
            drtyp=input("drop by phone/name(p/n): ")
            while drtyp!='p' and drtyp!='n':
                print("wrong")
                drtyp=input("drop by phone/name(p/n): ")
            if drtyp=='p':
                phone=input("phone: ")
                password=input("password: ")
                for x in mas:
                    if phone==x[3] and password==x[4]:
                        qn=True
                        break
                while qn==False:
                        print("phone or password or both are wrong")
                        phone=input("phone: ")
                        password=input("password: ")
                        for x in mas:
                            if phone==x[3] and password==x[4]:
                                qn=True
                                break
            elif drtyp=='n':
                fname=input("first name: ")
                lname=input("last name:")
                password=input("password: ")
                for x in mas:
                    if fname==x[1] and lname==x[2]:
                        qn=True
                        break
                while qn==False:
                    print("this name dont exist")
                    fname=input("first name: ")
                    lname=input("last name:")
                    password=input("password: ")
                    for x in mas:
                        if fname==x[1] and lname==x[2] and password!=x[4]:
                            qn=True
                            break

        if quer=='o':
            qa=False
            ou=input("operators username: ")
            op=input("operators password: ")
            if ou in operators:
                if operators[ou]==op:
                    qa=True
            while qa==False:
                print("try again")
                ou=input("operators username: ")
                op=input("operators password: ")
                if ou in operators:
                    if operators[ou]==op:
                        qa=True
            drtyp=input("drop by phone/name(p/n): ")
            while drtyp!='p' and drtyp!='n':
                print("wrong")
                drtyp=input("drop by phone/name(p/n): ")
            qn=False
            if drtyp=='p':
                phone=input("users phone: ")
                for x in mas:
                    if phone==x[3]:
                        qn=True
                        break
                while qn==False:
                    print("this user dont exist")
                    phone=input("users phone: ")
                    for x in mas:
                        if phone==x[3]:
                            qn=True
                            break
            elif drtyp=='n':
                fname=input("first name: ")
                lname=input("last name:")
                for x in mas:
                    if fname==x[1] and lname==x[2]:
                        qn=True
                        break
                while qn==False:
                    print("this name dont exist")
                    fname=input("first name: ")
                    lname=input("last name:")
                    for x in mas:
                        if fname==x[1] and lname==x[2]:
                            qn=True
                            break
        if quer=='a':
            qps=False
            au=input("admins username: ")
            ap=input("admins password: ")
            if au==aus and ap==apa:
                qps=True
            while qps==False:
                print("try again: ")
                au=input("admins username: ")
                ap=input("admins password: ")
                if au==aus and ap==apa:
                    qps=True
            drtyp=input("drop by phone/name(p/n): ")
            while drtyp!='p' and drtyp!='n':
                print("wrong")
                drtyp=input("drop by phone/name(p/n): ")
            qn=False
            if drtyp=='p':
                phone=input("users phone: ")
                for x in mas:
                    if phone==x[3]:
                        qn=True
                        break
                while qn==False:
                    print("this user dont exist")
                    phone=input("users phone: ")
                    for x in mas:
                        if phone==x[3]:
                            qn=True
                            break
            elif drtyp=='n':
                fname=input("first name: ")
                lname=input("last name:")
                for x in mas:
                    if fname==x[1] and lname==x[2]:
                        qn=True
                        break
                while qn==False:
                    print("this name dont exist")
                    fname=input("first name: ")
                    lname=input("last name:")
                    for x in mas:
                        if fname==x[1] and lname==x[2]:
                            qn=True
                            break
    with connection.cursor() as cur:
        if act==2 and conf==True and conf2==True:
            cur.execute(f"""UPDATE users
                        SET first_name='{fname}',
                        last_name='{lname}',
                        phone='{phone}',
                        password='{password}'
                        WHERE first_name='{p[0]}' AND last_name='{p[1]}' AND phone='{p[2]}';""")
            print("changed")
        if act==1 and numu=='m':
            for x in pepe:
                cur.execute(f"""INSERT INTO users(first_name,last_name,phone,password) values('{x[0]}','{x[1]}','{x[2]}','{x[3]}');""")
            if len(pepe)>0:
                print("inserted")
        if insert==True:
            for x in mas:
                if x[3]==phone:
                    insert=False
                    break
            if insert==True:
                cur.execute(f"""INSERT INTO users(first_name,last_name,phone,password) values('{fname}','{lname}','{phone}','{password}')""")
                print("inserted")
            else:
                print("user phone already busy")
        if act==3:
            if q1=='o':
                if q2=='n' and qp==True:
                    cur.execute(f"select first_name,last_name from users where phone='{phone}'")
                    row=cur.fetchall()
                elif q2=='p' and qn==True:
                    cur.execute(f"select first_name,last_name,phone from users where first_name='{fname}' and last_name='{lname}'")
                    row=cur.fetchall()
                elif q2=='s' and qa==True and qn==True:
                    cur.execute(f"select first_name,last_name,phone,password from users where first_name='{fname}' and last_name='{lname}'")
                    row=cur.fetchall()
                columns = []
                for desc in cur.description:
                    columns.append(desc[0])
                print(tabulate(row, headers=columns, tablefmt="psql"))
            elif q1=='a':
                off=0
                lim=len(mas)
                uo=input("use offset(y/n): ")
                while uo!='y' and uo!='n':
                    uo=input("try again: ")
                if uo=='y':
                    off=int(input("offset: "))
                ul=input("use limit(y/n): ")
                while ul!='y' and ul!='n':
                    ul=input("try again: ")
                if ul=='y':
                    lim=int(input("limit: "))

                uf=input("use filters? y/n:")
                if uf=='y':
                    fil=int(input("""filters for first name:
0-no filters
1-have some chars
2-begin with some chars
"""))
                    while fil<0 or fil>2:
                        fil=int(input("try again: "))
                    if fil==0:
                        ch1=f"%%"
                    elif fil==1:
                        ch=input("chars:")
                        ch1=f"%{ch}%"
                    elif fil==2:
                        ch=input("chars:")
                        ch1=f"{ch}%"
                    
                    fil1=int(input("""filters for last name:
0-no filters
1-have some chars
2-begin with some char
"""))
                    while fil1<0 or fil1>2:
                        fil1=int(input("try again: "))
                    if fil1==0:
                        ch2=f"%%"
                    elif fil1==1:
                        ch=input("chars:")
                        ch2=f"%{ch}%"
                    elif fil1==2:
                        ch=input("chars:")
                        ch2=f"{ch}%"
                    fil2=int(input("""filters for phone:
0-no filters
1-beeline 
2-KazakhTelecom
3-kcell
"""))
                    while fil2<0 or fil2>3:
                        fil2=int(input("try again: "))
                    if fil2==0:
                        ch3=[f"%%",f"%%",f"%%",f"%%"]
                        ch4=[f"%%",f"%%",f"%%",f"%%"]
                    elif fil2==1:
                        ch3=[f"8705%",f"8771%",f"8776%",f"8777%"]
                        ch4=[f"+7705%",f"+7771%",f"+7776%",f"+7777%"]
                    elif fil2==2:
                        ch3=[f"8750%",f"8751%",f"8760%",f"8761%"]
                        ch4=[f"+7750%",f"+7751%",f"+7760%",f"+7761%"]
                    elif fil2==3:
                        ch3=[f"8701%",f"8702%",f"8775%",f"8778%"]
                        ch4=[f"+7701%",f"+7702%",f"+7775%",f"+7778%"]
                else:
                    ch1=f"%%"
                    ch2=f"%%"
                    ch3=[f"%%",f"%%",f"%%",f"%%"]
                    ch4=[f"%%",f"%%",f"%%",f"%%"]


                if q2=='n':
                    cur.execute(f"select first_name,last_name from users where first_name ilike '{ch1}' and last_name ilike '{ch2}' offset {off} limit {lim};")
                    rows=cur.fetchall()
                elif q2=='p' and qa==True:
                    cur.execute(f"select first_name,last_name,phone from users where first_name ilike '{ch1}' and last_name ilike '{ch2}' and phone similar to '({ch3[0]}|{ch3[1]}|{ch3[2]}|{ch3[3]})|{ch4[0]}|{ch4[1]}|{ch4[2]}|{ch4[3]})' offset {off} limit {lim};")
                    rows=cur.fetchall()
                elif q2=='ps' and qps==True:
                    cur.execute(f"select * from users where first_name ilike '{ch1}' and last_name ilike '{ch2}' and phone similar to '({ch3[0]}|{ch3[1]}|{ch3[2]}|{ch3[3]}|{ch4[0]}|{ch4[1]}|{ch4[2]}|{ch4[3]})' offset {off} limit {lim};")
                    rows=cur.fetchall()
                columns = []
                for desc in cur.description:
                    columns.append(desc[0])
                print(tabulate(rows, headers=columns, tablefmt="psql"))
        if act==4:
            if qn==True:
                cur.execute(f"delete from users where phone='{phone}'")
        if updat==True:
            cur.execute(f"""UPDATE users
                        SET phone='{phone}'
                        WHERE first_name='{fname}' and last_name='{lname}';""")
            print("phone updated")
except Exception as _ex:
    print("[INFO] ERROR",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] closed")
