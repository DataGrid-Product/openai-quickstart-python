def generate_tool(message):
    return """  Translate the message into one or more tools.
                Tools: Lightdash, Postgres, MySQL, Fivetran, Airflow, Airbyte, Superset.

message: What is the revenue before return?
response: Lightdash, Superset

message: I need a topline chart.
response: Superset

message: What operations KPIs do we have?
response: Superset, Lightdash

message: Do we have dashboard regarding product roadmap?
response: report

message: I want to connect salesforce to our bi tool.
response: Lightdash, Fivetran, Airflow, Arbyte

message: How do I setup another department?
response: Postgres, MySQL, Superset

message: The definition of shipments before return is off.
response: Fivetran, Airbyte

message: I'd like to use looker.
response: Looker

message: Who need to know about the data warehouse deployment?
response: Postgres, MySQL

message: {}
response:""".format(
        message.capitalize()
    )