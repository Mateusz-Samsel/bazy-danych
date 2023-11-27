### Zadanie 1
```sql
CREATE TABLE kreatura select * from wikingowie.kreatura;
CREATE TABLE zasob select * from wikingowie.zasob;
CREATE TABLE ekwipunek select * from wikingowie.ekwipunek;

#pkt 2
select * from zasob;

#pkt 3
select * from zasob where rodzaj="jedzenie";

#pkt 4
select idZasobu,ilosc from ekwipunek where idKreatury in (1,3,5);
```

### Zadanie 2
```sql
select * from kreatura where rodzaj!="wiedzma" and udzwig>50; 
#pkt 2 
select * from zasob where waga between 2 and 5;
#pkt 3
select * from kreatura where nazwa like '%or%' and udzwig between 30 and 70;
```

### Zadanie 3
```sql
select * from zasob where dataPozyskania like '%07%' or dataPozyskania like '%08%';
#pkt2
select * from zasob where rodzaj is not null order by waga asc;
#pkt 3
select * from kreatura where dataUr is not null order by dataUr asc limit 5;
```

### Zadanie 4
```sql
select distinct(rodzaj) from kreatura;
#pkt 2
select concat(idKreatury,'-', nazwa) from kreatura where rodzaj like 'wi%';
#pkt 3
select (ilosc*waga) as "Całkowita waga" from zasob  where year(dataPozyskania) between 2000 and 2007;
```

### Zadanie 5
```sql
select (0.7*waga) as "Masa netto",(0.3*waga) as "Odpadki" from zasob where rodzaj="jedzenie";
#pkt 2
select * from zasob where rodzaj is null;
#pkt 3
select distinct(nazwa) from zasob where nazwa like 'Ba%' or nazwa like '%os' order by nazwa asc;
```
