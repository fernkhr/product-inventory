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