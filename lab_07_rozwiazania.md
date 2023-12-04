### Zadanie 1
```sql
select avg(waga) from kreatura;
#pkt 2
select avg(waga),count(waga) from kreatura group by rodzaj;
#pkt 3
select avg(year(now())-year(dataUr)) as "średni wiek" from kreatura group by rodzaj;
#sum(waga) - suma
#count(waga) - ilość wystąpień
```
### Zadanie 2
```sql
select sum(waga*ilosc),rodzaj from zasob group by rodzaj;
#pkt 2
select nazwa,avg(waga) from zasob where ilosc >= 4 group by nazwa HAVING sum(waga)>10;
#pkt 3
select count(nazwa)-count(distinct(nazwa)) from zasob group by rodzaj HAVING(count(nazwa)-count(distinct(nazwa)))>0;
#HAVING - Działa po agregacji;używa funkcji segregującej np.avg(), sum(), count()
#WHERE - działa przed agregacją (przed selectem)
```

### Zadanie 3
```sql
SELECT k.nazwa, e.ilosc,e.idZasobu  from kreatura k inner join ekwipunek e on k.idKreatury=e.idKreatury;
#pkt 2
SELECT k.nazwa, z.nazwa from kreatura k inner join ekwipunek e on k.idKreatury=e.idKreatury
inner join zasob z on e.idZasobu=z.idZasobu;
#pkt 3
select * from kreatura k left join ekwipunek e on k.idKreatury = e.idKreatury
where e.idKreatury is null;
#Polecenie na dole takie samo jak w pkt 1
#SELECT k.nazwa, k.idKreatury,e.idKreatury from kreatura k,ekwipunek e where k.idKreatury=e.idKreatury;
#podzapytanie do 3
#select idKreatury from kreatura where idKreatury not in (select idKreatury from ekwipunek where idKreatury is not null);
```
