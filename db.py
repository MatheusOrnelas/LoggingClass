# Libraries Import
import pandas as pd
from sqlalchemy import create_engine, MetaData, text

# Database Connection Class
class DatabaseConnection:
    def __init__(self):
        print('Database Connection Class Initialized!')

    @staticmethod
    def connect_to_db(username, password, host, database):
        """
        Establishes a database connection using provided credentials.

        Args:
            username (str): Database username.
            password (str): Database password.
            host (str): Database host address.
            database (str): Database name.

        Returns:
            engine: A database engine for the connection.
        """
        engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
        return engine

    @staticmethod
    def select_from_table(engine, table_name):
        """
        Selects all data from a specified table.

        Args:
            engine: The database engine.
            table_name (str): The name of the table to select data from.

        Returns:
            DataFrame: A DataFrame containing the selected table data.
        """
        sql_query = f'SELECT * FROM {table_name}'
        dataframe = pd.read_sql_query(sql_query, engine)
        return dataframe

    @staticmethod
    def insert_data_into_table(engine, dataframe, target_table):
        """
        Inserts data into a specified table.

        Args:
            engine: The database engine.
            dataframe (DataFrame): The DataFrame containing data to insert.
            target_table (str): The name of the target table.

        Exceptions:
            Catches and prints any exceptions that occur during the insert operation.
        """
        try:
            dataframe.to_sql(target_table, con=engine, if_exists='append', index=False)
            print('Data successfully inserted!')
        except Exception as error:
            print('The following error occurred:\n', error)

    @staticmethod
    def update_keywords(engine, keywords, table_name):
        """
        Updates keyword records in a specified table.

        Args:
            engine: The database engine.
            keywords (list): List of keywords to update.
            table_name (str): The name of the table containing the keywords.

        Note:
            Commits the updates to the database.
        """
        metadata = MetaData()
        metadata.reflect(engine)
        dim_ext_keyword_table = metadata.tables[table_name]
        with engine.connect() as connection:
            for keyword in keywords:
                update_query = dim_ext_keyword_table.update().where(
                    dim_ext_keyword_table.c.keywords == keyword).values(check='S')
                connection.execute(update_query)
            connection.commit()
        print('Keywords successfully updated!')

        

    @staticmethod
    def disable_safe_updates(engine):
        """
        Disables safe update mode for the database.

        Args:
            engine: The database engine.
        """
        with engine.connect() as connection:
            connection.execute(text("SET SQL_SAFE_UPDATES = 0;"))
            print('Safe update mode disabled.')

    @staticmethod
    def delete_from_table(engine, table_name):
        """
        Deletes all records from a specified table.

        Args:
            engine: The database engine.
            table_name (str): The name of the table to delete data from.

        Note:
            Commits the deletion to the database.
        """
        with engine.connect() as connection:
            connection.execute(text(f"DELETE FROM {table_name}"))
            print(f"Table {table_name} has been cleared.")
            connection.commit()
