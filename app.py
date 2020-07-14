from database import db_session, init_db
from schema import schema

from flask import Flask
from flask_graphql import GraphQLView


app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()
# if __name__ == "__main__":
    # init_db()
    # app.run()
