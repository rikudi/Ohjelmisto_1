from flask import Flask, jsonify

app = Flask(__name__)

def is_prime_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:n>', methods=['GET'])
def alkuluku(n):
    return jsonify({"Number": n, "isPrime": is_prime_number(n)})

if __name__ == '__main__':
    app.run(port=3000)
