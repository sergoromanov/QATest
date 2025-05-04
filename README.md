# Python Automation Project

## Описание

Этот проект состоит из трёх частей:

1. **process_numbers.py** — скрипт, который:
   - Запрашивает список чисел у пользователя,
   - Выводит только чётные числа,
   - Находит максимальное и минимальное значение,
   - Сортирует список чисел.

2. **test_example.py** — автотест с использованием Selenium, который:
   - Открывает сайт https://example.com,
   - Проверяет, что заголовок содержит слово "Example",
   - Находит ссылку "More information..." и кликает по ней,
   - Проверяет, что переход выполнен на https://www.iana.org/help/example-domains.

3. **requirements.txt** — файл зависимостей проекта.

---

## Требования

- Python 3.10 или новее
- Google Chrome
- ChromeDriver соответствующей версии (скачать можно отсюда: https://googlechromelabs.github.io/chrome-for-testing/)
- Установленные зависимости из `requirements.txt`

---

##  Установка

1. Склонируйте репозиторий:


git clone https://github.com/sergoromanov/QAtest.git
cd QAtest


2. Установите зависимости:


pip install -r requirements.txt


---

##  Запуск

### Часть 1: обработка чисел

python process_numbers.py

Скрипт запросит у вас ввод чисел через запятую и выведет:
- Чётные числа
- Максимум и минимум
- Отсортированный список

---

### Часть 2: Selenium-тест

1. Убедитесь, что путь к `chromedriver.exe` в `test_example.py` указан правильно:




2. Запустите тест:

    python test_example.py


Вывод при успешном выполнении:

```
Текущий URL: https://www.iana.org/help/example-domains
Тест пройден успешно!
```

---


##  Ссылка на репозиторий

https://github.com/sergoromanov/QAtest.git
