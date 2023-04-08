from flask import Flask, render_template, request
import time
import enchant

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    c_time = time.ctime()
    return render_template('index.html', current_time=c_time, time=time)


@app.route('/results', methods=['POST'])
def results():
    d = enchant.Dict("en_US")
    start_time = float(request.form['start_time'])
    end_time = time.time()
    time_elapsed = end_time - start_time
    user_input = request.form['text']
    words = user_input.split()
    num_words = len(words)
    num_correct_words = 0
    num_incorrect_words = 0
    for word in words:
        if d.check(word):
            num_correct_words += 1
        else:
            num_incorrect_words += 1
    speed = num_correct_words / (time_elapsed / 60)
    return render_template('results.html', speed=speed, num_words=num_words,
                           num_correct_words=num_correct_words, num_incorrect_words=num_incorrect_words)


if __name__ == '__main__':
    app.run(debug=True, port=5025)
