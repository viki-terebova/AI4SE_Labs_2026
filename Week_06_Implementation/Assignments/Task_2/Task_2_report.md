# Uloha 2

Kazdy zdrojovy Python subor sa rozdeli na useky s najviac 100 riadkami. Tato velkost obsahuje dostatok suvisiaceho kodu a pri tomto malom repozitari nie je prilis velka. Susedne useky maju 10 spolocnych riadkov, aby sa pri deleni nestratila suvislost. Jeden usek obsahuje kod iba z jedneho suboru.

Skript `chunk_repository.py` uklada useky do suboru `chunks.json`. Kazdy zaznam obsahuje oznacenie, cestu k suboru, cisla riadkov a obsah useku.
