# Przestrzenie nazw w Python ( Python namespaces )

# Namespace to zestaw aktualnie zdefiniowanych symbolicznych nazw wraz z informacja o tym
# jaki obiekt jest reprezentowany przez konkretna nazwe.
# Namespace mozna sobie wyobrazic jako dictionary w ktorym kluczem jest nazwa obiektu a wartoscia
# obiekt o tej wlasnie nazwie. Czyli kazda para klucz-wartosc pozwala mapowac nazwe do przypisanego
# jej obiektu.

# Mamy 4 rodzaje namespaces:
# a. built-in
# b. global
# c. enclosing
# d. local
# Maja one rozne czasy zycia. Podczas wykonywania programu Python tworzy na wlasne potrzeby
# kolejne namespaces kiedy ich potrzebuje i usuwa je kiedy ich dluzej juz nie potrzebuje.
# Czyli w danej chwili moze istniec kilka namespaces.

# Built-in namespace zawiera nazwy wszystkich wbudowanych obiektow Python
# Mozesz wypisac zawartosc tego namespace za pomoca
print(dir(__builtins__))
# Interpreter Python tworzy built-in namespace kiedy aplikacja rusza. Ten namespace bedzie obecny
# dopoki interpreter nie zakonczy swojego dzialania.

# Global namespace zawiera wszystkie nazwy, ktore sa zdefiniowane na poziomie skryptu poza jakakolwiek
# funkcja czy obiektem. Python tworzy ten namespace kiedy rusza cialo glownego skryptu. Ten namespace
# jest usuwany dopiero kiedy interpreter konczy swoje dzialanie.
# Interpreter tworzy globla namespace dla kazdego modulu, ktory zostanie zaladowany do aplikacji.

# Local oraz enclosing namespaces to przestrzenie nazw tworzone kiedy wywolywana jest nowa funkcja.
# Tego rodzaju namespace bedzie obecny dopoki wykonywane jest cialo funkcji.
# Rozpatrzmy prosty przyklad

def outer():
    print('Outer start')

    def inner():
        print('Inner start')
        print('Inner end')

    inner()

    print('Outer end')

outer()

# Kiedy zostanie wywolana funkcja outer Python tworzy nowy namespace dla funkcji outer.
# Kiedy wewnatrz funkcji outer zostanie wywolana funkcja inner wtedy Python tworzy osobny
# namespace dla tej funkcji. Namespace tworzony dla funkcji inner nazywamy local namespace.
# Namespace tworzony dla funkcji outer nazywamy enclosing namespace. Kazdy z tych namespace trwa tak
# dlugo jak wykonuje sie funkcja ktorej ten namespace zostal przyporzadkowany.
# Kiedy namespace nie jest juz potrzebnhy bedzie usuniety. Nie oznacza to ze Python od razu usuwa
# znajduja sie w nim obiekty - moze zajac mu to troche wiecej czasu, ale wszystkie odwolania
# w ramach tego namespace przestaja byc wazne.

# Zasieg zmiennych
# W momencie kiedy mamy wiele roznych namespaces moze sie zdarzyc ze mozemy miec instancje o tej samej
# nazwie jednak dopoki sa one w roznych namespaces to nie koliduja ze soba i moga dzialac rownolegle.
# Kiedy odwolujesz sie do pewnego obiektu o konkretnej nazwie Python musi wywnioskowac do ktorego
# namespace ma sie odwolac. Wtedy wlasnie wykorzysta koncepcje zakresu ( scope )
# Zakresem zmiennej nazywamy obszar w programie, w ktorym dana nazwa obiektu ma znaczenie / wystepuje.
# Python determinuje zakres zmiennej juz w runtime na podstawie tego gdzie wystapila deifnicja zmiennej
# i w ktorym miejscu programu odwolujesz sie do zmiennej

# Kiedy w kodzie wystapi odwolanie do pewnej nazwy zmiennej wtedy Python przeszukuje kolejne namespaces
# wedlug ustalonego porzadku ( zasada LEGB ):

# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in

# Przyklad 1
print('-------------------------------------------- 1 -------------------------------------------')

# def outer0():
#     def inner0():
#         print(v0)
#
#     inner0()
#
# outer0()

# Przyklad 2
print('-------------------------------------------- 2 -------------------------------------------')
v1 = 'a'

def outer1():
    def inner1():
        print(v1)

    inner1()

outer1()


# Przyklad 3
print('-------------------------------------------- 3 -------------------------------------------')
v2 = 'a'

def outer2():
    v2 = 'aa'

    def inner2():
        print(v2)

    inner2()

outer2()

# Przyklad 4
print('-------------------------------------------- 4 -------------------------------------------')
v3 = 'a'


def outer3():
    v3 = 'aa'

    def inner3():
        v3 = 'aaa'
        print(v3)

    inner3()

outer3()


print('-------------------------------------------- 5 -------------------------------------------')
# Teraz pokazemy jak odwolac sie faktycznie do dictionaries w postaci ktorych sa przechowywane namespaces
# w Python

my_var = 100
print(globals())  # zwraca referencje do zawartosci aktualnie ustawionego global namespace
# Mozesz normalnie odwolywac sie do zmiennych z takiego dictionary
print(globals()['my_var'])
# mozesz modyfikowac obiekt z poziomu globals()
globals()['my_var'] = 200
print(my_var)


print('-------------------------------------------- 6 -------------------------------------------')
def my_fun(aa, bb):
    xx = 11
    yy = 22
    print(locals())   # zwraca referencje do aktualnie ustawionego local namespace - masz tutaj parametry funkcji
    # oraz tworzone w niej obiekty lokalne
    print(globals())  # zauwaz ze pojawila sie tutaj nazwy funkcji !

my_fun(111, 222)

print('-------------------------------------------- 7 -------------------------------------------')
# Kiedy wywolujesz locals() poza jakakolwiek funkcja to przechowuje te same elementy co globals()

# Jest jeszcze jedna roznica pomiedzy locals() oraz globals()

glob = globals()  # glob jest referencja do dictionary z globals() i jezeli dodasz pewne obiekty do zakresu
# globalnego to glob uwzgledni te zmiany
print(glob)
counter = 10
print(glob)

def another_fun():
    temp1 = 11
    loc = locals()  # tutaj loc jest aktualna kopia zakresu w momencie przypisania do niej locals i nie bedzie
    # juz potem uwzgledniac nowo dodawanych do zakresu obiektow
    print(loc)

    temp2 = 22
    print(loc)  # nie ma temp2 w loc

another_fun()