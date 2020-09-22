
class Card(object):
    def __init__(self, card_faction = "free", card_name = "name", card_type = "type", card_abillity = "abillity", card_pimary_abillity_value = 1, card_cost = 0):
        self.card_faction = card_faction
        self.card_name = card_name
        self.card_type = card_type
        self.card_abillity = card_abillity
        self.card_pimary_abillity_value = card_pimary_abillity_value
        self.card_cost = card_cost

    def get_card_info(self):
        return f"{self.card_faction} - {self.card_type} - {self.card_name} - cost: {self.card_cost} - Ability: {self.card_abillity} [{self.card_pimary_abillity_value}]"