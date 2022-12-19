
import mysql.connector 
class Connection():
    credenziali = {"host":"localhost", "user":"root", "passwd": "MarNico2?", "port": "3306", "database": "sakila"}
    
    def __init__(self) -> None:
        self.miaconnession=None

    @classmethod
    def connessione(self):
        try:
            self.miaconnession = mysql.connector.connect(host = self.credenziali["host"] , user = self.credenziali["user"] , passwd = self.credenziali["passwd"],port=self.credenziali["port"],database=self.credenziali["database"] )
        except mysql.connector.Error as errore:
            print("Si è verificato un errore") 
            print(errore)
        

    @classmethod
    def query(self, mia_query):
        self.connessione()
        if self.miaconnession is not None:
            try:
                mycursor= self.miaconnession.cursor()
                mycursor.execute(mia_query)

                result= mycursor.fetchall()
                return(result)
            except mysql.connector.Error as errore:
                print("Si è verificato un errore") 
                print(errore)
            finally:
                if self.miaconnession is not None:
                    self.miaconnession.close()
                    print("connessione chiusa")
        else:
            print("database non ancora connesso")




