from re import L
from numpy import angle
from sympy import true


# print("hello world")
# print("i'm learning python now, yeay!")
# print("it's 15/4/2025")



# nama = "Angel"
# umur = 19
# jurusan = "teknik informatika"
# tinggi = 162.5
# single = true

# print("haloo, namaku", nama)
# print("aku umurnya", umur, "tahun")
# print("dari jurusan", jurusan)
# print("tinggiku standar lah ya", tinggi)
# print("apa aku single?", single)
# print("high-class jomblo fii sabilillah ni senggol dong")



# a = 15
# b = 2
# print("aritmatika nya nih")
# print("hasil tambah:", a+b)
# print("hasil kurang:", a-b)
# print("hasil kali:", a*b)
# print("sisa bagi:", a%b)



# name = input("your cool name: ")
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# add = num1 + num2
# mul = num1 * num2
# div = num1 / num2
# pangkat = num1 ** num2
# hb = num1 % num2

# print("hii, i am", name)
# print("this is my calculator")
# print("hasil pangkat:", pangkat)
# print("sisa hasil bagi:", hb)



# 3
# PROGRAM CEK NILAI
# nilai = int(input("Masukkan nilai: "))
# if nilai >= 90:
#     print("wih keren banget bro!")
# elif nilai >= 70:
#     print("boleh lah udah bagus, caresso!")
# else:
#     print("jangan scroll hp mulu woy!!!")

#TEBAK PASSWORD
# password = input("masukkan pw: ")
# if password == "angelcantik123":
#     print("betul banget bray")
# else:
#     print("tetot salah, coba lagi kalo mau")

#PROGRAM CEK USIA
# usia = int(input("masukkan umur anda: "))
# if usia <= 5:
#     print("kamu balita yh")
# elif usia <= 20:
#     print("remaja nich")
# elif usia <= 50:
#     print("udah mapan nih")
# else:
#     print("cie tua haha (nada bercanda)")

#SISTEM KLASIFIKASI PINTAR
while true:
    umur_input = input("Masukin umur: ")
    try:
        umur = int(umur_input)
        break
    except ValueError:
        print("harus angka dong!")


while true:
    gender = input("masukkan jenis kelamin (P/L): ").upper()

    valid_gender = ["P", "L"]
    if gender in valid_gender:
        break
    else:
        print("tidak walid!")

while true:
    status = input("apakah kamu mahasiswa? (ya/tidak): ").upper()

    if status == "YA" or status == "TIDAK":
        break
    else:
        print("input salah")


if umur < 12:
    print("kamu masi bocah")

elif umur >= 12 and umur <= 17 and status == "TIDAK":
    print("kamu remaja sekolah")

elif umur >= 17 and umur <= 25 and status == "YA":
    print("mahasiswa muda")

elif umur >= 25 and umur <= 35 and gender == "L" and status == "YA":
    print("pria dewasa dan masih kuliah, kiw semangat yah")

elif umur >= 25 and umur <= 35 and gender == "P" and status == "YA":
    print("wanita dewasa dan masih kuliah, kiw semangat yah")

elif umur > 35:
    print("sudah matang siap petik")

else:
    print("anomali lukh")

