### Онлайн каталог сотрудников для компании с более чем 50,000 сотрудников.

---

*Запуск сервера из корневой папки: python.exe .\manage.py runserver  
Тестовый аккаунт  
логин: root  
пароль: 12332113*
### Часть N1 (обязательная)  

Создана веб страница, которая выводит иерархию сотрудников в древовидной форме  

Информация о каждом сотруднике хранится в базе данных и содержит следующие данные:  
- ФИО;  
- Должность;  
- Дата приема на работу;  
- Размер заработной платы;  
У каждого сотрудника есть 1 начальник;  
База данных содержит не менее 50 000 сотрудников и 5 уровней иерархий;  

### Часть N2 (опциональная)  

1. Создана база данных используя миграции Django;  
2. Использован DB seeder для Django ORM для заполнения базы данных;  
3. Использован Twitter Bootstrap для создания базовых стилей страниц;  
4. Создана еще одна страница и выведен на ней список сотрудников со всей имеющейся о сотруднике информацией;  
5. Добавлена возможность поиска сотрудников по имени, должности и начальнику для страницы созданной в задаче 4;  
6. Используя стандартные функции Django, осуществлена аутентификация пользователя для раздела веб сайта доступного только для зарегистрированных пользователей;  
7. В разделе доступном только для зарегистрированных пользователей, реализованы остальные CRUD операции для записей сотрудников. Все поля касающиеся пользователей редактируемы, включая начальника каждого сотрудника;  
8. Осуществлена возможность загружать фотографию сотрудника и отображать ее на странице, где можно редактировать  данные о сотруднике. Добавлена дополнительная колонка с уменьшенной фотографией сотрудника на странице списка всех сотрудников;  
9. Реализована ленивая загрузка для дерева сотрудников. Показаны первые два уровня иерархии по умолчанию и подгружаются 2 следующих уровня дерева при клике на сотрудника;
