from gtts import gTTS
from playsound import playsound
from datetime import datetime


def playaudio(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("sound.mp3")
    playsound('sound.mp3')


def removeDigits(s):
    answer = []
    for char in s:
        if not char.isdigit():
            answer.append(char)
    return ''.join(answer)


def markAttendance(name):
    with open('Attendance.csv', 'r+') as csv:
        DataList = csv.readlines()
        NameList = []
        for line in DataList:
            entry = line.split(',')
            NameList.append(entry[0])
        if name not in NameList:
            now = datetime.now()
            dtString = now.strftime('%H : %M: %S')
            csv.writelines(f'\n{name}, {dtString}')
