## Preventing duplicate code

In deze kleine demo/discussie laat je de studenten zien hoe je `get_lowest_temp()` en `get_highest_temp()` uit de opgave Temperature versimpelt. Op deze hulppagina vind je informatie over verschillende manieren om duplicate code in temperature te voorkomen. Gebruik deze informatie om de studenten uitleg te geven over dit aspect van design.

> Als je gezien hebt dat je studenten veel gebruik gemaakt hebben van de functie `.index()` kan je ook het optionele gedeelte hierover behandelen.

### .index() (optioneel)

In het bestand [`index.py`](index.py) staan een aantal functies die het probleem van het gebruik van `.index()` aankaarten. De functie `fake_index()` laat zien hoe `.index()` intern werkt: de functie loopt over de mogelijke indices in lijst die hij binnenkrijgt heen, en controleert per element of dit het element is wat gezocht wordt. Wanneer hij deze gevonden heeft returned de functie de index van het element wat gevonden is. Dit is de index van het _eerste_ element wat gelijk is aan de waarde die gezocht wordt.

Buiten de toevoeging van extra complexiteit aan de code betekent dit dat er fundamentele problemen zijn die niet opgelost kunnen worden met `.index()`. Bijvoorbeeld als we het tweede, derde, laatste, etc. element uit een lijst willen hebben dat voldoet aan een bepaalde conditie. In dit soort gevallen is het eigenlijk altijd beter om in plaats van over de elementen van een lijst te loopen en dan de index terug te zoeken, direct de over de mogelijke indices van de lijst te loopen. (Hierover is ook een informatiepagina, <https://pdp.proglab.nl/python/en/loops/element-vs-index>)

Een voorbeeld hiervan is de functie `find_last_summerday()`. Hierin staat een stuk code uitgecomment dat het verkeerde resultaat teruggeeft in de specifieke situatie dat de temperatuur die op de laatste zomerdag plaatsvond meerdere keren in de lijst voorkomt. Een aantal van de studenten zal vast tegen een versie van dit probleem aangelopen zijn. De oplossing is simpel: houd vanaf het begin al de index bij, zodat je die kan gebruiken voor beide lijsten.

### Minimum and maximum temperatuur

Voor de opgave _Temperature_ hebben de studenten twee functies moeten schrijven: een functie die de laagste temperatuur en bijbehorende datum vind (`get_lowest_temp()`), en een functie die de hoogste temperatuur en bijbehorende datum vind (`get_highest_temp()`). De code voor deze twee functies lijkt heel erg op elkaar, en komt waarschijnlijk voor de meeste studenten neer op één tekentje verschil. Je kunt beginnen met de vraag of dit opgevallen is tijdens de code review, en of iemand een idee heeft voor een oplossing.

Begin met het laten zien wat precies het verschil is tussen het verkrijgen van de laagste en hoogste temperaturen:

    lowest_temp = temps[0]

    for i in range(len(temps)):
        temp = temps[i]

        if temp < some_temp:
            lowest_temp = temp
            lowest_temp_date = dates[i]

    highest_temp = temps[0]

    for i in range(len(temps)):
        temp = temps[i]

        if temp > highest_temp:
            highest_temp = temp
            highest_temp_date = dates[i]

Als we dit generiek willen maken kunnen we twee dingen doen: we kunnen afhankelijk van een boolean kiezen of we het groter of kleiner dan teken gebruiken, of we kunnen aan de functie een functie meegeven die de vergelijking doet. Leg dit aan de studenten uit en probeer iedereen te laten denken over de voor en nadelen van beide oplossingen. De boolean oplossing ziet er als volgt uit:

    def get_temp_boolean(dates, temps, get_lowest):
        """
        This function will get either the lowest or the highest temperature depending on the boolean `get_lowest`. When it is set to True the lowest temperature is returned, on False the highest temperature is returned.
        """

        some_temp = temps[0]

        for i in range(len(temps)):
            temp = temps[i]

            if get_lowest:
                if temp < some_temp:
                    some_temp = temp
                    some_date = dates[i]
            else:
                if temp > some_temp:
                    some_temp = temp
                    some_date = dates[i]

        return some_date, some_temp


Deze oplossing is nog steeds niet helemaal "duplicaatvrij" en we zouden dit op kunnen lossen door het volgende te doen:

    def get_temp_boolean(dates, temps, get_lowest):
        """
        This function will get either the lowest or the highest temperature depending on the boolean `get_lowest`. When it is set to True the lowest temperature is returned, on False the highest temperature is returned.
        """

        some_temp = temps[0]

        for i in range(len(temps)):
            temp = temps[i]

            if (get_lowest and temp < some_temp) or (not get_lowest and temp > some_temp):
                some_temp = temp
                some_date = dates[i]

        return some_date, some_temp

Dit is een net iets nettere oplossing, maar maakt de regel die beslist wanneer een temperatuur onthouden wordt aardig ingewikkeld.

Een ander alternatief is het gebruik van een techniek die de studenten in module 3 geleerd hebben: het meegeven van een functie als een argument aan een andere functie. Een voorbeeld hiervan is gegeven in [`minmax.py`](minmax.py). Hiervoor definiëren we twee functies `is_smaller()` en `is_bigger()` die door middel van een boolean aangeven of het eerste argument kleiner/groter is dan het tweede argument. We kunnen nu een algemene functie schrijven die doormiddel van een meegegeven vergelijkingsfunctie twee elementen, A en B, met elkaar vergelijkt. Als de vergelijkingsfunctie `True` teruggeeft, onthouden we element A, anders blijven we element B onthouden.

Hiermee voorkomen we dubbele code, en als we alle functies (en variabelen) goede namen geven blijft de code ook nog goed te begrijpen. Neem bijvoorbeeld de regel code uit `get_lowest_temp()`: `return get_temp_and_date(dates, temps, is_smaller)`. Het is duidelijk dat er een functie uitgevoerd wordt die de temperatuur en datum terug geeft uit een verzameling `dates` en `temps` en dat daarvoor `is_smaller` wordt gebruikt. Een nadeel van deze methode is dat het niet per se direct duidelijk is dat `is_smaller` een functie is. Dit, maar ook dat we de functionaliteit over drie verschillende functies verspreid hebben maakt het lastiger om overzicht te krijgen.
