from flask import Flask, request, Response
import math


app = Flask(__name__)


@app.route('/alkuluku/<numero>')
def primecheck(numero):
    number = int(numero)
    if number == 1 or number == 4:
        return f"{numero} ei ole alkuluku."
    elif number == 2 or number == 3:
        return f"{numero} on alkuluku."
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i) == 0:
                return f"{numero} ei ole alkuluku."
            else:
                return f"{numero} on alkuluku."



if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
,