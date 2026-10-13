## Task 1-Manual API Test
Dokumen hasil testing API Menggunakan Postman
- POST /pet – Menambahkan hewan peliharaan baru
- GET /pet/findByStatus – Mencari hewan peliharaan berdasarkan status
- DELETE /pet/{petId} – Menghapus hewan peliharaan berdasarkan ID

## Task 2 & 3_API Automation Testing

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
```
Task 2 & 3 - API & UI Automation Test/
│
├── .idea/                      # Konfigurasi IDE
├── allure-results/              # Hasil pengujian untuk Allure Report
│
├── pages/                       # Page Object Model untuk UI testing
│   ├── __init__.py
│   ├── cart_page.py             # Interaksi halaman cart
│   ├── checkout_page.py         # Interaksi halaman checkout
│   ├── inventory_page.py        # Interaksi halaman inventory
│   └── login_page.py            # Interaksi halaman login
│
├── reports/                     # Penyimpanan laporan pengujian
├── screenshots/                 # Screenshot hasil atau proses testing
│
├── tests/                       # Test cases
│   ├── petstore-testing/        # API testing untuk Petstore
│   │   ├── test_delete_pet.py   # Pengujian DELETE pet
│   │   ├── test_get_pet.py      # Pengujian GET pet
│   │   └── test_post_pet.py     # Pengujian POST pet
│   │
│   ├── __init__.py
│   └── Running_test.py          # Entry point untuk menjalankan test
│
├── Utils/                       # Helper dan utility functions
├── .gitignore                   # File yang diabaikan Git
├── README.md                    # Dokumentasi project
└── requirements.txt              # Daftar dependency Python
```

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

```bash
python --version
python -m pip --version
```

### 2. Clone Repository

Jalankan perintah berikut pada terminal:

```bash
git clone https://github.com/fayakunilham/SauceDemo-UI_API-Testing-PetStore-Swagger.git
```

### 3. Masuk ke Folder Proyek

```bash
cd SauceDemo-UI_API-Testing-PetStore-Swagger
```

### 4. Membuat Virtual Environment

```bash
python -m venv .venv
```

Aktifkan virtual environment menggunakan Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika menggunakan Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 5. Instal Dependency

```bash
python -m pip install -r requirements.txt
```

### 6. Instal Browser Playwright

```bash
python -m playwright install
```

## ▶️ Cara Menjalankan Pengujian

### Menjalankan Semua Test Case

```bash
python -m pytest -v
```

### Menjalankan Test Case dalam Folder Tests

```bash
python -m pytest tests/ -v
```

### Menjalankan File Test Tertentu

Ganti nama_file_test.py dengan nama file yang benar-benar tersedia di folder tests/.

```bash
python -m pytest tests/nama_file_test.py -v
```

### Menjalankan Test dengan Output Detail

```bash
python -m pytest -v -s
```

Keterangan:

- pytest — Menjalankan test case.
- -v — Menampilkan nama setiap test case dan statusnya.
- -s — Menampilkan output dari print() selama pengujian berlangsung.

## 📊 Allure Report

Allure Report digunakan untuk menyajikan hasil UI dan API Automation Testing dalam laporan HTML yang interaktif dan mudah dipahami.

### 1. Install Allure Pytest

```bash
python -m pip install allure-pytest
```

### 2. Run All Automation Tests

Jalankan seluruh test case dan simpan hasil pengujian ke folder `reports/allure-results/`.

```bash
python -m pytest -v -s --alluredir=reports/allure-results
```

### 3. Generate Allure HTML Report

Generate laporan HTML berdasarkan hasil pengujian yang telah dijalankan.

```bash
allure generate reports/allure-results --clean -o reports/allure-report
```

### 4. Open Allure Report

Buka laporan pengujian melalui browser.

```bash
allure open reports/allure-report
```

### Allure Report Features

- **Test Summary:** Menampilkan ringkasan hasil pengujian.
- **Test Status:** Menampilkan status Passed, Failed, Broken, dan Skipped.
- **Test Details:** Menampilkan detail setiap test case.
- **Execution Duration:** Menampilkan durasi eksekusi test.
- **Failure Analysis:** Membantu menganalisis penyebab kegagalan pengujian.

### Notes

- Pastikan `allure-pytest` sudah terinstal.
- Allure Commandline harus diinstal secara terpisah.
- Folder `reports/allure-results/` berisi hasil mentah pengujian.
- Folder `reports/allure-report/` berisi laporan HTML yang dihasilkan.
- Jalankan test terlebih dahulu sebelum membuat laporan.


## ✅ Validasi Pengujian

Pengujian otomatis digunakan untuk memeriksa:

- Kesesuaian hasil aktual dengan hasil yang diharapkan.
- Validasi skenario positif dan negatif.
- Visibilitas dan interaksi elemen pada aplikasi web.
- HTTP status code dan data response API.
- Kesesuaian fungsi aplikasi terhadap kebutuhan pengujian.

Hasil pengujian ditampilkan melalui terminal Pytest, termasuk jumlah test yang berhasil, gagal, atau mengalami error.


## 👨‍💻 Tentang Saya

**Fayakun Ilham Pradana**

Software Quality Assurance | QA Automation Testing

- GitHub: https://github.com/fayakunilham
- LinkedIn: https://www.linkedin.com/in/fayakun-ilham-pradana/

---
