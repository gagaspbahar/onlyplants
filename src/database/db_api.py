import sqlite3
from sqlite3 import Error
import hashlib
import base64

# 1. BIKIN KONEKSI
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# 2. BIKIN TABEL
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# 3. CONVERT GAMBAR JADI BINARY DATA (BLOB) -> untuk image blob
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# 4. TULIS BLOB DATA KE FILE
def write_to_file(binary_data, file_name):
  with open(file_name, 'wb') as file:
    file.write(binary_data)
  print("[DATA] : The following file has been written to file: ", file_name)

# 5. BACA BLOB DATA (IMAGE)
def read_blob_data(entryID):
  try:
    conn = sqlite3.connect('app.db')
    conn.text_factory = str  
    cur = conn.cursor()
    print("[INFO] : Connected to SQLite to read_blob_data")
    sql_fetch_blob_query = """SELECT * from uploads where id = ?"""
    cur.execute(sql_fetch_blob_query, (entryID,))
    record = cur.fetchall()
    for row in record:
      converted_file_name = row[1]
      photo_binarycode  = row[2]
      # parse out the file name from converted_file_name
      last_slash_index = converted_file_name.rfind("/") + 1 
      png_index = converted_file_name.find('.png')
      final_file_name = converted_file_name[last_slash_index:] 
      write_to_file(photo_binarycode, final_file_name)
      print("[DATA] : Image successfully stored on disk. Check the project directory. \n")
    cur.close()
  except sqlite3.Error as error:
    print("[INFO] : Failed to read blob data from sqlite table", error)
  finally:
    if conn:
        conn.close()

# 6. AKSES FILE
def retrieve_file(entryID):
  try:
    conn = sqlite3.connect('app.db')
    conn.text_factory = str   # added in to get rid of "u must not use 8 bit blah blah"
    cur = conn.cursor()
    sql_retrieve_file_query = """SELECT * FROM Tanaman WHERE idTanaman = ?"""   
    cur.execute(sql_retrieve_file_query, (entryID,))
    record = cur.fetchone()
    record_blob = record[2]    
    read_blob_data(entryID)
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "how tf did u get here."

# 7. INISIALISASI TABLE
def createInitializeTable (conn) :
    sql_create_akun_user_table = """ CREATE TABLE IF NOT EXISTS Akun_User (
                                    idAkun INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    customerName VARCHAR(225) NOT NULL,
                                    email VARCHAR(225) NOT NULL,
                                    username VARCHAR(30) NOT NULL,
                                    passwordHash VARBINARY(50) NOT NULL,
                                    noTelp VARCHAR(15) NOT NULL,
                                    address VARCHAR(300) NOT NULL,
                                    postalCode INT NOT NULL
                                ); """

    sql_create_tanaman_table = """CREATE TABLE IF NOT EXISTS Tanaman (
                                    idTanaman INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    nama VARCHAR(50) NOT NULL,
                                    harga DOUBLE NOT NULL,
                                    stok INT NOT NULL,
                                    deskripsi TEXT NOT NULL,
                                    image BLOB NOT NULL,
                                    asal_kota VARCHAR(50) NOT NULL 
                                );"""

    sql_create_pemesanan_table = """ CREATE TABLE IF NOT EXISTS Pemesanan (
                                    orderNumber INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    idPelanggan BIGINT UNSIGNED NOT NULL,
                                    tanggalPemesanan DATETIME NOT NULL,
                                    FOREIGN KEY (idPelanggan) REFERENCES Akun_User (idAkun)
                                ); """

    sql_create_detail_pemesanan_table = """CREATE TABLE IF NOT EXISTS Detail_Pemesanan (
                                    orderNumberDetail INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    orderNumber BIGINT UNSIGNED NOT NULL,
                                    idTanaman BIGINT UNSIGNED NOT NULL,
                                    kuantitas INT NOT NULL,
                                    from_date DATE NOT NULL,
                                    until_date DATE NOT NULL,
                                    status_penyewaan VARCHAR(50) NOT NULL CHECK( status_penyewaan IN ('not submitted','waiting for approval','menunggu pembayaran'
                                    , 'lunas', 'sedang pengiriman', 'sedang masa sewa', 'masa sewa habis') ) NOT NULL DEFAULT 'not submitted',
                                    price DOUBLE,
                                    FOREIGN KEY (orderNumber) REFERENCES Pemesanan (orderNumber),
                                    FOREIGN KEY (idTanaman) REFERENCES Tanaman (idTanaman)
                                );
                                """
    
    create_table(conn, sql_create_akun_user_table)
    create_table(conn, sql_create_tanaman_table)
    create_table(conn, sql_create_pemesanan_table)
    create_table(conn, sql_create_detail_pemesanan_table)

# 8. INISIALISASI SELECT DATA
# Login
def login(conn, username, password):
    c = conn.cursor()
    passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest() # Ubah password jadi hashlib
    c.execute("SELECT idAkun FROM Akun_User WHERE username = ? AND passwordHash = ?", (username, passwordHash))
    try :
        row = c.fetchone()[0]
        if row is None:
            return ""
        else:
            return row
    except:
        return ""

# 9. INISIALISASI INSERT DATA
# Register
def register(conn, username, password, customerName, email, noTelp, address, postalCode):
    c = conn.cursor()
    c.execute("INSERT INTO Akun_User (username, passwordHash, customerName, email, noTelp, address, postalCode) VALUES (?, ?, ?, ?, ?, ?, ?)", (username, password, customerName, email, noTelp, address, postalCode))
    conn.commit()

# Input tanaman
def addTanaman(conn, Nama, Harga, Stok, Deskripsi, image, asal_kota):
    c = conn.cursor()
    c.execute("INSERT INTO Tanaman (nama, harga, stok, deskripsi, image, asal_kota) VALUES (?, ?, ?, ?, ?, ?)", (Nama, Harga, Stok, Deskripsi, image, asal_kota))
    conn.commit()

# Input pemesanan
def addPemesanan(conn, idPelanggan, tanggalPemesanan):
    c = conn.cursor()
    c.execute("INSERT INTO Pemesanan (idPelanggan, tanggalPemesanan) VALUES (?, ?)", (idPelanggan, tanggalPemesanan))
    conn.commit()

# Input detail pemesanan
def addDetailPemesanan(conn, orderNumber, idTanaman, kuantitas, from_date, until_date, status_penyewaan, price):
    c = conn.cursor()
    c.execute("INSERT INTO Detail_Pemesanan (orderNumber, idTanaman, kuantitas, from_date, until_date, status_penyewaan, price) VALUES (?, ?, ?, ?, ?, ?, ?)", (orderNumber, idTanaman, kuantitas, from_date, until_date, status_penyewaan, price))
    conn.commit()

# 10. INISIALISASI UPDATE DATA
# Edit tanaman
def editTanaman(conn, idTanaman, Nama, Harga, Stok, Deskripsi, image, asal_kota):
    c = conn.cursor()
    c.execute("UPDATE Tanaman SET nama = ?, harga = ?, stok = ?, deskripsi = ?, image = ?, asal_kota = ? WHERE idTanaman = ?", (Nama, Harga, Stok, Deskripsi, image, asal_kota, idTanaman))
    conn.commit()

# Update status
def updateStatus(conn, orderNumber, status_penyewaan):
    c = conn.cursor()
    c.execute("UPDATE Detail_Pemesanan SET status_penyewaan = ? WHERE orderNumber = ?", (status_penyewaan, orderNumber))
    conn.commit()

# 11. INISIALISASI VIEW DATA
# View pemesanan
def viewPemesanan(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS ViewPemesanan")
    c.execute("CREATE VIEW ViewPemesanan AS SELECT * FROM Pemesanan NATURAL JOIN Detail_Pemesanan")
    row = c.fetchall()
    return row

# View daftar tanaman
def viewTanaman(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS ViewTanaman")
    c.execute("CREATE VIEW ViewTanaman AS SELECT * FROM Tanaman WHERE idTanaman NOT IN (SELECT idTanaman FROM Tanaman WHERE stok = 0)")
    row = c.fetchall()
    return row

def fetchTanaman(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Tanaman WHERE idTanaman NOT IN (SELECT idTanaman FROM Tanaman WHERE stok = 0)")
    row = c.fetchall()
    return row

def blobToBase64(blob):
    return base64.b64decode(base64.b64encode(blob).decode('utf-8'))

# View detail tanaman
def viewDetailTanaman(conn, idTanaman):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS detailTanaman")
    c.execute("CREATE VIEW detailTanaman AS SELECT nama, image, deskripsi, stok, harga, asal_kota FROM Tanaman WHERE idTanaman = ?", (idTanaman,)) 
    row = c.fetchone()
    return row

# View daftar pesanan aktif
def viewPesananAktif(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS listPesananAktif")
    c.execute("CREATE VIEW listPesananAktif AS SELECT IdPelanggan, orderNumber, status_penyewaan, orderNumberDetail FROM ViewPemesanan WHERE orderNumberDetail NOT IN (SELECT orderNumberDetail FROM Detail_Pemesanan WHERE (status_penyewaan = 'not submitted' OR status_penyewaan = 'masa sewa habis'))")
    row = c.fetchall()
    return row

# View daftar keranjang
def viewKeranjang(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS listKeranjang")
    c.execute("CREATE VIEW listKeranjang AS SELECT p.idPelanggan AS IdPelanggan, p.orderNumber AS OrderNumber, nama, kuantitas, from_date, until_date, price, dp.idTanaman as idTanamans FROM Akun_User u, Tanaman t, Pemesanan p, Detail_pemesanan dp WHERE u.idAkun = p.idPelanggan AND p.orderNumber = dp.orderNumber AND t.idTanaman = dp.idTanaman AND status_penyewaan = 'not submitted'")
    row = c.fetchall()
    return row

def hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

# Get Data View Keranjang Table
def getKeranjang(conn, idPelanggan):
    c = conn.cursor()
    c.execute("SELECT * FROM listKeranjang WHERE IdPelanggan = ?", (idPelanggan,))
    return c.fetchall()

# Get Data View PesananAktif Table
def getPesananAktif(conn, idPelanggan):
    c = conn.cursor()
    c.execute("SELECT * FROM listPesananAktif WHERE IdPelanggan = ?", (idPelanggan,))
    return c.fetchall()

def getNamaUser(conn, idPelanggan) :
    c = conn.cursor()
    c.execute("SELECT customerName FROM Akun_User WHERE idAkun = ?", (idPelanggan,))
    return c.fetchone()[0]

# Update Remove Data Table
def removeDetailPemesanan(conn, idTanamans, jumlah, tanggalSewa, tanggalPengembalian, orderNumber) :
    c = conn.cursor()
    c.execute("DELETE FROM Detail_Pemesanan WHERE orderNumber = ? AND kuantitas = ? AND from_date = ? AND until_date = ? AND idtanaman = ? AND status_penyewaan = 'not submitted", (orderNumber,jumlah, tanggalSewa, tanggalPengembalian, idTanamans) )
    return c.fetchall()

# Testing
if __name__ == '__main__':
    database = r".\src\database\onlyplants.db"

    # create a database connection
    conn = create_connection(database)
    createInitializeTable(conn)

    # testing input data
    password = "testaja"
    passwordHash = hashlib.sha256(str(password).encode('utf-8')).hexdigest() # Ubah password jadi hashlib
    register(conn, "Test aja", "testaja@gmail.com", "testaja", passwordHash, "08123456789", "test address", 12345)
    password = "testaja2"
    passwordHash = hashlib.sha256(str(password).encode('utf-8')).hexdigest() # Ubah password jadi hashlib
    register(conn, "Test aja2", "testaja2@gmail.com", "testaja2", passwordHash, "081234567810", "test address2", 12346)
    password = "testaja"
    passwordHash = hashlib.sha256(str(password).encode('utf-8')).hexdigest() # Ubah password jadi hashlib
    register(conn, "Test aja3", "testaja3@gmail.com", "testaja3", passwordHash, "081234567811", "test address3", 12347)

    # insert data tanaman
    image = convertToBinaryData(r".\img\bonsai.jpg")
    addTanaman(conn, "bonsai", 100000, 10, "ini adalah bonsai", image, "jogja")
    image = convertToBinaryData(r".\img\lavender.jpg")
    addTanaman(conn, "lavender", 200000, 20, "ini adalah lavender", image, "jakarta")
    image = convertToBinaryData(r".\img\lily.jpg")
    addTanaman(conn, "lily", 300000, 30, "ini adalah lily", image, "bandung")
    image = convertToBinaryData(r".\img\sakura.jpg")
    addTanaman(conn, "sakura", 400000, 40, "ini adalah sakura", image, "surabaya")

    # insert data pemesanan
    addPemesanan(conn, 1, "2020-01-01")
    addPemesanan(conn, 1, "2020-01-02")
    addPemesanan(conn, 2, "2020-01-02")

    # Insert data detail pemesanan
    addDetailPemesanan(conn, 1, 1, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
    addDetailPemesanan(conn, 1, 2, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
    addDetailPemesanan(conn, 2, 3, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
    
    # Update status
    updateStatus(conn, 2, "waiting for approval")

    # Bikin view
    # view gabisa pake parameter
    #viewPemesanan(conn, 1)
    viewTanaman(conn)
    #viewDetailTanaman(conn, 1)
    #viewPesananAktif(conn)
    #viewKeranjang(conn, 1)

    conn.commit()
    conn.close()