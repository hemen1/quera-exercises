from exceptions import *


class ORM:
    def __init__(self, db_path):
        self.db_path = db_path
        self.create_database_if_not_exist()

    def create_database_if_not_exist(self):
        pass

    def create_table(self, table_path, table_name):
        pass

    def add_value(self, table_path, table_name, **values):
        pass

    def add_values(self, table_path, table_name, values):
        pass

    def remove_value(self, table_path, table_name, **values):
        pass

    def remove_values(self, table_path, table_name, values):
        pass

    def get_values(self, table_path, table_name, **filters):
        pass
