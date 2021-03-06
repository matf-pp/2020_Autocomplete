# Autocomplete
### Kratak opis
-----------------

Implementacija jednostavne autocomplete aplikacije. U polje predviđeno za unos teksta korisnik unosi željenu nisku i na osnovu nje se izbacuju rezultati sortirani opadajuće po težinama u listboxu koji se nalazi ispod. 

![](https://github.com/matf-pp/2020_Autocomplete/blob/master/slika2.png)


Prikazaju se rezultati koji počinju na unetu nisku, ali implementirana je i funkcionalnost koja obezbeđuje da ukoliko je korisnik pogrešio jedno slovo, na primer, izađe željeni rezultat (slova **a** i  **s** su jedno pored drugog na tastaturi pa može doći do greške).

![](https://github.com/matf-pp/2020_Autocomplete/blob/master/png3.png)

Postoji i opcija `Show weights` koja ukoliko je uključena prikazuje dodeljene težine rečima koje predstavljaju popularnost pretrage. Ukoliko je uneto slovo **P** u pretrazi za gradove, očekivano je da na vrhu pretrage bude Pariz recimo, a ne Pančevo.

Klikom na neki od ponuđenih rezultata i potom na dugme `Search Google` otvara se Google pretraga izabranog rezultata.

![](https://github.com/matf-pp/2020_Autocomplete/blob/master/picture.png)
![](https://github.com/matf-pp/2020_Autocomplete/blob/master/pic5.png)




### Jezici i tehnologije
-----------------

Program je napisan u programskom jeziku Python3 korišćenjem biblioteke Tkinter za GUI.

### Operativni sistem
-----------------

Windows

### Pokretanje programa
-----------------

Potrebno je imati instaliranu tkinter biblioteku, kao i webbrowser i numpy.
U sekciji releases nalazi se fajl autocomplete.zip kog je potrebno skinuti i pokrenuti main.exe.


### Autori
1. Stevan Dragović 331/2016 stevandragovic.10@gmail.com 
2. Jovan Ranđelović 211/2016 jovan.ran87@gmail.com
