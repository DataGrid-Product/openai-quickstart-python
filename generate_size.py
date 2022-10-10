def generate_size(message):
    return """  Estimate the size of the request if it is s (small), m (medium), l (large), xl (extra large).

message: What is the revenue before return?
response: s

message: I need a topline chart.
response: m

message: What operations KPIs do we have?
response: s

message: Do we have dashboard regarding product roadmap?
response: m

message: I want to connect salesforce to our bi tool.
response: l

message: How do I setup another department?
response: l

message: The definition of shipments before return is off.
response: s

message: I'd like to use looker.
response: xl

message: Who need to know about the new redshift deployment?
response: s

message: I need access to our bi tool?
response: s

message: {}
response:""".format(
        message.capitalize()
    )
