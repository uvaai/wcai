## Werkcollege week 6
Afgelopen week zijn studenten bezig geweest met Decision Trees! Een "adempauze" tussen het lastige backpropagation algoritme en de Convolutional Neural Network die studenten deze week gaan krijgen. Het interessante van een Decision Tree, is dat het model veel beter te begrijpen is! Je ziet immers op welke variabelen er een split wordt gemaakt. Dit staat in groot contrast met de "black box" die studenten kennen van een Neural Network

De [slides](https://docs.google.com/presentation/d/1aoE6Zenc3Zs1sTMZI2pIqGkl3a1yp9ZXil7iWKexv7U/edit?usp=sharing) van deze week

## Intro
Begin met kort peilen hoe de studenten naar afgelopen week kijken. Snapt iedereen hoe een decision tree werkt? En is het gelukt om een mooie analyse te maken van YELP?

## Open vragen (15 min)
In de slides staan een aantal open vragen. Laat de studenten deze in tweetallen bespreken. De eerste gaat over pooling, het kan zijn dat studenten hier nog niet de theorie video van hebben gezien!


## Code review Crawler (25 min)
Doel: studenten van elkaar laten leren over goede design en style

🧑‍🏫 Uitleg aan studenten

Zet studenten in twee- of drietallen aan het werk. Laat ze focussen op design en style. Voor design in de Crawler opdracht kan je op het volgende letten:
- Goed gebruik van functies gemaakt? Doen ze allemaal "één ding"
- Is het duidelijk welke functie wat doet in het crawl proces?
- Duidelijke docstrings/comments?
- Goede variabel/functie namen? Geen get_data_1 get_data_2

Bespreek de laatste 5 minuten welke dingen studenten zijn opgevallen

## Convolutions (10 min)
Doel: studenten helpen met het begrijpen van een convolutie

🧑‍🏫 Uitleg aan studenten

Convoluties zijn een lastig wiskundig concept. Neem even de tijd in de werkgroep om uit te tekenen op het bord wat er gebeurd wanneer je een convolutie neemt. Hoe maak je een blur? Waarom is er padding nodig? Door stap voor stap een convolutie te maken, zien studenten nogmaals hoe dit werkt. Hiermee kunnen ze hopelijk aankomende week aan de slag! Adviseer verder om de video die in de slides staat te bekijken als het nog niet snappen!

Sta ook stil bij *waarom* een convolutie handig is voor Neurale Netwerken! Door onze input te filteren, kan een model leren op een specifieke eigenschap van een afbeelding! Dus als *edge detection* belangrijk is, kunnen we de randen van een object sterker naar voren doen komen vanuit de standaard input met een slimme convolutie. 

Als studenten dit snappen, kan je een stapje verder gaan: het leren van een convolutie

Een *edge detection* is voor ons een logische toepassing voor een convolutie. Zijn er ook convoluties die veel informatie kunnen blootleggen, die wat minder intuitief te begrijpen zijn? Jazeker! Daarom kan het *variabel* maken van je convolute, of het laten leren wélke convolutie het beste werkt, een hele goede verbetering zijn voor je model! Hiermee verlies je interpreteerbaarheid van je model: wij weten niet welke aspecten van de input als "belangrijk" worden gezien. Maar het model kan zelf bepalen welke aspecten het meeste naar voren zouden moeten komen! Wonderbaarlijk als je het mij vraagt ;)


## Written (15 min)

Doel: studenten prikkelen om kritisch te blijven schrijven. Probeer ze mee te geven dat ze het niet eens hoeven te zijn met de artikelen die ze lezen! Deze week ging over adverserial attacks. Kunnen de stundenten voorbeelden bedenken van systemen die hier kwetsbaar voor zijn? Wat zou er gebeuren als iemand alle bruggen open kan zetten omdat de brug denkt dat er altijd een boot aankomt?

Veel studenten schrijven simpelweg dat “de risico’s zijn te groot voor bepaalde industrieën, zoals zelfrijdende auto’s”. Dit impliceert dat ze vinden dat zelfrijdende auto’s verboden moeten worden. Vraag hier vooral op door, zorgen mensen niet voor veel meer verkeersdoden?

Daarnaast: Ook vinden studenten de risico’s bij healthcare te groot. Maar hoe ziet een adverserial attack eruit in de gezondheid? Gaan mensen mri scanns express aanpassen zodat er wel of geen ziekte wordt gedecteerd? Een verkeersbord zou een terrorist gemakkelijk kunnen bewerken, maar hoe relevant is de gezondheidszorg voor grote adverserial attacks? Studenten hierover laten nadenken voordat ze opschrijven dat “de risico’s te groot zijn dus altijd meot worden gecontroleerd”. 

## Administratie

Direct na afloop van de werkgroep:

- Als je weet dat je studenten mist en je hebt geen contact, maak een TODO op Basecamp aan voor de vakcoördinator. Deze zal achter de student aan gaan.
- Update het logboek op basecamp. Schrijf bij iedere student op hoe het met ze gaat. Wanneer er geen veranderingen zijn bij een student hoef je ook niets te veranderen in het logboek.
- Er kunnen vragen zijn opgekomen tijdens de werkgroep. Check voor alle vragen of je antwoorden kunt vinden in de handleiding, of in een post (Message) op Basecamp. Wees niet spaarzaam met je vragen! Liever teveel dan te weinig. De coördinator denkt dan mee en maakt eventueel ook een mededeling voor de andere mentoren.
