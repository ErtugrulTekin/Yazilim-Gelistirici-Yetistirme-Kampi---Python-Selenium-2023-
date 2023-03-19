class Human:

    #built-in
    #constructor
    #initialize

    def __init__(self, name):
        self.name = name
        print("Bir insan instance'i Uretildi")

    def __str__(self):
        return f"STR fonksiyonundan donen deger: {self.name}"

    def talk(self, sentence):
        print(f"{self.name} {sentence}")
    
    def walk(self):
        print(f"{self.name} is walking..")