#Документация к программе
## Инструкция к установке

1. pip install -r requirements.txt в терминале, находясь в той же папке, где и файл requirements.txt
(переместиться в папку можно с помощью команды "cd тут/указать/путь/к/папке" (вернуться на уровень выше можно с помощью "cd .."))
2. Открыть в редакторе файл config.py и выставить всё в соответсвии с нуждой
3. Для добавления новых сессий, просто добавить их в ту же папку, где и скрипт
4. Чтобы все аккаунты вступили в каналы - запустить файл join_chanels.py
5. После успешного вступления, можно запустить файл main.py
6. Скрипт сообщит о поступлении нового поста, а так же о его успешном репосте
## Стак используемых технологий
__python 3.9__
__pip__
__pyrogram__
__asyncio__
__random__

# Отзыв о разработке
### Цели и задачи
#### Цель
Разработать такую программу которая могла бы одновременно пересылать n количество постов, с помощью n количества аккаунтов. Работать скрипт должен паралельно.
####Задачи
1. Понять как строится ассинхронное исполнение сразу нескольких экземпляров функции
2. Познакомиться с новой для себя технологией разработки юзерботов на библиотеке pyrogram
3. Разработать программу так, чтобы один  экземпляр функции мог обработать несколько задач, приходящих в n время
4. Программно реализовать визуально живую активность

### Вывод
#### Сроки выполнения
Задача была выполненна в поставленный срок, самым долгим процессом оказалось тестирование скрипта на не тестовых каналах.
#### Сложности во время выполнения
Сложностей во время выполнения возникло мало, самой трудной частью скрипта оказалось составление рандомного количества работающих аккаунтов. Самой же простой, но в то же время трудной задачей оказался механизм ассинхронных очередей.
