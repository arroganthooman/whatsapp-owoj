from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse 
from model import Person


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world"

@app.route("/sms", methods=['POST'])
def reply():
    putaran = request.form.get('Body')
    
    if putaran.isdigit():
        msg = "بـــــــسم اللّـــــــه الرّحمن الرّحيـــــــم"
        msg += '\n\n📖LIST REKAP OWOJ📖\n'
        msg += "🕘Jam Lapor: 18.00-21.00\n\n"
        msg += f'Putaran ke-{putaran}\n'

        Person.aktifkan()

        for person in Person.listPengaji:
            person.tambahJuz(int(putaran)%30 - 1)
        
        Person.listPengaji.sort(key=lambda x:x.juz)

        for i in Person.listPengaji:
            msg += (str(i) + "\n")
        
        msg += "\n🕋: Tilawah/Tasmi'/Tarjim\n"
        msg += "🚺: Tasmi' / Tarjim"

        Person.listPengaji.clear()    
        resp = MessagingResponse()
        resp.message(msg)

        return str(resp)

    else:
        resp= MessagingResponse()
        resp.message("Masukkan putaran!")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)