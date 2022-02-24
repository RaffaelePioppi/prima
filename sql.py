import sqlite3

conn = sqlite3.connect('prova.db')
c = conn.cursor()

# tabella = ('''CREATE TABLE NUMERO
#              (ID INT PRIMARY KEY    NOT NULL,
#               NAME      VARCHAR(50)        NOT NULL,
#               AGE       TEXT        NOT NULL);''')
# c.execute(tabella)
nomi = input("numero nomi")
i = 0
while i < int(nomi):
    id = input('NUMERO ID:')
    name = input('NUMERO NAME:')
    age = input('NUMERO AGE')
    c.execute("INSERT INTO NUMERO (ID,NAME,AGE)"
              " VALUES(?,?,?)", (id, name, age))
    i += 1
# c.execute("SHOW TABLES")
for row in c:
    print(row)
# update = input("cosa vuoi aggiornare")

# c.execute("INSERT INTO NUMERO VALUES('1','raf','20')")#inserisce argomenti
#
# # c.execute("UPDATE NUMERO set AGE=49 WHERE ID=1") #aggiorna un argomento
# cursor = conn.execute("SELECT ID,NAME,AGE from NUMERO") #seleziona
# for row in cursor:
#     print("ID ", row[0])
#     print("NAME = ", row[1])
#     print("AGE = ", row[2])
# # conn.execute("""CREATE TABLE N
# #             (ID INT PRIMARY KEY NOT NULL);""")
# # c.execute("INSERT INTO N VALUES()")
# ID = input("enter id:")
# cursor = conn.execute("SELECT ID from NUMERO")
#
# print(num1)
# # c.execute("""DROP TABLE N""")
# # c.execute("""DROP TABLE NUMERO""")
conn.commit()
conn.close()
