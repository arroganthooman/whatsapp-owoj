listPengaji = open('list.txt', 'r').readlines()

print("بـــــــسم اللّـــــــه الرّحمن الرّحيـــــــم")
print("📖LIST REKAP RAMADHAN 📖\n")
for i in range(len(listPengaji)):
    print(f'{i+1}. {listPengaji[i].strip()}')
    print("Juz")
    print()