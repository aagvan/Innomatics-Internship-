from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def regular_expression():
    if request.method == 'POST':
        regex = request.form['in_1']
        string = request.form['in_2']

        match = re.findall(regex, string)
        count = len(match)

        return render_template('search.html', string=string, regex=regex, match=match, count=count)
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)