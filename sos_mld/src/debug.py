import config
from sos_mld import data


def debug(func):
    def wrapper(*args, **kwargs):
        if config.DEBUG:
            handler = func(*args, **kwargs)
            return handler
    return wrapper


@debug
def menu(body, client):
    user = data.user(None, body['event']['user'], client)
    client.chat_postMessage(
        text=f"O Usuário {user['name']} ({user['email']}) está no menu!",
        channel=config.SLACK_DEBUG_CHANNEL)


@debug
def trying(body, client, act):
    user = data.user(body['team_domain'], body['user_id'], client)
    client.chat_postMessage(
        text=f"O Usuário {user['name']} ({user['email']}) está abrindo {act}!",
        channel=config.SLACK_DEBUG_CHANNEL)


@debug
def button(body, client, act):
    user = data.user(body['team'], body['user']['id'], client)
    client.chat_postMessage(
        text=f"O Usuário {user['name']} ({user['email']}) está abrindo {act}!",
        channel=config.SLACK_DEBUG_CHANNEL)


@debug
def done(user, res, client, act):
    client.chat_postMessage(
        text=(f"O Usuário {user['name']} ({user['email']}) "
              f"abriu {act}:\nTítulo: {res['title']}"),
        channel=config.SLACK_DEBUG_CHANNEL)
