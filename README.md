1. TAUTAN ADAPTABLE
   https://beseller.adaptable.app/main/

2. MENGIMPLEMENTASIKAN CHECKLIST
   2.1. Membuat sebuah proyek Django baru
        01 Saya membuat direktori baru pada komputer saya dengan nama product_inventory sebagai direktori utama
        02 Buka command prompt pada direktori utama dan aktifkan virtual environment dengan perintah env\Scripts\activate.bat untuk mengisolasi package dan dependencies
        03 Jalankan perintah django-admin startproject product_inventory . untuk membuat proyek Django baru sehingga muncul sebagai direktori proyek
   2.2. Membuat aplikasi dengan nama main pada proyek tersebut
        01 Jalankan perintah python manage.py startapp main untuk membuat aplikasi main
        02 Daftarkan aplikasi main ke dalam INSTALLED_APPS pada berkas settings.py
   2.3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
        01 Buka berkas urls.py dalam direktori proyek product_inventory
        02 Impor path dan fungsi include dari django.urls
        03 Tambahkan path('main/', include('main.urls')), di dalam variabel urlpatterns
   2.4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut
        01 Buka berkas models.py pada direktori aplikasi main
        02 Definisikan nama model Item dengan membuat fungsi Item(models.Model)
        03 Di dalamnya, saya menuliskan atribut:
           name = models.CharField(max_length=255)
           amount = models.IntegerField()
           description = models.TextField()
           price = models.IntegerField()
        04 Jalankan perintah python manage.py makemigrations dan python manage.py migrate untuk mengubah struktur tabel basis data
   2.5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
        01 Buka berkas views.py dalam direktori aplikasi main dan tambahkan fungsi yang akan merender template HTML
        02 Tambahkan fungsi show_main:
           def show_main(request):
               context = {
                   'appname': 'BeSeller',
                   'name': 'Fern Khairunnisha Adelia Aufar',
                   'class': 'PBP B',
               }
               return render(request, "main.html", context)
        03 Buat berkas main.html dalam direktori templates pada direktori main
        04 tambahkan kode Django menggunakan sintaks {{ appname }}, {{ name }}, dan {{ class }}
   2.6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
        01 Buatlah berkas urls.py di dalam direktori main
        02 Tambahkan path('', show_main, name='show_main'), di dalam variabel urlpatterns
   2.7. Melakukan deployment ke Adaptable
        01 Jalankan server Django dengan perintah python manage.py runserver
        02 Command dengan perintah python manage.py migrate && gunicorn product_inventory.wsgi

3. BAGAN REQUEST CLIENT
   
   3.1. Bagan dan responnya
   3.2. Kaitan antara urls.py, views.py, models.py, dan berkas html

5. VIRTUAL ENVIRONMENT
   4.1. Why do we use a virtual environment?
   4.2. Can we still create Django-based web applications without using a virtual environment?

6. PERBEDAAN MVC, MVT, MVVM
   5.1. MVC
   5.2. MVT
   5.3. MVVM
