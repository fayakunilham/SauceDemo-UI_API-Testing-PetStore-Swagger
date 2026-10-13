## SauceDemo UI & API Automation Testing — PetStore Swagger

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-Testing-blue?logo=pytest)
![Testing](https://img.shields.io/badge/Testing-UI%20%7C%20API-orange)
![Status](https://img.shields.io/badge/Project-QA%20Automation-purple)

## 📌 Deskripsi Proyek

Repository ini berisi proyek **Quality Assurance (QA) Automation Testing** menggunakan Python, Playwright, dan Pytest.

Proyek ini dibuat untuk mempraktikkan pengujian otomatis pada aplikasi web dan layanan API, termasuk pengujian fungsional, validasi data, skenario positif dan negatif, serta penyusunan framework automation testing yang terstruktur.

## Tujuan Proyek

- Mengimplementasikan UI Automation Testing menggunakan Playwright.
- Menguji fungsionalitas aplikasi web secara otomatis.
- Mempraktikkan API Testing menggunakan Swagger PetStore.
- Membuat test case dengan skenario positif dan negatif.
- Menggunakan Pytest untuk menjalankan dan memvalidasi hasil pengujian.
- Menerapkan struktur kode yang mudah dipelihara dan dikembangkan menggunakan Page Object Model (POM).

## 🌐 Aplikasi yang Diuji

### 1. SauceDemo — UI Automation Testing

URL: https://www.saucedemo.com/

SauceDemo merupakan aplikasi demo e-commerce yang digunakan untuk mempraktikkan pengujian otomatis pada aplikasi web.

Cakupan skenario pengujian yang dapat dilakukan:

- Login dengan username dan password yang valid.
- Login dengan kredensial yang tidak valid.
- Validasi login ketika kolom input kosong.
- Validasi halaman produk setelah login.
- Menambahkan produk ke keranjang.
- Memvalidasi produk yang terdapat di keranjang.
- Menjalankan alur checkout hingga pesanan selesai.

### 2. Swagger PetStore — API Automation Testing

URL: https://petstore.swagger.io/

Swagger PetStore merupakan API demo yang digunakan untuk mempraktikkan pengujian REST API.

Cakupan skenario pengujian yang dapat dilakukan:

- Create Pet: menambahkan data hewan baru.
- Get Pet: mengambil detail hewan berdasarkan ID.
- Update Pet: memperbarui data hewan.
- Delete Pet: menghapus data hewan.
- Memvalidasi HTTP status code.
- Memvalidasi struktur dan isi JSON response.
- Menguji skenario positif dan negatif pada API.

> Catatan: Daftar skenario di atas merupakan cakupan yang dituju. Pastikan setiap skenario sudah tersedia dalam script sebelum menyatakannya sebagai pengujian yang telah diimplementasikan.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman untuk automation testing |
| Playwright | Otomatisasi pengujian aplikasi web |
| Pytest | Menjalankan test case dan assertion |
| REST API | Teknologi API yang diuji |
| Swagger PetStore | API demo untuk pengujian |
| Git & GitHub | Version control dan penyimpanan repository |
| Page Object Model (POM) | Mengorganisasi kode automation agar lebih mudah dipelihara |

## 📁 Struktur Proyek

Task 2 & 3 - API & UI Automation Test/
│
├── .idea/
│
├── allure-results/
│
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── screenshots/
│
├── tests/
│   ├── petstore-testing/
│   │   ├── test_delete_pet.py
│   │   ├── test_get_pet.py
│   │   └── test_post_pet.py
│   │
│   ├── __init__.py
│   └── Running_test.py
│
├── Utils/
│
├── .gitignore
├── README.md
├── requirements.txt
└── README.md

### Penjelasan Folder

- pages/ — Menyimpan class untuk halaman aplikasi dan interaksi dengan elemen UI.
- tests/ — Menyimpan script pengujian otomatis.
- Utils/ — Menyimpan fungsi pendukung yang dapat digunakan kembali.
- requirements.txt — Berisi daftar dependency Python yang diperlukan.
- .gitignore — Menentukan file atau folder yang tidak perlu dimasukkan ke Git.
- README.md — Dokumentasi proyek dan panduan penggunaan.

## ⚙️ Persiapan dan Instalasi

### 1. Prasyarat

Pastikan perangkat sudah memiliki:

- Python 3.x
- pip
- Git
- Visual Studio Code atau IDE Python lainnya

Periksa instalasi Python:

bash
python --version
python -m pip --version


### 2. Clone Repository

Jalankan perintah berikut pada terminal:

bash
git clone https://github.com/fayakunilham/SauceDemo-UI_API-Testing-PetStore-Swagger.git


### 3. Masuk ke Folder Proyek

bash
cd SauceDemo-UI_API-Testing-PetStore-Swagger


### 4. Membuat Virtual Environment

bash
python -m venv .venv


Aktifkan virtual environment menggunakan Windows PowerShell:

powershell
.\.venv\Scripts\Activate.ps1


Jika menggunakan Command Prompt:

cmd
.venv\Scripts\activate.bat


### 5. Instal Dependency

bash
python -m pip install -r requirements.txt


### 6. Instal Browser Playwright

bash
python -m playwright install


## ▶️ Cara Menjalankan Pengujian

### Menjalankan Semua Test Case

bash
python -m pytest -v


### Menjalankan Test Case dalam Folder Tests

bash
python -m pytest tests/ -v


### Menjalankan File Test Tertentu

Ganti nama_file_test.py dengan nama file yang benar-benar tersedia di folder tests/.

bash
python -m pytest tests/nama_file_test.py -v


### Menjalankan Test dengan Output Detail

bash
python -m pytest -v -s


Keterangan:

- pytest — Menjalankan test case.
- -v — Menampilkan nama setiap test case dan statusnya.
- -s — Menampilkan output dari print() selama pengujian berlangsung.

## ✅ Validasi Pengujian

Pengujian otomatis digunakan untuk memeriksa:

- Kesesuaian hasil aktual dengan hasil yang diharapkan.
- Validasi skenario positif dan negatif.
- Visibilitas dan interaksi elemen pada aplikasi web.
- HTTP status code dan data response API.
- Kesesuaian fungsi aplikasi terhadap kebutuhan pengujian.

Hasil pengujian ditampilkan melalui terminal Pytest, termasuk jumlah test yang berhasil, gagal, atau mengalami error.

## 🚀 Rencana Pengembangan

Beberapa peningkatan yang dapat dilakukan pada proyek ini:

- Menambah cakupan test case positif dan negatif.
- Mengembangkan reusable API testing utilities.
- Mengelola test data secara lebih terstruktur.
- Mengambil screenshot secara otomatis ketika UI test gagal.
- Mengintegrasikan Allure Report untuk dokumentasi hasil pengujian.
- Menambahkan perekaman video selama eksekusi browser jika diperlukan.
- Mengintegrasikan Jenkins untuk menjalankan automated test melalui CI/CD pipeline.
- Meningkatkan dokumentasi hasil pengujian dan analisis defect.

*Daftar di atas merupakan rencana pengembangan, bukan klaim bahwa semua fitur tersebut sudah tersedia.*

## 📚 Pembelajaran yang Didapatkan

Melalui proyek ini, saya mengembangkan pemahaman dan keterampilan dalam:

- Software Quality Assurance.
- UI Automation Testing.
- REST API Testing.
- Python Automation Testing.
- Playwright dan Pytest.
- Perancangan test case dan validasi fungsional.
- Page Object Model (POM).
- Eksekusi test, debugging, dan analisis kegagalan pengujian.

## 👨‍💻 Tentang Saya

**Fayakun Ilham Pradana**

Software Quality Assurance | QA Automation Testing

- GitHub: https://github.com/fayakunilham
- LinkedIn: https://www.linkedin.com/in/fayakun-ilham-pradana-866503194/

---

*Repository ini merupakan bagian dari proses pembelajaran dan pengembangan keterampilan saya dalam Software Quality Assurance dan Automation Testing.*
