# dataset_tts_json
**dataset.json** je vytvorený z dvoch častí  {text, audio}

audio je vo formáte .mp3

# Zostavenie datasetu na huggingface
Datasety pre modely na huggingface pre prevod textu na reč majú danú štruktúru aby boli kompatibilné s modelmi na huggingface platforme.

Veľakrát sú vo formáte text-audio a slúžia na trénovanie modelov aby generovali audio na základe textových vstupov.

Najčastejšie  sú uložené vo formáte JSON alebo JSONL, kde každý riadok predstavuje jednu položku datasetu.

Zvukové nahrávky majú najčastejšie formát .mp3 alebo .wav a sú odkázané relatívnymi cestami alebo url adresami.
