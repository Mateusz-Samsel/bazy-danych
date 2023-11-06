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

Kod umieszczany liniowo. Polecenie `SELECT` oznacza wybranie danych z bazy.
