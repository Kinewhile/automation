import os
import shutil

os.system("cls")
print("Current working directory:", os.getcwd())

folders = {
    "exe files": ".exe",
    "photo files": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
        ".webp", ".heic", ".heif", ".raw", ".cr2", ".nef",
        ".arw", ".orf", ".sr2", ".psd"],
    "zip files": ".zip"
}

for folder in folders.keys():
    os.makedirs(os.path.join(os.getcwd(), folder), exist_ok=True)

for file in os.listdir(os.getcwd()):
    for folder, ext in folders.items():
        if file.endswith(ext):
            shutil.move(
                os.path.join(os.getcwd(), file),
                os.path.join(os.getcwd(), folder, file)
            )
            break
