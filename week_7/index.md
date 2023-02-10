## Werkcollege week 7

Het laatste werkcollege voor het tentamen, maar tegelijkertijd ook direct het laatste werkcollege van dit blok! We bespreken kort het tentamen, benadrukken de belangrijkheid van het oefenen van Numpy en het gebruik van API's (dit komt in de vervolgcursussen heel vaak voor). 

### Terugblik (15 minuten)

Laat iedereen even vertellen hoe het ging, waar het knelde en of het gelukt is. We bespreken hier openlijk hoe het gaat. Zeg tegen je studenten dat klagen ook OK is, dat kan hier heel goed een onderdeel van zijn, en zeg dat je goed zult luisteren en noteren (beloof niet dat je er iets mee gaat doen! Het gaat vooral om luisteren, bespreekbaar maken en het totaalbeeld). Hier kan je ook de open vragen van Machine Learning extra bespreken.

⚠️ Jij als mentor moet het gesprek leiden, zorg dat iedereen aan de beurt komt!

- Nog opvallende dingen over specifieke studenten? Noteer ze op Basecamp!
- Nog dingen die mis lijken te gaan voor meerdere studenten? Noteer ze en deel ze na de werkgroep meteen met het team via een message in Basecamp.

### Terugblik Numpy (5--? minuten)

Doel: Controle dat alle studenten deze oefenopgaven voor Numpy zorgvuldig gemaakt en begrepen hebben.

De studenten hebben aan het begin van module 6 een introductie gedaan van een aantal Numpy concepten. Het begrip van deze concepten is **essentieel** voor k-means en een aantal andere toekomstige modules. Het is belangrijk dat de studenten dit serieus maken en begrijpen.

Vraag de studenten of er bepaalde concepten zijn die ze moeilijk vonden in de oefeningen. Geef extra uitleg waar nodig.

### Hoe lees je een API (5--10 minuten)

Doel: De studenten helpen bij het navigeren en interpreteren van API's.

Pak een voorbeeld van een functie, en laat zien hoe je dit googled. Voor de functie `read_csv` uit `pandas` kan je bijvoorbeeld googlen op `'read_csv pandas API'`. In de API staat een hoop tekst over de verschillende mogelijkheden en functionaliteiten van de `read_csv` functie. Leg uit:

- Allereerst zien we alle mogelijke parameters (op volgorde dat ze ingevoerd moeten worden), met hun "default" waardes. `delimiter=None` geeft bijvoorbeeld aan dat de _optionele parameter_ `delimiter` standaard de waarde `None` toegewezen krijgt.
- Direct hieronder zien we een kort stukje uitleg van wat de basisfunctionaliteit van deze functie is. In dit geval begint deze uitleg met 'Read a comma-separated values (csv) file into DataFrame.'.
- Vervolgens krijgen we een lijst met alle mogelijke parameters en het type dat verwacht wordt voor de functie. Voor `sep` staat er `str, default ‘,’`. Dit houdt in dat als je deze waarde wilt aanpassen, het een string moet zijn, en dat de standaardwaarde waarmee `read_csv` de velden in de inputfile van elkaar onderscheid een komma is. Daarna volgt nog wat extra informatie over wat verschillende waardes betekenen. Laat de studenten zien hoe ze dit moeten lezen, en leg ook uit hoe dit werkt voor bijvoorbeeld de parameter `header`.
- Als je een (flink) stuk naar beneden scrolt, kan je ook zien wat de functie `return`ed. In dit geval is dat `DataFrame or TextParser`. Dit kan heel handig zijn om te zien of een functie iets terug geeft (dit noemen we expliciet), of dat de functie iets in de originele structuur aanpast (impliciet, of in pandas ook wel `in_place` genoemd).
- Helemaal onderaan zie je ook een reeks voorbeelden voor hoe de functie gebruikt kan worden. Bij `read_csv` is dit er maar één, maar als je ook het voorbeeld van `groupby` laat zien heb je er hier veel meer!
- Doe hetzelfde voor een functie in Seaborn. Gebruik hiervoor de gallerij: <https://seaborn.pydata.org/examples/index.html>

Vraag de studenten of ze zelf functies hebben gezien die ze nog niet helemaal begrijpen, pak de API er bij, laat de voorbeelden zien en leg uit wat de functie doet.

### Tentamen (5--10 minuten)

Doel: Duidelijkheid over het verloop van het tentamens voor PDP en ML, en ook de planning van de tentamenweek.

Voor PDP bestaat het tentamen uit een reeks kleine programmeeropgaven gebaseerd op de modules uit het vak. De studenten krijgen 2.5 uur de tijd om de problemen uit te werken _op hun eigen laptop_ en mogen tijdens het tentamen gebruik maken van pdp.proglab.nl.

- Er is een overzichtspagina met alle belangrijke onderdelen van de cursus: <https://pdp.proglab.nl/exam>
- Het is niet toegestaan andere bronnen te gebruiken dan onze website.
- Er is geen gelegenheid tot assistentie tijdens het tentamen.
- De code zal niet beoordeeld worden op design of style, maar alleen op correctheid.
- Voorbeeldcode met voorbeeldoutput wordt gegeven.
- Het tentamen is pass/fail, en het is niet nodig om alles goed te hebben voor een pass.

Om de studenten een idee te geven van hoe het tentamen er uit ziet zullen ze de maandag van de tentamenweek een oefententamen maken wat daarna uitgebreid wordt besproken. Dit oefententamen doen we in _exact_ dezelfde setting als het echte tentamen; 2.5u, geen andere bronnen, geen hulp, eigen laptop, etc..

Dinsdag is het echte tentamen voor PDP.

Op woensdag doen we van 11:00 tot 13:00 een Q & A voor het tentamen van ML. Hier zullen we alle vragen beantwoorden over de stof van machine learning.

Het materiaal voor het ML1 tentamen bestaat uit alles wat behandeld is in de theorievideos en de programmeernotebooks. De theoriepagina’s van SOWISO en de artikelen uit de schrijfopgaven zijn geen onderdeel van het tentamenmateriaal. De focus van het tentamen zal liggen op het begrijpen van het materiaal en niet het uit je hoofd kennen van vergelijkingen. Dit betekent dat de student niet gevraagd zal worden om van een algoritme de wiskundige vergelijkingen op te schrijven, maar wel dat ze gevraagd kunnen worden om de termen in een vergelijking te benoemen en uit te leggen hoe ze relateren aan een stukje machine learning theorie. De student zal geen afgeleide van een vergelijking hoeven bepalen, maar wel uit moeten kunnen leggen wat een gradiënt is en hoe die gebruikt kan worden om de kostenfunctie van een model te optimaliseren. Voor dit tentamen krijgen studenten 3u de tijd, en mogen ze geen gebruik maken van externe bronnen.

Beantwoord de vragen van de studenten over het tentamen. Als je iets niet (zeker) weet, noteer dit dan in een message op Basecamp. De coördinator zorgt ervoor dat jij (en de studenten) antwoord krijgen op hun vragen.

### Algorithmic Bias (30 minuten)

Doel: iedereen krijgt de mogelijkheid om te praten en te discussiëren over een onderwerp uit de schrijfopdrachten.

Studenten zijn vaak benieuwd naar wat andere hebben geschreven over de schrijfopdracht en vinden het leuk hierover ideeën uit te wisselen en met elkaar in discussie te gaan. De rol van de mentor is om dit te faciliteren en het gesprek een beetje op gang te krijgen.

> Als er weinig interesse is om de schrijfopgave te bespreken, is het ook prima om door te gaan naar het volgende onderdeel van het werkcollege; niet elke week is even interessant, ook dat kan van groep tot groep verschillen. Je hoeft dit gesprek dus niet te forceren.

Dit werkcollege praten en discussiëren we klassikaal over de schrijfopdracht van de vorige week. De studenten mogen hier zelf voor een groot deel invulling aan geven. Als mentor is jouw rol in dit gesprek om mee te luisteren, het gesprek gaande te houden, en de gemoederen niet te hoog te laten oplopen. Je mengt je hierbij zo min mogelijk in het gesprek zelf. Om de boel op gang te helpen hebben we per schrijfopdracht een lijst onderwerpen/discussiepunten.

- Houd tijdens het gesprek het hoofdonderwerp in de gaten. Als deelnemers (te ver) afwijken, grijp dan in.
- Je hoeft het gesprek niet te beperken tot de gegeven onderwerpen/discussiepunten. Wanneer de studenten het over iets anders willen hebben wat ook gerelateerd is aan het hoofdonderwerp is dat prima! Ook hoef je ze niet op volgorde af te gaan; bedenk zelf welk onderwerp/discussiepunt op het moment het best in het gesprek past.
- Als het gesprek dreigt te stokken, stel dan nieuwe vragen of geef een nieuw onderwerp/discussiepunt aan.
- Wanneer iemand zijn mening niet duidelijk verwoordt, stel dan vragen om verduidelijking te krijgen.
- Niet iedereen die meedoet hoeft wat te zeggen, maar zorg er wel voor dat iedereen die dat wilt aan het woord kan komen. Soms kan het nodig zijn dat je een specifiek persoon om een mening moet vragen.

⚠️ Deelname aan de gesprekken over de schrijfopdrachten is niet verplicht voor de studenten. Studenten kunnen er zelf voor kiezen om met iets anders aan de slag te gaan. Geef bij de studenten die niet meedoen duidelijk aan dat half-meedoen geen optie is, en dat jij zelf niet beschikbaar bent voor vragen. Je bent zelf namelijk nodig bij het gesprek.

De onderstaande vragen dienen als suggesties/inspiratie om de discussie op gang te krijgen. Je kunt natuurlijk je eigen vragen stellen. Als het gesprek loopt of de studenten hun opdrachten aan het bespreken zijn, hoef je ook niet per se alle vragen langs te gaan.

- Rondvraag bij de studenten: Geef korte omschrijving van het artikel en de bias die je hebt gevonden.
    - Waren jullie verbaasd over de gevallen die je gevonden hebt of hadden jullie hier al eerder van gehoord?
- Was er iemand die twijfelde tussen selection of historic bias voor hun artikel?
    - Bespreek die gevallen met de groep (hier hoeft geen "goed" antwoord uit te komen, soms zijn er effecten van beiden)
- Was er iemand bij wiens artikel de bias heel makkelijk of juist heel moeilijk te voorkomen had kunnen worden door de ontwikkelaars?
    - Bespreek die gevallen met de groep (hier hoeft ook geen "goed" antwoord uit te komen, vaak is dit lastig in te schatten op basis van het artikel)

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Als je al snel problemen voorziet met een student, bijvoorbeeld als die zegt 3 dagen per week te werken terwijl deze de minor fulltime doet, maak dan ook een TODO aan voor de coördinator. Een van je taken is om zo vroeg mogelijk te signaleren dat er mogelijk iets mis gaat.
- Update het logboek op basecamp. Schrijf bij iedere student op hoe het met ze gaat. Wanneer er geen veranderingen zijn bij een student hoef je ook niets te veranderen in het logboek.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
