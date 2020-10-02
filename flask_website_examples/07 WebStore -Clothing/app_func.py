from flask import session
from app import db
from models import Product
from sqlalchemy import and_


def handle_cart():
    
    products = []
    grand_total = 0
    index = 0
    quantity_total = 0

    if 'cart' not in session:
        session['cart'] = []
    for item in session['cart']:
        product = Product.query.filter_by(id=item['id']).first()
        quantity = int(item['quantity'])
        total = quantity * product.price
        grand_total += total
        quantity_total += quantity

        products.append({'id' : product.id, 'name' : product.name, 'price' :  product.price, 'image' : product.image, 'quantity' : quantity, 'total': total, 'index': index})
        index += 1
    
    grand_total_plus_shipping = grand_total + 1000

    return products, grand_total, grand_total_plus_shipping, quantity_total


def calc_produtc(id_form, quantity):
    id_form = int(id_form)
    item_added = False
 
    if 'cart' not in session:
        session['cart'] = []
        session['cart_idx'] = []
        
    if  int(id_form) not in session['cart_idx']:
                session['cart'].append({'id': int(id_form), 'quantity': quantity})
                session['cart_idx'].append(int(id_form)) 
                item_added = True
            
    else:
        idx = session['cart_idx'].index(id_form)                    
        if session['cart'][idx]['id'] == id_form:
                product = Product.query.filter(and_(Product.id == id_form, Product.stock > 0)).all()   
                stock = int(str(product[0]))   
                if quantity +  session['cart'][idx]['quantity'] <= stock:                    
                    session['cart'][idx]['quantity'] += quantity
                    item_added = True
    return item_added 