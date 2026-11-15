# Uloha 3

Pre kazdy usek sa vytvori embedding s 1024 hodnotami. Text sa rozdeli na slova. SHA-256 urci, do ktorej casti embeddingu sa kazde slovo zapocita. Nakoniec sa hodnoty upravia na rovnaku mierku, aby sa dali embeddingy porovnavat.

Embedding sa vytvara z cesty k suboru a z obsahu useku. Cesta pomaha, ked zadanie obsahuje nazov suboru, triedy alebo modulu. Riesenie nepotrebuje externu sluzbu ani API kluc a pri kazdom spusteni vytvori rovnaky vysledok.

Skript `create_embeddings.py` cita `chunks.json` a vytvara `embeddings.json`. Kazdy zaznam obsahuje povodny usek a jeho embedding. Pre tento maly repozitar je subor JSON postacujuci.
