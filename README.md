# dataset_tts_json
**dataset.json** je vytvorený z dvoch častí  {text, audio}

Audio je vo formáte .mp3

JSON formát je vytvorený pre ukážku

# metadata.csv

Bolo použité na nahranie datasetu na huggingface

Je uložene spolu s audio nahravkami v jednom priečinku

Audio je vo formáte .mp3

Medatata.csv sa skladá z dvoch sĺpcov {file_name, text}

File_name je názov audio nahravky

Text je textový formát audia

Na nahratie som použil skript data_loader.py, ktorý sa nachádza v repozitáry 


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
