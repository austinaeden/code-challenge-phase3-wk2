class restaurant:
    all_restaurants=[]

    def __init__(self, name: str):
        self._name= name

    def name(self):
        return self._name
    
    @classmethod
    def all(cls):
        return cls.all_restaurants
    
