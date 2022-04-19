import db_api


if __name__ == "__main__":
  db = r".\src\database\onlyplants.db"
  conn = db_api.create_connection(db)
  db_api.createInitializeTable(conn)
  db_api.register(conn, "gagas", db_api.hash("gagas"), "Gagas Yeah", "gagas@gagas.com", "08080808111", "Jalan Kenangan", 13242)
  db_api.register(conn, "epibau", db_api.hash("epibau"), "Epi Bau", "epi@epi.com", "0801238405", "Jalan sama Kimmy", 29292)
  db_api.register(conn, "dewi", db_api.hash("dewi"), "Dewi", "dewi@epi.com", "0801238405", "Jalan sama Kimmy tp dimarahin Epi", 29292)