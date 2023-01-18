from flask import Flask, request, render_template
from pip._vendor import requests

from data import db_session
from forms.sqlrequestsform import SQLRequestsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flag_is_here'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    msg = ''
    answer = []
    length = 0
    form = SQLRequestsForm()
    if request.method == 'POST':
        db_sess = db_session.create_session()
        req = form.request.data
        try:
            answer = []
            res = db_sess.execute(req).all()
            #answer = [[i for j in res] for i in j]
            for i in res:
                answer.append(list(i))
            if answer:
                length = len(answer[0])
            msg = "SQLAlchemy понял ваш запрос! Ура!"
        except:
            msg = "SQLAlchemy не понимает ваш запрос)"
            print('Не понял')
    return render_template("training.html", form=form, message=msg, answer=answer, length=length)



def main():
    db_session.global_init("db/trainsql.sqlite")
    # serve(app, host='0.0.0.0', port=8080)
    app.run(port=8080, host='127.0.0.1')


main()
