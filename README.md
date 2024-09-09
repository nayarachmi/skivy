Link PWS: [http://naya-kusumahayati-skivy.pbp.cs.ui.ac.id/](http://naya-kusumahayati-skivy.pbp.cs.ui.ac.id/)

## Membuat Proyek Django Baru
Untuk memulai proyek Django baru, langkah pertama adalah membuka command prompt dan menavigasi ke direktori di mana saya ingin membuat proyek tersebut. Setelah berada di direktori yang diinginkan, saya membuat proyek baru dengan menjalankan perintah `django-admin startproject skivy`. Perintah ini akan membuat sebuah direktori baru dengan nama `skivy`, yang berisi struktur dasar proyek Django termasuk pengaturan utama, konfigurasi URL, dan skrip manajemen proyek. 

## Membuat Aplikasi Main
Untuk membuat aplikasi baru di dalam proyek Django yang sudah dibuat, langkah pertama adalah menavigasi ke direktori proyek tersebut. Saya melakukan ini dengan membuka command prompt dan menggunakan perintah `cd skivy` untuk berpindah ke direktori `skivy`. Setelah berada di dalam direktori proyek, saya membuat buat aplikasi baru dengan menjalankan perintah berikut:

```bash
python manage.py startapp main
```

Perintah ini akan membuat sebuah direktori baru bernama `main` di dalam proyek, yang berisi komponen penting seperti `models.py`, `views.py`, `urls.py`, dan lain-lain yang dibutuhkan untuk mengembangkan fitur spesifik dalam aplikasi. Aplikasi ini akan berfungsi sebagai bagian modular dari proyek yang menangani fungsionalitas tertentu, dan nantinya dapat diintegrasikan dengan keseluruhan proyek melalui konfigurasi di `settings.py` dan routing di `urls.py`.

## Melakukan Routing
Untuk melakukan routing di proyek Django, langkah pertama adalah memastikan aplikasi yang baru dibuat sudah terdaftar di dalam pengaturan proyek. Buka file `settings.py` yang ada di direktori proyek `skivy`, lalu tambahkan nama aplikasi `'main'` ke dalam daftar `INSTALLED_APPS`. Ini memungkinkan Django untuk mengenali aplikasi dan memuatnya sebagai bagian dari proyek.

Setelah itu, saya mengatur routing agar aplikasi dapat diakses melalui URL. Buka file `urls.py` yang ada di direktori proyek `skivy`, dan tambahkan routing untuk aplikasi `main` dengan menggunakan fungsi `include()`. Misalnya, tambahkan kode berikut di `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]
```

Dengan menambahkan `include('main.urls')`, saya mengarahkan Django untuk mencari pola URL tambahan di dalam file `urls.py` aplikasi `main`. Langkah ini memastikan bahwa permintaan yang diterima oleh server akan diarahkan ke aplikasi yang tepat berdasarkan URL yang diminta, memungkinkan setiap aplikasi dalam proyek untuk mengatur rute mereka secara mandiri.

### Membuat Model Product dalam Main
Untuk membuat model `Product` dalam aplikasi Django, pertama-tama buka file `models.py` yang berada dalam folder aplikasi Anda. Di dalam file tersebut, tambahkan model `Product` dengan mendefinisikan atribut-atribut yang diperlukan, seperti `name`, `price`, dan `description`. Contohnya, model saya definisikan sebagai berikut:

```python
from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    skin_type = models.CharField(max_length=20)

    @property
    def is_recommended_for_sensitive_skin(self): #ganti
        return 'sensitive' in self.skin_type.lower()
```

Setelah model ditambahkan, simpan perubahan pada file `models.py`. Langkah selanjutnya adalah menjalankan perintah migrasi untuk menerapkan perubahan tersebut ke database. Jalankan perintah `python manage.py makemigrations` untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada model. Kemudian, jalankan perintah `python manage.py migrate` untuk menerapkan migrasi dan membuat tabel `Product` di database.

### Membuat Fungsi pada Views.py
Untuk menambahkan fungsi pada file `views.py`, Saya melakukan beberapa langkah. Pertama, membuka file `views.py` yang sudah ada di proyek Django. File tersebut sudah berisi fungsi `show_main`, ubah kode sesuai kebutuhan web seperti berikut:

```python
from django.shortcuts import render

def show_main(request):
    context = {
        'price': '100.000',
        'name': 'Hatomugi Toner',
        'description': 'A Hydrating Toner',
        'skin_type': 'All Skin Type'
    }

    return render(request, "main.html", context)

```

Fungsi `show_main` tersebut sudah disiapkan untuk mengirimkan data ke template `main.html`. Data yang dikirimkan termasuk `price`, `name`, `description`, dan `skin_type`. Fungsi ini mengatur konteks yang berisi informasi produk dan menggunakan fungsi `render` untuk merender template `main.html` dengan konteks tersebut.

### Membuat Routing pada URLs.py di Main
Untuk mengatur routing di aplikasi Django, Saya membuat file `urls.py` di dalam folder aplikasi `main`. Berikut adalah langkah-langkahnya:

1. **Membuat File `urls.py` di Folder `main`:** Jika file `urls.py` belum ada, buat file baru bernama `urls.py` di dalam folder aplikasi `main`.

2. **Menambahkan Kode yang Mengatur Rute URL dengan `main`:** Setelah file `urls.py` dibuat, tambahkan kode berikut untuk mengatur routing URL:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.show_main, name='show_main'),
   ]
   ```

   Kode ini mengimpor fungsi `path` dari modul `django.urls` dan mengimpor `views` dari folder `main`. Selanjutnya, variabel `urlpatterns` didefinisikan untuk menyimpan daftar rute URL yang diatur untuk aplikasi ini. Dalam contoh ini, rute URL kosong (`''`) akan memanggil fungsi `show_main` yang ada di `views.py`. Rute ini juga diberi nama `'show_main'` untuk memudahkan referensi dalam aplikasi Anda.

3. **Menyertakan `urls.py` Main di File `urls.py` Proyek Utama:** Terakhir, pastikan rute dari aplikasi `main` disertakan dalam rute proyek utama. Buka file `urls.py` di folder proyek utama (biasanya terletak di folder yang berisi `settings.py`) dan tambahkan kode berikut jika belum ada:

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('main.urls')),  # Menyertakan rute aplikasi 'main'
   ]
   ```

### Melakukan Deployment ke PWS
1. **Menambahkan URL Deployment PWS ke `ALLOWED_HOSTS`:**  
   Pertama, buka file `settings.py` di proyek Django. Temukan bagian `ALLOWED_HOSTS` dan tambahkan URL deployment PWS ke dalam daftar. Pastikan URL ditulis dalam bentuk string. Contoh penyesuaian:

   ```python
   ALLOWED_HOSTS = [.., 'naya-kusumahayati-skivy.pbp.cs.ui.ac.id']
   ```

2. **Menambahkan Remote PWS dan Melakukan Push:**
   - Tambahkan remote baru untuk PWS dengan perintah berikut:
     ```bash
     git remote add pws http://pbp.cs.ui.ac.id/naya.kusumahayati/skivy
     ```
   - Mengubah cabang main menjadi master
     ```bash
     git branch -m master
     ```
   - Lakukan push ke remote PWS pada cabang yang sesuai:
     ```bash
     git push pws master
     ```
   - Ubah kembali cabang menjadi main
     ```bash
     git branch -m main
     ```

## Bagan Request Client ke Web
![image](https://github.com/user-attachments/assets/9d1333f3-1884-4e9b-beb0-a82ffe8eb679)
1. User/Client mengirimkan permintaan ke server melalui URL
2. urls.py digunakan untuk menentukan view mana yang harus menangani permintaan tersebut
3. View menjalankan logika yang diperlukan sepertiberinteraksi dengan models.py untuk mengambil data dari database
4. View merender template HTML dengan data yang diperoleh dan menyiapkan respon
5. Template kemudian dikirimkan kembali sebagai respon HTML yang ditampilkan di browser sebagai website

## Fungsi Git dalam Pengembangan Perangkat Lunak
1. Git memudahkan pengguna melacak perubahan kode yang sudah terjadi; pengguna dapat dengan mudah kembali ke versi kode sebelumnya jika dibutuhkan.
2. Git memungkinkan banyak pengguna bekerja pada satu proyek yang sama.
3. Git memudahkan backup kode karena kode disimpan di server remote.
4. Git memungkinkan pengguna membuat alur pengembangan yang terpisah tanpa mengganggu kode di cabang utama.

## Alasan Mengapa Framework Django Dijadikan Permulaan Pembelajaran
1. Banyak fitur yang sudah disediakan di awal sehingga pengguna tidak perlu melakukan banyak konfigurasi tambahan (pemula friendly).
2. Struktur proyek jelas dan terorganisir.
3. Komunitas yang dimiliki besar dan aktif sehingga banyak dukungan yang dapat membantu jika menemukan masalah.

## Mengapa Model pada Django Disebut sebagai ORM (Object Relational Mapping)
1. Karena fungsinya untuk memetakan objek di aplikasi ke tabel dalam database.
2. Dalam Django, setiap model Python merepresentasikan tabel di database dan tiap atribut dalam model merepresentasikan kolom di tabel.
