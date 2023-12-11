### Zadanie 1
```sql
#pkt 1
create table uczestnicy select * from wikingowie.uczestnicy;
create table etapy_wyprawy select * from wikingowie.etapy_wyprawy;
create table sektor select * from wikingowie.sektor;
create table wyprawa select * from wikingowie.wyprawa;
#pkt 2
select k.nazwa from kreatura k left join uczestnicy u on k.idKreatury=u.id_uczestnika where u.id_uczestnika is null;
#pkt 2
select k.nazwa from kreatura k left join uczestnicy u on k.idKreatury=u.id_uczestnika where u.id_uczestnika is null;
select * from wyprawa w inner join uczestnicy u on w.id_wyprawy=u.id_wyprawy left join kreatura k on k.idKreatury=u.id_uczestnika
left join ekwipunek e on k.idKreatury=e.idKreatury;

```
