from db_api import *

db = r".\src\database\onlyplants.db"
conn = create_connection(db)

print(len(fetchTanaman(conn)))