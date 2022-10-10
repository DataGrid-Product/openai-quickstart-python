import os

#import libraries
import openai
from flask import Flask, redirect, render_template, request, url_for
from jira import JIRA

#import modules
from generate_action import generate_action
from generate_step import generate_step
from generate_size import generate_size
from generate_domain import generate_domain
from generate_tool import generate_tool
from generate_de import generate_de
from generate_prio import generate_prio


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        message = request.form["message"]
        return redirect(url_for("review_lables",message=message))
    else:
        return render_template("index.html")



@app.route("/review_lables/<message>", methods=("GET", "POST"))
def review_lables(message):
    if request.method == "POST":
        return redirect(url_for("generate_issue"))
    else:
        action_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_action(message),
            temperature=0.5,
            max_tokens=5
        )
        step_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_step(message),
            temperature=0.5,
            max_tokens=5
        )
        size_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_size(message),
            temperature=0.5,
            max_tokens=5
        )
        tool_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_tool(message),
            temperature=0.5,
            max_tokens=20
        )
        domain_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_domain(message),
            temperature=0.5,
            max_tokens=10
        )
        de_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_de(message),
            temperature=0.5,
            max_tokens=100
        )
        prio_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_prio(message),
            temperature=0.5,
            max_tokens=100
        )
        return render_template("jira.html", message=message,
                                            action_result=action_response.choices[0].text, 
                                            step_result=step_response.choices[0].text, 
                                            size_result=size_response.choices[0].text, 
                                            tool_result=tool_response.choices[0].text, 
                                            domain_result=domain_response.choices[0].text, 
                                            de_result=de_response.choices[0].text, 
                                            prio_result=prio_response.choices[0].text)


@app.route("/generate_issue", methods=("GET", "POST"))
def generate_issue():
        return render_template("success.html")
jira_connection = JIRA(
    basic_auth=('jacob@data-grid.net', 'hT7JIhfXkyE4iwLnZXAh96E6'),
    server="https://data-grid.atlassian.net"
)

issue_dict = {
    'project': {'key': 'JOB'},
    'summary': 'new1',
    'description': 'Detailed ticket description.',
    'issuetype': {'id': '10001'},
    "customfield_10035":    {"self":"https://data-grid.atlassian.net/rest/api/2/customFieldOption/10023",
                            "value":"Strategic Development",
                            "id":"10023"},
    'customfield_10036': 60.0,
    "customfield_10037":    [{"self":"https://data-grid.atlassian.net/rest/api/2/customFieldOption/10032",
                            "value":"Superset",
                            "id":"10032"}],
    'customfield_10041':    {"self":"https://data-grid.atlassian.net/rest/api/2/customFieldOption/10042",
                            "value":"Weekly",
                            "id":"10042"}
}
new_issue = jira_connection.create_issue(fields=issue_dict)
        


