from slack_sdk.errors import SlackApiError

import config
from sos_mld.src import template


def ticket(body, client, logger):
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=template.TICKET_MODAL)
    except SlackApiError as err:
        logger.error(f"Error on opening modal: {err}")


def deal(body, client, logger):
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=template.DEAL_MODAL)
    except SlackApiError as err:
        logger.error(f"Error on opening modal: {err}")


def ticket_send(client, logger, res, user, ticket):
    try:
        client.chat_postMessage(
            channel=channel(user['domain']),
            text='Novo Ticket!',
            blocks=template.TICKET_BLOCK(user, ticket),
            attachments=template.TICKET_ATTACHMENTS(res))
    except SlackApiError as err:
        logger.error(f"Error on opening modal: {err}")


def deal_send(client, logger, res, user):
    try:
        client.chat_postMessage(
            channel=channel(user['domain']),
            text='Nova Melhoria!',
            blocks=template.DEAL_BLOCK(res, user),
            attachments=template.DEAL_ATTACHMENTS(res))
    except SlackApiError as err:
        logger.error(f"Error on opening modal: {err}")


def notificate_deal(client, logger, res, user):
    try:
        for _, channel in config.SLACK_NOTIFICATE_DEAL:
            client.chat_postMessage(
                channel=channel,
                text='Nova Melhoria!',
                blocks=template.DEAL_BLOCK(res, user),
                attachments=template.DEAL_ATTACHMENTS(res))
    except SlackApiError as err:
        logger.error(f"Error on opening modal: {err}")


def channel(domain):
    if domain in config.ORGANIZATIONS_CHANNELS.keys():
        return config.ORGANIZATIONS_CHANNELS[domain]
    return config.SLACK_DEBUG_CHANNEL
