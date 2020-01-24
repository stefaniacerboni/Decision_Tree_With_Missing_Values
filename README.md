# Decision Tree With Missing Values

L’obiettivo del progetto è quello di testare l’accuratezza degli alberi di decisione nella classificazione di dataset completi, sia di dataset con valori mancanti.
Per fare ciò, sono stati presi tre dataset senza valori mancanti e, progressivamente, in modo casuale e uniforme (con probabilità p) sono stati rimossi alcuni valori negli attributi.

## Esecuzione
L’interfaccia da cui è possibile eseguire i test è quella denominata testdataset.py. Per testare il programma è sufficiente eseguire tale interfaccia.
Nel progetto sono già stati importati tre dataset, disponibili online (tic-tac-toe, balance-scale, car). È possibile aggiungere ulteriori dataset importando il file contenente le istanze nel progetto e definendo la descrizione degli attributi del dataset stesso nella classe testdataset.py. Infine è sufficiente richiamare test(nome_dataset) da testdataset.py.

### Prerequisiti
Il codice è stato scritto in Python 3.7. In generale si consiglia di utilizzare una versione non inferiore alla 3.4. Perciò il codice non è eseguibile con Python 2.

### Riferimenti
Nella realizzazione del progetto sono stati usati i dataset reperibili nel sito di UCI Machine Learning Repository e porzioni di codice provenienti dal repository GitHub aima-python.
