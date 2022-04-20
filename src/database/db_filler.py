from db_api import *


if __name__ == "__main__":
  db = r".\src\database\onlyplants.db"
  conn = create_connection(db)
  createInitializeTable(conn)
  register(conn, "admin", hash("admin"), "Admin", "admin@onlyPlants.com", "08080808111", "Jalan Kenangan", 13242)
  register(conn, "Gagas", hash("gagas"), "Gagas Praharsa Bahar", "gagas@cust.com", "0801238405", "Jalan Bekasi", 29292)
  register(conn, "Dhika", hash("dhika"), "Andhika Arta Aryanto", "dhika@cust2.com", "08012384105", "Jalan Deket Kiara Artha", 29294)
  register(conn, "Rania", hash("rania"), "Gagas Praharsa Bahar", "rania@cust3.com", "08012383405", "Jalan BSD", 29293)
  register(conn, "Angel", hash("angel"), "Angelica Winasta Sinisuka", "angel@cust4.com", "08012384405", "Jalan Bandung", 29295)

  # insert data tanaman
  image = convertToBinaryData(r".\img\bonsai.jpg")
  addTanaman(conn, "Bonsai", 100000, 10, "Menurut buku ""Budidaya Bonsai"" yang ditulis oleh Iswarta Bima (2019), istilah bonsai merujuk pada bahasa Jepang, yakni bon yang berarti pot dan sai yang berarti tanaman. Dengan demikian, bonsai dapat diartikan sebagai tanaman yang dikerdilkan dan ditanam dalam pot.", image,"Jogja")
  image = convertToBinaryData(r".\img\lavender.jpg")
  addTanaman(conn, "Lavender", 200000, 20, "Lavender atau lavendel atau Lavandula adalah genus tumbuhan berbunga dalam suku Lamiaceae yang tersusun atas 25-30 spesies. Asal tumbuhan ini adalah dari wilayah selatan Laut Tengah sampai Afrika tropis dan ke timur sampai India—Dunia Lama. Genus ini termasuk tumbuhan menahun, tumbuhan dari jenis rumput-rumputan, semak pendek, dan semak kecil.",image, "Jakarta")
  image = convertToBinaryData(r".\img\lily.jpg")
  addTanaman(conn, "Lily", 300000, 30, "Lili adalah tumbuhan tahunan dengan tinggi 60–180 cm. Lili biasanya memiliki tangkai yang kokoh. Kebanyakan suku Lili membentuk umbi polos di bawah tanah. Di beberapa suku Amerika Utara, dasar dari umbi ini berkembang menjadi rizoma.", image,"Bandung")
  image = convertToBinaryData(r".\img\sakura.jpg")
  addTanaman(conn, "Sakura", 400000, 40, "Sakura (桜, 櫻) bersama dengan bunga seruni adalah bunga nasional Jepang yang mekar pada musim semi, yaitu sekitar akhir Maret hingga akhir Juni.", image,"Jepang")
  image = convertToBinaryData(r".\img\kaktus.jpg")
  addTanaman(conn, "Kaktus", 50000, 15, "Kaktus dapat tumbuh pada waktu yang lama tanpa air. Kaktus biasa ditemukan di daerah-daerah yang kering (gurun).[1] Kata jamak untuk kaktus adalah kakti. Kaktus memiliki akar yang panjang untuk mencari air dan memperlebar penyerapan air dalam tanah. Air yang diserap kaktus disimpan dalam ruang di batangnya. Kaktus juga memiliki daun yang berubah bentuk menjadi duri sehingga dapat mengurangi penguapan air lewat daun. ", image,"Afganistan")
  image = convertToBinaryData(r".\img\orchid.jpg")
  addTanaman(conn, "Orchid", 250000, 30, "Suku anggrek-anggrekan (bahasa Latin: Orchidaceae) merupakan satu suku tumbuhan berbunga dengan anggota jenis terbanyak. Jenis-jenisnya tersebar luas dari daerah tropika basah hingga wilayah sirkumpolar, meskipun sebagian besar anggotanya ditemukan di daerah tropika. Kebanyakan anggota suku ini hidup sebagai epifit, terutama yang berasal dari daerah tropika. Anggrek di daerah beriklim sedang biasanya hidup di tanah.", image,"Jakarta")
  image = convertToBinaryData(r".\img\rose.jpg")
  addTanaman(conn, "Mawar", 150000, 45, "Mawar adalah suatu jenis tanaman semak dari genus Rosa sekaligus nama bunga yang dihasilkan tanaman ini. Mawar liar terdiri dari 100 spesies lebih, kebanyakan tumbuh di belahan bumi utara yang berudara sejuk. Spesies mawar umumnya merupakan tanaman semak yang berduri atau tanaman memanjat yang tingginya bisa mencapai 2 sampai 5 meter. Walaupun jarang ditemui, tinggi tanaman mawar yang merambat di tanaman lain bisa mencapai 20 meter.", image,"London")
  image = convertToBinaryData(r".\img\sunflower.jpg")
  addTanaman(conn, "Sunflower", 50000, 10, "Bunga matahari (Helianthus annuus L.) adalah tumbuhan semusim dari suku kenikir-kenikiran (Asteraceae) yang populer, baik sebagai tanaman hias maupun tanaman penghasil minyak. Bunga tumbuhan ini sangat khas: besar, biasanya berwarna kuning terang, dengan kepala bunga yang besar (diameter bisa mencapai 30 cm).",image, "Uzbekistan")
  image = convertToBinaryData(r".\img\raflesiarnoldi.jpg")
  addTanaman(conn, "Raflesia Arnoldi", 10000000, 3, "Rafflesia adalah sebuah genus tumbuhan berbunga yang semua spesiesnya hidup sebagai parasit. Anatomi tumbuhan pada Rafflesia tidak lengkap. Organ tubuh dari Rafflesia hanya berbentuk bunga yang mekar atau kuncup saja. Rafflesia tidak memiliki bagian daun, batang dan akar.", image, "Bogor")
  image = convertToBinaryData(r".\img\lidahbuaya.jpg")
  addTanaman(conn, "Lidah Buaya", 10000, 500, "Lidah buaya (Aloe vera) adalah spesies tumbuhan dengan daun berdaging tebal dari genus Aloe. Tumbuhan ini bersifat menahun, berasal dari Jazirah Arab, dan tanaman liarnya telah menyebar ke kawasan beriklim tropis, semi-tropis, dan kering di berbagai belahan dunia. Tanaman lidah buaya banyak dibudidayakan untuk pertanian, pengobatan, dan tanaman hias, dan dapat juga ditanam di dalam pot.", image, "Sumba")
  image = convertToBinaryData(r".\img\jeruk.jpg")
  addTanaman(conn, "Jeruk", 30000, 10, "Jeruk atau limau adalah semua tumbuhan berbunga anggota marga Citrus dari suku Rutaceae (suku jeruk-jerukan). Anggotanya berbentuk pohon dengan buah yang berdaging dengan rasa masam yang segar, meskipun banyak di antara anggotanya yang memiliki rasa manis. Rasa masam berasal dari kandungan asam sitrat yang memang menjadi terkandung pada semua anggotanya.", image, "Klaten")
  image = convertToBinaryData(r".\img\kelapa.jpg")
  addTanaman(conn, "Kelapa", 40000, 50, "Kelapa atau nyiur (Cocos nucifera) adalah anggota tunggal dalam marga Cocos dari suku aren-arenan atau Arecaceae. Arti kata kelapa (atau coconut, dalam bahasa Inggris) dapat merujuk pada keseluruhan pohon kelapa, biji, atau buah, yang secara botani adalah pohon berbuah, bukan pohon kacang-kacangan. ", image, "Jonggol")
  image = convertToBinaryData(r".\img\melati.jpg")
  addTanaman(conn, "Melati", 57000, 15, "Melati merupakan tanaman bunga hias berupa perdu berbatang tegak yang hidup menahun. Melati merupakan genus dari semak dan tanaman merambat dalam keluarga zaitun (Oleaceae). Terdiri dari sekitar 200 spesies tumbuhan asli daerah beriklim tropis dan hangat dari Eurasia, Australasia dan Oseania, melati secara luas dibudidayakan untuk aroma khas bunganya yang harum. ", image, "Afrika")
  image = convertToBinaryData(r".\img\KembangSepatu.jpg")
  addTanaman(conn, "Kembang Sepatu", 50000, 20, "Kembang sepatu (bahasa Jawa: ꦏꦼꦩ꧀ꦧꦔ꧀ꦮꦺꦴꦫꦮꦫꦶ, translit. kêmbang worawari; bahasa Latin: Hibiscus rosa-sinensis L.) adalah tanaman semak suku Malvaceae yang berasal dari Asia Timur dan banyak ditanam sebagai tanaman hias di daerah tropis dan subtropis. Bunga besar, berwarna merah dan tidak berbau.", image, "Banten")
  image = convertToBinaryData(r".\img\kapas.jpg")
  addTanaman(conn, "Kapas", 20000, 30, "Kapas (dari bahasa Hindi kapas, sendirinya dari bahasa Sanskerta karpasa[1]) adalah serat halus yang menyelubungi biji beberapa jenis Gossypium (biasa disebut ""pohon""/tanaman kapas), tumbuhan 'semak' yang berasal dari daerah tropika dan subtropika. Di Pulau Ambon kapas dikenal dengan istilah lokal aha, dan dalam bahasa Banda disebut dengan karamboa.", image, "Bogor")

  # insert data pemesanan
  addPemesanan(conn, 1, "2020-01-01")
  addPemesanan(conn, 1, "2020-01-02")
  addPemesanan(conn, 2, "2020-01-02")

  # Insert data detail pemesanan
  addDetailPemesanan(conn, 1, 1, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
  addDetailPemesanan(conn, 1, 2, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)
  addDetailPemesanan(conn, 2, 3, 10, "2020-01-01", "2020-01-02", "not submitted", 100000)