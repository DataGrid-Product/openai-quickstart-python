def generate_prio(message):
    return """  Estimate the priotization of the request ranging from 4 to 1000 where higher numbers are more important. Inform that decision based on how complex it seems to be (high efford) with lower values vs easier task with high values and how important they are where critical tickets get high valuesa and one off request low values.

message: What is the revenue before return?
response: 720

message: I need a topline chart.
response: 324

message: What operations KPIs do we have?
response: 532

message: Do we have dashboard regarding product roadmap?
response: 398

message: I want to connect salesforce to our bi tool.
response: 474

message: How do I setup another department?
response: 600

message: The definition of shipments before return is off.
response: 935

message: I'd like to use looker.
response: 91

message: Who need to know about the new database deployment?
response: 211

message: {}
response:""".format(
        message.capitalize()
    )