from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/fast-search/')
def fast_search():
    search_result = {
        "prénom": "Melon",
        "nom": "Husk",
        "email": "melon.husk@gamil.com",
        "addresse": "11 rue des petits pois, 12345 Paradis",
        "tel": "+33 123456578"
    }
    return jsonify({
        "type": "success",
        "search_result": search_result
    }), 200

@app.route('/api/advanced-search/')
def advanced_search():
    search_result = {
        "prénom": "Melon",
        "nom": "Husk",
        "email": "melon.husk@gamil.com",
        "addresse": "11 rue des petits pois, 12345 Paradis",
        "tel": "+33 123456578",
        "company": "Twitter, 'the' cage aux fauves humaine"
    }
    return jsonify({
        "type": "success",
        "search_result": search_result
    }), 200

# Exemple d'autre route
@app.route('/api/sample')
def hello():
    return jsonify({"message": "Sample!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

