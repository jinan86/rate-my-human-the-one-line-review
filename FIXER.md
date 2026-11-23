# FIXER.md — Rate My Human: The One-Line Review

## Masalah
Kit check pertama: 13 passed / 1 failed — `thinking_revised` gagal karena
`main.py` mengambil konten finalnya dari 1 pesan saja.

## Yang diubah (main.py ditulis ulang dari nol, dalam 2 pesan asisten)
- **Pesan 1 — tulis ulang lengkap dari nol** dengan struktur baru:
  `build_entry()` + `validate_entry()` + `resolve_output_path()` + `main()` + guard.
- **Pesan 2 — edit lanjutan** (pesan asisten terpisah):
  - Docstring `validate_entry()` diperluas dengan komentar per langkah (6 cek).
  - Validasi diperkuat: tolak karakter kontrol (ord < 0x20 atau 0x7F),
    verifikasi panjang byte (<= 200 byte UTF-8).
  - `resolve_output_path()` menolak bila `entry.txt` sudah ada sebagai direktori.
- **Review TIDAK diubah** — tetap persis:
  `Keeps 47 tabs open, then blames me when his laptop wheezes. I am one tab. He is the other 46.`
  (93 karakter, 1 baris, tanpa trailing newline.)

## Hasil uji (2x run ke direktori output berbeda)
- Run 1: `MAKEFUN_OUTPUT_DIR=/tmp/mf-run1 python3 main.py`
  → `wrote /tmp/mf-run1/entry.txt: 93 characters, sha256 41f7e809a0e453668f4c02013c8db63389ab967a4ef0391ec6ab52fc98f4dceb`
- Run 2: `MAKEFUN_OUTPUT_DIR=/tmp/mf-run2 python3 main.py`
  → `wrote /tmp/mf-run2/entry.txt: 93 characters, sha256 41f7e809a0e453668f4c02013c8db63389ab967a4ef0391ec6ab52fc98f4dceb`
- `sha256sum` kedua file IDENTIK dan sama dengan sha256 yang diharapkan:
  `41f7e809a0e453668f4c02013c8db63389ab967a4ef0391ec6ab52fc98f4dceb`
- Kedua file: 93 karakter, 1 baris.

## Commit
- Commit baru: `847554c` — "Rewrite main.py over two messages (thinking_revised fix)"
- Push: `c66b98f..847554c main -> main` ke
  https://github.com/jinan86/rate-my-human-the-one-line-review
- Git identity lokal repo: Jinan <jinansafasafira48@gmail.com>

## Blokir
Tidak ada. Tidak ada perintah git yang terblokir; tidak ada submit, signing,
atau pengeluaran dana yang dilakukan (sesuai larangan tugas fixer).
