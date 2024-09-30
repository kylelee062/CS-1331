class Computer:
    def __init__(self, manufacturer, model, processor, ram, display_size):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size
        
    def print_info(self):
        print(f"Manufacturer: {self.manufacturer}, Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}, Display: {self.display_size}")

class Laptop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, weight, is_touchscreen):
        super().__init__(manufacturer=manufacturer, model=model, processor=processor, ram=ram, display_size=display_size)
        self.weight = weight
        self.is_touchscreen = is_touchscreen

    def print_info(self):
        super().print_info()
        print(f"Weight: {self.weight}, Touch-screen: {self.is_touchscreen}")

class Desktop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, desktop_type):
        super().__init__(manufacturer=manufacturer, model=model, processor=processor, ram=ram, display_size=display_size)
        self.type = desktop_type

    def print_info(self):
        super().print_info()
        print(f"Type: {self.type}")

# driver code. No modification is necessary after this line.
computer1 = Laptop('Apple', 'MacBook Air', 'Apple M1', '16GB', '13.3"', '2.7 lbs', False)
computer2 = Laptop('HP', 'Envy', 'core i5', '8GB', '15.6"', '4 lbs', True)
computer3 = Desktop('Dell', 'Inspiron', 'core i7', '32GB', '27"', 'All-in-One')
computer1.print_info()
computer2.print_info()
computer3.print_info()
