'''import sys
import gc
"""
a = [1,2,3,4]
print(sys.getsizeof(a))
for i in range(len(a)):
    del a[-1]
    gc.collect()
for i in range(len(a)):
    a.pop()
print(sys.getsizeof(a))"""
c = {"a": 12342341293479178239481923478921347}
print(sys.getsizeof(c))
#for i in list(a.keys()):
#    del a[i]
#    gc.collect()
#for i in range(len(a)):
#    a.popitem()'''
'''
import psycopg2
import json
d = {"k'":"l","h":"k"}
conn = psycopg2.connect("""host=localhost port=5432 user=postgres password=password dbname=testdb""")
cur = conn.cursor()
cur.execute("""INSERT INTO x (a) VALUES (%s);""", (json.dumps(d),))
conn.commit()
cur.execute("""SELECT name FROM x;""")

cur.execute("""SELECT age FROM x;""")
print(list(cur))'''

try:
    a = 1/2
except:
    print("error")
else:
    print("nope")
finally:
    y = "y"
    print("final")
print(y)



