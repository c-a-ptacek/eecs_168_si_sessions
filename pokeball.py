#pokeball.py

class Pokeball:

    def __init__(self, name, price, effectiveness):
        self.name = name
        self._price = 0
        self._effectiveness = 1
        self.set_price(price)
        self.set_effectiveness(effectiveness)

    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            pass
    
    def set_effectiveness(self, effectiveness):
        if effectiveness >= 1:
            self._effectiveness = effectiveness
        else:
            pass

    def get_effectiveness(self):
        return self._effectiveness

    def get_price(self):
        return self._price

    def __gt__(self, other):
        return self._effectiveness > other.get_effectiveness()

    def __eq__(self, other):
        return self._effectiveness == other.get_effectiveness()

    """Since we've defined how > and == work for Pokeballs, we can directly use these when
    defining the other magic methods. However, if this confuses you, there are comments bellow each
    magic method that show the 'regular' way of defining them.
    
    Also, please double check my logic before blindly memorizing these for a test. I'm 99% confident they are correct,
    but I make no promises. I'd hate for you to lose points on a test because you copied a careless mistake that I made!
    """
    def __ne__(self, other):
        return not self == other
        #return self._effectiveness != other.get_effectiveness()

    def __le__(self, other):
        return not self > other
        #return self._effectiveness <= other.get_effectiveness()

    def __lt__(self, other):
        return not self == other and not self > other
        #return self._effectiveness < other.get_effectiveness()

    def __ge__(self, other):
        return self > other or self == other
        #return self.effectiveness >= other.get_effectiveness()

    def __str__(self):
        return f"Pokeball Name: {self.name}\nPrice: {self._price} Pokemon Dollars\nEffectiveness Rate: {self._effectiveness}x"

    def __repr__(self):
        return f"Pokeball({self.name}, {self._price}, {self._effectiveness})"