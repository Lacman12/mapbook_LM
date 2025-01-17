import psycopg2 as ps

db_params=ps.connect(user='aaaaaaa',password='aaaaaaa',host='localhost',database='aaaaaaa' ,port='5434')



cursor=db_params.cursor()
query="SELECT name,surname,posts,location,st_astext(cords),id FROM public.users ORDER BY id ASC"
cursor.execute(query)
users=cursor.fetchall()
cursor.close()

#print(users)
for user in users:
    print(float(users[4][6:-1].split()[0]))
    print(float(users[4][6:-1].split()[1]))