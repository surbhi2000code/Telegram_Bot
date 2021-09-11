from datetime import datetime
import wikipedia
import pyjokes
import pywhatkit


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if "what" in user_message:
        info = wikipedia.summary(user_message, 1)
        return str(info)

    if "who" in user_message:
        inf = wikipedia.summary(user_message, 1)
        return str(inf)

    if "how" in user_message:
        infor = wikipedia.summary(user_message, 1)
        return str(infor)

    if "play" in user_message:
        song = pywhatkit.playonyt(user_message)
        return song

    if user_message in ("who are you", "who are you?"):
        return "I am Surbhi's tele bot!"

    if user_message in ("how are you", "how are you?"):
        text = ''' Thanks for asking.
I am fine! What about you?'''
        return str(text)

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("joke", "funny"):
        music = pyjokes.get_joke()  
        return str(music) 

    if user_message in ("hello", "hi", "sup"):
        return '''Hey! How's you doing
I am Surbhi's tele bot!'''

    else:
        return "I don't understand you!"