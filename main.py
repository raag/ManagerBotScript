#!/usr/bin/python

from time import sleep
from datetime import date, datetime
import random
from enum import Enum

# Add here your favorite PM phrases
MANAGER_PRHASES = [
    "Any update?"
    "Coul you finish it by the end of the day?",
    "Let’s try thinking outside the box",
    "Why don’t we circle back on this?",
]

END_OF_THE_DAY_HOUR = 18
pizza_ordered = False


def main():
    print("Hello I'm your manager bot...")
    while True:
        annoy_developer()
        check_tasks()
        wait_15_minutes()


def annoy_developer():
    phrase = random.choice(MANAGER_PRHASES)
    print(phrase)


def check_tasks():
    tasks = get_list_of_tasks()
    for task in tasks:
        if task.status != TASK_STATUS.CLOSED:
            developer_estimation = ask_developer_for_estimation(task)
            real_estimation = register_developer_estimation_for_task(task, developer_estimation)

            current_hour = datetime.now().hour
            if current_hour + (real_estimation / 60) > END_OF_THE_DAY_HOUR:
                order_pizza()


def get_list_of_tasks():
    # TODO: Implement API call to get tasks
    # from your favorite software, for example Jira
    return []


def ask_developer_for_estimation(task):
    estimation_in_minutes = 0
    while estimation_in_minutes == 0:
        developer_estimation = input("How much longer do you estimate task %s will take? (in minutes) " % task.id)
        try:
            estimation_in_minutes = int(developer_estimation)
        except ValueError:
            print("I'm not jocking, give me a number")
    return estimation_in_minutes


def register_developer_estimation_for_task(task, developer_estimation):
    real_estimation = developer_estimation / 5.0
    ## TODO: call software API to register real estimation
    return real_estimation


def order_pizza():
    if not pizza_ordered:
        # TODO: call your favorite pizza store API
        pizza_ordered = True


def wait_15_minutes():
    sleep(15 * 60)



class TASK_STATUS(Enum):
    OPEN = "open"
    IN_PROGRESS = "in progress"
    CLOSED = "closed"


if __name__ == "__main__":
    main()
