### Uruchamianie aplikacji:
Przed uruchomieniem aplikacji upewnij się, że masz zainstalowane lokalnie lub w środowisku wirtualnym biblioteki wymagane do poprawnego jej działania. Żeby je zainstalować uruchom terminal, wejdź do folderu projektu a następnie użyj polecenia "pip install -r requirements.txt"
Aby zmienić parametry takie jak udostępniane porty, musisz zmodyfikować plik Dockerfile w linii: EXPOSE <port\> lub w pliku docker-compose.yaml w linii : ports - <port\>.

Następnie wybierz jeden z trzech sposobów urachamiarnia aplikacji:
1. Lokalnie:\
Aby uruchomić aplikację potrzebujesz wejść do folderu, w którym znajduje się plik app.py i użyć komendy "gunicorn -w 4 -b 0.0.0.0:5000 app:app". Otwórz przeglądarkę i wpisz adres http://0.0.0.0:5000.
    
2. Za pomocą Dockera:\
Uruchomienie aplikacji w kontenerze Dockera umożliwia plik Dockerfile. Aby to zrobić na początku zbuduj obraz za pomocą komendy "docker build -t <nazwa obrazu\> . " a następnie uruchom konter z aplikacją używając "docker run -p 5000:5000 <nazwa obrazu\>". Otwórz przeglądarkę i wpisz adres http://0.0.0.0:5000.

3. Za pomocą Docker Compose
Ostatnim sposobem jest użycie narzędzia Docker Compose, które pozwala na uruchomienie wielu kontenerów jednocześnie. Aby uruchomić aplikację za pomocą Docker Compose użyj polecenia "docker compose up". Otwórz przeglądarkę i wpisz adres http://0.0.0.0:5000.
