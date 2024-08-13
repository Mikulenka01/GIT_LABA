import pyodbc

server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

spojeni = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=' + server + ';'
'DATEBASE=' + database + ';'
'UID=' + username + ';'
'PWD=' + password)

c = conn.kurzor()


c.execute