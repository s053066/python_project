import speech_recognition as sr
import webbrowser
import time
from time import ctime
import playsound
from gtts import gTTS
import random
import os

# 音声認識インスタンス
r = sr.Recognizer()

# マイクで話したことがどう認識されたか出力
def record_audio(ask=False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='ja-JP')
            print(voice_data)
        except sr.UnknownValueError:
            speak('何と言ったかわかりません')
        except sr.RequestError:
            speak('音声認識が起動していません')
        return voice_data

# 引数の文字列を話す
def speak(audio_string):
    tts = gTTS(text=audio_string,lang='ja')
    r = random.randint(1,1000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file) 

# 応答する
def respond(voice_data):
    # 名前を教えて？
    if '名前を教えて' in voice_data:
        speak('私の名前はアルファです')
    # 今何時？
    if '今何時' in voice_data:
        print('今の時間は' + ctime())
    # 検索して
    if '検索して' in voice_data:
        search = record_audio('what do you search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search )
    # 場所を教えて
    if '場所を教えて' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        print('Here is the location of ' + location )
    if '終了' in voice_data:
        exit()
    
time.sleep(1)
speak('何をしましょうか？')
while 1:
    voice_data = record_audio()
    respond(voice_data)

