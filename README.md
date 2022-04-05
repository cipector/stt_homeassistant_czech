# stt_homeassistant_czech
ovládání home assistanta hlasem, česky 

## použití
zatím jsem řešil pouze ON/OFF switche podle Vámi zadaných frází.
příklad : "Rožni světlo v koupelně"

a takto vypadí mé entity světel
<img align="left" src="https://github.com/cipector/stt_homeassistant_czech//blob/master/svetla.PNG?raw=true">


mycroft skill použiva fuzzy matching
https://dataladder.com/fuzzy-matching-101/

vycházel jsem z tohodle návodu: https://www.techwithtim.net/tutorials/voice-assistant/
a pro zjednodušení práce s api jsem použil ha_skill od mycroftu : https://github.com/MycroftAI/skill-homeassistant/blob/20.08/ha_client.py

## Home Assistant 
stačí vygenerovat long term token - https://www.atomicha.com/home-assistant-how-to-generate-long-lived-access-token-part-1/
