from flask import Flask, jsonify, request, render_template
#flask looks for templates folder
app = Flask(__name__)

stores = [
    {
        'name': 'Albertsons Zombie Store',
        'items': [
            {
            'name': 'Real Blood',
            'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET store/string name
@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores, if store matches return it, or error if none
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'no matching store found'})

# GET /get_stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/string name / item{name:price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'no matching store found'})

# GET /store/string name / item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items'" store['items']"})
    return jsonify({'message': 'store not found'})


app.run(port=5000)


#rest apis should be stateless - they rely on nothing else
