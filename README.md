Link PWS: [http://naya-kusumahayati-skivy.pbp.cs.ui.ac.id/](http://naya-kusumahayati-skivy.pbp.cs.ui.ac.id/)

# Tugas 2
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

# Tugas 3
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
### XML
![image](https://github.com/user-attachments/assets/b0625deb-a850-4bc1-a5a5-a0667233520b)
### XML by ID
![image](https://github.com/user-attachments/assets/bf15623d-9c92-4e05-a112-47ede394acd1)
### JSON
![image](https://github.com/user-attachments/assets/294064a7-3192-4acd-9af6-878d3b9f08dc)
### JSON by ID
![image](https://github.com/user-attachments/assets/7f843c3c-d901-4cc0-9869-35f27946536c)

# Tugas 4
## Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()` : Fungsi bawaan Django yang memberitahu browser untuk melakukan redirect ke URL yang diberikan
`redirect()` : Shortcut yang lebih ringkas dan fleksibel. Selain URL, fungsi ini juga dapat menerima nama URL pattern atau model object

Kesimpulannya, `redirect()` lebih fleksibel karena dapat menerima nama URL, objek, maupun URL string langsung, sedangkan `HttpResponseRedirect()` hanya bisa menerima URL string.

## Cara Kerja Penghubungan Model `Product` dengan `User`
Untuk menghubungkan model `Product` dengan model `User` di Django, biasanya digunakan relasi ForeignKey. Misalkan, jika produk dimiliki oleh pengguna, kita bisa membuat hubungan one-to-many antara User dan Product. Contoh implementasinya adalah sebagai berikut:

```python
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    skin_type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Field `user` pada model tersebut menggunakan ForeignKey, yang menunjukan bahwa setiap profuk dimiliki oleh satu pengguna, tetapi seorang penggunda dapat memiliki banyak produk.

## Perbedaan antara Authentication dan Authorization
- Authentication: Proses yang memverifikasi identitas pengguna, misalnya dengan username dan password. Jika berhasil, pengguna akan dianggap sebagai pengguna yang sah. Dilakukan menggunakan fungsi seperti `authenticate()` untuk memverifikasi kredensial pengguna, dan `login()` untuk membuat sesi pengguna yang telah terautentikasi
- Authorization: Proses menentukan hak akses pengguna yang telah terautentikasi. Setelah berhasil login, Django akan menentukan apakah pengguna memiliki izin untuk melakukan aktivitas atau mengakses sumber tertentu. Dilakukan dengan mengecek apakah pengguna memiliki izin tertentu melalui mekanisme permissions atau groups di Django. Django juga memiliki decorators seperti `@login_required`

## Bagaimana Django Mengingat Pengguna yang Telah Login? Kegunaan Lain dari Cookies dan Apakah Semua Cookies Aman Digunakan?
Django mengingat pengguna yang telah login melalui mekanisme session. Saat pengguna berhasil login, Django akan membuat entri sesi di server (biasanya disimpan dalam database) dan mengirimkan cookie sesi ke browser pengguna. Cookie ini berisi ID sesi, yang nantinya akan digunakan oleh Django untuk mengidentifikasi pengguna di setiap request berikutnya.

Setiap kali pengguna melakukan request, browser mengirimkan cookie ini, dan Django memeriksa ID sesi untuk mendapatkan detail pengguna yang terkait.

## Kegunaan Lain dari Cookies
- Iklan dan analitik: Untuk melacak aktivitas pengguna di situs atau bahkan lintas situs
- Pelacakan preferensi: Misalnya, untuk menyimpan preferensi tampilan atau pengaturan situs pengguna
- Pelacakan sesi pengguna: Seperti untuk mengingat item yang ditambahkan ke keranjang belanja dalam aplikasi e-commerce

## Keamanan Cookies
Tidak semua cookie aman, ada beberapa faktor yang mempengaruhi keamanan cookies:
- HttpOnly flag: Cookies dengan HttpOnly flag tidak dapat diakses oleh JavaScript, sehingga mengurangi risiko serangan XSS (Cross-Site Scripting)
- Sesi Expiry: Cookies harus memiliki waktu kedaluwarsa yang wajar untuk menghindari penggunaan yang terlalu lama
- Cookie harus dienkripsi: Cookie yang berisi informasi sensitif seperti sesi pengguna harus dienkripsi untuk mencegah pencurian data
- Secure flag: Cookies harus dikirim melalui koneksi HTTPS dengan menggunakan `Secure` flag

## Mengimplementasikan Fungsi Registrasi, Login, dan Logout
Pertama, saya menambahkan fungsi Register pada file `views.py`, fungsi tersebut berfungsi untuk menghasilkan form registrasi secara otomatis dan membuat akun pengguna ketika data di submit dari form.

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Lalu membuat berkas HTML baru dengan nama `register.html`. Tidak lupa untuk mengimpor fungsi register yang sudah dibuat tadi pada file `urls.py` dan menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor

Berikutnya, untuk membuat fungsi Login, pertama saya mengimpor `authenticate`, `login`,dan `AuthenticationForm` pada file `views.py`. Lalu pada file yang sama menambahkan fungsi `login_user`.

```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Setelahnya saya membuat berkas HTML baru dengan nama `login.html`. Tidak lupa untuk mengimpor fungsi login_user yang sudah dibuat tadi pada file `urls.py` dan menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor

Terakhir, untuk membuat fungsi logout yang saya lakukan kurang lebih sama dengan sebelumnya, pertama saya mengimpor `logout` pada file `views.py`, lalu saya menambahkan fungsi `logout_user()` ke dalam file yang sama

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Lalu saya menambahkan potongan kode berikut pada file `main.html`
```HTML
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
Tidak lupa untuk mengimpor fungsi logout_user yang sudah dibuat tadi pada file `urls.py` dan menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor

## Membuat 2 Akun Pengguna dengan 3 Dummy Data
Saya menjalankan program terlebih dahulu dengan perintah
```python
python manage.py runserver
```
Setelah itu melakukan registrasi untuk membuat akun, Setelah registrasi selesai, saya login menggunakan akun tersebut dan melakukan aksi menambahkan product entry dengan menekan tombol `Add New Product Entry` setelah itu memasukkan data produk dan menekan tombol `Add Product Entry`. Melakukan hal yang sama sampai berhasil membuat 3 dummy data di masing-masing akun

## Menghubungkan Model `Product` dengan `User`
Pertama saya mengimpor model pada file `models.py`
```python
from django.contrib.auth.models import User
```
lalu pada model `Product` yang sudah ada pada file tersebut, menambahkan user 
```python
class Product(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Setelah itu saya mengubah potongan kode pada fungsi `create_product_entry` pada file `views.py` dan mengubah value dari `product_entries` dan `context` pada `show_main` menjadi seperti berikut
```python
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
...
```
Hal tersebut berfungsi untuk menampilkan objek `product_entries` sesuai dengan yang terasosiasi atau terhubung dengan user yang sedang login. Terakhir, tidak lupa untuk melakukan migrasi model dengan perintah
```python
manage.py makemigrations
manage.py migrate
```

## Menampilkan Detail Informasi User yang sedang Logged In seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
Untuk menampilkan detail informasi user yang sedang login, hal pertama yang saya lakukan ialah mengimpor `HttpResponseRedirect`, `reverse`, dan `datetime` pada file `views.py`. Lalu pada fungsi `login_user` tambahkan cookie dengan nama `last_login` untuk menampilkan kapan terakhir kali user melakukan login dengan cara mengubah kode pada bagian `if form.is_valid()` menjadi berikut
```python
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
Lalu berikutnya pada fungsi `show_main` menambahkan potongan kode `last_login`
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```
Setelah itu mengubah fungsi `logout_user` untuk menghapus cookie `last_login` saat pengguna melakukan logout
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Selanjutnya menambahkan kode HTML untuk menampilkan keterangan terakhir login milik user pada file `main.html`
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

# Tugas 5
## Urutan Prioritas CSS Selector
1. **Inline Styles:** Gaya yang diterapkan langsung pada elemen HTML dengan atribut `style`
``` HTML
<div style="color: black;">Hello, Everyone!</div>
```
2. **ID Selector:** Selector yang menggunakan ID, diawali dengan `#`
``` CSS
#myId {
    color: black;
}
```
3. **Class Selector, Attribute Selector, Pseudo-class:** Selector ini diawali dengan `.`(class), `[attribute]`, atau menggunakan pseudo-class
``` CSS
.myClass {
    color: black;
}
```
4. **Element Selector & Pseudo-element:** Selector yang langsung menargetkan elemen HTML dan pseudo-element
``` CSS
div {
    color: black;
}
``` 
5. **Universal Selector:** elector yang menargetkan semua elemen, ditulis dengan `*`
``` CSS
* {
    color: black;
}
```

## Pentingnya Responsive Design
Responsive design adalah pendekatan dalam pengembangan web yang bertujuan untuk membuat situs web terlihat baik dan berfungsi dengan baik di berbagai perangkat, baik desktop maupun mobile. Ini penting karena:
1. Pengalaman Pengguna: Membuat situs web yang mudah digunakan di berbagai perangkat meningkatkan pengalaman pengguna
2. Search Engine Optimiziation: Google lebih menyukai situs web yang responsif dalam hasil pencariannya
3. Aksesibilitas: Memastikan konten dapat diakses oleh lebih banyak pengguna di berbagai perangkat

### Contoh Aplikasi
- Yang sudah menerapkan Responsive Design: Google, Twitter (X), Instagram
- Yang belum menerapkan Responsive Design: Blog tua yang tidak menggunakan framework modern, dan beberapa situs web pemerintah daerah yang tidak dioptimalkan untuk perangkat mobile

## Perbedaan antara Margin, Border, dan Padding
- **Margin:** Ruang diluar elemen atau jarak antara elemen tersebut dan elemen lain di sekitarnya. Dapat diatur dengan menggunakan properti `margin`
``` CSS
.myElement {
    margin: 20px; /* Jarak luar 20px */
}
```
- **Border:** Garis yang mengelilingi elemen. Dapat diatur dengan menggunakan properti `border`
``` CSS
.myElement {
    border: 2px solid black; /* Border 2px, solid, berwarna hitam */
}
```
- **Padding:** Ruang di dalam elemen, antara konten dan border. Dapat diatur dengan menggunakan properti `padding`
``` CSS
.myElement {
    padding: 10px; /* Ruang dalam 10px */
}
```

## Konsep Flexbox dan Grid Layout
- **Flexbox:** Flexible Box Layout adalah model layout yang dirancang untuk mengatur elemen dalam satu dimensi (baris atau kolom). Ini memungkinkan elemen untuk dapat tumbuh, menyusut, dan beradaptasi dengan ruang yang tersedia. Sangat cocok untuk tata letak yang responsif, seperti menu navigasi dan form
``` CSS
.container {
    display: flex;
    justify-content: space-between; /* Mengatur jarak antar elemen */
}
```

- **Grid Layout:** Grid layout adalah model layout yang memungkinkan pengaturan elemen dalam dua dimensi (baris dan kolom). Ini memungkinkan pembagian ruang yang lebih kompleks dan terstruktur. Cocok untuk tata letak yang lebih kompleks, seperti layout halaman penuh dengan banyak elemen
``` CSS
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Membagi grid menjadi 3 kolom */
}
```
## Implementasi Fungsi Delete dan Edit Product
Pada file `views.py` membuat fungsi baru `edit_product()` dengan parameter `request` dan `id` lalu menambahkan import
``` python
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect

...
def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=product) #hmmmm

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```
Lalu membuat file HTML `edit_product.html` untuk tampilan pada page edit product
```HTML
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Mood</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Mood"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Tak lupa untuk mengimport fungsi yang baru dibuat dan menambahkan path URL pada file `urls.py`. Setelah itu, pada file `main.html` menambahkan kode berikut agar menampilkan tombol edit
``` HTML
...
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
</tr>
...
```
Selanjutnya, untuk menambahkan fitur hapus product, saya melakukan hal yang kurang lebih sama seperti pada edit product. Pertama, saya membuat fungsi `delete_product()` dengan parameter `request` dan `id` 
``` python
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
Tidak lupa untuk mengimport fungsi tersebut dan menambahkan path URL pada file `urls.py`. Setelah itu, pada file `main.html` menambahkan kode berikut agar menampilkan tombol hapus
``` HTML
...
<tr>
    ...
    <td>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
</tr>
...
```
## Kustomisasi Halaman Login, Register, dan Tambah Product
### Login
Pada halaman Login saya menempatkan semuanya di tengah halaman dengan elemen utama sebuah div di tengah layar dan logo diatasnya. Menggunakan desain yang bersih dan modern dengan background `pink-100` dan form login berwarna putih. Pada tombol `Sign In` menggunakan kelas tailwind CSS dengan efek hover. Kode lengkapnya dapat dilihat pada file `login.html`
> Tampilan Login Page
![image](https://github.com/user-attachments/assets/002881b8-c285-49dd-902f-db923ce08ac0)

### Register
Menggunakan div utama dengan kelas `min-h-screen` untuk memposisikan form di tengah layar. Elemen form dibungkus dalam sebuah div lalu memberikan efek shadow dan border berwarna pink serta radius yang membuat sudutnya melengkung. Tombol `Submit` juga diberikan efek agar ketika hover warna berubah. Kode lengkapnya dapat dilihat pada file `register.html`
> Tampilan Register Page
![image](https://github.com/user-attachments/assets/51fbc946-76ac-4bed-ac87-f7ea7d1a37ca)

### Tambah Product
Menyertakan template navigation bar `navbar.html` pada bagian atas. Tema halaman menyesuaikan dengan tema tema sebelumnya, dengan desain dan efek yang kurang lebih sama. Tombol pun menggunakan efek yang jika di hover berubah warna
> Tampilan Page Add Product
![image](https://github.com/user-attachments/assets/e89cd91c-d8fb-4124-b7bb-0fffc8780b91)

## Kustomisasi Halaman Daftar Produk
Menggunakan Tailwind CSS dengan layout yang responsif dan rapi menggunakan grid, dan shadow. Produk ditampilkan dalam grid yang rapi dan minimalis dan dalam bentuk card dengan tombol delete dan edit, namun jika belum ada product maka akan ditambilkan gif dengan ekspresi sedih dan keterangan bahwa belum ada produk
> Tampilan Page Product
![image](https://github.com/user-attachments/assets/448a91db-1de8-4df9-a4c4-2fe540dbe760)
> Tampilan Page Product tanpa Product
![image](https://github.com/user-attachments/assets/5dd28802-77ab-46ab-ae5a-590ddda4da76)

## Kustomisasi Card Product
Tampilan kartu produk yang berfungsi untuk menampilkan tiap keterangan pada produk yang dilengkapi dengan tombol hapus dan edit. Elemen pada div utama memiliki class yang mengatur layout dan efek seperti shadow, border, dan efek hover yang memperbesar kartu sedikit dengan transisi 300ms. Lalu saya juga memastikan kartu tidak pecah saat tampil dalam kolom dengan `break-inside-avoid`. Pada kartu produk menampilkan Nama produk yang ditampilkan dalam `<h3>`, deskripsi produk menggunakan `<p>` dan harga produk yang ditampilkan dengan warna berbeda. Lalu saya juga membuat tombol edit dan hapus menggunakan ikon dan warna yang cerah. Tombol hapus akan mengarahkan pengguna ke URL untuk menghapus produk, Tombol edit akan mengarahkan pengguna ke page lain untuk mengedit produk
``` HTML
<!-- Action Buttons (Edit, Delete) -->
    <div class="flex justify-between items-center p-4 border-t border-gray-200">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
```

## Navigation Bar
Pertama, saya membuat berkas HTML baru yaitu `navbar.html` lalu saya mengisinya dengan kode untuk tampilan navigation bar yang saya inginkan dengan logo pada kiri atas dan greeting user serta tombol logout di kanan
``` HTML
{% load static %}  <!-- Pastikan untuk memuat static di awal file -->

<nav class="bg-pink-600 shadow-lg fixed top-0 left-0 z-50 w-full">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <!-- Logo Image -->
        <img src="{% static 'image/logo.png' %}" alt="Skivy Logo" class="h-12 w-auto">
      </div>
      <!-- Desktop Menu -->
      <div class="hidden md:flex items-center space-x-4">
        {% if user.is_authenticated %}
          <span class="text-gray-100 text-sm">Welcome, <strong>{{ user.username }}</strong></span>
          <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded-full transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-full transition duration-300">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-full transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button focus:outline-none">
          <svg class="w-8 h-8 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
      </div>
    </div>
  </div>
  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden bg-pink-500 text-center py-4 px-6">
    <div class="space-y-3">
      {% if user.is_authenticated %}
        <span class="block text-gray-100">Welcome, <strong>{{ user.username }}</strong></span>
        <a href="{% url 'main:logout' %}" class="block bg-red-500 hover:bg-red-600 text-white font-semibold py-2 rounded-full transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 rounded-full transition duration-300">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block bg-green-500 hover:bg-green-600 text-white font-semibold py-2 rounded-full transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>

  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```
lalu saya menambahkan navigation bar ini pada file tampilan page lainnya seperti `main.html`,`create_product_entry.html`, dan `edit_product.html` menggunakan tags `include`. Pada struktur kode HTML tersebut sudah dipastikan Navigation Bar responsive dengan class `md:hidden` yang memastikan tombol hanya muncul di tampilan mobile
> Tampilan Navigation Bar Responsive
![image](https://github.com/user-attachments/assets/4548cf85-ade4-49e4-8b90-8654e672d965)
![image](https://github.com/user-attachments/assets/1636c66f-2c36-45bf-ab03-13686fb959fd)

# Tugas 6
## Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web
1. **Responsif**: Menggunakan JavaScript memungkinkan aplikasi web menjadi lebih responsif terhadap input pengguna, memberikan pengalama yang lebih baik karena adanya interaksi secara real-time
2. **Interaktif & Dinamis**: JavaScript memungkinkan pengembangan interface yang interaktif dan dinamis. Dengan JavaScript, pengguna dapat berinteraksi dengan halaman web tanpa harus memuat ulang seluruh halaman
3. **AJAX**: JavaScript memungkinkan penggunaan AJAX, yang memungkinkan web melakukan request ke server tanpa harus memuat ulang halaman, dapat mempercepat dan meningkatkan performa aplikasi
4. **Single Page Application**: Dengan JavaScript, pengembang dapat membuat aplikasi Single Page Application dimana pengguna bisa berinteraksi dengan satu halaman tanpa harus berpindah-pindah halaman
5. **Ekosistem yang Kuat**: Ekosistem JavaScript besar dan dididukung oleh library dan framework yang dapat mempercepat pengembangan aplikasi

## Fungsi `await` ketika Menggunakan `fetch()` dan Yang Terjadi Jika Tidak Digunakan
`await` digunakan untuk menunggu hasil dari Promise, seperti dari `fetch()` yang sifatnya asinkron. Ketika kita menggunakan `await()` di depan `fetch()`, eksekusi kode akan menunggu hingga data dari server dikembalikan sebelum melanjutkan ke instruksi berikutnya. Jika tidak menggunakan `await` maka `fetch()` akan tetap berjalan namun kode berikutnya dieksekusi sebelum hasil dari `fetch()` tersedia. Hal ini dapat menyebabkan error ketika mencoba mengakses data yang belum tersedia

## Mengapa Menggunakan Decorator `csrf_exempt` untuk AJAX POST
Decorator `csrf_exempt` digunakan untuk menonaktifkan pemeriksaan CSRF di Django pada view tertentu. Hal tersebut diperlukan karena secara default, Django memerlukan token CSRF untuk semua request POST sebagai langkah kemananan. Ketika kita mengirimkan request POST menggunakan AJAX, mungkin tidak ada token CSRF yang disertakan sehingga request tersebut akan ditolak. Dengan `csrf_exempt`, kita mengizinkan request AJAX tersebut tanpa token CSRF

## Mengapa Pembersihan Data Input Pengguna Dilakukan di Backend?
Pembersihan data di Backend diperlukan untuk keamanan dan keandalan aplikasi. Data yang diterima oleh server bisa dimanipulasi oleh pengguna yang tidak bertanggung jawab, baik melalui bypass pada validasi frontend atau dengan mengirimkan request manual melalui tools seperti Postman atau curl. Validasi di backend memastikan bahwa data yang masuk aman dan sesuai. Alasan lainnya ialah Frontend hanya berjalan di sisi pengguna dan bisa dihindari atau diubah oleh pengguna. Jika validasi hanya dilakukan di frontend, data berbahaya masih bisa mencapai server lalu terkadang, pembersihan atau validasi data memerlukan interaksi dengan database atau aturan bisnis yang lebih kompleks, yang lebih baik dilakukan di backend.
