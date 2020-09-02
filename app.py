from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse 
from model import Person

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

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world"

@app.route("/sms", methods=['POST'])
def reply():
    putaran = request.form.get('Body')
    
    if putaran.isdigit():
        msg = '📖LIST REKAP OWOJ📖\n'
        msg += "🕘Jam Lapor: 18.00-21.00\n\n"
        msg += f'Putaran ke-{putaran}\n'

        for person in Person.listPengaji:
            person.tambahJuz(int(putaran)%30 - 1)
        
        Person.listPengaji.sort(key=lambda x:x.juz)

        for i in Person.listPengaji:
            msg += (str(i) + "\n")
        
        msg += "\n🕋: Tilawah/Tasmi'/Tarjim\n"
        msg += "🚺: Tasmi' / Tarjim"
        resp = MessagingResponse()
        resp.message(msg)

        return str(resp)
    else:
        resp= MessagingResponse()
        resp.message("Masukkan putaran!")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)