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
