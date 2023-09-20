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
3. JSON didukung oleh banyak bahasa pemrograman sehingga dapat dilakukan pertukaran data yang seragam antara berbagai bagian aplikasi, bahkan jika ditulis dalam bahasa yang berbeda
