# notes_service
Rest сервис для управления заметками

Использует basic authentication для авторизации пользователей (имеются ввиду сервисные пользователи, созданные для интеграции с сервисом), пользователи создаются из админик (/admin)

Пользователю доступны заметки и операции над ними, только если он является их владельцем(создателем)

Формат принимаемых и возвращаемых данных: JSON

Поля заметки:
* id: идентификатор
* title: заголовок
* text: текст заметки
* outer_user_id: идентификатор пользователя во внешней(вызывающей) системе

## API:

**Получение списка заметок**

GET: /api/notes/
    
    Пример ответа        
    [{"id":2,"title":"test_tile","text":"test_text","outer_user_id":3}]


**Получение списка заметок по идентфикатору пользователя внешней системы**

GET /api/notes/?outer_user_id={outer_user_id}
    
    Пример ответа        
    [{"id":2,"title":"test_tile","text":"test_text","outer_user_id":3}]


**Получение одной заметки по идентификатору**

GET: /api/notes/{id}

    Пример ответа        
    {"id":2,"title":"test_tile","text":"test_text","outer_user_id":3}


**Создание заметки**

POST: /api/notes

    Пример параметров запроса
    Media type: application/json
    Body: {"title":"test_tile","text":"test_text","outer_user_id":3}


**Редактирование заметки с идентификатором id**

PUT: /api/notes/{id}

    Пример параметров запроса
    Media type: application/json
    Body: {"title":"test_tile_change","text":"test_text_change","outer_user_id":3}


**Удаление заметки с идентификатором id**

DELETE: /api/notes/{id}