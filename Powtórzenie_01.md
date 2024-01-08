## Zestaw powtórzeniowy przed kolokwium zestaw 1 
```sql
# PKT 1 
select imie,nazwisko,year(data_urodzenia) as "Rok Urodzenia" from pracownik;
# PKT 2 
SELECT imie,nazwisko, year(now())-year(data_urodzenia) as "Wiek" from pracownik;
#PKT 3
SELECT  dzial.nazwa,count(p.id_pracownika) from dzial inner join pracownik p on p.dzial=id_dzialu group by dzial.nazwa; 
#PKT 4
select k.nazwa_kategori, count(sm.ilosc) as "Liczba produktów"  from kategoria k inner join towar t on t.kategoria=k.id_kategori inner join stan_magazynowy sm on t.id_towaru=sm.towar group by k.nazwa_kategori;
#PKT 5
SELECT k.nazwa_kategori,group_concat(' ', t.nazwa_towaru) from kategoria k inner join towar t on t.kategoria=k.id_kategori group by k.nazwa_kategori;
#PKT 6
SELECT round(avg(pensja),2) from pracownik;
#PKT 7
SELECT round(avg(pensja),2) from pracownik where year(curdate()-data_zatrudnienia)>=5;
#PKT 8
select t.nazwa_towaru,sum(pz.ilosc) from towar t inner join pozycja_zamowienia pz 
on t.id_towaru=pz.towar group by t.nazwa_towaru order by 2 desc limit 10;
#PKT 8 rozwiązanie drugie
select t.nazwa_towaru,count(pz.id_pozycji) from towar t inner join pozycja_zamowienia pz 
on t.id_towaru=pz.towar group by t.nazwa_towaru order by 2 desc limit 10;
#PKT 9
select z.numer_zamowienia, sum(pz.ilosc * pz.cena) from zamowienie z inner join pozycja_zamowienia pz on z.id_zamowienia=pz.zamowienie
where year(z.data_zamowienia)=2017 and quarter(z.data_zamowienia)=1 group by z.id_zamowienia;
#PKT 10
select p.imie,p.nazwisko,sum(pz.ilosc * pz.cena) from pracownik p inner join zamowienie z on p.id_pracownika=z.pracownik_id_pracownika 
inner join pozycja_zamowienia pz on z.id_zamowienia=pz.zamowienie group by p.id_pracownika order by 3 desc;
```
