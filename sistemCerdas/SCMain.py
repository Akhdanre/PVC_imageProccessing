import pyfiglet
import time
import sys
from rich.console import Console
from rich.table import Table
from rich.live import Live

TEXT_SPEED = 0.1
REFRESH_RATE = 1

console = Console()


def print_slow(text, colorTxt="white"):
    """Print text slowly, one character at a time."""
    for letter in text:
        console.print(letter, style=colorTxt, end="")
        time.sleep(TEXT_SPEED)


def get_user_input(prompt):
    """Get user input and handle any exceptions."""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        sys.exit(0)


def main():
    title = pyfiglet.figlet_format("Sistem Cerdas")
    print(title)

    print_slow("Masukkan namamu\n")
    name = get_user_input("Nama : ")
    print_slow(f"Hallo, {name}\n")
    print_slow(
        "Kami akan menampilkan Daftar Gejala untuk menemukan penyakit apa yang kamu alamai\n")

    table = Table(title="Daftar Gejala")
    table.add_column("Kode", justify="right", style="cyan", no_wrap=True)
    table.add_column("Nama Gejala", style="magenta")

    list_gejala = [
        ["G01", "Pandangan kabur saat melihat objek"],
        ["G02", "Sering menyipitkan mata"],
        ["G03", "Sakit kepala"],
        ["G04", "Mata lelah"],
        ["G05", "Sering menggosok mata"],
        ["G06", "Frekuensi mengedipkan mata yang berlebihan"],
        ["G07", "Melihat objek jauh terlihat jelas"],
        ["G08", "Melihat objek dekat terlihat buram"],
        ["G09", "Mengerlingkan mata untuk melihat objek jelas"],
        ["G10", "Kesulitan Membaca"],
        ["G11", "Mata terasa panas dan gatal"],
        ["G12", "Distorsi pengelihatan"],
        ["G13", "Pandangan samar"],
        ["G14", "Sulit melihat saat malam hari"],
        ["G15", "Mata sering tegang dan mudah lelah"],
        ["G16", "Sensitif pada sorotan cahaya"],
        ["G17", "Kesulitan membedakan warna yang mirip"],
        ["G18", "pengelihatan ganda"],
        ["G19", "membutuhkan penerangan lebih saat membaca"],
        ["G20", "Sulit membaca huruf berukuran kecil"]
    ]

    dataKeputusanPakar = {
        "G01": {"P01": 0.25,  "P02": 0, "P03": 0, "P04": 0.25},
        "G02": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0.25},
        "G03": {"P01": 0.25,  "P02": 0.25, "P03": 0.25, "P04": 0.25},
        "G04": {"P01": 0.25,  "P02": 0, "P03": 0, "P04": 0},
        "G05": {"P01": 0.25,  "P02": 0, "P03": 0, "P04": 0},
        "G06": {"P01": 0.25,  "P02": 0, "P03": 0, "P04": 0},
        "G07": {"P01": 0,  "P02": 0.25, "P03": 0, "P04": 0},
        "G08": {"P01": 0,  "P02": 0.25, "P03": 0, "P04": 0},
        "G09": {"P01": 0,  "P02": 0.25, "P03": 0, "P04": 0},
        "G10": {"P01": 0,  "P02": 0.25, "P03": 0, "P04": 0},
        "G11": {"P01": 0,  "P02": 0.25, "P03": 0, "P04": 0},
        "G12": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0},
        "G13": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0},
        "G14": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0},
        "G15": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0},
        "G16": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0},
        "G17": {"P01": 0,  "P02": 0, "P03": 0, "P04": 0.25},
        "G18": {"P01": 0,  "P02": 0, "P03": 0.25, "P04": 0},
        "G19": {"P01": 0,  "P02": 0, "P03": 0, "P04": 0.25},
        "G20": {"P01": 0,  "P02": 0, "P03": 0, "P04": 0.25},
    }

    with Live(table, refresh_per_second=REFRESH_RATE):
        for row in list_gejala:
            time.sleep(0.2)
            table.add_row(row[0], row[1])

    # print("\n")
    print_slow(
        "jika anda memiliki beberapa gejala yang ada pada table, masukkan kode di bawah \n")
    print_slow(
        "pisahkan dengan tanda - pada kode, contoh G01-G02-G11 \n")
    value = get_user_input("kode : ")
    value = value.split("-")
    for k in range(4):
        for i in value:
            print(i)
       
            

if __name__ == "__main__":
    main()
