"""
    Team Class with all the information about the teams

"""

class Team:
    
    """
        Constructor 
    """
    
    def __init__(self, country):
        
        # Initializing Team Values

        self._country = country
        self._match_Played = 0 
        self._match_won = 0
        self._match_drawed = 0
        self._match_lost = 0

    """ Setters"""

    def match_won_setter(self):

        self._match_won += 1
        self._match_Played += 1

    def match_drawed_setter(self):

        self._match_drawed += 1
        self._match_Played += 1

    def match_lost_setter(self):

        self._match_lost += 1
        self._match_Played += 1

    
    """ getters """

    def country_getter(self):
        
        return self._country

    def match_Played_getter(self):
        
        return self._match_Played

    def match_won_getter(self):
        
        return self._match_won

    def match_drawed_getter(self):
        
        return self._match_drawed

    def match_lost_getter(self):
        
        return self._match_lost

    """ information methods"""

    def __str__(self) -> str:
        return f"Country: {self.country_getter()}\nmp: {self.match_Played_getter()}\nw: {self.match_won_getter()}\nD: {self.match_drawed_getter()}\nL: {self.match_lost_getter()}"

    def print_information(self):
        print(self)
