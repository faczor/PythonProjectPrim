Algorytm Prim.

Jest to algortym, który wyznacza minimalne drzewo rozpinające dla grafu spójnego.

Rozpiska klas:
Edge - odpowiada za krawedz w grafie,
Vertex - odpowiada za wierzchołek grafu,
Graph - klasa reprezentująca graf, w niej możemy znalezc dodatkowo metody takie jak dodawanie wierzchołka, dodawanie krawedzi,
Reader - klasa dzięki której odczytujemy graf z pliku i tworzymy graf na podstawie danych,
Prim - main klasa naszego algorytmy, to właśnie tą klase należy uruchomić

Format pliku wejściowego:

ilość_wierzchołków ilość_krawędzi
wiechołek wierzchołek waga_krawędzi
.
.
.

Aby zmienić plik z którego chcemy odczytać graf należy w pliku Prim.py w linijce 58 zmienić nazwe pliku, plik powinien znajdowac się w folderze naszej aplikacji.