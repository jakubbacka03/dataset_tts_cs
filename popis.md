# dataset_tts_json
**dataset.json** je vytvorený z dvoch častí  {text, audio}

audio je vo formáte .mp3

# metadata.csv

bolo použité na nahranie datasetu na huggingface

je uložene spolu s audio nahravkami v jednom priečinku

audio je vo formáte .mp3

medatata.csv sa skladá z dvoch sĺpcov {file_name, text}

file_name je názov audio nahravky

text je textový formát audia

na nahratie som použil skript data_loader.py, ktorý sa nachádza v repozitáry 


# Zostavenie datasetu na huggingface
Datasety pre modely na huggingface pre prevod textu na reč majú danú štruktúru aby boli kompatibilné s modelmi na huggingface platforme.

Veľakrát sú vo formáte text-audio a slúžia na trénovanie modelov aby generovali audio na základe textových vstupov.

Najčastejšie  sú uložené vo formáte JSON alebo JSONL, kde každý riadok predstavuje jednu položku datasetu.

Zvukové nahrávky majú najčastejšie formát .mp3 alebo .wav a sú odkázané relatívnymi cestami alebo url adresami.

Na nahratie datasetu na huggingface je viacero možnosti.

Jedná z nich je cez python skript

Návod na nahratie: https://huggingface.co/docs/datasets/audio_load

1. Treba si vytvoriť Access Token a dať mu read-write práva

2. pripraviť si data

dataset/
├── common_voice_cs_20424365.mp3
├── common_voice_cs_20424366.mp3
├── ...
└── metadata.csv

 csv sa musí volať metadata.csv a v nej sa musí nachádzať stĺpec file_name

3. napísanie skriptu viz. data_loader.py

