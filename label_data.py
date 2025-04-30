import os
import cv2
from tqdm import tqdm

# Ganti dengan path folder yang berisi gambar
path_folder = "D:\PTRIDIKC\Projek\Lina_deteksi_umur_padi\dataset\Padi 12 minggu"
kelas = 11  # Nomor kelas yang akan digunakan

output_folder = os.path.join(path_folder, "resized")
os.makedirs(output_folder, exist_ok=True)

for k in tqdm(os.listdir(path_folder)):
    path_gambar = os.path.join(path_folder, k)

    # Pastikan hanya memproses file gambar
    if not (k.endswith(".jpg") or k.endswith(".png") or k.endswith(".jpeg")):
        continue

    # Baca gambar
    img = cv2.imread(path_gambar)
    if img is None:
        continue  # Lewati jika gambar tidak dapat dibaca

    # Dapatkan ukuran asli
    h_asli, w_asli = img.shape[:2]

    # Resize ke 640x640
    img_resized = cv2.resize(img, (640, 640))

    # Simpan gambar yang telah di-resize
    output_gambar = os.path.join(output_folder, k)
    cv2.imwrite(output_gambar, img_resized)

    # Hitung bounding box (seluruh gambar)
    x_center = 0.5
    y_center = 0.5
    width = 1.0
    height = 1.0

    # Simpan anotasi dalam file .txt dengan nama yang sama
    nama_txt = os.path.splitext(k)[0] + ".txt"
    path_txt = os.path.join(output_folder, nama_txt)

    with open(path_txt, "w") as f:
        f.write(f"{kelas} {x_center} {y_center} {width} {height}\n")
