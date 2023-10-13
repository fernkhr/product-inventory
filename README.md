# TUGAS 2
### 1. TAUTAN ADAPTABLE
Link: https://beseller.adaptable.app/main/

### 2. MENGIMPLEMENTASIKAN CHECKLIST
- **Membuat sebuah proyek Django baru**
1. Saya membuat direktori baru pada komputer saya dengan nama product_inventory sebagai direktori utama
2. Buka command prompt pada direktori utama dan aktifkan virtual environment dengan perintah `env\Scripts\activate.bat` untuk mengisolasi package dan dependencies
3. Jalankan perintah `django-admin startproject product_inventory .` untuk membuat proyek Django baru sehingga muncul sebagai direktori proyek
- **Membuat aplikasi dengan nama main pada proyek tersebut**
1. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi main
2. Daftarkan aplikasi main ke dalam INSTALLED_APPS pada berkas settings.py
- **Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
1. Buka berkas urls.py dalam direktori proyek product_inventory
2. Impor path dan fungsi include dari django.urls
3. Tambahkan `path('main/', include('main.urls')),` di dalam variabel urlpatterns
- **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut**
1. Buka berkas models.py pada direktori aplikasi main
2. Definisikan nama model Item dengan membuat fungsi Item(models.Model)
3. Di dalamnya, saya menuliskan atribut:
`name = models.CharField(max_length=255)
amount = models.IntegerField()
description = models.TextField()
price = models.IntegerField()`
4. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mengubah struktur tabel basis data
- **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML**
1. Buka berkas views.py dalam direktori aplikasi main dan tambahkan fungsi yang akan merender template HTML
2. Tambahkan fungsi show_main:
`def show_main(request):
context = {
'appname': 'BeSeller',
'name': 'Fern Khairunnisha Adelia Aufar',
'class': 'PBP B',
}
return render(request, "main.html", context)`
3. Buat berkas main.html dalam direktori templates pada direktori main
4. tambahkan kode Django menggunakan sintaks {{ appname }}, {{ name }}, dan {{ class }}
- **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**
1. Buatlah berkas urls.py di dalam direktori main
2. Tambahkan `path('', show_main, name='show_main'),` di dalam variabel urlpatterns
- **Melakukan deployment ke Adaptable**
1. Jalankan server Django dengan perintah `python manage.py runserver`
2. Command dengan perintah `python manage.py migrate && gunicorn product_inventory.wsgi`

### 3. BAGAN REQUEST CLIENT
- **Bagan**

Client (User) --> |URLS (urls.py)| --> |View (views.py)| <--> |Model (models.py)|

      ^                                       ^
      |                                       |
      \________ |Template (main.html)|_______/
- **Kaitan antara urls.py, views.py, models.py, dan berkas html**
1. Client mengirimkan request dengan mengakses suatu URL web atau aplikasi yang terhubung dengan Django
2. urls.py akan menentukan view yang akan menangani request tersebut dengan mengarahkan URL ke view function yang sesuai
3. View function akan memproses request yang masuk dan berinteraksi dengan model (database) untuk mengambil atau menyimpan data yang diperlukan
4. Setelah selesai memproses request, view akan merender berkas template HTML yang nantinya akan dikirim sebagai respons HTML ke client (HTTP Response) 

### 4. VIRTUAL ENVIRONMENT
- **Why do we use a virtual environment?**
Virtual environment digunakan untuk mengisolasi package dan dependencies di satu aplikasi sehingga tidak bertabrakan dengan versi lain atau proyek lain dalam satu komputer
- **Can we still create Django-based web applications without using a virtual environment?**
Pembuatan aplikasi web berbasis Django tanpa menggunakan virtual environment masih bisa dilakukan, akan tetapi memungkinkan terjadinya masalah saat proses pengembangan, yaitu terjadi konflik dependensi antar proyek yang berbeda dan muncul masalah pada saat mengelola beberapa proyek yang memiliki versi Python yang berbeda

### 5. PERBEDAAN MVC, MVT, MVVM
1. **MVC**: MVC berperan dalam mengendalikan alur aplikasi serta menjadi perantara antara model dan view 
2. **MVT**: MVT berperan dalam mengatur tampilan HTML dan merender data dari model ke view
3. **MVVM**: MVVM berperan dalam mengelola tampilan UI serta menghubungkan model dan viewmodel

# TUGAS 3
### 1. MENGIMPLEMENTASIKAN CHECKLIST
- **Membuat input form untuk menambahkan objek model pada app sebelumnya**
1. Saya membuat berkas `forms.py` pada direktori main untuk membuat struktur form yang dapat menerima input data item baru
2. Isi dari form disimpan menjadi sebuah objek Item dan list fields berisi name, amount, description, dan price
- **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**
1. Buka `views.py` pada direktori main dan import modul HttpResponseRedirect, ProductForm, reverse, HttpResponse, dan serializers
2. Buat fungsi baru dengan nama `create_item(request)` untuk menghasilkan formulir yang dapat menambahkan data item secara otomatis ketika meng-klik button submit
3. Ubah fungsi `show_main` dengan menambahkan fungsi `Item.objects.all()` yang tersimpan di dalam variable items untuk mengambil seluruh object Item
4. Buat fungsi-fungsi baru dengan nama `show_xml` dan `show_json` yang menerima parameter request dan tambahkan `data = Item.objects.all()` serta return function berupa HttpResponse
5. Buat fungsi-fungsi baru dengan nama `show_xml_by_id` dan `show_json_by_id` yang menerima parameter request dan tambahkan `data = Item.objects.filter(pk=id)` serta return function berupa HttpResponse
- **Membuat routing URL untuk masing-masing views**
1. Buat file HTML baru dengan nama `create_item` pada direktori main/templates untuk render views
2. Buka `urls.py` pada direktori main dan import fungsi create_item dan tambahkan `path('create-item', create_item, name='create_item')`
3. Tambahkan import fungsi show_xml, show_json, show_xml_by_id, show_json_by_id dan tambahkan path url untuk masing-masing views ke dalam urlpatterns

### 2. PERBEDAAN FORM POST DAN FORM GET
1. **Form POST**: Suatu method pengiriman data dari user ke server yang langsung ditampung oleh action. Data dikirimkan secara tersembunyi, yaitu data tidak ditampilkan pada URL sehingga lebih aman dan tidak terlihat oleh user atau pada log server. Form POST umumnya digunakan untuk mengirimkan data sensitif atau melakukan perubahan di server, contohnya mengirimkan data formulir pendaftaran
2. **Form GET**: Suatu method pengiriman data dari user ke server melalui URL sebagai bagian dari alamat halaman web sehingga data dapat dilihat oleh user dan dapat terlihat di log server. Form GET umumnya digunakan untuk melakukan permintaan yang tidak mengubah data di server, contohnya pencarian atau penampilan halaman di mesin pencarian web browser

### 3. PERBEDAAN XML, JSON, HTML
1. **XML**: Digunakan untuk pertukaran data struktural antara berbagai sistem dan juga digunakan dalam integrasi sistem
2. **JSON**: Digunakan untuk pertukaran data terstruktur dalam format yang mudah dibaca oleh manusia dan diproses oleh komputer sehingga sering digunakan dalam pengembangan web maupun aplikasi
3. **HTML**: Digunakan untuk mendefinisikan struktur dan tampilan halaman web, bukan untuk pertukaran data

### 4. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
1. JSON memiliki struktur data yang mirip dengan objek JavaScript sehingga pemrosesan data di browser dapat dilakukan dengan cepat dan efisien
2. JSON memiliki format data yang ringan, mudah dibaca oleh manusia, dan mudah dipahami oleh komputer
3. JSON didukung oleh banyak bahasa pemrograman sehingga dapat dilakukan pertukaran data yang seragam antara berbagai komponen aplikasi

### 5. SCREENSHOT POSTMAN
1. **html**
![Screenshot (933)](https://github.com/fernkhr/product-inventory/assets/137986413/33be664b-4425-48bf-a4f0-5e3dc0629c34)
2. **xml**
![Screenshot (934)](https://github.com/fernkhr/product-inventory/assets/137986413/57345d53-5484-4e13-ab5a-925e9781f162)
3. **json**
![Screenshot (935)](https://github.com/fernkhr/product-inventory/assets/137986413/dbeabbc9-a7b2-431a-8577-545343099e02)
4. **xml by id**
![Screenshot (936)](https://github.com/fernkhr/product-inventory/assets/137986413/53a2dedd-57ad-492c-8fdd-f96653569ab0)
5. **json by id**
![Screenshot (937)](https://github.com/fernkhr/product-inventory/assets/137986413/42b8c81b-6010-45d5-86f9-3ed04e426db9)

# TUGAS 4
### 1. MENGIMPLEMENTASIKAN CHECKLIST
- **Mengimplementasikan fungsi registrasi, login, dan logout**
1. Buka `views.py` pada direktori main. Import modul UserCreationForm, messages, authenticate, login, dan logout
2. Buat fungsi dengan nama register, login_user, dan logout_user yang menerima parameter request
3. Fungsi register berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna baru
4. Fungsi login_user berfungsi untuk mengautentikasi pengguna yang ingin login dan fungsi logout_user berfungsi untuk melakukan mekanisme logout
5. Buat template untuk tampilan halaman register di berkas `register.html`
6. Buat template untuk tampilan halaman login di berkas `login.html`
7. Buka berkas `main.html` dan tambahkan kode untuk membuat button logout yang akan ditampilkan di halaman main
8. Buka `urls.py` pada direktori main. Import fungsi register, login_user, dan logout_user serta tambahkan `path('register/', register, name='register'),` `path('login/', login_user, name='login'),` `path('logout/', logout_user, name='logout'),` di `urlpatterns`
- **Membuat dua akun pengguna dengan masing-masing tiga dummy data**
1. Buka `views.py` pada direktori main dan tambahkan import login_required agar bisa merestriksi akses halaman main
2. Tambahkan kode `@login_required(login_url='/login')` di atas fungsi show_main agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi)
- **Menghubungkan model Item dengan User**
1. Buka `models.py` pada direktori main dan tambahkan import User
2. Pada `Item(models.Model)`, tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` untuk mengasosiasikan satu item dengan seorang user
3. Buka `views.py` pada direktori main dan modifikasi fungsi `create_product` agar Django tidak langsung menyimpan objek yang telah dibuat dari form ke database
4. Ubah potongan kode pada fungsi `show_main` menjadi `items = Item.objects.filter(user=request.user)` dan `'name': request.user.username,`
- **Menampilkan detail informasi pengguna yang sedang logged in dan menerapkan cookies seperti last login pada halaman utama aplikasi**
1. Tambahkan import datetime agar bisa mengakses waktu dan tanggal saat ini
2. Tambahkan fungsi pada fungsi `login_user` dengan menambahkan cookie yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan login
3. Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login'],` ke dalam variabel `context` untuk menampilkan informasi last_login di halaman main
4. Hapus cookie `last_login` setiap pengguna melakukan `logout`
5. Menampilkan teks informasi last login dengan menambahkan potongan kode di `main.html`

### 2. Django UserCreationForm
1. **Pengertian**
      - Django UserCreationForm adalah salah satu formulir bawaan yang disediakan oleh Django untuk mempermudah pengembangan aplikasi web yang melibatkan autentikasi pengguna. UserCreationForm digunakan untuk membuat form registrasi yang berisi username, password, dan konfirmasi password
2. **Kelebihan**
      - Memudahkan para pengembang untuk membuat form registrasi dengan cepat tanpa perlu menulis kode HTML atau membuat validasi secara manual
      - UserCreationForm menyediakan beberapa tingkatan validasi dan keamanan bawaan, seperti pengujian keunikan username dan validasi password
      - UserCreationForm terintegrasi dengan user model bawaan Django sehingga pengembang tidak perlu menulis kode khusus untuk menyimpan data pengguna ke dalam basis data
3. **Kekurangan**
      - Appearance dan behavior dari UserCreationForm kadang tidak sesuai dengan design atau kebutuhan khusus proyek
      - UserCreationForm tidak menyediakan fitur-fitur tambahan atau custom logic
      - UserCreationForm tidak dapat mengimplementasikan pengiriman email konfirmasi saat registrasi user

### 3. AUTENTIKASI DAN OTORISASI
1. **Autentikasi**: Proses verifikasi identitas pengguna. Dalam Django, saat login, pengguna akan memasukkan username dan password untuk membuktikan bahwa pengguna adalah akun yang sah
2. **Otorisasi**: Proses penentuan perizinan untuk pengguna yang sudah terautentikasi. Otorisasi akan menentukan apakah pengguna memiliki izin untuk mengakses halaman tertentu, melihat data tertentu, atau melakukan tindakan tertentu pada aplikasi
3. **Mengapa keduanya penting?** Autentikasi bertujuan untuk memastikan bahwa hanya pengguna yang sah yang memiliki akses masuk ke aplikasi, sedangkan otorisasi bertujuan untuk memastikan bahwa beberapa pengguna hanya memiliki akses ke bagian aplikasi yang sesuai dengan peran atau hak akses mereka. Hal ini penting untuk menjaga keamanan dan mencegah akses yang tidak sah

### 4. COOKIES
1. **Pengertian**: Data yang digunakan untuk menyimpan informasi yang berisi rekam jejak dan aktivitas pengguna ketika menelusuri sebuah website. Cookies biasanya berbentuk teks dan tersimpan dalam bentuk file teks di komputer pengguna. Cookies akan mengaktifkan suatu website untuk mengingat data pengguna, seperti informasi login
2. **Cookies pada Django**: Cookies akan mengelola data sesi pengguna dengan mengidentifikasi pengguna yang sudah terautentikasi. Informasi yang diolah dan disimpan adalah ID sesi. Django menggunakan cookies melalui komponen middleware dan session framework. Middleware yang dimiliki oleh Django adalah `django.contrib.sessions.middleware.SessionMiddleware`. Middleware ini berfungsi untuk menyimpan data sesi pengguna secara aman pada sisi pengguna dan mengembalikannya saat pengguna membuat permintaan berikutnya

### 5. KEAMANAN COOKIES
1. **Apakah penggunaan cookies aman secara default dalam pengembangan web?** Keamanan penggunaan cookies dalam pengembangan web tergantung pada bagaimana pengguna menggunakannya. Cookies sebenarnya tidak berbahaya karena malware sulit masuk ke dalam komputer pengguna. Namun, pengguna harus tetap membatasi penggunaan cookies untuk mencegah beberapa risiko
2. **Risiko potensial yang dapat terjadi**
      - Jika cookies mengandung informasi yang sensitif seperti ID sesi, penyerang dapat mengakses akun pengguna atau data sesi sehingga sangat disarankan untuk menggunakan mekanisme keamanan seperti HTTPS untuk mengenkripsi data yang dikirimkan antara peramban dan server
      - Dalam serangan XSS, penyerang dapat memasukkan skrip jahat ke dalam website yang kemudian dieksekusi oleh user browser. Hal ini berfungsi untuk mencuri cookies pengguna atau melakukan tindakan berbahaya atas nama pengguna
      - Dalam serangan CSRF, penyerang mengirimkan permintaan palsu dari user browser  yang mengandung cookies autentikasi yang dapat membahayakan aplikasi. Django memiliki mekanisme bawaan untuk melindungi web dari serangan CSRF, tetapi pengembang harus memastikan bahwa mekanisme ini sudah diaktifkan dan digunakan dengan benar

# TUGAS 5
### 1. MENGIMPLEMENTASIKAN CHECKLIST
- **Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin**
1. Menambahkan bootstrap css dan js ke aplikasi
2. Menambahkan navbar pada halaman login, register, dan daftar inventori
3. Menambahkan fitur edit dan menghapus data item pada halaman daftar inventori
- **Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card**
1. Menambahkan warna background halaman web dengan menggunakan class background-color dari Bootstrap
2. Menambahkan warna pada teks
3. Menambahkan warna background navbar

### 2. MANFAAT ELEMENT SELECTOR
- **Element Selector**: Memilih semua elemen dengan tag yang sama. Digunakan ketika memodifikasi semua paragraf atau semua tautan
- **Class Selector**: Memilih elemen dengan kelas tertentu. Digunakan ketika membuat tombol dengan kelas "btn"
- **ID Selector**: Memilih elemen dengan ID unik. Digunakan ketika ingin menerapkan fungsi khusus pada satu elemen tertentu yang memiliki ID unik, seperti header
- **Universal Selector**: Memilih semua elemen dalam dokumen. Digunakan ketika dalam situasi yang sangat spesifik, karena dapat mempengaruhi seluruh dokumen
- **Descendant Selector**: Memilih elemen yang berada dalam elemen lain. Digunakan ketika ingin memilih elemen dalam hubungan hierarki, seperti memilih semua elemen daftar (li) dalam elemen daftar tak tertordered (ul)
- **Attribute Selector**: Memilih elemen berdasarkan atribut dan nilainya. Digunakan ketika ingin memilih elemen berdasarkan tipe tertentu, misalnya memilih semua input dengan tipe "text"

### 3. HTML5 TAG
- **< html >**: Elemen akar dari setiap halaman HTML5. Semua elemen lainnya akan berada di dalam elemen ini
- **< head >**: Berisi informasi meta tentang halaman, seperti judul, karakter set, dan tautan ke file CSS
- **< title >**: Untuk menentukan judul halaman yang akan ditampilkan di bilah judul browser
- **< body >**: Elemen yang berisi semua konten yang akan ditampilkan di halaman web, seperti teks, gambar, dan elemen lainnya
- **< a >**: Untuk membuat tautan (hyperlink) ke halaman lain atau sumber eksternal
- **< table >, < tr >, < th >, dan < td >**: Untuk membuat tabel di halaman web
- **< meta >**: Untuk memberikan informasi tentang halaman, seperti karakter set atau deskripsi halaman, yang dapat digunakan oleh mesin pencari

### 4. PERBEDAAN MARGIN DAN PADDING
1. **Margin**: Ruang di luar batas luar elemen HTML dan digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya. Margin tidak memiliki latar belakang atau warna, dan digunakan untuk mengendalikan seberapa dekat atau jauh elemen tersebut dari elemen-elemen lain di sekitarnya
2. **Padding**: Ruang di antara batas luar elemen dan kontennya sendiri. Padding digunakan untuk mengatur jarak antara batas luar elemen dan isi atau konten elemen tersebut. Padding dapat memiliki latar belakang atau warna, sehingga memungkinkan untuk memberikan elemen tampilan yang lebih menarik dan mengendalikan seberapa jauh konten elemen tersebut dari batas luar

### 5. PERBEDAAN FRAMEWORK CSS TAILWIND DAN BOOTSTRAP
1. **Tailwind**: Digunakan untuk membangun tampilan web dengan cara menambahkan kelas-kelas kecil untuk mengatur gaya elemen secara detail. Tailwind memiliki tingkat kustomisasi yang tinggi karena dapat mengatur setiap gaya elemen dengan kelas-kelas yang tersedia. Tailwind cocok digunakan untuk membuat desain yang unik dan sesuai dengan preferensi desain pengembang
2. **Bootstrap**: Bootstrap menyediakan komponen-komponen siap pakai dengan gaya yang telah ditentukan sehingga tidak perlu mengatur gaya secara detail. Kustomisasi Bootstrap lebih terbatas karena komponen yang digunakan telah ditentukan oleh Bootstrap sehingga lebih banyak usaha untuk mengubahnya. Pengembang dapat menggunakan Bootstrap jika ingin cepat membangun tata letak web dengan desain yang sudah ada dan cukup stabil apalagi jika pengembang tidak memiliki waktu yang banyak untuk menyesuaikan tampilan dengan sangat mendetail

# TUGAS 6
### PERBEDAAN ASYNCHRONOUS DAN SYNCHRONOUS PROGRAMMING
1. **Asynchronous programming**: Dalam asynchronous programming, tugas-tugas dieksekusi secara independen dan tidak memblokir eksekusi tugas lainnya. Sebagai contoh, ketika tugas A sedang menunggu data dari jaringan, program tidak akan terhenti dan dapat menjalankan tugas-tugas lainnya. Ketika data yang dibutuhkan sudah tersedia, tugas A akan dijalankan. Ini memungkinkan program untuk tetap responsif dan efisien, terutama dalam kasus seperti operasi jaringan atau I/O yang memerlukan waktu
2. **Synchronous programming**: Dalam synchronous programming, tugas-tugas dieksekusi satu per satu, mulai dari yang pertama hingga selesai. Artinya, jika suatu tugas memerlukan waktu yang lama untuk menyelesaikan operasi, maka program akan terhenti dan menunggu hingga operasi tersebut selesai sebelum melanjutkan ke tugas berikutnya. Ini dapat mengakibatkan program menjadi lambat jika ada tugas yang memerlukan waktu lama

### PARADIGMA EVENT-DRIVEN PROGRAMMING
1. **Pengertian**: Pendekatan pemrograman di mana program merespons peristiwa (events) yang terjadi, seperti klik tombol, input pengguna, atau penerimaan data dari jaringan. Program akan mengikuti aliran peristiwa yang terjadi secara asinkron, dan tugas-tugas akan dieksekusi hanya ketika peristiwa yang sesuai terjadi
2. **Contoh**: Dalam penggunaan AJAX (Asynchronous JavaScript and XML) untuk mengambil data dari server tanpa harus memuat ulang seluruh halaman web. Saat seorang pengguna mengklik tombol atau mengisi formulir, Anda dapat menggunakan AJAX untuk mengirim permintaan ke server dan merespons data yang diterima tanpa mengganggu pengalaman pengguna

### ASYNCHRONOUS PROGRAMMING PADA AJAX
AJAX memanfaatkan asynchronous programming untuk mengirim permintaan ke server dan menerima respon tanpa memblokir tampilan atau interaksi pengguna. Ini biasanya dilakukan dengan menggunakan objek XMLHttpRequest atau Fetch API dalam JavaScript. Berikut langkah-langkah umumnya:
1. Membuat objek XMLHttpRequest atau menggunakan Fetch API untuk mengirim permintaan ke server.
2. Menetapkan fungsi callback yang akan dipanggil ketika respon dari server tiba.
3. Melakukan permintaan ke server dengan metode seperti xhr.send() atau fetch().
4. Ketika respon diterima dari server, fungsi callback akan dieksekusi untuk memproses data tersebut tanpa mengganggu interaksi pengguna yang lain.

### FETCH API DAN LIBRARY jQUERY
1. **AJAX dengan Fetch API**: Fetch API adalah API baru dalam JavaScript yang menyediakan cara modern dan kuat untuk mengambil dan mengirim data asinkron. Ini adalah standar web yang baru dan memiliki dukungan yang baik di seluruh browser modern. Fetch API memungkinkan Anda untuk membuat permintaan HTTP dan mengelola respons dengan lebih mudah
2. **AJAX dengan Library jQuery**: jQuery adalah library JavaScript yang telah lama digunakan untuk mengelola permintaan asinkron (AJAX) dan banyak tugas lainnya dalam pengembangan web. Namun, dengan kemajuan Fetch API dan peningkatan dukungan JavaScript modern, penggunaan jQuery dalam proyek-proyek baru mungkin menjadi kurang umum
