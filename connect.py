import mysql.connector
con = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Dexter#786', database = 'bank')
if con.is_connected():
    print("Connected")
else:
    print("Not connected")

curs = con.cursor()
curs.execute("Show tables")
for i in curs:
    print(i)

curs = con.cursor()
curs.execute("select * from customer")
table = curs.fetchall()
for i in table:
    print(i)

curs = con.cursor()
curs.execute("insert into customer values(420, 'sukuna', 5000, 15000)")
con.commit()
print('value inserted')

#the programs for insert, update and delete are the same,
#just the query has to be changed
