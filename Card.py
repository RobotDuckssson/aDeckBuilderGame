
class Card:
    
    def __init__(self, card_faction, card_name = None, card_type = None, card_abillity = None, card_pimary_abillity_value = None, card_cost = None):
        self.card_faction = "free"
        self.card_name = "name"
        self.card_type = "type"
        self.card_abillity = "abillity"
        self.card_cost = 0
        self.card_pimary_abillity_value = 1

        if card_faction != None:
            self.card_faction = card_faction
        if card_name != None:
            self.card_name = card_name
        if card_type != None:
            self.card_type = card_type
        if card_abillity != None:
            self.card_abillity = card_abillity
        if card_pimary_abillity_value != None:
            self.card_pimary_abillity_value = card_pimary_abillity_value
        if card_cost != None:
            self.card_cost = card_cost
      
    @property
    def card_name(self):
        return self.__card_name

    @card_name.setter
    def card_name(self, card_name):
        self.__card_name = card_name

    @property
    def card_type(self):
        return self.__card_type

    @card_type.setter
    def card_type(self, card_type):
        self.__card_type = card_type

    @property
    def card_abillity(self):
        return self.__card_abillity

    @card_abillity.setter
    def card_abillity(self, card_abillity):
        self.__card_abillity = card_abillity

    @property
    def card_cost(self):
        return self.__card_cost

    @card_cost.setter
    def card_cost(self, card_cost):
        self.__card_cost = card_cost

    @property
    def card_pimary_abillity_value(self):
        return self.__card_pimary_abillity_value

    @card_pimary_abillity_value.setter
    def card_pimary_abillity_value(self, card_pimary_abillity_value):
        self.__card_pimary_abillity_value = card_pimary_abillity_value
        
    @property
    def card_faction(self):
        return self.__card_faction

    @card_faction.setter
    def card_faction(self, card_faction):
        self.__card_faction = card_faction
        
