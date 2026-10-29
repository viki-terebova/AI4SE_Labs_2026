# Uloha 1

AI asistent bol poziadany, aby precital poziadavky projektu RentYourExpert a pocas diskusie zapisoval hlavne poznamky. Nasleduje zhrnutie diskusie o troch navrhnutych architekturach.

## Zhrnutie poziadaviek

RentYourExpert je webova platforma, ktora spaja zakaznikov s odbornikmi. Pouzivatelia maju tri roly: zakaznik, odbornik a administrator.

System ma podporovat:

- registraciu, prihlasenie a spravu profilu,
- vyhladavanie odbornikov podla zrucnosti a lokality,
- odosielanie a spracovanie poziadaviek na sluzby,
- otazky zakaznikov a odpovede odbornikov,
- pridavanie, upravu a mazanie hodnoteni,
- administraciu pouzivatelov, poziadaviek, otazok a hodnoteni.

Poziadavky neurcuju pocet pouzivatelov, ocakavanu zataz ani velkost vyvojoveho timu. AI preto ako pracovny predpoklad pouzil beznu webovu aplikaciu vyvijanu mensim timom.

## Navrh 1 - Vrstveny monolit

Cely backend tvori jedna aplikacia s jednou relacnou databazou. Zdrojovy kod je rozdeleny na prezentacnu, aplikacnu a datovu vrstvu.

Po prijati HTTP poziadavky ju kontroler odovzda aplikacnej sluzbe. Sluzba vykona obchodne pravidla a pomocou datovej vrstvy ulozi zmenu do databazy. Rovnakym sposobom sa riesia ucty, profily, poziadavky aj hodnotenia.

### Vyhody

- jednoducha implementacia a nasadenie,
- jedna databaza a jednoduche transakcie,
- lahke lokalne spustenie a testovanie,
- centralne riesene prihlasovanie a opravnenia.

### Nevyhody

- jednotlive funkcie sa mozu silno previazat,
- aplikacne sluzby mozu casom prilis narast,
- zmena jednej casti moze ovplyvnit cely system,
- vrstvy neurcuju, kto vlastni konkretne obchodne pravidla.

### Problemy pri implementacii

Najvacsim problemom je mazanie udajov, ktore spolu suvisia. Pri odstraneni odbornika treba vyriesit jeho poziadavky, otazky a hodnotenia. Bez jasnych hranic moze administracia obchadzat obchodne pravidla a menit udaje priamo.

## Navrh 2 - Modularny monolit

Backend je stale jedna aplikacia, ale je rozdeleny podla funkcnych oblasti:

- Pouzivatelia a opravnenia,
- Katalog odbornikov,
- Poziadavky na sluzby,
- Otazky a odpovede,
- Hodnotenia,
- Administracia.

Kazdy modul obsahuje vlastne pravidla a spravuje svoje databazove tabulky. Ostatne moduly s nim komunikuju cez definovane rozhranie. Cela aplikacia sa nasadzuje naraz a pouziva jednu databazu.

Pri vytvoreni poziadavky modul Poziadavky overi prihlaseneho zakaznika, existenciu odbornika a ulozi poziadavku v stave `CAKA`. Odbornik ju moze neskor prijat alebo odmietnut. Vsetky zmeny stavu riadi ten isty modul.

### Vyhody

- jednoduche nasadenie jednej aplikacie,
- jasne rozdelenie zodpovednosti,
- jednoduche databazove transakcie,
- mensie riziko neprehladneho a prepojeneho kodu,
- moznost neskor oddelit vybrany modul.

### Nevyhody

- moduly sa nedaju nasadzovat samostatne,
- cela aplikacia sa skaluje ako jeden celok,
- dodrziavanie hranic modulov zavisi od discipliny a testov.

### Problemy pri implementacii

Moduly nesmu priamo menit cudzie tabulky. Zlozitejsie operacie, napriklad odstranenie pouzivatela, sa musia koordinovat cez ich verejne rozhrania. Dolezite su aj testy opravneni, aby odbornik nemohol spracovat poziadavku urcenu inemu odbornikovi.

## Navrh 3 - Mikrosluzby

System je rozdeleny na viac samostatnych sluzieb, napriklad sluzbu pouzivatelov, katalogu, poziadaviek, komunikacie a hodnoteni. Kazda sluzba ma vlastnu databazu. Klient komunikuje so systemom cez API branu.

Sluzby medzi sebou komunikuju pomocou HTTP volani alebo sprav. Pri vytvoreni poziadavky musi sluzba poziadaviek overit pouzivatela aj odbornika v inych sluzbach.

### Vyhody

- kazda sluzba sa moze nasadit a skalovat samostatne,
- chyba v jednej sluzbe nemusi zastavit cely system,
- jednotlive sluzby mozu vyvijat samostatne timy.

### Nevyhody

- zlozitejsie nasadenie, monitorovanie a testovanie,
- viac sietovej komunikacie a moznosti zlyhania,
- narocnejsie udrziavanie konzistentnych udajov,
- vyssie prevadzkove naklady.

### Problemy pri implementacii

Jedna pouzivatelska operacia moze prechadzat cez viac sluzieb. Ak niektora sluzba neodpoveda, treba pouzit casove limity a opakovanie poziadaviek. Spravy mozu prist viackrat alebo v nespravnom poradi. Vyvojari musia riesit aj centralizovane logovanie a sledovanie chyb medzi sluzbami.

## Porovnanie

| Kriterium | Vrstveny monolit | Modularny monolit | Mikrosluzby |
|---|---|---|---|
| Narocnost vyvoja | nizka | nizka az stredna | vysoka |
| Prehladnost funkcnych oblasti | stredna | vysoka | vysoka |
| Databazove transakcie | jednoduche | jednoduche | zlozite |
| Nasadenie | jednoduche | jednoduche | zlozite |
| Samostatne skalovanie | nie | nie | ano |
| Vhodnost pre RentYourExpert | dobra | najlepsia | zatial zbytocne zlozita |

## Zaver

Pre RentYourExpert je najvhodnejsi **modularny monolit**. Zachovava jednoduche nasadenie a transakcie, ale zaroven oddeluje hlavne casti systemu. Mikrosluzby by priniesli vyhody az pri velkej zatazi alebo viacerych samostatnych timoch, co zo zadania nevyplyva.
