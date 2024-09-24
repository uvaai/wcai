## Werkcollege week 4

We bespreken de afgelopen week. Daana gaan we, met een korte pauze ertussen, twee code reviews doen. De eerste gaat over football analysis, waarin de focus ligt op het herschrijven en opdelen van de code. In de tweede code-review, over Temperature, gaat het over alle tot nu toe behandelde design en style-aspecten. De feedback hieruit kunnen de studenten meenemen voor module 4.

De [slides](https://docs.google.com/presentation/d/133YaZvgRkFLStt4zGnrCSD4h_GFBP0DgCSo2KPvHZbU/edit?usp=drive_link) van deze week.

### Terugblik (15 minuten)

Laat iedereen even vertellen hoe het ging, waar het knelde en of het gelukt is. We bespreken hier openlijk hoe het gaat. Zeg tegen je studenten dat klagen ook OK is, dat kan hier heel goed een onderdeel van zijn, en zeg dat je goed zult luisteren en noteren (beloof niet dat je er iets mee gaat doen! Het gaat vooral om luisteren, bespreekbaar maken en het totaalbeeld). Hier kan je ook de open vragen van Machine Learning extra bespreken.

⚠️ Jij als mentor moet het gesprek leiden, zorg dat iedereen aan de beurt komt!

- Nog opvallende dingen over specifieke studenten? Noteer ze op Basecamp!
- Nog dingen die mis lijken te gaan voor meerdere studenten? Noteer ze en deel ze na de werkgroep meteen met het team via een message in Basecamp.

### Code review football analysis (20 min)

**We reviewen in deze codereview `football_analysis` uit module 3 van PDP.** Studenten die alleen ML1 doen kunnen hier meekijken met andere studenten, maar hoeven dat niet te doen.

Doel: Studenten zien andere aanpakken dan die van hunzelf. Ze leren te discussiëren over code en zich uit te drukken in aspecten die relateren aan programmeren.

We bespreken de oefening/opdracht football analysis waarbij de studenten code kregen van matig ontwerp die ze aan moesten passen naar een beter ontwerp.

- Je hebt net al wat uitleg gegeven over de aspecten (vorige week bij Design benoemd, met hieronder wat specifieke toevoegingen).
- We doen code reviews in tweetallen. Is er een oneven aantal studenten? Dan mag er één drietal zijn. Zorg ervoor dat je andere tweetallen maakt dan de vorige keer.
- Studenten werken samen, hardop denkend, achter één computer met de code die op dat moment gereviewd wordt. Als dit klaar is, wisselen ze naar de volgende computer voor het stuk code van de ander.
- (5 minuten) We beginnen met een klassikaal deel over de opgave waarover de code review gaat:
  - Wat moest er ook alweer gebeuren in de opgave?
  - Wat was er moeilijk?
  - Zijn er dingen die de assistent tijdens het nakijken zijn opgevallen, en waar specifiek op gelet kan worden?
- (10 minuten) Iedereen voert de code review uit, mentor loopt langs en bemoeit zich er soms mee, maar is vooral bezig met kritisch luisteren.
- (5 minuten) Vraag een aantal tweetallen of er specifieke dingen zijn geweest die hun opgevallen zijn. Probeer deze te relateren aan de opgaves die de studenten deze week in moeten leveren.

Het verwerken van data is altijd een beetje "messy". Dat betekent natuurlijk niet dat we niet ons best kunnen doen om het overzichtelijk te maken! De voorbeeldcode uit de opgave heeft eigenlijk 3 grote problemen:

- Er wordt geen gebruik gemaakt van de `with` statement
- De hoofdloop van de code leest, verwerkt, en berekent dingen tegelijkertijd
- Er wordt geen gebruik gemaakt van functies

⚠️ Hou het positief. Zorg dat studenten concrete suggesties doen over hoe het beter kan, en niet alleen benoemen wat "fout" is. Noemt iemand een "fout", leg dan zorgvuldig uit waarom het inderdaad niet goed is (leesbaarheid, begrijpelijkheid, consistentie) en vraag de kritiek-gever om een concrete suggestie voor verbetering.

Leg uit dat de studenten code reviews altijd kunnen/mogen gebruiken om elkaars code te beoordelen, waarna het verbeterd kan worden voor de deadline. Het is hierbij wel belangrijk dat (het onderdeel van) de opgave die gereviewd wordt door **beide** studenten eerst volledig is afgerond.

### Code review Temperature (30 minuten)

**We reviewen in deze codereview Temperature van PDP.** Studenten die alleen ML1 doen kunnen hier meekijken met andere studenten, maar hoeven dat niet te doen.

Doel: Studenten zien andere aanpakken dan die van hunzelf. Ze leren te discussiëren over code en zich uit te drukken in aspecten die relateren aan programmeren.

De opgave Temperature is voor de studenten de eerste opgave waar ze beoordeeld worden op style en design. Dit is _het_ moment om de studenten nog een keer na te laten denken over code-design. Dit gaan we doen doormiddel van een code review.

- Geef kort uitleg over de aspecten (deze staan hieronder bij de code review).
- We doen code reviews in tweetallen. Is er een oneven aantal studenten? Dan mag er één drietal zijn. Zorg ervoor dat je andere tweetallen maakt dan de vorige keer.
- Studenten werken samen, hardop denkend, achter één computer met de code die op dat moment gereviewd wordt. Als dit klaar is, wisselen ze naar de volgende computer voor het stuk code van de ander.
- (5-10 minuten) We beginnen met een klassikaal deel over de opgave waarover de code review gaat:
  - Wat moest er ook alweer gebeuren in de opgave?
  - Wat was er moeilijk?
  - Zijn er dingen die de assistent tijdens het nakijken zijn opgevallen, en waar specifiek op gelet kan worden?
- (15-20 minuten) Iedereen voert de code review uit, mentor loopt langs en bemoeit zich er soms mee, maar is vooral bezig met kritisch luisteren.
- (5 minuten) Vraag een aantal tweetallen of er specifieke dingen zijn geweest die hun opgevallen zijn. Probeer deze te relateren aan de opgaves die de studenten deze week in moeten leveren.

Voorbeelden van aspecten waar de studenten op kunnen letten voor Temperature zijn de volgende:

- Design
  - Gebruik van de juiste loops
  - Gebruik van functies (voorkomen repetitieve structuren)
  - Pure functies
  - Herhalende structuren
  - Redundante elementen
  - "Magische" getallen
- Style
  - Opdelen van code in blokken mbv witregels
  - Comments
    - Header bovenaan
    - Inhoudelijke kwaliteit
    - Kwantiteit (te veel/weinig)
    - Consistentie (wel/niet hoofdletters, alles Nederlands/Engels, etc.)
  - Namen van variabelen
  - Indentatie
  - Spaties rond operatoren

Al deze elementen zijn in eerdere modules uitgelegd en zouden bekend moeten zijn bij de studenten.

⚠️ Hou het positief. Zorg dat studenten concrete suggesties doen over hoe het beter kan, en niet alleen benoemen wat "fout" is. Noemt iemand een "fout", leg dan zorgvuldig uit waarom het inderdaad niet goed is (leesbaarheid, begrijpelijkheid, consistentie) en vraag de kritiek-gever om een concrete suggestie voor verbetering.

### Preventing duplicate code (15 minuten)

Doel: Studenten begrijpen hoe functies aan andere functies meegegeven kunnen worden, en hebben hiermee een extra instrument om gedupliceerde code te vermeiden.

De studenten hebben net een code review gedaan van temperature, en de functies uit die opgave zitten als het goed is vers in het geheugen. In deze kleine demo/discussie laat je ze zien hoe je `get_lowest_temp()` en `get_highest_temp()` (die erg op elkaar lijken) versimpelt. [Op deze hulppagina](/week_4/duplicate-code/) vind je informatie over verschillende manieren om duplicate code in temperature te voorkomen. Gebruik deze informatie om de studenten uitleg te geven over dit aspect van design.

> Als je gezien hebt dat je studenten veel gebruik gemaakt hebben van de functie `.index()` kan je ook het optionele gedeelte hierover ([op dezelfde pagina](/week_4/duplicate-code/)) behandelen.

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Als je al snel problemen voorziet met een student, bijvoorbeeld als die zegt 3 dagen per week te werken terwijl deze de minor fulltime doet, maak dan ook een TODO aan voor de coördinator. Een van je taken is om zo vroeg mogelijk te signaleren dat er mogelijk iets mis gaat.
- Update het logboek op basecamp. Schrijf bij iedere student op hoe het met ze gaat. Wanneer er geen veranderingen zijn bij een student hoef je ook niets te veranderen in het logboek.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
