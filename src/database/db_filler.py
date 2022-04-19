from db_api import *


if __name__ == "__main__":
  db = r".\src\database\onlyplants.db"
  conn = create_connection(db)
  createInitializeTable(conn)
  register(conn, "gagas", hash("gagas"), "Gagas Yeah", "gagas@gagas.com", "08080808111", "Jalan Kenangan", 13242)
  register(conn, "epibau", hash("epibau"), "Epi Bau", "epi@epi.com", "0801238405", "Jalan sama Kimmy", 29292)
  register(conn, "dewi", hash("dewi"), "Dewi", "dewi@epi.com", "0801238405", "Jalan sama Kimmy tp dimarahin Epi", 29292)

  # insert data tanaman
  image = convertToBinaryData(r".\img\bonsai.jpg")
  addTanaman(conn, "bonsai", 100000, 10, "ini adalah bonsai", image,"jogja")
  image = convertToBinaryData(r".\img\lavender.jpg")
  addTanaman(conn, "lavender", 200000, 20, "ini adalah lavender",image, "jakarta")
  image = convertToBinaryData(r".\img\lily.jpg")
  addTanaman(conn, "lily", 300000, 30, "ini adalah lily", image,"bandung")
  image = convertToBinaryData(r".\img\sakura.jpg")
  addTanaman(conn, "sakura", 400000, 40, "ini adalah sakura", image,"surabaya")

  # insert data pemesanan
  addPemesanan(conn, 1, "2020-01-01")
  addPemesanan(conn, 1, "2020-01-02")
  addPemesanan(conn, 2, "2020-01-02")

  # Insert data detail pemesanan
  addDetailPemesanan(conn, 1, 1, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
  addDetailPemesanan(conn, 1, 2, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
  addDetailPemesanan(conn, 2, 3, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)