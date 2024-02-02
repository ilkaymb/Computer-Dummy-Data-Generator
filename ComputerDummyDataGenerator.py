import mysql.connector
from faker import Faker
import random

# Veritabanı bağlantısını kurun
db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="database"
)

cursor = db.cursor()
fake = Faker()

for i in range(500):  # 200 sahte bilgisayar kaydı oluşturun
    brand = fake.company()
    model = fake.word()
    processor = fake.word()
    ram_capacity = random.randint(4, 64)  # Rastgele RAM kapasitesi
    storage_capacity = random.randint(128, 1024)  # Rastgele depolama kapasitesi (GB)
    price = round(random.uniform(300, 2000), 2)  # Rastgele fiyat
    image_path = f"/assets/computer-image{i % 5 + 1}.svg"  # 1 ila 10 arası rasgele sıralama

    # Bilgisayar verilerini tabloya ekleyin
    cursor.execute("INSERT INTO products_computer (brand, model, processor, ram_capacity, storage_capacity, price,image_path) VALUES (%s, %s, %s, %s, %s, %s,%s)",
                   (brand, model, processor, ram_capacity, storage_capacity, price,image_path))

# Değişiklikleri kaydet
db.commit()

# Veritabanı bağlantısını kapat
db.close()
