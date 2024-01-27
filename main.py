from flask import Flask, render_template, request
import qi
import codecs


import numpy as np


Listwithtxt = []
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text1.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text2.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text3.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text4.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text5.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text6.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text7.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text8.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text9.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text10.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text11.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text12.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text13.txt")
Listwithtxt.append("/home/mateusz/PycharmProjects/flaskProject1/files/text14.txt")
Listwithlinks = []
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1LVukDcCShoq4wTo5rDDKf7bT4Rm3J5uV")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=148aHnL8hUegSstGbRCxgUhsWxE5DOTx3")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1eH2EPyikWsb_dl-Z1FwPBBMjQlquERbu")
Listwithlinks.append("https://d#rive.google.com/uc?export=download&id=1HOIHkIOwXW1SJaN9VuYx7CL4H7vKa5_O")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1jJWgZia1w6NDC9jFTBUhszNOw0SXQDnK")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1SUUFskv9h4m8CJZglo_Kgp8abZy-ecTu")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=18gUX-9_t3aPhrP9OVh4V_3vxYbZ7LJc1")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1zniY5flS6cgzz80vXyqVlC-S-zD_YkP1")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1sBsncbyGTUyMfJKV_v0YQs8iIrywvG6i")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1-lhzRJzD2ePfWLw7M3CRVv4qtvPbjeJj")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1c6lfDyOrtr8EmwwsaShu936FhyzDcqGQ")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=18p_YSxXCnTI0DMJLy_Pl2mw_9U7ljG0Y")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=12_-bcxVWRDlgbMM8ChsG0ft-kTvXZlYq")
Listwithlinks.append("https://drive.google.com/uc?export=download&id=1aj7aewz-_ccM5LEY0BGkJpBR3Feh8edC")

Listforcounter = [0]


appflask = Flask(__name__)
app = qi.Application(url="tcp://192.168.0.107:9559")
app.start()
session = app.session
tts = session.service("ALTextToSpeech")
motion = session.service("ALMotion")
show = session.service("ALTabletService")
camera = session.service("ALVideoDevice")

AL_kTopCamera = 0
AL_kQVGA = 1            # 320x240
AL_kBGRColorSpace = 13
captureDevice = camera.subscribeCamera(
    "test", AL_kTopCamera, AL_kQVGA, AL_kBGRColorSpace, 10)

width = 320
height = 240
image = np.zeros((height, width, 3), np.uint8)

result = camera.getImageRemote(captureDevice)

if result == None:
    print('cannot capture')
elif result[6] == None:
    print('no image data string')
else:
    print(ord('5'))


@appflask.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'START':
            Listforcounter[-1] = 0
            show.showImage(Listwithlinks[0], _async=True)
            openfile = codecs.open(Listwithtxt[Listforcounter[-1]], encoding='utf-8')
            to_say = openfile.read()
            tts.say(to_say, _async=True)
        elif request.form.get('action2') == 'NEXT':
            Listforcounter[-1] = Listforcounter[-1]+1
            show.showImage(Listwithlinks[Listforcounter[-1]], _async=True)
            openfile = codecs.open(Listwithtxt[Listforcounter[-1]], encoding='utf-8')
            to_say = openfile.read()
            tts.say(to_say, _async=True)
        elif request.form.get('action3') == 'PREVIOUS':
            if Listforcounter[-1] == 0:
                pass
            else:
                Listforcounter[-1] = Listforcounter[-1] + -1
                show.showImage(Listwithlinks[Listforcounter[-1]], _async=True)
                openfile = codecs.open(Listwithtxt[Listforcounter[-1]], encoding='utf-8')
                to_say = openfile.read()
                tts.say(to_say, _async=True)
        elif request.form.get('action4') == 'CLEAR TABLET':
            show.hideImage()
        elif request.form.get('action5') == 'MOVE 50 CM':
            motion.moveTo(0.5, 0, 0)
        elif request.form.get('action6') == 'MOVE BY A NUMBER':
            tomoveincm = request.form.get("NUMBER")
            tomoveincm = float(tomoveincm)
            tomove = tomoveincm / 100
            motion.moveTo(tomove, 0, 0)
    return render_template("index.html")


appflask.run()
