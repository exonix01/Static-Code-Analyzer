# Static-Code-Analyzer

## EN
### Description

Static-Code-Analyzer is a script that checks the correctness of the analysed Python code with some Python code syntax rules.

The following rules are checked during the analysis:

* Whether the number of characters in a line does not exceed 79 characters;
* Whether the indentation consists of multiples of four spaces;
* Whether there are any unnecessary semicolons in the code (except for comments);
* Is the inline comment separated by at least two spaces;
* Whether there is a "TODO" in the comments;
* Whether there are more than two blank lines in a row in the code;
* Whether there are too many spaces after the keyword "def" or "class";
* Whether the class name is written in CamelCase style;
* Whether the function name is written in snake_case style;
* Whether the name of the function argument is written in snake_case style;
* Whether the name of the variable in the function is written in snake_case style;
* Whether the default value of a function argument is not mutable.

The script is run via the command line. The argument it takes is the path to a file (.py) or folder (containing .py files). If the argument is the path to a file - the file is analysed, if the argument is the path to a folder - every .py file in the folder is analysed.

Sample input:
> code_analyzer.py D:\Static Code Analyzer\task\test

Sample output:
> D:\Static Code Analyzer\task\test\test_3.py: Line 9: S012 The default argument value is mutable
> 
> D:\Static Code Analyzer\task\test\test_4.py: Line 2: S010 Argument name "Beta" should be written in snake_case
> 
> D:\Static Code Analyzer\task\test\test_5.py: Line 3: S011 Variable "Beta" should be written in snake_case
> 
> D:\Static Code Analyzer\task\test\test_5.py: Line 9: S011 Variable "Variable" should be written in snake_case`

## PL
### Opis
Static-Code-Analyzer to skrypt sprawdzający poprawność analizowanego kodu Pythona z niektorymi zasadami składni kodu Pythona.

Podczas analizy sprawdzane są następujace zasady:
* Czy liczba znaków w wierszu nie przekracza 79 znaków;
* Czy wcięcie składa się z wielokrotności czterech spacji;
* Czy w kodzie znajdują się niepotrzbne średniki (poza komentarzami);
* Czy komentarz znajdujący się w linii z kodem oddzielony jest conajmniej dwoma spacjami;
* Czy w komantarzach znajduje się "TODO";
* Czy w kodzie występują więcej niż dwa puste wiersze pod rząd;
* Czy po słowie kliczowym "def" lub "class" nie znajduje się zbyt wiele spacji;
* Czy nazwa klasy zapisana jest stylem CamelCase;
* Czy nazwa funkcji zapisana jest stylem snake_case;
* Czy nazwa argumentu funkcji zapisana jest stylem snake_case;
* Czy nazwa zmiennej w funkcji zapisana jest stylem snake_case;
* Czy domyślna wartośc argumentu funkcji nie jest mutowalna.

Skrypt jest uruchamiany za pomocą linii komend. Argumentem jaki przyjmuje jest ściezka dostępu do pliku (.py) lub folderu (zawierającego pliki .py). Jeśli argumentem jest ścieżka do pliku - plik jest analizowany, jeśli argumentem jest ściezka do folderu - analizowany jest każdy plik .py znajdujący się w folderze.

Przykładowe uruchomienie skryptu:
> code_analyzer.py D:\Static Code Analyzer\task\test

Przykładowy wynik:
> D:\Static Code Analyzer\task\test\test_3.py: Line 9: S012 The default argument value is mutable
> 
> D:\Static Code Analyzer\task\test\test_4.py: Line 2: S010 Argument name "Beta" should be written in snake_case
> 
> D:\Static Code Analyzer\task\test\test_5.py: Line 3: S011 Variable "Beta" should be written in snake_case
> 
> D:\Static Code Analyzer\task\test\test_5.py: Line 9: S011 Variable "Variable" should be written in snake_case`

*Project from JetBrains Academy*
