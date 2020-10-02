from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(100))
    # Relationship
    orders = db.relationship('Order_Item', backref='product', lazy=True)


    def __repr__(self):
        return str(self.stock)



class Order(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(5), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    status = db.Column(db.String(10))
    payment_type = db.Column(db.String(10), nullable=False)
    # Relationship
    items = db.relationship('Order_Item', backref='order', lazy=True)
    
    # Cart Total
    def order_total(self):
        try:
            return db.session.query(db.func.sum(Order_Item.quantity * Product.price)).join(Product).filter(Order_Item.order_id == self.id).scalar() + 1000
        except TypeError as err:
            print(err)
            return None

    # TODO what does this function do, is not used ?
    def quantity_total(self):
        return db.session.query(db.func.sum(Order_Item.quantity)).filter(Order_Item.order_id == self.id).scalar()


class Order_Item(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'id: {self.id} product_id: : {self.product_id} order_id: {self.order_id} quantity: {self.quantity}'