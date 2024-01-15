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
### Zadanie 3
```sql
#pkt 1
SELECT IFNULL(COUNT(ew.sektor), 0) as ile_razy, s.nazwa as nazwa FROM sektor s
LEFT JOIN etapy_wyprawy ew ON ew.sektor=s.id_sektora GROUP BY s.id_sektora;
#pkt 2
SELECT k.nazwa, CASE
WHEN COUNT(u.id_uczestnika) > 0 THEN 'bral udzial w wyprawie' 
ELSE 'nie bral udzialu w wyprawie' 
END as czy_bral_udzial 
FROM kreatura k LEFT JOIN uczestnicy u ON u.id_uczestnika=k.idKreatury GROUP BY k.nazwa;
```
### Zadanie 4
```sql
#PKT 1
SELECT w.nazwa, SUM(CHAR_LENGTH(ew.dziennik)) AS suma_znakow
FROM wyprawa w JOIN etapy_wyprawy ew ON w.id_wyprawy=ew.idWyprawy
GROUP BY w.nazwa HAVING suma_znakow < 400;
#pkt 2
SELECT w.nazwa, SUM(z.waga*e.ilosc)/COUNT(u.id_uczestnika) AS sr_waga FROM 
wyprawa w INNER JOIN uczestnicy u ON w.id_wyprawy=u.id_wyprawy
INNER JOIN kreatura k ON u.id_uczestnika=k.idKreatury 
INNER JOIN ekwipunek e ON e.idKreatury=k.idKreatury 
INNER JOIN zasob z ON z.idZasobu=e.idZasobu GROUP BY w.nazwa;
```
### Zadanie 5
```sql
SELECT k.nazwa, DATEDIFF(w.data_rozpoczecia, k.dataUr) as wiek_w_dniach, w.nazwa 
FROM etapy_wyprawy ew INNER JOIN sektor s ON ew.sektor=s.id_sektora
INNER JOIN wyprawa w ON w.id_wyprawy=ew.idWyprawy INNER JOIN uczestnicy u ON w.id_wyprawy=u.id_wyprawy
INNER JOIN kreatura k ON k.idKreatury=u.id_uczestnika WHERE s.nazwa='Chatka dziadka' GROUP BY k.nazwa;
```
