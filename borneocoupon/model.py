from google.appengine.ext import db

#ORM for Borneo Coupon

# Coupons model
class Coupon(db.Model):
    coupon_id = db.IntegerProperty()
    dealer_id = db.IntegerProperty()
    date_created = db.DateTimeProperty(auto_now_add=True)
    date_ended = db.DateTimeProperty()
    date_offered = db.DateTimeProperty()
    date_expired = db.DateTimeProperty()
    current_sold = db.IntegerProperty()
    target_sold = db.IntegerProperty()
    description = db.StringProperty(multiline=True)
    value = db.IntegerProperty()
    discounts = db.IntegerProperty()