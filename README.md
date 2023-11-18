# tsoha-Tietokanta-Peli


### Pelin idea
Pelissä pelaajan on tarkoitus arvata mihin tietokannan tauluun annettu arvo kuuluu. Pelaajalle annetaan satunnainen arvo joka löytyy tietokannan tauluista ja kysytään mihin tämä arvo kuuluu tarkalleen. Pelissä seurataan kuinkamonta oikeaavastausta pelaaja on saanut putkeen. Pelissä voitaisiin myös kysyä mihin taulun sarakkeeseen arvo kuuluu sitten, kun se on arvattu oikein tai antaa vinkkejä taulun sarakkeen muista arvoista, jos arvaus on mahdotonta tehdä.

Ohjelman toimia siten että sille voi antaa mitä tahansa taulua. Käyttäjä tällöin voi tuoda omia tauluja tietokantaan ja pelata niillä, tai jopa käyttää omaa tietokantaansa pelaamiseen.

Peliä voitaisiin vaikeuttaa esimerkiksi tekemällä eri taulu joukkoja joissa on arvoja jotka voisivat olla missä tahansa tauluissa. Esimerkiksi taulut joissa on paljon numeroita.

### Välipalautus 2
Tällä hetkellä ohjelman pää toiminnallisuudet ovat valmiina. Käyttäjä pääsee pelaamaan peliä ja tallentamaan pisteensä pelin loputtua. Ohjelma myös näyttää top 3 pisteet ja käyttäjäien antamat nimet kotisivulla. 

Ohjelmassa pitää vielä kirjoittaa asennus scripti. Scriptillä käyttäjä pystyisi valitsemaan mitä tietokantaa hän haluaa käyttää. Jos käyttäjä haluaa käyttää omaa tietokantaansa scriptillä pitäisi pystyä kopioimaan käyttäjän tietokannan ettei omat tiedot muutu alkuperäisessä tietokannassa. Scripti lisäisi myös uuteen tietokantaan taulun johon tallennetaan käyttäjien pisteet.

Haluaisin vielä implementoida jonkin laisen tavan jolla käyttäjä voisi valita mitkä taulut olisivat käytössä. Ehkä kotisivulla voitaisiin tehdä togglattavan listan josta käyttäjä voisi valita mitä tauluja käytettäisiin. Tällöin pitäsi myös muuntaa pisteytys taulua sisältämään myös mitä tauluja käyttäjä käytti pisteden saamiseen.

Koodia pitäsi vielä refaktoroida ettei kaikki ohjelma logiikka olisi app.py tiedoston sisällä.


#### Ohjelman voi aloittaa komennoilla:
    source venv/bin/activate
    pip install -r ./requirements.txt
    flask run
    vaihotestoisesti:
        flask run --debug
    deactivate