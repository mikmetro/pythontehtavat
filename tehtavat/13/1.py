from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    n = 2
    isPrime = True
    while n < luku:
        if luku % n == 0:
            isPrime = False
            break
        n += 1

    return {
        "Number": luku,
        "isPrime": isPrime
    }

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=8532)
