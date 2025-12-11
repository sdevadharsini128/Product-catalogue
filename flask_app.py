
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# MongoDB 

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['ekthaa_db']
products_collection = db['products']

# Helper function to convert MongoDB ObjectId to string
def serialize_product(product):
    if product:
        product['_id'] = str(product['_id'])
    return product

#  Add Product
@app.route('/add-product', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        
        
        product = {
            'shop_id': data.get('shop_id', 'default_shop'),
            'name': data.get('name'),
            'sku': data.get('sku', ''),
            'cost_price': data.get('cost_price', 0),
            'selling_price': data.get('selling_price', 0),
            'stock_quantity': data.get('stock_quantity', 0),
            'description': data.get('description', ''),
            'image_url': data.get('image_url', 'https://via.placeholder.com/300'),
            'is_visible_in_catalogue': data.get('is_visible_in_catalogue', True),
            'created_at': datetime.utcnow()
        }
        
        # Insert into database
        result = products_collection.insert_one(product)
        product['_id'] = str(result.inserted_id)
        
        return jsonify({
            'success': True,
            'message': 'Product added successfully',
            'product': product
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400

#  Get Public Catalogue
@app.route('/catalogue', methods=['GET'])
def get_catalogue():
    try:
       
        shop_id = request.args.get('shop_id', 'default_shop')
        
      
        query = {
            'shop_id': shop_id,
            'is_visible_in_catalogue': True
        }
        
        products = list(products_collection.find(query))
        
        # Convert ObjectId to string for JSON 
        for product in products:
            product['_id'] = str(product['_id'])
            # Convert datetime to string
            if 'created_at' in product:
                product['created_at'] = str(product['created_at'])
        
        return jsonify({
            'success': True,
            'count': len(products),
            'products': products
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400

# Frontend
@app.route('/')
def index():
    return render_template('catalogue.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
