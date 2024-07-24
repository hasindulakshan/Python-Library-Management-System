class Book:
    def __init__(self, isbn_no, title, format, subject, rental_price, num_copies):
        self.isbn_no = isbn_no  
        self.title = title 
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        #self.available_copies = num_copies
