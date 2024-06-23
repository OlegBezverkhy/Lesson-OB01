import datetime as dt


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Не выполнено"

    def mark_task_completed(self):
        self.status = 'Выполнено'


START_DATE = dt.date(2024, 6, 20)

tasks_template = ('Написать письмо                          ',
                  'Согласовать письмо с начальником отдела  ',
                  'Подписать письмо у генерального директора',
                  'Отправить письмо контрагенту             ',
                  'Получить письмо с ответом от контрагента ')

tasks_list = []


def add_task(description, deadline, tasks_list_tmp):
    new_task = Task(description, deadline)
    tasks_list_tmp.append(new_task)
    return


def display_tasks(task_list_tmp, task_status_control=False):
    index = 1
    for task in task_list_tmp:
        if task.status == "Не выполнено" or not task_status_control:
            print(f'Индекс {index} '
                  f'Задача : {task.description} '
                  f'Cрок выполнения: {task.deadline} '
                  f'Статус : {task.status}')
        index += 1

    return


def main():
    # Создаем несколько объектов сдвиг дедлайнов - 2 дня:
    days_plus = 0
    for task in tasks_template:
        add_task(task, START_DATE+dt.timedelta(days=days_plus), tasks_list)
        days_plus += 2
    # Проверяем результат добавления объектов
    print(f'Старт проекта : {START_DATE}')
    print('Список задач :')
    display_tasks(tasks_list)
    # Изменение статуса задачи
    while True:
        try:
            task_index = int(input('Введите индекс задачи, для изменения ее '
                                   'статуса на "Выполнено" : '))
        except ValueError:
            print('Неправильный ввод')
            continue
        if task_index in range(1, len(tasks_list)+1):
            tasks_list[task_index-1].mark_task_completed()
            break
        else:
            print(f'Задачи с индексом {task_index} не существует')
    # Проверяем результат изменения статуса
    print(f'Изменение статуса задачи {task_index} :')
    print(f'Индекс {task_index} '
          f'Задача : {tasks_list[task_index-1].description} '
          f'Cрок выполнения: {tasks_list[task_index-1].deadline} '
          f'Статус : {tasks_list[task_index-1].status}')
    # Вывод списка неневыполенных задач:
    print('Список нерешенных задач :')
    display_tasks(tasks_list, True)


if __name__ == '__main__':
    main()
