from slack_bolt import App
from slack_sdk.errors import SlackApiError

import config
from sos_mld import data, zendesk, hubspot
from sos_mld.src import debug, template, views


app = App(token=config.SLACK_BOT_TOKEN,
          signing_secret=config.SLACK_SIGNING_SECRET)


@app.event("app_home_opened")
def home_tab(client, event, body, logger):
    try:
        client.views_publish(user_id=event["user"], view=template.APP_HOME)
        debug.menu(body, client)
    except SlackApiError as err:
        logger.error(f"Error publishing home tab: {err}")


@app.command("/sos")
def handle_ticket_command(body, ack, client, logger):
    ack()
    debug.trying(body, client, 'Ticket')
    views.ticket(body, client, logger)


@app.command("/melhoria")
def handle_deal_command(body, ack, client, logger):
    ack()
    debug.trying(body, client, 'Proposta')
    views.deal(body, client, logger)


@app.action("button-ticket")
def handle_button_ticket(body, ack, client, logger):
    ack()
    debug.button(body, client, 'Ticket')
    views.ticket(body, client, logger)


@app.action("button-deal")
def handle_button_deal(body, ack, client, logger):
    ack()
    debug.button(body, client, 'Proposta')
    views.deal(body, client, logger)


@app.view("ticket-modal")
def view_submission_ticket(ack, body, client, logger):
    ack()
    user = data.user(body['team'], body['user'], client)
    res = data.ticket(body["view"]["state"]["values"])
    debug.done(user, res, client, 'Ticket')
    ticket = zendesk.create_ticket(user, res)
    views.ticket_send(client, logger, res, user, ticket)


@app.view("deal-modal")
def view_submission_deal(ack, body, client, logger):
    ack()
    user = data.user(body['team'], body['user'], client)
    res = data.deal(body["view"]["state"]["values"])
    debug.done(user, res, client, 'Proposta')
    properties = hubspot.set_properties(res, data.user_text(user))
    hubspot.create_new_deal(properties)
    views.deal_send(client, logger, res, user)
    # views.notificate_deal(client, logger, res, user)


@app.action("priority_action")
def handle_priority(ack):
    ack()


@app.action("type_action")
def handle_type(ack):
    ack()


if __name__ == '__main__':
    app.start(port=3000)
