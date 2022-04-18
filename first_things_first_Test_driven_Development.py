def test_sort(sorting_algorithm):
    """ Тестируем алгоритм, сортирующий список по возрастанию."""    
    # Напечатать имя функции
    print(f'Тестируем: {sorting_algorithm.__doc__}')

    assert sorting_algorithm([1, 3, 2.0, 4]) == [1, 2.0, 3, 4], (
        "Неправильно сортирует список содержащий int и float")
    assert sorting_algorithm([1, 3, 2.0, 4]) == [1, 2.0, 3, 4], (
        "Неправильно сортирует список содержащий отрицательные величины или"
        "нулевое значение")
    assert sorting_algorithm([1, 1, 1, 1]) == [1, 1, 1, 1], (
        "Неправильно сортирует список содержащий одинаковые числа")
    assert sorting_algorithm([]) == [], (
        "Неправильно сортирует пустой список")

    print(f'Тест для {sorting_algorithm.__name__} пройден')
	
# Ипортируем тестируемые функции из пакета ttd_sprint5_data
test_sort(bubble_sort)
test_sort(timsort_sort)
test_sort(selection_sort)
test_sort(insertion_sort)
test_sort(merge_sort)
test_sort(heap_sort)  
test_sort(quick_sort)
test_sort(sus_sort)
