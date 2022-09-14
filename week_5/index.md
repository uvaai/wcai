## Werkcollege week 5

In dit werkcollege bespreken we de style en design van Temperature. De feedback hieruit kunnen de studenten meenemen voor module 4. We sluiten af met een discussie over de Chinese room.

### Terugblik (15 minuten)

Laat iedereen even vertellen hoe het ging, waar het knelde en of het gelukt is. We bespreken hier openlijk hoe het gaat. Zeg tegen je studenten dat klagen ook OK is, dat kan hier heel goed een onderdeel van zijn, en zeg dat je goed zult luisteren en noteren (beloof niet dat je er iets mee gaat doen! Het gaat vooral om luisteren, bespreekbaar maken en het totaalbeeld). Hier kan je ook de open vragen van Machine Learning extra bespreken.

⚠️ Jij als mentor moet het gesprek leiden, zorg dat iedereen aan de beurt komt!

- Nog opvallende dingen over specifieke studenten? Noteer ze op Basecamp!
- Nog dingen die mis lijken te gaan voor meerdere studenten? Noteer ze en deel ze na de werkgroep meteen met het team via een message in Basecamp.

### Code review Temperature (30 minuten)

Doel: Studenten zien andere aanpakken dan die van hunzelf. Ze leren te discussiëren over code en zich uit te drukken in aspecten die relateren aan programmeren.

De opgave Temperature was voor de studenten de eerste opgave waar ze beoordeeld werden op style en design. De feedback op de Temperature hebben ze als het goed is al gehad. Ze zullen snel ook de volgende opgave in moeten leveren. Dit is _het_ moment om de studenten nog een keer na te laten denken over code design. Dit gaan we doen doormiddel van een code review.

- Geef kort uitleg over de aspecten (deze staan hieronder bij de code review).
- We doen code reviews in tweetallen. Is er een oneven aantal studenten? Dan mag er één drietal zijn.
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

De studenten hebben net een code review gedaan van temperature, en de functies uit die opgave zitten als het goed is vers in het geheugen. In deze kleine demo/discussie laat je ze zien hoe je `get_lowest_temp()` en `get_highest_temp()` (die erg op elkaar lijken) versimpelt. [Op deze hulppagina](/week_5/duplicate-code/) vind je informatie over verschillende manieren om duplicate code in temperature te voorkomen. Gebruik deze informatie om de studenten uitleg te geven over dit aspect van design.

> Als je gezien hebt dat je studenten veel gebruik gemaakt hebben van de functie `.index()` kan je ook het optionele gedeelte hierover ([op dezelfde pagina](/week_5/duplicate-code/)) behandelen.

### Chinese Room (30 minuten)

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

- Poll: Wie was er voor/tegen "understanding" bij:
    1. Het Naive Bayes programma
    2. Zelf tweets lezen en classificeren
    3. Zelf tweet labels reproduceren
    4. Het gecombineerd systeem van Naive Bayes en programmeur

    Bespreek hierbij ook gelijk de verschillen, als die er zijn

- Denken jullie dat gecombineerde systemen ooit begrip kunnen hebben?
    - De chinese room is ook een gecombineerd systeem, met de persoon in de kamer en een groot boek van herschrijfregels voor symbolen
        - Heeft de kamer als geheel dan begrip?
    - Is het voorbeeld met de Naive Bayes en programmeur daarin anders of hetzelfde?
        - Waarom heeft deze combinatie wel/geen begrip?

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Als je al snel problemen voorziet met een student, bijvoorbeeld als die zegt 3 dagen per week te werken terwijl deze de minor fulltime doet, maak dan ook een TODO aan voor de coördinator. Een van je taken is om zo vroeg mogelijk te signaleren dat er mogelijk iets mis gaat.
- Update het logboek op basecamp. Schrijf bij iedere student op hoe het met ze gaat. Wanneer er geen veranderingen zijn bij een student hoef je ook niets te veranderen in het logboek.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
