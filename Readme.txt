# Diplom_2
# Файловый состав проекта:

# helpers - файл с тестовыми данными для параметрических тестов.
# requirements - зависимости.
# pytest.ini - добавлен, т.к. без него не запускались тесты allure.

# Папка objects сдержит классы объектов:
#   client - класс клиентов
#   ingredient - класс ингредиентов
#   order - класс заказов

# Папка tests содержит данные тестов
#   conftest - содержит фикстуру для регистрации и удаления клиента
#   tests_client_data_changing - Тесты на изменение клиентских данных
#   tests_client_logining - Тесты на вход клиентов
#   tests_client_registering - Тесты для регистрации клиентов.
#   tests_order_creating - Тесты на создание заказов.
#   tests_order_list_getting - Тесты на получение списоков заказов.

#   Папка allure_results - содержит все результаты тестов.
