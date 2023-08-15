from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User, Comment, CustomField

import config
from sos_mld import data

client = Zenpy(**config.ZENDESK_CREDENTIALS)  # type: ignore


def create_ticket(user: dict, res: dict):
    requester_id = requester(user['name'], user['email']).id
    custom_priority = p_priority(res['priority'])
    ticket = client.tickets.create(
        Ticket(subject=res['title'],
               requester_id=requester_id,
               submitter_id=requester_id,
               assignee=User(id=data.assignee()),
               comment=Comment(body=res['description'],
                               author_id=requester_id,
                               public=True),
               custom_fields=[CustomField(id=360056298473,
                                          value=custom_priority)],
               priority=res['priority'],
               tags=['porto']))
    return ticket.ticket.id


def requester(name: str, email: str) -> User:
    user = client.users.search(query=email)
    try:
        return next(user)
    except StopIteration:
        return client.users.create(
            User(name=name,
                 email=email,
                 organization_id=config.ORGANIZATIONS['porto']))


def p_priority(value: str):
    match value:
        case 'urgent':
            return 'p1_-_parada_crítica'
        case 'high':
            return 'p2_-_parada_intermitente'
        case 'normal':
            return 'p3_-_duvida_solicitacao'
