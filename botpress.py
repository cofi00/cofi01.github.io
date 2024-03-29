from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def process_data():
    # Pretpostavljamo da su podaci u JSON formatu
    data = request.json

    # Vraćamo HTML stranicu sa popunjenim podacima
    return render_template('index.html', ime=data['ime'], prezime=data['prezime'], email=data['email'], datum=data['datum'], broj=data['broj'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)

