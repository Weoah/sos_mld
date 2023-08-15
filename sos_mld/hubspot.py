import hubspot
from hubspot.crm.deals import SimplePublicObjectInputForCreate, ApiException

import config as conf


client = hubspot.Client.create(access_token=conf.HUBSPOT_API_KEY)


def set_properties(values: dict, user: str) -> dict:
    properties = {
        "dealname": values['title'],
        "pipeline": "default",
        "dealstage": "appointmentscheduled",
        "description": f"{values['description']}\n\n{user}",
        "hubspot_owner_id": "48548904"}
    return properties


def create_new_deal(properties: dict) -> None:
    deal = SimplePublicObjectInputForCreate(
        properties=properties)
    try:
        client.crm.deals.basic_api.create(
            simple_public_object_input_for_create=deal)
    except ApiException as err:
        print("Exception when calling basic_api->create: %s\n" % err)
