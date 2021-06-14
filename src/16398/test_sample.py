import unittest
from exceptions import *
from orm import ORM
import os

class OrmTest2(unittest.TestCase):
    @staticmethod
    def remove_database_file(db_path):
        try:
            os.remove(db_path)
        except OSError:
            pass

    @staticmethod
    def create_database_file(db_path):
        import sqlite3
        sqlite3.connect(db_path)

    def test_sample(self):
        self.db_path = r'databases/first.sqlite3'
        self.table_path = 'tables.user'
        self.table_name = 'User'
        self.orm_obj = ORM(self.db_path)
        self.remove_database_file(self.db_path)
        self.create_database_file(self.db_path)
        values = [
            {
                'name': 'mohammad bagher',
                'family': 'tabrizi',
                'likes': 2
            },
            {
                'name': 'mohammad javad',
                'family': 'naderi',
                'likes': 1
            },
            {
                'name': 'mostafa',
                'family': 'karimi',
                'likes': 1
            },
            {
                'name': 'mostafa',
                'family': 'tabrizi',
                'likes': 2
            },
            {
                'name': 'mostafa',
                'family': 'tabrizi',
                'likes': 4
            },
        ]
        self.orm_obj.create_table(self.table_path, self.table_name)
        self.orm_obj.add_value(self.table_path, self.table_name, **values[3])
        added_values = self.orm_obj.get_values(self.table_path, self.table_name, name='mostafa')
        self.assertEqual(added_values, [values[3]])
        self.orm_obj.add_values(self.table_path, self.table_name, [values[1], values[2]])
        added_values = self.orm_obj.get_values(self.table_path, self.table_name)
        self.assertEqual(added_values, values[1:4])
        self.orm_obj.remove_value(self.table_path, self.table_name, name='mostafa')
        added_values = self.orm_obj.get_values(self.table_path, self.table_name)
        self.assertEqual(added_values, [values[1]])
        self.orm_obj.add_values(self.table_path, self.table_name, [values[2], values[3]])
        self.orm_obj.remove_values(self.table_path, self.table_name, [values[1], values[2]])
        added_values = self.orm_obj.get_values(self.table_path, self.table_name)
        self.assertEqual(added_values, [values[3]])
        self.orm_obj.add_value(self.table_path, self.table_name, **values[1])
        has_error = False
        try:
            self.orm_obj.add_value(self.table_path, self.table_name, **values[1])
        except ValueExistException:
            has_error = True
        self.assertTrue(has_error)
