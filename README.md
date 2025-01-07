# Проект автотестов для учебного сервиса «Яндекс.Самокат»

## Описание проекта
Данный проект содержит автотесты для проверки функциональности сервиса «Яндекс.Самокат».  
Для тестирования используется браузер **Mozilla Firefox**.  

Проект построен с использованием принципов Page Object Model (POM):  
- Локаторы для страниц вынесены в отдельные файлы в папке `locators`.  
- Реализация взаимодействий с элементами страниц осуществляется через методы, описанные в файлах папки `pages`.  
- Базовые методы, такие как клики, ввод текста и проверки видимости элементов, находятся в `base_page` (папка `pages`).  

## Тестовые сценарии
### 1. Выпадающий список в разделе «Вопросы о важном»
Проверка отображения текста ответа при нажатии на вопрос.  
Для каждого вопроса написан отдельный тест.  
Тесты находятся в файле:  
```
tests/test_questions.py
```

### 2. Позитивный сценарий заказа самоката
Тесты проверяют полный позитивный сценарий заказа с двумя наборами данных.  
Проверяемые элементы сценария:  
- Две кнопки заказа: «Заказать» в верхней и нижней частях страницы.  
- Заполнение формы заказа.  
- Отображение всплывающего окна с сообщением об успешном создании заказа.  
- Переход на главную страницу «Самоката» при клике на логотип.  
- Переход на главную страницу Дзена через редирект при клике на логотип Яндекса.  

Тесты находятся в файле:  
```
tests/test_order.py
```

## Структура проекта
```
Sprint_6/
│
├── allure_results/            # Папка для хранения результатов тестов Allure
│
├── locators/                  # Локаторы для страниц
│   ├── __init__.py            # Пустой файл для создания Python-пакета
│   ├── main_page_locators.py  # Локаторы для главной страницы
│   └── order_page_locators.py # Локаторы для страницы заказа
│
├── pages/                     # Реализация взаимодействий с элементами страниц
│   ├── __init__.py            # Пустой файл для создания Python-пакета
│   ├── base_page.py           # Базовые методы для работы с веб-элементами
│   ├── main_page.py           # Методы для работы с главной страницей
│   └── order_page.py          # Методы для работы со страницей заказа
│
├── tests/                     # Тестовые сценарии
│   ├── __init__.py            # Пустой файл для создания Python-пакета
│   ├── test_order.py          # Тесты для сценариев заказа
│   └── test_questions.py      # Тесты для вопросов о важном
│
├── config.py                  # Параметры конфигурации проекта
├── conftest.py                # Фикстуры для тестов
├── constants.py               # Константы для тестов
├── requirements.txt           # Список зависимостей для проекта
└── README.md                  # Описание проекта
```

### Основные зависимости
Для работы проекта требуется установить зависимости, указанные в `requirements.txt`.  
Используйте следующую команду:  
```bash
pip install -r requirements.txt
```

## Запуск тестов
### Запуск всех тестов:
```bash
pytest tests/
```

### Формирование отчёта Allure
Перед запуском отчёта папка `allure_results` должна быть очищена.  

1. Запустите автотесты с сохранением результатов в формате Allure:  
```bash
pytest tests/ --alluredir=allure_results
```

2. Сформируйте отчёт Allure:  
```bash
allure serve allure_results
```

## Особенности реализации
- **Page Object Model (POM):**
  - `MainPage` и `OrderPage` используют базовые методы из `BasePage`.
  - Локаторы страниц вынесены в файлы `main_page_locators.py` и `order_page_locators.py` в папке `locators`.

- **Фикстуры и конфигурация:**
  - Фикстуры для инициализации браузера и других операций находятся в файле `conftest.py`.
  - Константы (например, тестовые данные) определены в `constants.py`.
  - Конфигурационные параметры вынесены в `config.py`.


