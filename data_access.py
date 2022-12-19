from myconnection import Connection

class Film:
    lista_film = []
    lista_actor = []
    lista_query = []

    @classmethod
    def lista(self, query):
        self.lista_query = Connection.query(query)

    
    @classmethod
    def stampa_film(self):
        self.lista("select title from film")
        self.lista_film = self.lista_query
        for i in range(len(self.lista_film)):
            print(self.lista_film[i])
    

    @classmethod
    def stampa_actor(self):
        self.lista("select first_name, last_name from actor")
        self.lista_actor = self.lista_query
        for i in range(len(self.lista_actor)):
            print(self.lista_actor[i])