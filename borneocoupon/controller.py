import os
import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

#Controllers for Borneo Coupon

#Main page
class Daily(webapp.RequestHandler):
    def get(self):
	    #The Query interface prepares a query using instance methods.
        #coupons_query = Coupon.all().order('date_created') 
		#The GqlQuery interface prepares a query using a GQL query string.
        coupons_query = db.GqlQuery("SELECT * FROM Coupon ORDER BY date_created ASC")
        coupons = coupons_query.fetch(10)
        todayDate = datetime.date.today()

        template_values = {
            'coupons': coupons,
            'todayDate': todayDate,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

#Deals page
class Deal(webapp.RequestHandler):
    def get(self):

        #get url parameter first
        coupon_id = self.request.get('coupon_id', '')
		
        if (coupon_id):
           #If coupon id is passed in, try to find it
		   #The GqlQuery interface prepares a query using a GQL query string.
           coupons_query = db.GqlQuery("SELECT * FROM Coupon WHERE coupon_id = " + coupon_id)
           coupons = coupons_query.fetch()

           template_values = {
               'coupons': coupons,
           }
        else:
           #do nothing if no coupon id passed in
           coupon_id = ''
           template_values = {
           }

        path = os.path.join(os.path.dirname(__file__), 'deal.html')
        self.response.out.write(template.render(path, template_values))
        
    def post(self):
        coupon = Coupon()
		
        coupon.coupon_id = self.request.get('coupon_id')
        coupon.dealer_id = self.request.get('dealer_id')
        coupon.date_created = self.request.get('date_created')
        coupon.date_ended = self.request.get('date_ended')
        coupon.date_offered = self.request.get('date_offered')
        coupon.date_expired = self.request.get('date_expired')
        coupon.current_sold = self.request.get('current_sold')
        coupon.target_sold = self.request.get('target_sold')
        coupon.description = self.request.get('description')
        coupon.value = self.request.get('value')
        coupon.discounts = self.request.get('discounts')
		
        coupon.put() #save new coupon as deal of the day
        self.redirect('/')