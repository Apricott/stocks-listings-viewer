# stocks-listings-viewer

PL

Program pozwala na wyświetlanie oraz podstawową analizę wykresu przedstawiającego notowania giełdowe wybranej spółki.

Program wykorzystuje następujące biblioteki języka python:
-pandas
-pandas-datareader
-scipy
-matplotlib
-statsmodels

Po uruchomieniu programu użytkownik podaje symbol spółki (ticker symbol) używany przez nią na giełdzie (dla platformy Yahoo Finance, ponieważ tam znajduje się baza z danymi, z których kozysta aplikacja). Przykładowe symbole: AAPL - Apple Inc., TSLA - Tesla, Inc.,
 MSFT - Microsoft Corporation, FB - Facebook, Inc., KGHA.F - KGHM Polska Miedz SA

W kolejnym kroku użytkownik może podać rodzaj danych, ktore mają zostać przedstawione na wykresie:
close - cena zamknięcia
open - cena otwarcia
high - najwyższa cena uzyskana danego dnia
low - najniższa cena uzyskana danego dnia
volume - wolumen obrotu
growth - dzienny wzrost

Domyślnie aplikacja pokazuje cenę zamknięcia.

Następnie może on wprowadzić datę początku oraz końca okresu, dla którego dane mają zostać wyświetlone (nie wcześniej
 niż 10 lat wstecz). Nie jest to jednak wymagane. W przypadku, w którym uzytkownik nie wprowadzi dat, wyświetlone zostą dane z
podstawowego okresu 10-ciu lat.

Przyciskiem 'Show Plot' wywołujemy żądany wykres. (Możliwe jest również wywolanie wykresu klawiszem Enter, jeśli pole
wprowadzania symbolu spółki jest aktywne)

Oprócz samego wykresu wyświetlany jest trend, wartości minimalne i maksymalne oraz średnia całego wykresu oraz kolejnych lat z 
wybranego przedziału.


Michał Król, Krystian Wojewoda - 
2019
