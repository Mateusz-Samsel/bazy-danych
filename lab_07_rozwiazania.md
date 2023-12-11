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

### Zadanie 4
```sql
select k1.nazwa, z1.nazwa from kreatura k1,ekwipunek ek natural join zasob z1 where k1.dataUr like '167%' ;
#pkt 2
select k.nazwa, e.ilosc, z.nazwa from kreatura k inner join ekwipunek e on k.idKreatury=e.idKreatury
inner join zasob z on z.idZasobu=e.idZasobu where z.rodzaj="jedzenie" order by k.dataUr desc limit 5;
#pkt 3
select concat(k1.nazwa,' - ',k2.nazwa) from kreatura k1, kreatura k2 where k1.idKreatury -k2.idKreatury =5;
```
### Zadanie 5
```sql
select k.rodzaj, avg(e.ilosc*z.waga) from kreatura k inner join ekwipunek e on 
k.idKreatury=e.idKreatury inner join zasob z on z.idZasobu=e.idZasobu
where k.rodzaj not in ('malpa','waz') and e.ilosc<30 group by k.rodzaj;
#pkt 2
select concat(k1.nazwa,', ',k2.nazwa)as "min, max",p.rodzaj,p.min, p.max from (select rodzaj,min(dataUr) min,max(dataUr) max from kreatura group by rodzaj) as p inner join kreatura k1 on k1.dataUr=p.min inner join kreatura k2 on k2.dataUr=p.max;
#lub
#select concat(k1.nazwa,', ',k2.nazwa)as "najstarszy, najmlodszy",p.rodzaj,p.min, p.max from (select rodzaj,min(dataUr) min,max(dataUr) max from kreatura group by rodzaj) as p inner join kreatura k1 on k1.dataUr=p.min inner join kreatura k2 on k2.dataUr=p.max;
select 'najmlodsza',a.maxData,b.nazwa, a.rodzaj from (select max(dataUr) maxData,rodzaj from kreatura group by  rodzaj) a,
(select nazwa,dataUr from kreatura) b where a.maxData = b.dataUr
union
select 'najstarsza',a.minData,b.nazwa,a.rodzaj from (select min(dataUr) minData, rodzaj from kreatura group by rodzaj) a,
(select nazwa,dataUr from kreatura) b where a.minData=b.dataUr;
```
