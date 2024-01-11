# tsoha-Tietokanta-Peli

### Pelin idea
Pelissä pelaajan on tarkoitus arvata mihin tietokannan tauluun annettu arvo kuuluu. Pelaajalle annetaan satunnainen arvo joka löytyy tietokannan tauluista ja kysytään mihin tämä arvo kuuluu tarkalleen. Pelissä seurataan kuinkamonta oikeaavastausta pelaaja on saanut putkeen. Pelissä voitaisiin myös kysyä mihin taulun sarakkeeseen arvo kuuluu sitten, kun se on arvattu oikein tai antaa vinkkejä taulun sarakkeen muista arvoista, jos arvaus on mahdotonta tehdä.

Ohjelman toimia siten että sille voi antaa mitä tahansa taulua. Käyttäjä tällöin voi tuoda omia tauluja tietokantaan ja pelata niillä, tai jopa käyttää omaa tietokantaansa pelaamiseen.

Peliä voitaisiin vaikeuttaa esimerkiksi tekemällä eri taulu joukkoja joissa on arvoja jotka voisivat olla missä tahansa tauluissa. Esimerkiksi taulut joissa on paljon numeroita.

### Välipalautus 2
Tällä hetkellä ohjelman pää toiminnallisuudet ovat valmiina. Käyttäjä pääsee pelaamaan peliä ja tallentamaan pisteensä pelin loputtua. Ohjelma myös näyttää top 3 pisteet ja käyttäjäien antamat nimet kotisivulla. 

Ohjelmassa pitää vielä kirjoittaa asennus scripti. Scriptillä käyttäjä pystyisi valitsemaan mitä tietokantaa hän haluaa käyttää. Jos käyttäjä haluaa käyttää omaa tietokantaansa scriptillä pitäisi pystyä kopioimaan käyttäjän tietokannan ettei omat tiedot muutu alkuperäisessä tietokannassa. Scripti lisäisi myös uuteen tietokantaan taulun johon tallennetaan käyttäjien pisteet.

Ohjelmaan pitää vielä lisätä useampi taulu jotta pelin pelaaminen olisi haastavampaa.

Haluaisin vielä implementoida jonkin laisen tavan jolla käyttäjä voisi valita mitkä taulut olisivat käytössä. Ehkä kotisivulla voitaisiin tehdä togglattavan listan josta käyttäjä voisi valita mitä tauluja käytettäisiin. Tällöin pitäsi myös muuntaa pisteytys taulua sisältämään myös mitä tauluja käyttäjä käytti pisteden saamiseen.

Koodia pitäsi vielä refaktoroida ettei kaikki ohjelma logiikka olisi app.py tiedoston sisällä.


### Ohjelman asennus
Luo tiedosto ``secretInfo.py`` ja lisää siihen tietokannan osoite muuttujaan esimerkiksi näin: `DB_URL = "postgresql://<käyttäjä>:<salasana>@localhost/<tietokannan_nimi>"`

Ohjelmaa voi käyttää useammmalla tavalla. Ohjelman käyttöön kannattaa luoda uusi tietokanta, johon lisätään tauluja. Tähän uuteen tietokantaan pitää lisätä taulu `user_scores` taulu. Komento tälle löytyy ``schema.sql`` tiedostosta.

`user_scores` taulun lisäksi tietokantaan pitää lisätä muita tauluja että peliä voi pelata. Jos haluat pelata peliä omalla tietokanalla kopioi halutun tietokannan taulut uuteen tietokantaan. Jos peliä halutaan pelata valmiilla tauluilla, nämä voidaan tuoda tietokantaan komento riviltä venv ympäristössä komennolla: `python3 dataImport.py`

Kun tietokantaan ollaan lisätty tarvittavat taulut, niin pelin voi aloittaa seuraavilla komennoilla:

    pip install -r ./requirements.txt
    source venv/bin/activate
    flask run

venv ympäristön voi sitten sulkea komennolla:

    deactivate
