## Werkcollege week 4

Omdat werkcollege erg dicht op de deadline van module 3 plaatsvindt, is er veel ruimte gemaakt voor extra persoonlijke hulp. We bespreken de afgelopen week, proberen in kaart te brengen wie eigenlijk al klaar is, en wie nog dingen moet afronden. Daarna bespreken we kort nog een keer design met een voor de studenten bekend probleem: Greedy.

⚠️ Vergeet niet om nog een laatste keer te melden dat er vanaf module 3 ook echt beoordeeld wordt op design en style!

### Terugblik (15 minuten)

Laat iedereen even vertellen hoe het ging, waar het knelde en of het gelukt is. We bespreken hier openlijk hoe het gaat. Zeg tegen je studenten dat klagen ook OK is, dat kan hier heel goed een onderdeel van zijn, en zeg dat je goed zult luisteren en noteren (beloof niet dat je er iets mee gaat doen! Het gaat vooral om luisteren, bespreekbaar maken en het totaalbeeld). Hier kan je ook de open vragen van Machine Learning extra bespreken.

⚠️ Jij als mentor moet het gesprek leiden, zorg dat iedereen aan de beurt komt!

- Nog opvallende dingen over specifieke studenten? Noteer ze op Basecamp!
- Nog dingen die mis lijken te gaan voor meerdere studenten? Noteer ze en deel ze na de werkgroep meteen met het team via een message in Basecamp.

### Design (20 min)

Doel: Studenten worden bewust van verschillende design-oplossingen en bijbehorende voor en nadelen. Er is niet één oplossing beter dan alle andere, maar er zijn wel dingen waar we extra op kunnen letten.

Code design is een moeilijk onderwerp waar veel ervaring voor nodig is om goede keuzes te maken. Vaak denken studenten dat er één beste oplossing is, maar vaak zijn er voor en nadelen aan iedere aanpak. Je gaat het met je studenten hebben over verschillende aanpakken voor een probleem wat ze een aantal weken terug hebben geprogrammeerd: greedy.

[Bijgeleverd zijn 6 verschillende manieren om greedy te implementeren.](greedy_design.zip) Alle code geeft dezelfde uitkomst, maar er zijn grote verschillen in de gemaakte designkeuzes. Neem voor het werkcollege ieder van de bestanden goed door. Doorloop met de studenten één voor één deze files en focus daarbij op de volgende design-aspecten:

- Vermijd herhalende structuren
- Verwijder redundante elementen
- Vermijd "magische" getallen
- Houd je code beknopt
- Verdeel blokken code over functies, en complexe formules over meerdere regels; voeg lagen abstractie toe

Laat de studenten zo veel mogelijk aanwijzen welke elementen van het programma beter kunnen en uitleggen waarom dit zo is. Een aantal van de aspecten lijken elkaar soms tegen te spreken, dan is het belangrijk de juiste balans te vinden.

### Code review football analysis (20 min)

**We reviewen in deze codereview `football_analysis` uit module 3 van PDP.**

Doel: Studenten zien andere aanpakken dan die van hunzelf. Ze leren te discussiëren over code en zich uit te drukken in aspecten die relateren aan programmeren.

De meeste studenten zullen zo dicht op de deadline bijna klaar zijn met de opgaven. Goed moment om nog een keer naar wat onderdelen te kijken. We bespreken de oefening/opdracht football analysis waarbij de studenten code kregen van matig ontwerp die ze aan moesten passen naar een beter ontwerp.

- Je hebt net al wat uitleg gegeven over de aspecten (hierboven bij Design benoemd, met hieronder wat specifieke toevoegingen).
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

Leg uit dat de studenten code reviews altijd kunnen/mogen gebruiken om elkaars code te beoordelen, waarna het verbeterd kan worden voor de deadline. Het is hierbij wel belangrijk dat (het onderdeel van) de opgave die gereviewed wordt door **beide** studenten eerst volledig is afgerond.

### Assistentie (de rest van de tijd)

Gebruik de tijd die over is om studenten die nog niet helemaal klaar zijn te helpen. Ook studenten die al wel klaar zijn hebben wat te doen: die kunnen natuurlijk vragen stellen over style en design. Benoem dit ook écht even, zodat studenten dit daadwerkelijk doen. Ook de vraag "Zou je nog even naar mijn code kunnen kijken voor style en design?" is een goede vraag!

Laat waar mogelijk deze studenten eerst met elkaar de code bespreken. Zodra ze samen een oplossing voor een bepaald probleem hebben bedacht kunnen ze dat met jou bespreken. _Communiceer dit duidelijk._ Het is erg belangrijk dat de studenten zelf nadenken over hoe hun code beter kan.

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Als je al snel problemen voorziet met een student, bijvoorbeeld als die zegt 3 dagen per week te werken terwijl deze de minor fulltime doet, maak dan ook een TODO aan voor de coördinator. Een van je taken is om zo vroeg mogelijk te signaleren dat er mogelijk iets mis gaat.
- Update het logboek op basecamp. Schrijf bij iedere student op hoe het met ze gaat. Wanneer er geen veranderingen zijn bij een student hoef je ook niets te veranderen in het logboek.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
