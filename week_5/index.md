## Werkcollege week 5

<!-- TODO -->

### Terugblik (15 minuten)

Laat iedereen even vertellen hoe het ging, waar het knelde en of het gelukt is. Zeg ook gewoon tegen je studenten dat **klagen** OK is, en zeg dat je goed zult luisteren en noteren (beloof niet dat je er iets mee gaat doen! Het gaat vooral om luisteren, bespreekbaar maken en het totaalbeeld). Hier kan je ook de open vragen van Machine Learning extra bespreken.

⚠️ Jij als mentor moet het gesprek leiden, zorg dat iedereen aan de beurt komt!

- Nog opvallende dingen over specifieke studenten? Noteer ze op Basecamp!
- Nog dingen die mis lijken te gaan voor meerdere studenten? Noteer ze en deel ze na de werkgroep meteen met het team via Basecamp.

### Code review Temperature (30 minuten)

Doel: Studenten zien andere aanpakken dan die van hunzelf. Ze leren te discussiëren over code en zich uit te drukken in aspecten die relateren aan programmeren.

De opgave Temperature was voor de studenten de eerste opgave waar ze beoordeeld werden op style en design. De feedback op de Temperature hebben ze als het goed is al gehad. Ze zullen snel ook de volgende opgave in moeten leveren. Dit is _het_ moment om de studenten nog een keer na te laten denken over code design. Dit gaan we doen doormiddel van een code review.

- Geef kort uitleg over de aspecten (hieronder bij de code review).
- We doen code reviews in tweetallen. Is er een oneven aantal studenten? Dan mag er één drietal zijn.
- Studenten werken samen, hardop denkend, achter één computer met de code die op dat moment gereviewd wordt. Als dit klaar is, wisselen ze naar de volgende computer voor het stuk code van de ander.
- (5-10 minuten) We beginnen met een klassikaal deel over de opgave waarover de code review gaat:
  - Wat moest er ook alweer gebeuren in de opgave?
  - Wat was er moeilijk?
  - Zijn er dingen die de assistent tijdens het nakijken zijn opgevallen, en waar specifiek op gelet kan worden?
- (15-20 minuten) Iedereen voert de code review uit, mentor loopt langs en bemoeit zich er soms mee, maar is vooral bezig met kritisch luisteren.
- (5 minuten) Vraag een aantal tweetallen of er specifieke dingen zijn geweest die hun opgevallen zijn. Probeer deze te relateren aan de opgaves die de studenten deze week in moeten leveren.

De aspecten waar de studenten op kunnen letten voor Temperature zijn de volgende:

- Design
  - Gebruik van de juiste loops
  - Gebruik van functies (voorkomen repetitieve structuren)
  - Pure functies
  - Herhalende structuren
  - Redundante elementen
  - "Magische" getallen
- Style
  - Opdelen van code in blokken
  - Comments
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

De studenten hebben net een code review gedaan van temperature, en de functies uit die opgave zitten als het goed is vers in het geheugen. In deze kleine demo/discussie laat je ze zien hoe je `get_lowest_temp()` en `get_highest_temp()` (die erg op elkaar lijken) versimpelt. [Op deze hulppagina](/duplicate-code) vind je informatie over verschillende manieren om duplicate code in temperature te voorkomen. Gebruik deze informatie om de studenten uitleg te geven over dit aspect van design.

> Als je gezien hebt dat je studenten veel gebruik gemaakt hebben van de functie `.index()` kan je ook het optionele gedeelte hierover ([op dezelfde pagina](/duplicate-code)) behandelen.

### Chinese Room (30 minuten)

<!-- TODO -->

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Als je vermoed dat een student het moeilijk heeft, er een gesprek met gevoerd moet worden, of op een andere manier extra aandacht nodig is, maak dan ook een TODO aan voor de coördinator. Een van je taken is om zo vroeg mogelijk te signaleren dat er mogelijk iets mis gaat.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
