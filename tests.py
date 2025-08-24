import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_one_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_add_new_book_name_of_book_over_40_symb_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби. Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_one_book_genre_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_book_genre('Восточный экспресс') == 'Детективы'

    def test_get_book_genre_one_book_got_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_book_genre('Восточный экспресс') == 'Детективы'

    def test_get_books_with_specific_genre_two_book_got_detective_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        collector.add_new_book('Десять негретят')
        collector.set_book_genre('Десять негретят', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Восточный экспресс', 'Десять негретят']

    def test_get_books_genre_of_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_books_genre() == {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Восточный экспресс': 'Детективы'
        }

    def test_get_books_for_children_two_books_got_one_book_mult(self):
        collector = BooksCollector()
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_books_for_children() == ['Золушка']

    # --- Тесты для работы с избранным (используем только публичные методы) ---

    @pytest.mark.parametrize(
        "to_add, favorite, expected_favorites",
        [
            (
                ['Гордость и предубеждение и зомби', 'Восточный экспресс', 'Десять негретят'],
                ['Восточный экспресс'],
                ['Восточный экспресс']
            ),
            (
                ['Три мушкетёра', 'Мастер и Маргарита'],
                ['Мастер и Маргарита'],
                ['Мастер и Маргарита']
            )
        ]
    )
    def test_add_book_in_favorites(self, to_add, favorite, expected_favorites):
        collector = BooksCollector()
        for book in to_add:
            collector.add_new_book(book)
        for fav in favorite:
            collector.add_book_in_favorites(fav)
        assert collector.get_list_of_favorites_books() == expected_favorites
    def test_delete_book_from_favorites_was_deleted_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Восточный экспресс')
        collector.add_new_book('Десять негретят')
        collector.add_book_in_favorites('Восточный экспресс')
        collector.delete_book_from_favorites('Восточный экспресс')
        assert 'Восточный экспресс' not in collector.get_list_of_favorites_books()
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("favorite_books", [
        (['Восточный экспресс', 'Десять негретят']),
        (['Гордость и предубеждение и зомби']),
        ([])
    ])
    def test_get_list_of_favorites_books(self, favorite_books):
        collector = BooksCollector()
        all_books = ['Гордость и предубеждение и зомби', 'Восточный экспресс', 'Десять негретят']
        for book in all_books:
            collector.add_new_book(book)
        for book in favorite_books:
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == favorite_books
