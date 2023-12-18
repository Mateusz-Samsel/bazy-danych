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
#pkt 3
SELECT wyprawa.nazwa, SUM(ekwipunek.ilosc) FROM wyprawa INNER JOIN uczestnicy ON wyprawa.id_wyprawy=uczestnicy.id_wyprawy INNER JOIN ekwipunek ON ekwipunek.idKreatury=uczestnicy.id_uczestnika GROUP BY wyprawa.nazwa;
```
### Zadanie 2
```sql
SELECT wyprawa.nazwa, COUNT(uczestnicy.id_uczestnika), GROUP_CONCAT(kreatura.nazwa SEPARATOR ', ')
AS imiona_uczestnikow FROM wyprawa LEFT JOIN uczestnicy ON
wyprawa.id_wyprawy=uczestnicy.id_wyprawy LEFT JOIN kreatura ON kreatura.idKreatury=uczestnicy.id_uczestnika GROUP BY wyprawa.nazwa;
#pkt 2
SELECT ew.kolejnosc, s.nazwa, k.nazwa FROM wyprawa w INNER JOIN etapy_wyprawy ew ON
w.id_wyprawy=ew.idWyprawy INNER JOIN sektor s ON s.id_sektora=ew.sektor INNER JOIN
kreatura k ON k.idKreatury=w.kierownik ORDER BY ew.kolejnosc ASC, w.data_rozpoczecia ASC;
```
