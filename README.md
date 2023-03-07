## Przypomnienie o zwrocie pożyczonej książki!

Program korzysta z baza danych stworzonej w ramach SQLite (do repozytorium dołączony szablon) przechowującej informację o ID, imieniu,nazwisku oraz e-mailu czytelnika. Dodatkowo baza przechowuje dane, którą książke czytelnik wypożyczył ,datę wypożyczenia oraz zwrotu. Aby program działał poprawnie należy stworzyć i uzupełnić własną baze danych. 
Celem programu jest wysyłanie wiadomości e-mail obsługującej format HTML czytelnikowi z przypomnieniem o zwrocie książki. Jeśli program zostanie uruchomiony w dniu, który przypada na dzień zwrotu lub w dniach późniejszych program wyśle do tej osoby email z komunikatem przypominającym o konieczności zwrotu pożyczonej książki.

### Zmienne środowiskowe
W pliku .env.dist pokazany jest szablon jak powinny wyglądać zmienne środowiskowe, które są wykorzystywane. Aby program działał należy stworzyć plik .env i dostosować zmienne środowiskowe do własnych potrzeb. Program jest dostosowany do obsługi połączeń z protokołem sieciowym SSL. W szablonie dane portu i smtp server podane zostały dla Gmail'a. W przypadku korzystania z innych serwisów pocztowych należy te zmienne ustawić tak aby były zgodne z danym serwisem pocztowym.Zmienne SENDER_EMAIL,PASSWORD powinny być usatwione na osobisty login oraz hasło do poczty. Zmienna DB_NAME domyślnie nie przyjmuje wartości. Chcąc korzystać z własnej bazy danych należy w tym miejscu wpisać nazwę pliku zawierającego baze danych, z którego chce się korzystać.

### Wykorzystane technologie:
Python,HTML,CSS,SQLite
