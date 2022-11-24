from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import re
import gevent.monkey
from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

from give_answer import answer_question
import unicodedata
import wolframalpha
import wikipedia


def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)


    app.config['SECRET_KEY']= '78qw76eqw78egdsyudgs7a8dtewdgsuctwe67cwdcfw67wtydfw6cwecwecgcgc6deg'


    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            try:
                question = request.form['question']
            except KeyError as e:
                print('key error')
                print(f'Exception has occured as {e}')
            except:
                print('I got another exception, but I should re-raise')
                raise


            print(question)
            answer = answer_question(question)
            print(f'answer: {answer}')
            answer=re.sub('([(].*?[)])',"",answer)

            return render_template('answer.html', answer=answer, question=question)

        return render_template('index.html')



    return app

# create main callable
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # http_server = WSGIServer(('127.0.0.1', 9191), app)
    # print("starting server on port 9191")
    # http_server.serve_forever()
    
