class Person():

    listPengaji = []
    
    def __init__(self, name, juz):
        self.name = name
        self.juz = juz
        self.listPengaji.append(self)

    def tambahJuz(self, jumlah):
        self.juz += jumlah


    def __repr__(self):
        if 0 < self.juz < 10:
            return f'Juz 0{self.juz} ⚪{self.name}'
        else:
            return f'Juz {self.juz} ⚪{self.name}'

    @staticmethod
    def aktifkan():
        a = Person("Atikah", 1)
        dd = Person("Azka", 2)
        b =Person("Omay", 3)
        c =Person("Chaca", 4)
        d =Person("Ita", 5)
        e =Person("Ais", 6)
        f =Person("Eliah", 7)
        g =Person("Wahid", 8)
        h =Person("Nadia", 9)
        i =Person("Irfan", 10)
        j =Person("Nuni", 11)
        k =Person("Nadira", 12)
        l =Person("Ica", 13)
        m =Person("Uton", 14)
        n =Person("Fitri", 15)
        o =Person("Fikri", 16)
        p =Person("Maman", 17)
        q =Person("Adel", 18)
        r =Person("Ulul", 19)
        s =Person("Nita", 20)
        t =Person("Farida", 21)
        u =Person("Rara", 22)
        v =Person("Kenti", 23)
        w =Person("Rana", 24)
        x =Person("Syifa", 25)
        y =Person("Iyus", 26)
        z =Person("Juju", 27)
        aa =Person("Faza", 28)
        bb =Person("Rendy", 29)
        cc =Person("Lala", 30)