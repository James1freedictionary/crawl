import psycopg2
import json
import gc
database = """host=localhost port=5432 user=postgres password=password dbname=testdb"""
conn = psycopg2.connect(database)
cur = conn.cursor()
try:
    cur.execute("""SELECT * FROM done;""")
    print("successfully select table done. TABLE done: ", list(cur))
except:
    print("error! THERE IS NO TABLE done.")
else:
    print("downloading content ...")
    cur.execute("""SELECT * FROM content;""")
    print("finish downloading")
print("writing to disk ...")
for i in cur:
    d = json.loads(i[0])
    with open("dict.txt", "a") as f:
        f.write(d["word"] + "\n" + d["content"] + "\n" + "</>" + "\n")
    del d, i
    gc.collect()
print("you are done!")



