import psycopg2
conn = psycopg2.connect(dbname="project_db",user="postgres",password="17042008",host="localhost",port="5433")
cursor = conn.cursor()
cursor.execute("INSERT INTO users (nickname,password) VALUES (%s,%s);", ('oleg',17623))
conn.commit()
#ПЕРЕДЕЛАТЬ БД ШОБЫ ID БЫЛ PRIMARY KEY И SERIAL
cursor.execute("SELECT * FROM users WHERE nickname = 'dima'")
records = cursor.fetchall()
if records == []:
    print("Пользователь не найден")
print(records)
cursor.close()
conn.close()