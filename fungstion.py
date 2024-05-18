#1
def angka(a,b):
    return a * b
print(angka(3,5))

#2
def angka_tambah(my_list):
    hasil = 0
    for i in my_list:
        hasil += i
    return hasil
print(angka_tambah([1,2,3,4,5]))

#3
def hitung_keliling_luas(l,p):
    keliling = 2 * (l + p)
    luas = p * l
    return [keliling, luas]
print(hitung_keliling_luas(3,5))

#4
def angka_unik(my_list):
    angka_yang_unik = set(my_list)
    return len(angka_yang_unik)
print(angka_unik([1, 2, 3, 3, 4, 4, 5]
))
        
#5
def paktorial(n):
    if n == 0:
        return 1
    else:
        return n * paktorial(n-1)
print(paktorial(5))

#6
def hitungKata(s:str):
    s_list = s.strip().split()
    return len(s_list)

print(hitungKata("Ini adalah contoh kalimat"))

#7
def cek_palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return f"{kata} adalah palindrom"
    else:
        return f"{kata} bukan palindrom"
print(cek_palindrom("level"))

#8
def angka_besar(my_list):
    return max(my_list)
print(angka_besar([10, 20, 5,30,15]))

#9
def alfabet(string):
    return ''.join(sorted(string))
string = "python"
print(alfabet(string))    

#10
def anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(anagram('listen', 'silent'))
