## Werkcollege week 4

Afgelopen week hebben de studenten voor het eerst een volledig NN gemaakt! Een goed moment om even stil te staan bij wat ze precies aan het doen zijn door even uit te zoomen van de code en alleen naar de stappen te kijken die in het "leerproces" van een NN zitten. Dit wordt een drukke werkgroep met veel uitleg, zorg dat je alle studenten scherp houdt!

De [slides](https://docs.google.com/presentation/d/1kTfsxe25qHevIzyCxT3MTkbviHJ1Z3psdIMy6C8iWhU/edit?usp=sharing) van deze week

## Intro

Begin met kort peilen hoe de studenten naar afgelopen week kijken. Het was een week met pittige theorie, dus vraag welke dingen lastig zijn.

## Neural Networks (15 min)

Doel: studenten stap voor stap door het "leerproces" van een NN laten gaan en stil te staan bij de verschillen in activatie functies

🧑‍🏫 Uitleg aan studenten

Neem je tijd om rustig uit te leggen wat de forward en backward pass doen.

Forward: gegeven de gewichten in het model, maak op basis van de input een voorspelling. Omdat we met willekeurige gewichten beginnen, gaat dit natuurlijk niks zinnigs voorspellen!

Backward: gegeven de voorspelling die het model heeft gemaakt én de voorspelling die we hadden willen maken, pas de gewichten dusdanig aan dat we met dezelfde input wél de juiste voorspelling maken. Het werkt goed om even klassikaal de matrix multiplicatie uit te tekenen die je krijgt wanneer backward gebruikt!

Sinds de laatste modules gebruiken we de termen "forward" en "backward", maar eigenlijk is dit concept al lang bekent bij studenten! Bijvoorbeeld wanneer ze `fit()` gebruiken bij `temperature.py`! Of wanneer ze aan ChatGPT een vraag stellen, maken ze een forward pass met de geleerde gewichten van het model!

## Activaties (20 min)

Doel: studenten het verschil tussen sigmoid en soft-max laten begrijpen

🧑‍🏫 Uitleg aan studenten

De studenten hebben twee activatie functies gezien: de sigmoid en de soft-max. Wat zijn de verschillen?

De sigmoid functie is binair. Het is 0 of 1. We willen dus voorspellen of iets 1 is óf 0. Het is belangrijk dat wanneer het model denkt dat iets niet van een bepaalde klasse is, hier 0 wordt voorspeld. Dit zien we terug in de kostenfunctie. Het tweede deel is speciaal ontworpen om een waarde te geven aan hoe sterk het model "dacht" dat voorspelling 0 moest zijn. Neem een plaatje van een hond met een model wat kan voorspellen of het een hond of een kat is. De sigmoid functie zal beide kunnen voorspellen, dus het is belangrijk dat zowel de waarde voor hond dicht bij 1 komt en de waarde van kat dicht bij 0. Teken dit uit met wat waardes! Je zal zien dat er hogere kosten zijn wanneer je `y_hat = 0.5` neemt dan wanneer je `y_hat = 0.1` met `y=0`.

De soft-max functie is niet binair! Deze is er om uit meerdere categorien te kiezen welke categorie het meest waarschijnlijk is. Alle probabilities tellen samen op naar 1. Neem opnieuw een plaatje van een hond met een model wat kan voorspellen of het een hond of een kat is. De soft-max functie zal de waarde van hond zo dicht mogelijk bij 1 proberen te krijgen. Als gevolg hiervan, wordt de waarde voor kat lager. Maar aangezien dit is gekoppeld aan de waarde van een hond, hoeven we niet de kosten van de "kat-voorspelling" mee te nemen! Dit zien we terug in de kostenfunctie, waar we enkel kijken hoe hoog de voorspelling voor het juiste antwoord was. Hiermee wordt de rest vanzelf lager! Teken dit uit op het bord naast de sigmoid om het verschil te laten zien!

Concluderend: de sigmoid geeft een losse kans *per* klasse, de soft-max geeft een kans *verspreid over* de klasses.


### Open vragen activatie functies (10 min)

Doel: studenten samen laten nadenken over activatie functies

Nu is het de beurt aan de studenten! Laat ze in tweetallen werken en samen de open vragen beantwoorden! Je kan even rondlopen, het zijn er niet veel dus de studenten zullen niet veel tijd nodig hebben.

Na ± 5 min kan je klassikaal bespreken wat is opgevallen. Wees kritisch op de antwoorden! Ze moeten goed uitgebreid zijn, net als in de notebooks!

### Code review `climate.py` (15 min)

Doel: studenten samen laten focussen op design

🧑‍🏫 Uitleg aan studenten

#### Eerste 10 min:

De werkgroep is tot nu toe vrij theoretisch geweest, nu is er tijd om juist te focussen op design! Kijk naar elkaars code en let goed op de volgende dingen:

1. Zie je ergens dezelfde code meerdere keren?
2. Doen functies 1 ding of meerdere (inladen, uitrekenen, plotten)?
3. Is de style goed? Is er voldoende uitleg?


#### Laatste 5 min:

Bespreek met z'n allen welke dingen opvielen, wie is erachter gekomen dat er nog ruimte is voor design verbeteringen?

## Written (15 min)

Doel: studenten prikkelen om kritisch te blijven schrijven. Probeer ze mee te geven dat ze het niet eens hoeven te zijn met de artikelen die ze lezen!

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Update het logboek op basecamp. Schrijf bij iedere student op hoe het met ze gaat. Wanneer er geen veranderingen zijn bij een student hoef je ook niets te veranderen in het logboek.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
