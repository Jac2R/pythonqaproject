# UI Automation Testing with PyTest+Selenium

---

## Описание проекта | Project Description

Данный репозиторий содержит простой UI автотест для заполнения и отправки веб-формы. Тест реализован с использованием Selenium и PyTest.

При запуске, программа выполняет следующие действия:

1. Открывает страницу веб-сайта по ссылке
2. Заполняет все представленные на странице поля формы
3. Нажимает кнопку отправки запроса
4. Проверяет содержимое во всплывающем сообщении Alert

Тест считается успешно выполненным, если программа получила сообщение в Alert: "Message received!"

---

## Требования | Pre-requisites:

* Python 3.10
* Установленный браузер Chrome (необязательно). Программа запустится в headless режиме.

---

### Тестируемый вебсайт | Tested Website

[Practice Automation Form](https://practice-automation.com/form-fields/)

---

## Содержание

- [Описание проекта | Project Description](#описание-проекта--project-description)
- [Требования | Pre-requisites](#требования--pre-requisites)
  - [Тестируемый вебсайт | Tested Website](#тестируемый-вебсайт--tested-website)
- [Технологии | Tech Stack](#технологии--tech-stack)
- [Как запустить автотесты? | How to run Tests?](#как-запустить-автотесты--how-to-run-tests)
  - [Локальная установка проекта | Local Installation Guide](#локальная-установка-проекта--local-installation-guide)
- [Тестовая документация | Test Documentation](#тестовая-документация--test-documentation)
  - [Тест-кейсы | Test Cases](#тест-кейсы--test-cases)
    - [TC01 - Successful Form Submission (Positive)](#tc01---successful-form-submission-positive)
    - [TC02 - Invalid Email (Negative)](#tc02---invalid-email-negative)
    - [TC03 - No Email (Positive)](#tc03---no-email-positive)
    - [TC04 - No Name (Negative)](#tc04---no-name-negative)
    - [TC05 - Invalid Name (Negative)](#tc05---invalid-name-negative)
- [Allure Report](#allure-report)

---

## Технологии | Tech Stack

Проект реализован с использованием следующих инструментов:

* Python 3.10
* Selenium WebDriver 4.41.0
* PyTest 9.0.2
* Allure Reports 2.38.1

Необходимые версии модулей для установки указаны в файле проекта [requirements.txt](requirements.txt )

---

## Как запустить автотесты? | How to run Tests?

### Локальная установка проекта | Local Installation Guide

Перед загрузкой репозитория убедись, что у тебя установлена версия Python 3.10. Инструкция по установке версии 3.10 находится тут.

1. Клонируй репозиторий с проектом в свою любимую папку с проектами:
```
    git clone git@github.com:Jac2R/pythonqaproject.git
```
2. Установи модули, использовав команду:
```
    pip install -r requirements.txt
```
3. Запусти тесты:
```
    pytest -v
```
4. Запусти Allure report:
```
    pytest --alluredir=allure-results
    allure serve allure-results
```

---

# Тестовая документация | Test Documentation

## Тест-кейсы | Test Cases

### TC01 - Successful Form Submission (Positive)

**Предусловия**

Открыть https://practice-automation.com/form-fields/

**Шаги**

1. Ввести имя пользователя "**_Ivan Ivanov_**" в поле Name
2. Ввести пароль "**_Password13_**" в поле Password
3. Выбрать варианты "**_Milk_**" и "**_Coffee_**" в списке "What is your favorite drink?"
4. Выбрать цвет "**_Yellow_**" в списке "What is your favorite color?"
5. Выбрать любой из вариантов в выпадающем списке "Do you like automation?"
6. Ввести почту "**_ivan@exmail.com_**" в поле Email
7. Написать "**_5, Katalon Studio_**" в поле Message
8. Нажать на кнопку Submit

**Ожидаемый результат**

Форма отправляется.
Появляется всплывающий Alert с сообщением:
`Message received!`

---

### TC02 - Invalid Email (Negative)

**Предусловия**

Открыть https://practice-automation.com/form-fields/

**Шаги**

1. Ввести имя пользователя "**_Ivan Ivanov_**" в поле Name
2. Ввести пароль "**_Password13_**" в поле Password
3. Выбрать варианты "**_Milk_**" и "**_Coffee_**" в списке "What is your favorite drink?"
4. Выбрать цвет "**_Yellow_**" в списке "What is your favorite color?"
5. Выбрать любой из вариантов в выпадающем списке "Do you like automation?"
6. Ввести почту "**_ivanmail.com_**" в поле Email
7. Написать "**_5, Katalon Studio_**" в поле Message
8. Нажать на кнопку Submit

**Ожидаемый результат**

Возникает ошибка проверки формы или форма не отправляется.

---

### TC03 - No Email (Positive)

**Предусловия**

Открыть https://practice-automation.com/form-fields/

**Шаги**

1. Ввести имя пользователя "**_Ivan Ivanov_**" в поле Name
2. Ввести пароль "**_Password13_**" в поле Password
3. Выбрать варианты "**_Milk_**" и "**_Coffee_**" в списке "What is your favorite drink?"
4. Выбрать цвет "**_Yellow_**" в списке "What is your favorite color?"
5. Выбрать любой из вариантов в выпадающем списке "Do you like automation?"
6. Оставить поле Email пустым
7. Написать "**_5, Katalon Studio_**" в поле Message
8. Нажать на кнопку Submit

**Ожидаемый результат**

Поле email остаётся пустым, форма отправляется.
Появляется всплывающий Alert с сообщением:
`Message received!`

---

### TC04 - No Name (Negative)

**Предусловия**

Открыть https://practice-automation.com/form-fields/

**Шаги**

1. Оставить поле Name пустым
2. Ввести пароль "**_Password13_**" в поле Password
3. Выбрать варианты "**_Milk_**" и "**_Coffee_**" в списке "What is your favorite drink?"
4. Выбрать цвет "**_Yellow_**" в списке "What is your favorite color?"
5. Выбрать любой из вариантов в выпадающем списке "Do you like automation?"
6. Ввести почту "**_ivan@exmail.com_**" в поле Email
7. Написать "**_5, Katalon Studio_**" в поле Message
8. Нажать на кнопку Submit

**Ожидаемый результат**

Форма не отправляется, страница возвращается к полю Name.

---

### TC05 - Invalid Name (Negative)

**Предусловия**

Открыть https://practice-automation.com/form-fields/

**Шаги**

1. Ввести "**_234_**" в поле Name
2. Ввести пароль "**_Password13_**" в поле Password
3. Выбрать варианты "**_Milk_**" и "**_Coffee_**" в списке "What is your favorite drink?"
4. Выбрать цвет "**_Yellow_**" в списке "What is your favorite color?"
5. Выбрать любой из вариантов в выпадающем списке "Do you like automation?"
6. Ввести почту "**_ivan@exmail.com_**" в поле Email
7. Написать "**_5, Katalon Studio_**" в поле Message
8. Нажать на кнопку Submit

**Ожидаемый результат**

Форма не отправляется, страница возвращается к полю Name.
Возникает подсказка пользователю, что необходимо ввести корректное имя.

---


## Allure Report

Сформированный отчет в Allure

![Allure Report](screenshots/Allure%20report.png)
