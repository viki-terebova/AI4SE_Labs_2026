---
name: navrh-architektury
description: Analyzuje poziadavky na softver, porovna vhodne architektonicke riesenia, vyberie jedno z nich a vytvori ADR. Pouzi pri navrhu architektury alebo dokumentovani architektonickeho rozhodnutia.
---

# Navrh architektury a ADR

## Postup

1. Z poziadaviek vyber akterov, hlavne funkcie, dolezite udaje, integracie a bezpecnostne poziadavky. Fakty oddel od predpokladov a neznamych informacii.
2. Navrhni aspon tri rozdielne a realne architektury. Pri kazdej uved komponenty, tok poziadavky, sposob nasadenia, ulozenie udajov, vyhody, nevyhody a narocne casti implementacie.
3. Moznosti porovnaj podla rovnakych kriterii odvodenych z poziadaviek. Ziadnu moznost zamerne nezjednodusuj iba preto, aby vybrane riesenie vyzeralo lepsie.
4. Odporuc jedno riesenie a vysvetli, preco su jeho nevyhody prijatelne. Chybajuce informacie oznac ako predpoklady.
5. Vytvor ADR, ktore obsahuje stav, kontext, rozhodovacie kriteria, posudzovane moznosti, rozhodnutie, strucnu schemu, vlastnictvo udajov, bezpecnostne hranice, dosledky, rizika a podmienky opatovneho posudenia.
6. Skontroluj, ci ma kazda hlavna poziadavka zodpovedajuci komponent a ci ADR zodpoveda predchadzajucemu porovnaniu.

## Pravidla

- Nevymyslaj poziadavky na vykon, rozpocet, dostupnost ani velkost timu.
- Nezamienaj architektonicky styl s vyberom konkretnej technologie.
- Vysvetli transakcie, opravnenia, spracovanie chyb a konzistenciu udajov tam, kde ovplyvnuju rozhodnutie.
- Mikrosluzby neodporucaj iba na zaklade mozneho buduceho rastu. Zohladni ich prevadzku, komunikaciu, opakovanie sprav a distribuovane udaje.
- Pouzi kratku porovnavaciu tabulku a iba taky diagram, ktory zlepsuje pochopenie navrhu.
- Pis jednoducho a rozsah prisposob poziadavke pouzivatela.
