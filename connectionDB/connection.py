from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    
    def __init__(self) -> None:
        db_path = "database/"
        db_url = 'sqlite:///%s/db.sqlite3' % db_path

        # self.__connection_string = 'postgresql://postgres:root@localhost:5432/cinema'
        self.__connection_string = db_url
        self.__engine = self.__create_database_engine()
        self.session = None
        
    def __create_database_engine(self):
        engine =  create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        
        