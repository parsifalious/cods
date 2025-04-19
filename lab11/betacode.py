
import psycopg2
import random
from tabulate import tabulate

try:
    connection=psycopg2.connect(
        dbname="phonebook",
        host="localhost",
        user="postgres",
        password="1234"
    )
    p=[]
    n=5
    for i in range(n):
        k=int(input())
        p.append(k)
    with connection.cursor() as cur:
        cur.execute(f"""DO $$
BEGIN
    FOR i IN 1..{n} LOOP
         insert into oooo(num) values({p['i']});
    END LOOP;
END $$;""")
except Exception as _ex:
    print("[INFO] ERROR",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] closed")