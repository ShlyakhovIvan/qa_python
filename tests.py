from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #Проверяем, что у добавленной книги нет жанра
    def test_add_new_book_one_book_has_no_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    #Проверяем, что нельзя добавить новую книгу с названием больше 40 символов
    def test_add_new_book_name_of_book_over_40_symb_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби. Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    #проверяем, что необходимый жанр добавился
    def test_set_book_genre_one_book_genre_is_added(self, collector):
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.books_genre['Восточный экспресс'] == 'Детективы'

    #проверяем, что по имени можно получить жанр
    def test_get_book_genre_one_book_got_genre(self, collector):
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_book_genre('Восточный экспресс') == 'Детективы'

    #проверяем, что можно вывести список книг по специфичному жанру
    def test_get_books_with_specific_genre_two_book_got_detective_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        collector.add_new_book('Десять негретят')
        collector.set_book_genre('Десять негретят', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Восточный экспресс', 'Десять негретят']
    
    # Проверяем, что можно получить список книг, состоящий из двух книг
    def test_get_books_genre_of_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби' : 'Ужасы', 'Восточный экспресс' : 'Детективы'}

    # Проверяем, что можно получить список, разрещенный детям
    def test_get_books_for_children_two_books_got_one_book_mult(self, collector):
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспреcc', 'Детективы')
        assert collector.get_books_for_children() == ['Золушка']

    # Проверяем, что можно добавить книгу в избранное
    def test_add_book_in_favorites_one_book_added_to_favorite(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Восточный экспресс')
        collector.add_new_book('Десять негретят')
        collector.add_book_in_favorites('Восточный экспресс')
        assert 'Восточный экспресс' in collector.favorites

    #Проверяем, что можно удалить книгу из избравнного
    def test_delete_book_from_favorites_was_deleted_one_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Восточный экспресс')
        collector.add_new_book('Десять негретят')
        collector.add_book_in_favorites('Восточный экспресс')
        collector.delete_book_from_favorites('Восточный экспресс')
        assert len(collector.favorites) == 0

    # Провеяем, что можно получить список избранных
    def test_get_list_of_favorites_books_got_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Восточный экспресс')
        collector.add_new_book('Десять негретят')
        collector.add_book_in_favorites('Восточный экспресс')
        collector.add_book_in_favorites('Десять негретят')
        assert collector.get_list_of_favorites_books() == ['Восточный экспресс', 'Десять негретят']