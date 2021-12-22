

#parent class Computers
class Computers:
    CPU = True
    connects_internet = True
    operating_system = "must have"
    PSU = True
    
#child class    
class Desktop(Computers):
    #unique attributes
    screen_size = "wide range"
    input_devices = "external"
    
    
#child class
class Laptop(Computers):
    #unique attributes
    has_touchpad = True
    has_mobility = True
    
    
    
    
    
    
    
