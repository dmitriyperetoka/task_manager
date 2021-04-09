# task_manager
Проект развёрнут на сервере http://84.201.176.23
 
### Примеры запросов:
| Путь  | Метод | Данные | Описание |
| ------- | --------- | ---------| --------- |
| http://84.201.176.23/api/v1/signup/ | POST | username, full_name, password |  Зарегистрировать нового пользователя |
| http://84.201.176.23/api/v1/token | POST | username, password |  Получить JWT-токен |
| http://84.201.176.23/api/v1/tasks | GET |  |  Получить список всех задач |
| http://84.201.176.23/api/v1/tasks/ | POST | performers (id) (many), title, description, deadline (YYYY-MM-DD), attachment* |  Создать новую задачу |
| http://84.201.176.23/api/v1/tasks/{id}/ | PUT | performers (id) (many), title, description, deadline (YYYY-MM-DD), attachment* |  Обновить задачу |
| http://84.201.176.23/api/v1/tasks/{id}/ | PATCH | Поля, которые нужно обновить |  Частично обновить задачу |
| http://84.201.176.23/api/v1/tasks/{id}/ | DELETE |  |  Удалить задачу |

\* необязательное поле
