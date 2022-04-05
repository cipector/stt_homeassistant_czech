# stt_homeassistant_czech
ovládání home assistanta hlasem a česky, prostě jak nám zobák narostl

## použití
zatím jsem řešil pouze ON/OFF switche podle Vámi zadaných frází.
příklad : "Rožni světlo v koupelně"

## takto vypadají mé entity světel
<img src="https://github.com/cipector/stt_homeassistant_czech//blob/master/svetla.PNG?raw=true">


## mycroft skill použiva fuzzy matching
https://dataladder.com/fuzzy-matching-101/

vycházel jsem z tohodle návodu: https://www.techwithtim.net/tutorials/voice-assistant/

a pro zjednodušení práce s api jsem použil ha_skill od mycroftu : https://github.com/MycroftAI/skill-homeassistant/blob/20.08/ha_client.py

## Home Assistant 
stačí vygenerovat long term token - https://www.atomicha.com/home-assistant-how-to-generate-long-lived-access-token-part-1/

kdyby to někoho nadchlo natolik, že by mi chtěl pomoct s kodem a rozšířit o další funkce z home assistantu budu jedine rád 
