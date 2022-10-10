def generate_de(message):
    return """  Describe the message in a ticket format for jira.
                Involve an acceptance criteria and rephrase the ticket in a descriptive manner.

message: {}
response:""".format(
        message.capitalize()
    )
