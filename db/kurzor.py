

db_path = "crud.db"


conn = sqlite3.connect(db_path)

c = conn.cursor()
c.execute(""")
