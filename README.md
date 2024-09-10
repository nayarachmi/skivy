Link PWS: http://naya-kusumahayati-skivy.pbp.cs.ui.ac.id/

> membuat proyek django baru
1. buka command prompt dan arahkan ke direktori dimana aku mau buat projeknya
2. tulis django-admin startproject skivy (nama projeknya)

> membuat aplikasi main
1. navigasi ke direktori skivy (cd skivy)
2. lalu tulis python manage.py startapp main

> melakukan routing
1. membuka file settings.py yang ada di projek skivy lalu menambahkan 'main' di installed_apps
2. membuka file urls.py dan menambahkan routing untuk main (, include('main.urls'))

> membuat model product dalam main
1. membuka file models.py lalu menambhakna model product
2. menjalankan perintah migrasi untuk membuat tabel di database (makemigrations, migrate)

> membuat fungsi views.py 
1. membuka file views.py lalu menambahkan data seperti yang berada di file models.py dan dikembalikan ke dalam template HTML yang sudah dibuat sebelumnya

> membuat rooting urls.py di main
1. membuat file urls.py di folder main dan menambahkan routing 
2. menambahkan kode yang mengatur rute URL dengan main

> melakukan deployment ke PWS
1. menambahkan url deployment PWS ke allowed_hosts di settings.py
2. melakuka git remote add pws dan push pws

>> bagan request client ke web

> fungsi git dalam pengembangan perangkat lunak
1. git memudahkan pengguna melacak perubahan kode yang sudah terjadi, pengguna dapat dengan mudah kembali ke versi kode sebelumnya jika dibutuhkan
2. git memungkinkan banyak pengguna bekerja pada satu proyek yang sama
3. git memudahkan backup kode karena kode disimpan di server remote
4. git memungkinkan pengguna membuat alur pengembangan yang terpisah tanpa mengganggu kode di cabang utama

> alasan mengapa framework django dijadikan permulaan pembelajaran
1. banyak fitur yang sudah disediakan diawal sehingga pengguna tidak perlu melakukan banyak konfigurasi tambahan (pemula friendly)
2. struktur projek jelas dan terorganisir
3. komunitas yang dimiliki besar dan aktif sehingga banyak dukungan yang dapat membantu jika menemukan masalah

> mengapa model pada django disebut sebagai ORM (object relational mapping)
1. karena fungsinya untuk memetakan objek di aplikasi ke tabel dalam database
2. dalam django setiap model python merepresentasikan tabel di database dan tiap atribut dalam model merepresentasikan kolom di tabel