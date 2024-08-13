import sqlite3
db_path = "crud.db"

conn = sqlite3.connect(db_path)

c = conn.cursor()

c.execute("""

CREATE TABLE studenti (
id INTEGER PRIMARY KEY,
jmeno TEXT,
prijmeni TEXT,
rok_narozeni INTEGER,
obor TEXT,
pohlavi TEXT,
          )
          """)
c.execute(
    """
   CREATE TABLE kurzy (
   id INTEGER PRIMARY KEY,
   nazev TEXT,
   pocet_body INTEGER,
   semestr TEXT, ); 
    
    
    
    """
)

c.execute("""

CREATE TABLE registrace
(id INTEGER PRIMARY KEY,
student_id INTEGER,
kurz_id INTEGER,
rok INTEGER,
FOREIGN KEY (studenti_id) REFERENCES studenti(id),
FOREIGN KEY (kurz_id) REFERENCES kurzy (id)

""")

c.execute ("""
INSERT INTO studenti (jmeno, prijmeni, rok_narozeni, obor, pohlavi
VALUES
('Jan', 'Novak', 2000, 'Informatika','M'),
('Anna', 'Svobodova', 2001, 'Fyzika, 'F'),
('Petr', 'Kral', 1999, 'Matematika','M'),
('Michaela','Jirankova', 1997, 'Informatika', 'F'),
('Ondrej','Dolezal', 1997,'Fyzika', 'M'),
('Eva', 'Kovarova', 1997, 'Informatika', 'F'),
""")

c.execute ("""
INSERT INTO kurzy (nazev,pocet_bodu,semestr)
VALUES
('Programovani I', 6, 'ZS'),
('Fyzikalni praktikum I',5,'ZS'),
('Linearni algebra', 7, 'ZS'),
('Programovani II', 6, 'LS'),
('Fyzikalni praktikum II',5, 'LS'),



""")

c.execute("""
INSERT INTO registrace (student_id,kurz_id,rok)
VALUES
(1,1,2023),
(1,3,2023),
(2,2,2023),
(3,1,2023),
(3,3,2023),
(2,1,2023),
(3,2,2023),
(4,1,2024),
(4,2,2024),
(5,5,2024),
(6,1,2023),
(6,4,2023),
(7,2,2023),
(7,3,2023),


""")


