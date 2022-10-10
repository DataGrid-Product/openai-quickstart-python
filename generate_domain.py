def generate_domain(message):
    return """  Translate the request into one department.
                sales: selling products and calling people
                marketing: communicating to customers through advertising channels
                hr: hiring people into the company
                tech: building and coding the product
                finance: calculating company financials and keeping track of earnings and spending
                operations: organizing the company processes to keep everyone in line with the companies objectives

message: What is the revenue before return?
response: sales

message: I need a topline chart.
response: finance

message: What operations KPIs do we have?
response: operations

message: Do we have dashboard regarding product roadmap?
response: tech

message: I want to connect salesforce to our bi tool.
response: sales

message: How do I setup another department?
response: any

message: The definition of shipments before return is off.
response: sales

message: I'd like to use looker.
response: any

message: Who need to know about the data warehouse deployment?
response: any

message: I wan't to know how efficient our campaigns run
response: marketing

message: How often do we need to hire new sales agents?
response: hr

message: I'd like to get numbers to inform our PnL.
response: finance

message: {}
response:""".format(
        message.capitalize()
    )