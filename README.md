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

class Product(models.Model):
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
from .models import Product # type: ignore

def show_main(request):
    context = {
        'npm': '2306230685',
        'name': 'Naya Kusumahayati Rachmi',
        'class': 'PBP B',
        'store_name': 'Skivy',
    }

    return render(request, "main.html", context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main.html', context)

```

Fungsi `show_main` tersebut sudah disiapkan untuk mengirimkan data ke template `main.html`. Data yang dikirimkan termasuk `npm`, `name`, `class`, dan `store_name`. Fungsi ini mengatur konteks yang berisi informasi utama web dan menggunakan fungsi `render` untuk merender template `main.html` dengan konteks tersebut.

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
3. View menjalankan logika yang diperlukan seperti berinteraksi dengan models.py untuk mengambil data dari database
4. View merender template HTML dengan data yang diperoleh dan menyiapkan respon
5. Template kemudian dikirimkan kembali sebagai respon HTML yang ditampilkan di browser sebagai website
> Kaitan antara `urls.py`,`views.py`,`models.py`,`html`
>> `urls.py`: Menentukan rute URL dan mengarahkan permintaan pengguna ke view yang sesuai
>> 
>> `views.py`: Mengandung logika aplikasi. Menerima permintaan dari urls.py, memproses data, dan berinteraksi dengan model (models.py)
>> 
>> `models.py`: Mendefinisikan struktur data dan berinteraksi dengan database. Digunakan oleh view untuk mengambil atau mengubah data
>> 
>> `html`: Merender data dari view menjadi halaman HTML yang siap dikirim ke pengguna

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

## Membuat Input Form Untuk Menambahkan Objek Model
Pertama, saya membuat input form untuk menambahkan objek ke dalam database. Saya memastikan model yang akan digunakan sudah tersedia di file `models.py`. Setelah model siap, saya membuat form di `forms.py` menggunakan Django ModelForm yang secara otomatis menghubungkan form dengan model yang ada. Selanjutnya di file `views.py` saya membuat fungsi untuk menangani form ini, fungsi berfungsi untuk memeriksa apakah request adalah POST (untuk menyimpan data) atau GET (untuk menampilkan form). Jika form valid, objek baru akan disimpan ke database. Setelah itu menambahkan berkas HTML baru dengan nama `create_product_entry` dan menambahkan token CSRF yang berfungsi sebagai perlindungan form dari serangan keamanan.

## Menambahkan 4 Fungsi Views untuk Menampilkan Objek dalam Format XML & JSON
Setelah berhasil membuat input form dan menambahkan objek ke dalam database, tahap berikutnya adalah membuat empat fungsi views yang akan menampilkan objek yang sudah ditambahkan dalam format XML dan JSON. Saya mengambil semua data dari database menggunakan `Product.objects.all()`, lalu menggunakan `serialize('json', data)` untuk mengubah data menjadi JSON dan mengembalikannya sebagai response. Hal yang sama berlaku untuk format XML.  Untuk menampilkan objek tertentu berdasarkan ID, fungsi ini menggunakan query `Product.objects.filter(pk=id)` untuk mengambil data spesifik berdasarkan primary key (ID). Setelah itu, data diubah ke format XML. dan JSON.

## Membuat Routing URL untuk Masing-Masing Views
Setelah menambahkan fungsi views untuk menampilkan data dalam format XML dan JSON, baik untuk semua objek maupun berdasarkan ID, langkah selanjutnya adalah menambahkan routing URL di file `urls.py`. 

```python


urlpatterns = [
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'), 
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

Penjelasan:
- **`path('xml/', show_xml, name='show_xml')`**: Mengarahkan URL `xml/` ke view `show_xml` yang menampilkan semua objek dalam format XML.
- **`path('json/', show_json, name='show_json')`**: Mengarahkan URL `json/` ke view `show_json` yang menampilkan semua objek dalam format JSON.
- **`path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id')`**: Mengarahkan URL seperti `xml/1/` ke view `show_xml_by_id`, yang menampilkan objek berdasarkan ID dalam format XML. Parameter ID diambil sebagai string (`<str:id>`).
- **`path('json/<str:id>/', show_json_by_id, name='show_json_by_id')`**: Mengarahkan URL seperti `json/1/` ke view `show_json_by_id`, yang menampilkan objek berdasarkan ID dalam format JSON.

Dengan pengaturan ini, setiap URL sudah terhubung dengan fungsi view yang sesuai, memungkinkan kita untuk mengakses data produk dalam format yang diinginkan, baik secara keseluruhan atau berdasarkan ID tertentu.

### Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?
Data delivery sangat penting dalam pengimplementasian platform karena merupakan mekanisme yang memungkinkan pertukaran informasi antara klien dan server. Platform modern umumnya membutuhkan data yang dinamis, seperti permintaan user, input dari form, atau informasi real-time yang terus diperbarui. Data delivery membantu memastikan bahwa informasi ini dapat dikirim dari sisi klien ke server (misalnya, untuk menyimpan data pengguna ke dalam database), dan dari server ke klien (misalnya, untuk menampilkan konten yang diminta). Dengan pengiriman data yang efisien, platform dapat berfungsi dengan baik, memungkinkan interaksi pengguna yang lancar, pemrosesan data yang cepat, dan komunikasi antara berbagai komponen platform.

### Mana yang Lebih Baik Antara XML dan JSON? Mengapa JSON Lebih Populer Dibandingkan XML?
Dalam perbandingan antara XML dan JSON, JSON umumnya dianggap lebih baik dan lebih populer di dunia modern, terutama untuk aplikasi web. JSON lebih sederhana, ringan, dan mudah dibaca baik oleh manusia maupun mesin. JSON lebih efisien dalam hal penggunaan ruang, karena tidak memerlukan tag penutup seperti XML, yang membuat ukuran datanya lebih kecil. Di sisi lain, XML lebih kompleks dan biasanya digunakan untuk data yang lebih terstruktur dan membutuhkan elemen-elemen yang lebih fleksibel dan dapat diatur, seperti metadata. Meskipun XML masih digunakan dalam beberapa aplikasi spesifik, JSON lebih populer karena lebih mudah diintegrasikan dengan aplikasi web modern, dan API.

### Fungsi dari Method `is_valid()` pada Form Django dan Mengapa Kita Membutuhkannya?
Method `is_valid()` dalam form Django digunakan untuk memeriksa apakah data yang dimasukkan pengguna ke dalam form memenuhi semua aturan validasi yang ditentukan dalam form tersebut. Saat metode ini dipanggil, Django akan melakukan serangkaian pengecekan, seperti memastikan data yang diinput sesuai dengan tipe yang diharapkan, wajib diisi (jika required), atau mematuhi batasan lainnya yang telah ditetapkan di form atau model. Jika semua validasi terpenuhi, method ini akan mengembalikan nilai True, yang berarti data tersebut dapat diproses lebih lanjut (seperti disimpan ke database). Kita memerlukan `is_valid()` untuk memastikan bahwa aplikasi tidak menerima data yang tidak valid atau berpotensi merusak sistem, yang dapat menyebabkan error atau gangguan pada platform.

### Mengapa Kita Membutuhkan `csrf_token` Saat Membuat Form di Django? Apa yang Dapat Terjadi Jika Tidak Menambahkan `csrf_token`?
CSRF (Cross-Site Request Forgery) adalah jenis serangan di mana penyerang mencoba membuat pengguna yang sudah login melakukan aksi yang tidak diinginkan tanpa sepengetahuan mereka. Token CSRF adalah mekanisme keamanan yang ditambahkan Django untuk memastikan bahwa form yang dikirim berasal dari sumber yang sah, yakni dari aplikasi itu sendiri, bukan dari sumber eksternal yang berbahaya. Jika kita tidak menambahkan `csrf_token` pada form Django, aplikasi menjadi rentan terhadap serangan CSRF. Dengan menggunakan `csrf_token`, kita melindungi aplikasi dari serangan ini, karena setiap form yang sah akan menyertakan token unik yang harus cocok dengan token yang dihasilkan oleh server.

## Tampilan Postman
![image](https://github.com/user-attachments/assets/b0625deb-a850-4bc1-a5a5-a0667233520b)
![image](https://github.com/user-attachments/assets/294064a7-3192-4acd-9af6-878d3b9f08dc)
