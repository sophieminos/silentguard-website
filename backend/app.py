from flask import Flask, jsonify, request
from search_somebody_like import search_somebody_like

app = Flask(__name__)

@app.route('/api/search/')
def fast_search():
    result = {}
    first_name = request.args.get('first_name');
    last_name = request.args.get('last_name');
    pseudo = request.args.get('pseudo');
    email = request.args.get('email');
    result = search_somebody_like(first_name, last_name, pseudo, email)
    
    if result:
        search_result = result
 
    return jsonify({
        "type": "success",
        "search_result": search_result
    }), 200

if __name__ == '__main__':
    app.run(debug=True)

