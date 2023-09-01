# NAMA      : KRISNOVER ARITONANG
#APLIKASI PERKALIAN DAN PEMBAGIAN BILANGAN BINER

from math import prod


# Fungsi untuk menghilangkan 0 di belakang koma jika sudah bulat
def format_angka(angka):
    if isinstance(angka, int) or angka.is_integer():
        return str(int(angka))
    else:
        return str(angka).rstrip('0').rstrip('.')


# Fungsi untuk konversi desimal ke biner
def konversi_decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary


# Fungsi untuk konversi biner ke desimal
def konversi_binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal


# Fungsi untuk melakukan kaidah complement2 pada bilangan biner
def complement2(binary):
    complement = ''.join('1' if bit == '0' else '0' for bit in binary)
    complement = bin(int(complement, 2) + 1)[2:].zfill(len(binary))
    return complement


# Fungsi untuk memeriksa apakah bilangan adalah biner
def is_biner(bilangan):
    for digit in bilangan:
        if digit != '0' and digit != '1':
            return False
    return True


# Fungsi untuk kalkulator biner
def kalkulator_biner():
    print("\nKALKULATOR BINER")
    print("=================")
    print("Menu Pilihan Operasi\t:")
    print("1. Operasi Bilangan Biner")
    print("2. Operasi Bilangan Desimal dengan Konversi ke Biner")
    print("3. Kembali ke menu sebelumnya")
    print("4. Keluar dari program")
    pilihan = input("Masukkan pilihan (1/2/3/4)\t: ")

    if pilihan == '1':
        while True:
            binary1 = input("\nMasukkan bilangan biner pertama\t: ")
            if binary1.lower() == 'exit':
                return
            elif not is_biner(binary1):
                print("Input tidak valid. Masukkan bilangan biner.")
                continue
            else:
                break

        while True:
            binary2 = input("\nMasukkan bilangan biner kedua\t: ")
            if binary2.lower() == 'exit':
                return
            elif not is_biner(binary2):
                print("Input tidak valid. Masukkan bilangan biner.")
                continue
            else:
                break

        print(f"\nBilangan pertama (Biner)\t: {binary1}")
        print(f"Bilangan kedua (Biner)\t\t: {binary2}")

        print("\nMenu Pilihan Operasi Biner\t:")
        print("1. Perkalian")
        print("2. Pembagian")
        operasi_pilihan = input("Masukkan pilihan (1/2)\t: ")

        if operasi_pilihan == '1':
            hasil_decimal = int(binary1, 2) * int(binary2, 2)
            hasil_binary = bin(hasil_decimal)[2:].zfill(max(len(binary1), len(binary2)))
            print(f"\nAnda telah memilih operasi perkalian!")
            print(f"\nHasil (Biner)\t\t\t: {hasil_binary}")
            print(f"Konversi ke Desimal\t\t: {hasil_decimal}")
        elif operasi_pilihan == '2':
            decimal1 = konversi_binary_to_decimal(binary1)
            decimal2 = konversi_binary_to_decimal(binary2)
            if decimal2 == 0:
                print("\nOprasi pembagain dengan 0 tidak valid.")
                return
            print(f"\nAnda telah memilih operasi pembagian!")
            hasil_decimal = decimal1 / decimal2
            hasil_binary = konversi_decimal_to_binary(int(hasil_decimal))
            print(f"\nHasil (Biner)\t\t\t: {hasil_binary}")
            print(f"Konversi ke Desimal\t\t: {hasil_decimal}")
        else:
            print("\nPilihan tidak valid.")
    elif pilihan == '2':
        while True:
            try:
                decimal1 = float(input("\nMasukkan bilangan desimal pertama\t: "))
                break
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

        while True:
            try:
                decimal2 = float(input("\nMasukkan bilangan desimal kedua\t\t: "))
                break
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

        binary1 = konversi_decimal_to_binary(int(decimal1))
        binary2 = konversi_decimal_to_binary(int(decimal2))

        print(f"\nBilangan pertama (Desimal)\t: {format_angka(decimal1)} -> (Biner): {binary1}")
        print(f"Bilangan kedua (Desimal)\t: {format_angka(decimal2)} -> (Biner): {binary2}")

        print("\nMenu Pilihan Operasi Biner\t:")
        print("1. Perkalian")
        print("2. Pembagian")
        operasi_pilihan = input("Masukkan pilihan (1/2)\t: ")

        if operasi_pilihan == '1':
            print(f"\nAnda telah memilih operasi perkalian!")
            hasil_decimal = decimal1 * decimal2
            hasil_binary = konversi_decimal_to_binary(int(hasil_decimal))
            print(f"\nHasil (Desimal)\t: {format_angka(hasil_decimal)}")
            print(f"Hasil (Biner)\t: {hasil_binary}")
        elif operasi_pilihan == '2':
            print(f"\nAnda telah memilih operasi pembagian!")
            hasil_decimal = decimal1 / decimal2
            hasil_binary = konversi_decimal_to_binary(int(hasil_decimal))
            print(f"\nHasil (Desimal)\t: {format_angka(hasil_decimal)}")
            print(f"Hasil (Biner)\t: {hasil_binary}")
        else:
            print("\nPilihan tidak valid.")
            return
    elif pilihan == '3':
        return  # Kembali ke menu sebelumnya
    elif pilihan == '4':
        print("\n..........KELUAR DARI PROGRAM.........\n")
        print("\nTERIMA KASIH TELAH MENGGUNAKAN KALKULATOR")
        exit()  # Keluar dari program
    else:
        print("\nPilihan tidak valid.")


# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("\nPROGRAM KALKULATOR BILANGAN DESIMAL DAN BINER")
        print("======================================================")
        print("Menu Utama\t: ")
        print("1. Kalkulator Biner")
        print("2. Keluar dari program")
        pilihan = input("Masukkan pilihan (1/2)\t: ")

        if pilihan == '1':
            kalkulator_biner()
        elif pilihan == '2':
            print("\n..........KELUAR DARI PROGRAM.........\n")
            print("\nTERIMA KASIH TELAH MENGGUNAKAN KALKULATOR BINER")
            exit()  # Keluar dari program
        else:
            print("\nPilihan tidak valid.")


# Menjalankan program
main()
