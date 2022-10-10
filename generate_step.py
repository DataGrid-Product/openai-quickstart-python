def generate_step(message):
    return """  Translate the message into one step from the framework. Must return from the framework.
                Framework steps: domain, integration, dwh, schema, table, column, model, bi tool, folder, report, metric, group, permission, user, source.

message: What is the revenue before return?
response: metric

message: I need a topline chart.
response: report

message: What operations KPIs do we have?
response: metric

message: Do we have dashboard regarding product roadmap?
response: report

message: I want to connect salesforce to our bi tool.
response: source

message: How do I setup another department?
response: domain

message: I want to create a new environment in our data warehouse for our team.
response: schema

message: The definition of shipments before return is off.
response: model

message: I'd like to use looker.
response: bi tool

message: Who need to know about the new redshift deployment?
response: dwh

message: I'd like to add a user to our environment
response: user

message: {}
response:""".format(
        message.capitalize()
    )