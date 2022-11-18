
from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<Number>')


def alkuluku(Number):
        Number = float(Number)
        isPrime = luku_alku(Number)

        vastaus = {
            "Number": Number,
            "isPrime": isPrime
        }
        return vastaus

def luku_alku(tulos):
    if tulos > 1:
        for i in range(2, int(tulos / 2) + 1):
            if (tulos % i) == 0:
                return "false"
        else:
            return "true"

    
    else:
        return "false"



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)