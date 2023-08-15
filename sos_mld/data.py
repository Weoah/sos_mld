import random
from datetime import datetime

import config


def user(team, user, client) -> dict:
    if isinstance(user, str):
        user = client.users_info(user=user)
    else:
        user = client.users_info(user=user['id'])

    try:
        name = user['user']['real_name']
    except KeyError:
        name = user['user']['profile']['real_name']

    if team is not None and not isinstance(team, str):
        team = team['domain']

    return {
        "name": name,
        "email": user['user']['profile']['email'],
        "domain": team
    }


def ticket(values: dict) -> dict:
    response = {
        "title": get_text(values["title"]),
        "priority": get_selection(values['priority']),
        "description": get_text(values["description"])}
    return response


def deal(values: dict) -> dict:
    response = {
        "title": get_text(values['title']),
        "description": get_text(values['description'])}
    return response


def get_text(_dict: dict) -> str:
    value = tuple(_dict.values())[0]
    return value['value']


def get_selection(_dict: dict) -> str:
    action = tuple(_dict.values())[0]
    return action['selected_option']['value']


def assignee():
    time = datetime.now().hour
    if time in range(6, 11):
        return config.TICKET_ASSIGNEE_BY_HOUR['6_11']
    elif time in range(11, 18):
        return config.TICKET_ASSIGNEE_BY_HOUR['11_18']
    elif time in range(18, 22):
        return config.TICKET_ASSIGNEE_BY_HOUR['18_22']
    elif time in range(22, 24) or time in range(0, 6):
        return random.choice(config.TICKET_ASSIGNEE_BY_HOUR['22_6'])


def user_text(values: dict):
    return f"Nome: {values['name']}\nEmail: {values['email']}"
