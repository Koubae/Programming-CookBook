import random
from sqlalchemy.exc import IntegrityError
from app import app, db, photos
from flask import render_template, redirect, url_for, session, flash
from models import *
from forms import *
from app_func import *
from mail_client import *


#Index
@app.route('/')
def index():
    
    products = Product.query.all()
    
    products_ = Product.query.filter(and_(Product.id == 4, Product.stock > 0)).all()
    x = int(str(products_[0]))
    
    return render_template('index.html', products=products)

# Product view
@app.route('/product/<int:id>')
def product(id):
    
    product = Product.query.filter_by(id=id).first()
    form = AddToCart()
    return render_template('view-product.html', product=product, form=form)

# Checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    
    form = Checkout()

    products, grand_total, grand_total_plus_shipping, quantity_total = handle_cart()

    if form.validate_on_submit():

        try:
            order = Order()
            form.populate_obj(order)
            order.reference = ''.join([random.choice('ABCDE') for _ in range(5)])
            order.status = 'PENDING'

            for  product in products:
                order_item = Order_Item(quantity=product['quantity'], product_id=product['id'])
                order.items.append(order_item)
                # Remove Product from Stock
                product = Product.query.filter_by(id=product['id']).update({'stock' : Product.stock - product['quantity']})
            db.session.add(order)
            db.session.commit()
            session['cart'] = []
            session.modified = True

            flash('Order has been placed succesfully')
            return redirect(url_for('index'))
        except IntegrityError as err:
            print(repr(err))
            flash('Your cart is Empty')
            return redirect(url_for('checkout'))
    return render_template('checkout.html', form=form, grand_total=grand_total, grand_total_plus_shipping=grand_total_plus_shipping, quantity_total=quantity_total)

####################################
#---------< CART >----------------# 
####################################

# Quick add
@app.route('/quick-add/<int:id_>')
def quick_add(id_):
    
    get_cart = calc_produtc(id_, 1)
    session.modified = True
    if not get_cart:
        flash('Product out of stock')
        return redirect(url_for('index'))         
        
    flash('Item added sussecfully')
    return redirect(url_for('index'))


# Add to cart
@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    

    form = AddToCart()
    get_cart = calc_produtc(form.id.data, form.quantity.data)
    session.modified = True
    if not get_cart:
        flash('Product out of stock')
        return redirect(url_for('index'))
    
    flash('Item added sussecfully')
    return redirect(url_for('index'))
  
# Remove from cart
@app.route('/remove-from-cart/<index>')
def remove_from_cart(index):
    
    del session['cart'][int(index)]
    session.modified = True
    
    flash('Product removed from Chart')
    return redirect(url_for('cart'))

# Cart
@app.route('/cart')
def cart():

    products, grand_total, grand_total_plus_shipping, quantity_total = handle_cart()
    return render_template('cart.html', products=products, grand_total=grand_total, grand_total_plus_shipping=grand_total_plus_shipping, quantity_total=quantity_total)


####################################
#---------< ADMIN >----------------# 
####################################
# TODO 3 implement flask_login, flask_admin and secure this views
#
# Admin View
@app.route('/admin', methods=['GET', 'POST'])
def admin():

    products = Product.query.all()    
    products_in_stock = Product.query.filter(Product.stock > 0).count()
    orders = Order.query.all()
 
    
    return render_template('admin/index.html', admin=True, products=products,  products_in_stock=products_in_stock, orders=orders)

# TODO 5 Add item already added - both from /admin and admin/add
# Add product to store
@app.route('/admin/add')
def add():
    
    form = AddProduct()

    products = Product.query.all()
    if form.validate_on_submit():
        image_url = photos.url(photos.save(form.image.data))
        new_product = Product(name=form.name.data, price=form.price.data, \
                            stock=form.stock.data, description=form.description.data, \
                            image=image_url)
        db.session.add(new_product)
        db.session.commit()

        flash('You added a new product')
        return redirect(url_for('admin'))
    return render_template('admin/add-product.html', admin=True, form=form, products=products)


@app.route('/admin/add/<int:item_id>')
def add_item(item_id):

    form = Add_Item_Admin()
    products = Product.query.filter_by(id=item_id)
    product = [[x.name, x.price, x.stock, x.description] for x in products]
    # print(product)
    for i in product:
        price = int(i[1] / 100)
        stock = int(i[2])
        form.name.data = i[0]
        form.price.data = price
        form.stock.data = stock
        form.description.data = i[3]
    if form.validate_on_submit():
        print('calidare')

    return redirect('add-product-one.html', form=form)


# Check Orders
@app.route('/admin/order/<int:order_id>' , methods=['GET', 'POST'])
def order(order_id):
    
    form = Rejct_Or_Fetch()
    order = Order.query.filter_by(id=int(order_id)).first()
    if form.validate_on_submit():
        if form.reject.data:
            #msg_send_reject(order_id)
            print('Email sent')
            db.session.delete(order)
            db.session.commit()
            print('Order deleted from DB')
            flash(f'Order {order_id} has been rehected')
            return redirect(url_for('admin'))
        elif form.fetch.data:
            #msg_send_fetch(order_id)
            print('Email sent')
            db.session.delete(order)
            db.session.commit()
            print('Order deleted from DB')
            flash(f'Order {order_id} has been shipped')
            return redirect(url_for('admin'))


    return render_template('admin/view-order.html', order=order, admin=True, form=form, order_id=order_id)