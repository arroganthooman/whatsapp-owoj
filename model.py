class Person():

    listPengaji = []
    
    def __init__(self, name, juz):
        self.name = name
        self.juz = juz
        self.listPengaji.append(self)

    def tambahJuz(self, jumlah):
        if self.juz + jumlah > 30:
            self.juz = (self.juz + jumlah) % 30
        else:
            self.juz += jumlah


    def __repr__(self):
        if 0 < self.juz < 10:
            return f'Juz 0{self.juz} ⚪{self.name}'
        else:
            return f'Juz {self.juz} ⚪{self.name}'

    @staticmethod
    def aktifkan():
        lst = open("list.txt", "r").readlines()
        counter = 1
        for person in lst:
            Person(person.strip("\n"), counter)
            counter += 1