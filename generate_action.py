def generate_action(message):
    return """  Translate the message into one action from the framework. Must return from the framework.
                Framework actions: request, create, instruct, investigate, update/fix, use, delete.

message: What is the revenue before return?
response: investigate

message: I need a topline chart.
response: create

message: What operations KPIs do we have?
response: investigate

message: Do we have dashboard regarding product roadmap?
response: investigate

message: I want to connect salesforce to our bi tool.
response: create

message: How do I setup another department?
response: request

message: The definition of shipments before return is off.
response: update/fix_model

message: I'd like to use looker.
response: request

message: Who need to know about the new redshift deployment?
response: instruct

message: {}
response: """.format(
        message.capitalize()
    )