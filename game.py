import random
# import os

skor_pemain = 0
skor_komp = 0
maks_skor= 3


pilihan = [" ", "Gunting", "Batu", "kertas"]
pilihan_pemain = None
history_permainan = []

babak = 1

while skor_pemain < maks_skor and skor_komp < maks_skor:
    # os.system ("cls") untuk menghapus permainan per babak
    print(f"\nkamu:lawan\n{skor_pemain}:{skor_komp}\n")
    for i in range(1, 4):
        print (f"{i}. {pilihan[i]}")
    print()

    pilihan_pemain = int(input("pilihan : "))

    if pilihan_pemain == 0:
        break

    elif pilihan_pemain not in [1,2,3]:
        print(f"pilihan kamu tidak valid\n")
        continue #mengulang looping
        
    print(f"pilihan kamu : {pilihan[pilihan_pemain]}")

    pilihan_komp = random.randint(1,3)
    print(f"pilihan lawan : {pilihan[pilihan_komp]}")

    if pilihan_pemain == pilihan_komp:
        pass
    else:
        if (pilihan_pemain == 1 and pilihan_komp == 2) or (pilihan_pemain == 2 and pilihan_komp == 3) or (pilihan_pemain == 3 and pilihan_komp== 1):
            skor_pemain +=1
        else:
            skor_komp +=1
        
    history_permainan.append(f"babak {babak} : kamu {pilihan[pilihan_pemain]}, komputer {pilihan[pilihan_komp]}")
    babak += 1  

if skor_pemain > skor_komp:
    print("\nSELAMAT KAMU MENANG")
elif skor_pemain < skor_komp:
    print("\nMAAF KAMU KALAH")
else:
    print("\nPERMAINAN SERI")

# print("History Permainan:")
# for langkah in history_permainan:
#     print(langkah)
