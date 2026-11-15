# Uloha 5

Skript `solve_tasks.py` nacita zadania z `missing_code.json`. Pre kazde zadanie vyberie 5 najpodobnejsich usekov a posle ich so zadanim modelu `gpt-6-luna` cez OpenAI API. Vrateni kod zapise do urceneho suboru.

Vysledok testov:

```text
Ran 481 tests in 0.057s
FAILED (failures=1)
```

Zlyhal test, ktory ocakava, ze sklad obsahuje polozku aj pri nulovom stave. Zadanie vsak pozaduje kladny stav, preto kod vracia `False`.
