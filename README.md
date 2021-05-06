# task_manager
Планировщик задач с возможностью назначить список исполнителей и крайний срок для каждой задачи. Для автора задачи доступно её редактирование и удаление. Взаимодействие с сервисом через API. Авторизация через JWT токен.

### Примеры запросов:
| Путь  | Метод | Данные | Описание |
| ------- | --------- | ---------| --------- |
| /api/v1/signup/ | POST | username, full_name, password |  Зарегистрировать нового пользователя |
| /api/v1/token | POST | username, password |  Получить пару JWT-токенов refresh и access |
| /api/v1/token/refresh/ | POST | refresh | Обновить access JWT-токен |
| /api/v1/tasks | GET |  |  Получить список всех задач |
| /api/v1/tasks/own | GET |  |  Получить список всех задач созданных пользователем, отправляющим запрос |
| /api/v1/tasks/ | POST | performers (id) (many), title, description, deadline (YYYY-MM-DD), attachment* |  Создать новую задачу |
| /api/v1/tasks/{id}/ | PUT | performers (id) (many), title, description, deadline (YYYY-MM-DD), attachment* |  Обновить задачу |
| /api/v1/tasks/{id}/ | PATCH | Поля, которые нужно обновить |  Частично обновить задачу |
| /api/v1/tasks/{id}/ | DELETE |  |  Удалить задачу |

\* необязательное поле
