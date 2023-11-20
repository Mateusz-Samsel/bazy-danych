### Zadanie 1 
```sql
#pkt 1
select * from postac where rodzaj='wiking' order by wiek DESC;
delete from postac where id_postaci in(6,8)
#pkt b
#krok 1
alter table walizka drop foreign key walizka_ibfk_1;
alter table przetwory drop foreign key przetwory_ibfk_1;
alter table przetwory drop foreign key przetwory_ibfk_2;
#krok2
alter table postac modify id_postaci int;
#krok 3
alter table postac drop primary key;
#SET fereign_key_checks = 1;
#Może się przydać przy przywraaniu bazy
```
### Zadanie 2
```sql
#pkt a
#krok 1 
alter table postac add pesel char(11) first;
#krok 2 wstawianie danych
update postac set pesel='17763874635' where id_postaci=1;
update postac set pesel='17763874635' + id_postaci;
#krok 3 dodanie klucza głównego
alter table postac add primary key(pesel);

#pkt b
alter table postac modify rodzaj enum('wiking','ptak','kobieta','syrena');
#pkt c
Insert into postac values("17763874687","11","Gertruda Nieszczera", "syrena","1678-05-17",21)
```

### Zadanie 3
```sql
#pkt a
update postac set statek='Skidbladnir' where nazwa like '%a%';

#select * from postac where nazwa like '_j%';
#select * from postac where nazwa regexp '[0-9]{1,2}-[0-9]{3}'
#[0-9] od 0 do 9
#[a-k] od a do k
#[abcdef] jeden ze znaków ([] - zbiór)
#{} określenie krotności
#{n} dokładnie n razy
#{n,m} co namniej n razy, nie więcej jak m razu
#{n,} co najmniej n razystateknazwa_statkudata_wodoawnia
#select * from statek where data_wodoawnia between '1901-01-01' and'2000-12-31';
#select * from statek where year(data_wodoawnia) between 1901 and 2000;

#pkt b
update statek set max_ladownosc = 0.7 * max_ladownosc where year(data_wodoawnia) between 1901 and 2000;

#pkt c
alter table postac add check (wiek < 1000);
```

### Zadanie 4
```sql
#pkt a
alter table postac modify rodzaj enum('wiking','ptak','kobieta','syrena','wąż') DEFAULT NULL;
insert into postac values ("17763874648",12,"Loko","wąż");

#pkt b
create table marynarz like postac;
insert into marynarz select * from postac where statek is not null;

#pkt c
alter table marynarz add foreign key(statek) references statek(nazwa_statku) ON DELETE SET NULL;
```

### Zadanie 5
```sql
#pkt a
update marynarz set statek=null;

#pkt b
delete from marynarz where id_postaci=10;

#pkt c
delete from statek where rodzaj_statku;

#pkt d
alter table postac drop foreign key postac_ibfk_1;
alter table marynarz drop foreign key marynarz_ibfk_1;
drop table statek;

#pkt e
create table zwierz(id int auto_increment primary key, nazwa varchar(120), wiek int unsigned);
#pkt f
insert into zwierz select * from postac where rodzaj="ptak" or rodzaj="wąż";
```
