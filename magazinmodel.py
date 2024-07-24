class Magazine:
    def __init__(self, mag_no, title, color_or_blackwhite_print, subject, rental_price, num_copies):
        self.mag_no = mag_no  
        self.title = title 
        self.color_or_blackwhite_print = color_or_blackwhite_print
        self.subject =  subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        #self.available_copies = num_copies