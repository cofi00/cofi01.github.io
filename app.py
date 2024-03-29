from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


received_data = {}

@app.route('/api', methods=['POST'])
def process_data():
    global received_data
    # Pretpostavljamo da su podaci u JSON formatu
    data = request.json
    received_data.update(data)  
    return jsonify({"status": "Podaci primljeni"}), 200

@app.route('/view-data', methods=['GET'])
def view_data():
   
    return render_template('index.html', **received_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


