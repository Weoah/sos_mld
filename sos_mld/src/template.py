IMAGE = 'https://ca.slack-edge.com/T01K83NGFCM-U033T5U137G-643476167a6d-512'


APP_HOME = {
    "type": "home",
    "callback_id": "home",
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Seja bem-vindo ao nosso bot de atendimento! "
                    ":heart:\n\n"
                    "Aqui, você tem a praticidade de *abrir um ticket* ou "
                    "*solicitar uma proposta de negócio* "
                    "de maneira ágil e descomplicada.\n"
                    "Basta nos informar suas necessidades, "
                    "e nós cuidaremos de todo o processo.")
            },
            "accessory": {
                "type": "image",
                "image_url": IMAGE,
                "alt_text": "SOS Mundo Livre. Digital"
            }
        },
        {
            "type": "actions",
            "block_id": "buttons",
            "elements": [
                {
                    "type": "button",
                    "action_id": "button-ticket",
                    "text": {
                        "type": "plain_text",
                        "text": "Abra um ticket!"
                    }
                },
                {
                    "type": "button",
                    "action_id": "button-deal",
                    "text": {
                        "type": "plain_text",
                        "text": "Solicite uma proposta!"
                    }
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Mundo Livre. Digital"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ("Acesse nosso site! "
                         "<https://mundolivre.digital/|Mundo Livre. Digital>")
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ("Veja as "
                         "<https://mundolivre.digital/|Perguntas Frequentes>")
            }
        }
    ]
}

TICKET_MODAL = {
    "type": "modal",
    "callback_id": "ticket-modal",
    "title": {
        "type": "plain_text",
        "text": "Novo ticket"
    },
    "submit": {
        "type": "plain_text",
        "text": "Enviar"
    },
    "close": {
        "type": "plain_text",
        "text": "Cancelar"
    },
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ("*Nossa equipe de suporte está pronta "
                         "para ajudar!*\n\n"
                         "Para abrir um ticket, "
                         "basta preencher os campos abaixo e *enviar* :)")
            },
            "accessory": {
                "type": "image",
                "image_url": IMAGE,
                "alt_text": "SOS Mundo Livre. Digital"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "input",
            "block_id": "title",
            "element": {
                "type": "plain_text_input"
            },
            "label": {
                "type": "plain_text",
                "text": "Título"
            }
        },
        {
            "type": "input",
            "block_id": "priority",
            "label": {
                "type": "plain_text",
                "text": "Prioridade"
            },
            "element": {
                "type": "static_select",
                "action_id": "priority_action",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "P1 - Crítica de negócios"
                        },
                        "value": "urgent"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "P2 - Serviço degradado"
                        },
                        "value": "high"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "P3 - Dúvidas gerais"
                        },
                        "value": "normal"
                    }
                ]
            }
        },
        {
            "type": "input",
            "block_id": "description",
            "element": {
                "type": "plain_text_input",
                "multiline": True
            },
            "label": {
                "type": "plain_text",
                "text": "Descrição"
            }
        }
    ]
}

DEAL_MODAL = {
    "type": "modal",
    "callback_id": "deal-modal",
    "title": {
        "type": "plain_text",
        "text": "Nova proposta"
    },
    "submit": {
        "type": "plain_text",
        "text": "Enviar"
    },
    "close": {
        "type": "plain_text",
        "text": "Cancelar"
    },
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Nossa equipe de negócios cuidará da análise "
                    "da sua proposta com atenção!*\n\n"
                    "Para solicitar uma proposta, "
                    "basta preencher os campos abaixo e *enviar* :)")
            },
            "accessory": {
                "type": "image",
                "image_url": IMAGE,
                "alt_text": "SOS Mundo Livre. Digital"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Informações"
            }
        },
        {
            "type": "input",
            "block_id": "title",
            "element": {
                "type": "plain_text_input"
            },
            "label": {
                "type": "plain_text",
                "text": "Título"
            }
        },
        {
            "type": "input",
            "block_id": "description",
            "element": {
                "type": "plain_text_input",
                "multiline": True
            },
            "label": {
                "type": "plain_text",
                "text": "Descrição"
            }
        }
    ]
}


def priority(priority):
    match priority:
        case 'urgent':
            return 'P1 - Crítica de negócios'
        case 'high':
            return 'P2 - Serviço degradado'
        case 'normal':
            return 'P3 - Dúvidas gerais'


def TICKET_BLOCK(user, ticket):
    first_name = user['name'].split(' ')[0]
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"O ticket {ticket} foi criado, {first_name}!\n"
                    "Já recebemos e estamos dando seguimento.\n"
                    "Você pode acompanhar e interagir pelo "
                    f"email {user['email']}."
                )
            }
        }
    ]


def TICKET_ATTACHMENTS(values):
    return [
        {
            "color": "#23ff55",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": (
                            f"Título: {values['title']}\n"
                            f"Prioridade: {priority(values['priority'])}\n"
                            f"Descrição: {values['description']}"),
                        "emoji": True
                    }
                }
            ]
        }
    ]


def DEAL_BLOCK(deal, user):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Ficamos felizes em receber a sua nova sugestão: "
                    f"{deal['title']}\nAgradecemos, {user['name']}!"
                )
            }
        }
    ]


def DEAL_ATTACHMENTS(values):
    return [
        {
            "color": "#4169e1",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": (
                            f"Título: {values['title']}\n"
                            f"Descrição: {values['description']}"),
                        "emoji": True
                    }
                }
            ]
        }
    ]
