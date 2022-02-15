# Racks
**Racks** – это прототип системы учета используемого пространства для телекоммуникационных шкафов и стоек.  

| ![racks-3](https://user-images.githubusercontent.com/96002587/153874276-4bb91100-915f-484f-8163-2a1c2a1c12c2.png) |
|:--:| 
| *Карта стоек* |

| ![units-3](https://user-images.githubusercontent.com/96002587/153874295-4ed3773e-517a-4f04-bf9b-c542eba34729.png) |
|:--:| 
| *Схема стойки* |

**Стек:**
- Python 3.6.9
- Django 2.2.2
- Gunicorn 19.9.0
- PostgreSQL 10.18

# Функционал
Прототип системы представляет из себя набор форм для внесения данных, разбавленный некоторым кол-вом костылей для их корректного отображения в виде схем стоек. Пользовательский интерфейс выполнен с учетом минимальных требований функциональности. На главной странице формируется дерево стоек, отображающее их территориальное расположение. Там же можно добавить необходимые объекты для добавления стойки. После создания стойки в нее можно добавить устройства, либо обозначить юниты как зарезервированные или недоступные для использования. Предусмотрены несколько стилей отображения занятых юнитов. Устройства, находящиеся в зоне ответственности организации или общей структуры над отделами окрашиваются в зеленый цвет, вне этой зоны – в красный (к примеру, оборудование операторов связи у которых организация арендует канал). Устройства (или юниты) имеющие статус отличный от “Оборудование в работе”, отмечаются штрихованной линией. Если устройство резервируется, можно указать порядковый номер резерва при заполнении формы в соответствующем поле, который будет отображаться в карточке устройства как ссылка. Для упрощения рутинной работы персонала на местах предусмотрены шаблоны для печати обеих сторон стойки. В такой шаблон можно внести основные данные, как в черновик на месте описи стойки и в последующем перенести в систему. Так же предусмотрена выгрузка сводных отчетов включающих все стойки и всё оборудование, внесенное в систему. В обоих отчетах есть поле со ссылкой на карточку устройства или стойки.  
### QR-коды
Для удобстава инвентаризации предусмотрена генерация QR-кодов (по требованию, пути не хранятся в БД). Можно распечатать сразу все коды для стойки и установленных в ней устройств. 

| ![device-3](https://user-images.githubusercontent.com/96002587/153874252-2c299c8d-67b2-47d2-9969-b542e1a74af4.png) |
|:--:| 
| *Карточка устройства* |

# Особенности
Большинство существующих решений с похожим функционалом имеют стандартные опции в рамках разделения прав пользователей и рассчитаны на то, что все данные будут вноситься, удаляться и изменяться администраторами. Это не позволяет безопасно использовать подобные системы, если технические специалисты на местах (территориально) не обладают достаточной квалификацией и могут удалить данные вне зоны своей ответственности. Данная проблема решена максимально примитивно, за счет простой схемы БД и проверки первичных ключей для каждого изменяемого объекта. Таким образом, реализовано некоторое подобие механизма горизонтальных прав «в инвалидном кресле», которое позволяет запрещать или разрешать изменения для объектов в рамках одной и той же модели. Для того чтобы пользователь мог работать только в пределах зоны ответственности своего отдела, необходимо создать группу с названием отдела и добавить его в эту группу. * *Примечание: при создании пользователя обязательно указывать First name и Last name в Personal info.* * Для надежности предусмотрено логирование и добавлен простой скрипт `pg_backup.sh` для бэкапов БД.

# Selenium тесты
Функциональные тесты написаны под уже существующий сетап. Для проверки соответсвия сетапа предусмотрены предварительные тесты 1_1 - 1_7. В сетап входит тестовый пользователь `selenium` с правами на изменение объектов в зоне ответственности одного из отделов.

