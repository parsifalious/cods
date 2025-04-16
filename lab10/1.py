import psycopg2
from tabulate import tabulate
connection=None
try:
    connection=psycopg2.connect(
        dbname="phonebook",
        host="localhost",
        user="postgres",
        password="1234"
    )
    connection.autocommit=True
    with connection.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id BIGSERIAL NOT NULL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        phone VARCHAR(12) NOT NULL,
        password VARCHAR(10) NOT NULL,
        CHECK (char_length(password) BETWEEN 4 AND 10)
    );""")
    print("Table created")

    with connection.cursor() as cur:
        cur.execute("""INSERT INTO users(first_name,last_name,phone,password)
                   VALUES ('Ryba','Ezh','87773676398','5555')""")
    print("Inserted")

    operators={
        "figma":"78952",
        "A4":"etolamba"
    }
    aus="Jele"
    apa="crecker7456"
    with connection.cursor() as cur:
        cur.execute("select * from users;")
        mas=cur.fetchall()
    act=None
    act=int(input("1 to insert, 2 to update,3 to Querying,4 to drop data:"))
    while act!=1 and act!=2 and act!=3 and act!=4:
        act=int(input("try again: "))
    insert=False
    if act==1:
        fname=input("first name: ")
        lname=input("last name: ")
        phone=input("your phone: ")
        password=input("install password(from 4 to 10 chars): ")
        passcheck=input("confirm your password: ")
        while password!=passcheck or len(password)<4 or len(password)>10:
            print("it didnt confirm, try again")
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
                cha=input("what do you want change?(1-first name, 2-last name, 3-phone, 4-password, n-nothing):")
                if cha=='1':
                    fname=input("first name: ")
                elif cha=='2':
                    lname=input("last name: ")
                elif cha=='3':
                    phone=input("phone: ")
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
            qn=False
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
            qn=False
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
    with connection.cursor() as cur:
        if act==2 and conf==True and conf2==True:
            cur.execute(f"""UPDATE users
                        SET first_name='{fname}',
                        last_name='{lname}',
                        phone='{phone}',
                        password='{password}'
                        WHERE first_name='{p[0]}' AND last_name='{p[1]}' AND phone='{p[2]}';""")
            print("changed")
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
                    elif fil2==1:
                        ch3=[f"8705%",f"8771%",f"8776%",f"8777%"]
                    elif fil2==2:
                        ch3=[f"8750%",f"8751%",f"8760%",f"8761%"]
                    elif fil2==3:
                        ch3=[f"8701%",f"8702%",f"8775%",f"8778%"]
                else:
                    ch1=f"%%"
                    ch2=f"%%"
                    ch3=[f"%%",f"%%",f"%%",f"%%"]


                if q2=='n':
                    cur.execute(f"select first_name,last_name from users where first_name ilike '{ch1}' and last_name ilike '{ch2}'")
                    rows=cur.fetchall()
                elif q2=='p' and qa==True:
                    cur.execute(f"select first_name,last_name,phone from users where first_name ilike '{ch1}' and last_name ilike '{ch2}' and phone similar to '({ch3[0]}|{ch3[1]}|{ch3[2]}|{ch3[3]})'")
                    rows=cur.fetchall()
                elif q2=='ps' and qps==True:
                    cur.execute(f"select * from users where first_name ilike '{ch1}' and last_name ilike '{ch2}' and phone similar to '({ch3[0]}|{ch3[1]}|{ch3[2]}|{ch3[3]})'")
                    rows=cur.fetchall()
                columns = []
                for desc in cur.description:
                    columns.append(desc[0])
                print(tabulate(rows, headers=columns, tablefmt="psql"))
        if act==4:
            if qn==True:
                cur.execute(f"delete from users where phone='{phone}'")
except Exception as _ex:
    print("[INFO] ERROR",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] closed")
