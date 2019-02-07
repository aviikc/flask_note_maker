from datetime import time

unique_id = 0

class Person:
    def __init__(self, f_name, l_name, address, city):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.city = city
        global unique_id
        unique_id += 1
        self.id = unique_id

        


