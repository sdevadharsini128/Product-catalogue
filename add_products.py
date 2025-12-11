
import requests



products = [
        {
            "name": "Basmati Rice 5kg",
            "selling_price": 650,
            "stock_quantity": 20,
            "description": "Premium quality basmati rice",
            "is_visible_in_catalogue": True
        },
        {
            "name": "Wheat Flour 10kg",
            "selling_price": 450,
            "stock_quantity": 15,
            "description": "Fresh wheat flour",
            "is_visible_in_catalogue": True
        },
        {
            "name": "Cooking Oil 1L",
            "selling_price": 180,
            "stock_quantity": 0,
            "description": "Refined cooking oil - Out of Stock",
            "is_visible_in_catalogue": True
        },
        {
            "name": "Sugar 1kg",
            "selling_price": 55,
            "stock_quantity": 100,
            "description": "Pure white sugar",
            "is_visible_in_catalogue": True
        },
          {
            "name": "rice flour 20kg",
            "selling_price": 95,
            "stock_quantity": 68,
            "description": "Pure white sugar",
            "is_visible_in_catalogue": True
        },
      
        
    ]
for product in products:
    response= requests.post("http://localhost:5000/add-product",json=product)
    print(f"added:{product['name']}")