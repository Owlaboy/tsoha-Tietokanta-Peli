# tsoha-Tietokanta-Peli


### Pelin idea
Pelissä pelaajan on tarkoitus arvata mihin tietokannan tauluun annettu arvo kuuluu. Pelaajalle annetaan satunnainen arvo joka löytyy tietokannan tauluista ja kysytään mihin tämä arvo kuuluu tarkalleen. Pelissä seurataan kuinkamonta oikeaavastausta pelaaja on saanut putkeen. Pelissä voitaisiin myös kysyä mihin taulun sarakkeeseen arvo kuuluu sitten, kun se on arvattu oikein tai antaa vinkkejä taulun sarakkeen muista arvoista, jos arvaus on mahdotonta tehdä.

Ohjelman toimia siten että sille voi antaa mitä tahansa taulua. Käyttäjä tällöin voi tuoda omia tauluja tietokantaan ja pelata niillä, tai jopa käyttää omaa tietokantaansa pelaamiseen.

Peliä voitaisiin vaikeuttaa esimerkiksi tekemällä eri taulu joukkoja joissa on arvoja jotka voisivat olla missä tahansa tauluissa. Esimerkiksi taulut joissa on paljon numeroita.

#### Ohjelman voi aloittaa komennoilla:
    source venv/bin/activate
    pip install -r ./requirements.txt
    flask run
    vaihotestoisesti:
        flask run --debug
    deactivate