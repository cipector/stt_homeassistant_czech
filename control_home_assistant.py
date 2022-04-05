import ha_client
# https://github.com/MycroftAI/skill-homeassistant/blob/20.08/ha_client.py
import speech_recognition as sr
# import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

_KONFIG_HA_ = {'ssl': False, 'verify': True, 'ip_address': "192.168.1.214", 'token': "tvůj long term token", 'port_number': "8123"}

_BUDICI_FRAZE_ = "hej domku"

ha = ha_client.HomeAssistantClient(config=_KONFIG_HA_)


def rekni(text):
    """
    Text to speech pomocí google
    ukládám do mp3 a poté přehravám pomocí playsound a zase mažu

    TODO udělat to do budoucna bez ukladani na HDD

    :param text: string
    :return:
    """
    tts = gTTS(text=text, lang="cs")
    cesta = r"c:\\Prace\\python_programy\\stt-homeassistant-czech\\"
    soubor = f"rekni.mp3"
    tts.save(soubor)
    playsound(cesta + soubor)
    os.remove(soubor)


def poslouchej():

    """
    Speech to text pomocí googlu (není nutno používat google)

    :return:
    """
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("poslouchám")
        audio = r.listen(source)
        stt = ""

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        stt = r.recognize_google(audio, language="cs")
        print("Google Speech Recognition thinks you said " + stt.lower())
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return stt.lower()


def main():
    """

    Budící fráze mi moc dobře nefunguje, chce to doladit, navíc se mi nelíbí řešení když by mě cokoliv nonstop poslouchalo
    a odesilalo vše co řeknu na google servery.

    V mém připadě jsem testoval se sluchátky, kde šlo ztlumovat mikrofon, tedy budící frázy nepotřebuji.

    :return:
    """

    # entity_typu = []
    ZAPNI_SLOVA = ["rožni", "zapni", "rozsviť"]
    VYPNI_SLOVA = ["zhasni", "vypni"]

    while True:
        text = poslouchej()

        if text.count(_BUDICI_FRAZE_) > 0:
            rekni("ano pane")
            text = poslouchej()

        # Když budete chtít použít budící frázi stačí tento blok if posunout o tabulator (nebo 4 mezery ;-))
        # text = "zapni žebřík v koupelně"
        if len(text) > 0:

            seznam_slov = text.split(" ")

            for slovo in seznam_slov:

                if len(slovo) < 4:
                    continue
                elif slovo in ZAPNI_SLOVA:
                    servis = "turn_on"
                    potvrzeni = "zapnula"
                elif slovo in VYPNI_SLOVA:
                    servis = "turn_off"
                    potvrzeni = "vypnula"
                elif slovo == "světlo":
                    zarizeni = slovo
                elif slovo == "žebřík":
                    zarizeni = slovo
                else:
                    mistnost = slovo

                    nalezena_entita = ha.find_entity(f"{mistnost}_{zarizeni}", "switch")

                    if nalezena_entita:
                        print(nalezena_entita["id"])
                        id_entity = nalezena_entita["id"]
                        odpoved = ha.execute_service("switch", servis, {"entity_id": f"{id_entity}"})
                        rekni(f"{zarizeni} v {mistnost} jsem {potvrzeni}")

                    else:
                        continue

                        # if odpoved.status_code == 200:
                        #     rekni(f"Rožnula jsem světlo v {}")


if __name__ == "__main__":
    main()
