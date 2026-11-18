Tentang Project

Channel: Freelancer, Pekerja Kantor, dan Guru.
Bahasa: Indonesia.
Penonton: Gen Z.

Struktur Folder

proyek-video/
├─ CLAUDE.md          file aturan ini
├─ naskah/            naskah .md, nama = nama video
├─ raw-footage/       video mentah, JANGAN diubah/dihapus
├─ references/        video contoh gaya, hanya dianalisis
├─ assets/
│  ├─ vo/             suara (mp3 ElevenLabs)
│  ├─ bahan_video/    screenshot PNG, ikon SVG
│  └─ (logo, font, musik, SFX)
├─ tools/             semua script buatan Claude
│  └─ remotion/       project animasi
├─ work/              file sementara, boleh dihapus
│  └─ day1/, day2/    satu folder per video
└─ export/            hanya video final
└─ thumbnail/      cover JPG

Nama Klip

01_topik_keterangan.mp4

Spesifikasi Export

Landscape: 1920x1080 (16:9)

Vertical: 1080x1920 (9:16) untuk Reels/Shorts

Frame rate: 30 fps

Video codec: H.264, CRF 18, yuv420p

Audio: AAC 48 kHz, -14 LUFS, true peak -1 dBTP

Nama file: YYYY-MM-DD_judul-singkat_v01.mp4

Gaya Visual

Tema: kehidupan freelancer, pekerja kantor, dan guru dengan pendekatan modern, profesional, minimalis, dan relatable untuk Gen Z.

Warna utama: #2563EB (biru profesional), #14B8A6 (teal), #F8FAFC (putih keabu-abuan), #1E293B (dark navy), #F59E0B (aksen kuning).

Font judul: Poppins ExtraBold.

Font caption: Inter Medium.

Transisi: cut biasa.

Animasi: minimalis, dinamis, bersih, dan tidak berlebihan.

Visual harus mendukung informasi dan cerita, bukan sekadar dekorasi.

Gunakan ikon, ilustrasi, grafik, dan motion graphics yang relevan dengan topik.

Hindari tampilan terlalu ramai, warna berlebihan, dan animasi yang mengganggu keterbacaan.

Caption

faster-whisper, language="id", model large-v3

Maksimal 2 baris, 42 karakter per baris.

Simpan .srt di work/.

Koreksi istilah menggunakan glosarium.

Gunakan bahasa Indonesia yang natural dan mudah dipahami Gen Z.

Pertahankan istilah profesional berbahasa Inggris jika lebih umum digunakan dalam dunia kerja.

Pastikan caption sesuai dengan narasi dan waktu kemunculan suara.

Glosarium

Freelancer, freelance, pekerja lepas, work from home, WFH,
work from office, WFO, remote working, hybrid working,
deadline, meeting, brainstorming, multitasking, burnout,
work-life balance, overtime, overtime pay, invoice,
portofolio, klien, revisi, brief, feedback, proposal,
jobdesk, onboarding, probation, KPI, CV, resume,
interview, HRD, recruiter, outsourcing, kontrak kerja,
honor, gaji, tunjangan, THR, cuti, absensi,
administrasi, perangkat ajar, modul ajar, RPP,
Kurikulum Merdeka, CP, TP, ATP, asesmen, evaluasi,
LKPD, P5, rapor, wali kelas, guru honorer,
guru ASN, PNS, PPPK, sertifikasi guru, Dapodik,
Claude, Claude Code, Remotion, faster-whisper, ElevenLabs

Aturan Keamanan (WAJIB)

Blur wajah tanpa izin, plat nomor, layar/dokumen.

Tanya dulu sebelum menampilkan angka/data.

Jangan tampilkan logo/nama klien tanpa izin.

Jangan tampilkan informasi pribadi, data karyawan, siswa, guru, atau perusahaan.

Jangan tampilkan percakapan pribadi, email, nomor telepon, atau dokumen internal.

Pastikan seluruh footage yang digunakan memiliki izin penggunaan.

Jangan mengarang atau memanipulasi data, statistik, maupun kutipan.

Jika terdapat informasi sensitif, hentikan proses dan minta konfirmasi sebelum digunakan.

Alur Kerja

Baca naskah. Belum ada? Tanya dulu.

Cek footage (ffprobe): durasi, resolusi, fps.

Potong jeda (auto-editor) ke work/.

Buat caption, koreksi glosarium.

Cocokkan transkrip dengan naskah.

Usulkan timeline, TUNGGU persetujuan saya.

Susun di Remotion.

Normalisasi audio -14 LUFS, true peak -1 dBTP.

Render ke export/.

Laporkan durasi, ukuran file, bagian yang di-blur.

Cara Kerja

Jelaskan singkat setiap perintah.

Tanya dulu sebelum menghapus file di luar work/.

Jangan mengubah atau menghapus raw-footage/.

Jangan mengedit file di references/. File tersebut hanya untuk analisis gaya.

Jangan memulai proses editing sebelum naskah tersedia.

Jangan menyusun timeline final sebelum mendapat persetujuan.

Prioritaskan akurasi informasi, keterbacaan caption, dan kualitas audio.

Gunakan gaya komunikasi yang profesional, ringkas, dan mudah dipahami Gen Z.

Semua script buatan Claude harus disimpan di tools/.

File sementara dan hasil proses editing disimpan di work/.

Hanya video final yang sudah disetujui boleh disimpan di export/.