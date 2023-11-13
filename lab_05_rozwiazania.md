### Zadanie 1
```sql
Select * FROM osoba;
create table postac ( id_postaci int primary key auto_increment, nazwa varchar(40) not null, rodzaj enum('wiking','ptak','kobieta'), data_ur date, wiek int unsigned);
insert into postac values(default,"Bjorn","wiking","895-10-23",21);
insert into postac(nazwa, rodzaj, data_ur, wiek) values("Damian","wiking","891-10-23",25);
delete from postac where id_postaci=2;
insert into postac values(default,"Drozd","ptak","0895-04-21",5);
insert into postac values(default,"Tesciowa","kobieta","0865-04-21",65);
update postac set wiek=88 WHERE rodzaj="kobieta";
```
### Zadanie 2
```sql
create table walizka ( id_walizki int primary key auto_increment, pojemnosc int unsigned, kolor enum("rozowy","czerwony","teczowy","zolty"), id_wlasciciela int, foreign key(id_wlasciciela) references postac(id_postaci) on delete cascade);
alter table walizka alter kolor set default "rozowy";
insert into walizka values(default,"50","teczowy",1);
insert into walizka values(default,"45","czerwony",4);
```
### Zadanie 3
```sql
CREATE TABLE izba ( adres_budynku varchar(50) NOT NULL, nazwa_izby varchar(50) NOT NULL, metraz int unsigned, wlasciciel int, primary key(adres_budynku, nazwa_izby), foreign key(wlasciciel) references postac(id_postaci) on delete set null);
ALTER TABLE izba ADD kolor_izby enum("czarny", "czerwony") AFTER metraz;
ALTER TABLE izba ALTER kolor_izby SET DEFAULT "czarny";
INSERT INTO izba values("Nordycka 1", "Spizarnia", "80", default, 1);
```
### Zadanie 4 
```sql
CREATE TABLE przetwory (id_przetworu INT AUTO_INCREMENT, rok_produkcji VARCHAR(4) DEFAULT '1654', id_wykonawcy INT, zawartosc VARCHAR(30), dodatek VARCHAR(30) DEFAULT 'papryczka chilli', id_konsumenta INT, PRIMARY KEY(id_przetworu), FOREIGN KEY(id_wykonawcy) REFERENCES postac(id_postaci), FOREIGN KEY(id_konsumenta) REFERENCES postac(id_postaci));

INSERT INTO przetwory (id_wykonawcy,zawartosc,id_konsumenta) VALUES ('1','bigos','3');
```
### Zadanie 5
```sql
INSERT INTO postac values();
INSERT INTO postac values(default,'Asgard','wiking','1678-08-12',340), 
(default,'Khorad','wiking','1618-08-12',40),
(default,'Andrzej','wiking','1678-08-13',240),
(default,'Zbyszek','wiking','1672-08-12',140),
(default,'Lech','wiking','1678-01-12',34);

#pkt 2 
create table statek (
nazwa_statku varchar(50) primary key,
rodzaj_statku enum('handlowy', 'wojenny'),
data_wodoawnia date,
max_ladownosc int unsigned);

#pkt 3
insert into statek values('Skidbladnir','handlowy','1678-09-13','75'),
('Nagelfar','wojenny','1574-02-12','7500');

#pkt 4
alter table postac add funkcja varchar(50);
# pkt 5
update postac set funkcja='kapitan' where nazwa='Bjorn';

# pkt 6
# krok 1 - dodanie odpowiedniej kolumny dla klucza obcego
alter table postac add column statek varchar(50);
#krok 2 - dodanie klucz obcego
alter table postac add foreign key(statek) references statek(nazwa_statku) on delete set null;

#pkt 7
update postac set statek='Skidbladnir' where id_postaci=1 OR id_postaci=3;
update postac set statek='Nagelfar' where id_postaci>4;
# pkt 8
delete from izba where nazwa_izby='spizarnia';
DROP TABLE izba;
```
Kod umieszczany liniowo. Polecenie `SELECT` oznacza wybranie danych z bazy.

# Tytuł
## Poziom2
###### Poziom 6

Lista zadań do wykonania
* todo 1
* todo2
  * ok
 
1. Rozdział 1
2. Rozdział 2

**Listing 1**
_listing 2_
