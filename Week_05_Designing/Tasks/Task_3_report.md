# Uloha 3

## Vytvoreny skill

Pred vytvorenim skillu AI asistent precital zaznamy z Ulohy 1 a Ulohy 2 a identifikoval opakujuce sa kroky.

V repozitari bol vytvoreny skill `navrh-architektury`. Jeho ulohou je:

- vybrat z poziadaviek informacie dolezite pre architekturu,
- navrhnut aspon tri realne moznosti,
- vysvetlit ich vyhody, nevyhody a problemy implementacie,
- porovnat moznosti podla rovnakych kriterii,
- vybrat riesenie a vytvorit ADR.

## Prve vypracovanie bez skillu

Pri prvom vypracovani bolo potrebne samostatne urcit strukturu porovnania. Niektore dolezite casti, napriklad vlastnictvo udajov, opravnenia, diagram a podmienky zmeny rozhodnutia, sa doplnili az pri dalsich upravach ADR.

## Nove vypracovanie so skillom

V novom spusteni bol skill pouzity na rovnake poziadavky RentYourExpert. Najprv oddelil fakty od predpokladov, potom pripravil tri architektury podla rovnakych kriterii a nakoniec vytvoril strukturu ADR.

Uz prvy navrh obsahoval moduly, pracu s udajmi, bezpecnostne pravidla, dosledky rozhodnutia a podmienky jeho buduceho prehodnotenia. Potrebna bola iba kontrola strucnosti a zrozumitelnosti textu.

## Porovnanie

| Oblast | Bez skillu | So skillom |
|---|---|---|
| Zaciatok prace | bolo potrebne navrhnut postup | postup bol urceny vopred |
| Navrhy architektur | detaily sa doplnali postupne | vsetky moznosti mali rovnaku strukturu |
| Predpoklady | bolo ich potrebne dodatocne pomenovat | boli oddelene od faktov na zaciatku |
| ADR | potreboval viac obsahovych uprav | hlavne casti boli pripravene hned |
| Kontrola vysledku | manualna kontrola diskusie a ADR | skill vyzadoval kontrolu suladu |
| Celkova praca | viac opakovanych krokov | menej opakovania a rychlejsi vysledok |

## Zaver

Pouzitie skillu zrychlilo vypracovanie, pretoze nebolo potrebne znovu vymyslat postup ani strukturu ADR. Vysledok bol uplnejsi uz v prvej verzii. Kontrola clovekom je vsak stale potrebna, najma ak zadanie neobsahuje informacie o zatazi, rozpocte alebo velkosti timu.
