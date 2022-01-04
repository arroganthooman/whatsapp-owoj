from whatstk import WhatsAppChat
import re

def message_popper(arr):
    for i in range(6):
        arr.pop(0)

    for i in range(3):
        arr.pop(-1)

file_path = "E:/Fikri/Project/Project WhatsApp OWOJ/WhatsApp Chat with OWOJ Keluarga Amroni.txt"

chat = WhatsAppChat.from_source(filepath=file_path)


person_list = open("list.txt", 'r').readlines()
person_dict = {p.strip():set() for p in person_list}

for index, row in chat.df.iterrows():
    if index > 1:
        if "Gelombang ke-2" in row.message:
            message = row.message.split("\n")
            message_popper(message)

            for i in range(len(message)):
                message[i] = message[i].split(" ")

            for i in message:
                # try:
                    if len(i) == 4:
                        juz = i[1]
                        if i[2] == '⚪':
                            person_dict[i[3].title()].add(juz)
                        else:
                            try:
                                person_dict[i[3].title()].remove(juz)
                            except KeyError:
                                continue
                    elif len(i) == 3:
                        juz = i[1]
                        if '⚪' in i[2]:
                            # name = i[2].replace("⚪", "").strip().title()
                            name = re.sub("[^a-zA-Z]+", "", i[2]).title()
                            person_dict[name].add(juz)
                        else:
                            try:
                                # name = i[2].replace("⚪", "").strip().title()
                                name = re.sub("[^a-zA-Z]+", "", i[2]).title()
                                person_dict[name].remove(juz)
                            except KeyError:
                                continue

                # except:
                #     print(i)

for k,v in person_dict.items():
    juz_list = sorted(v)
    if len(juz_list) == 0:
        remainder = "SELESAI"
        print(k+ ":\n" + "SELESAI")
    else:
        remainder = ", ".join(juz_list)
        print(k + ":\nJuz", remainder)
    
    print()