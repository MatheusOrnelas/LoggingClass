from datetime import datetime
import pandas as pd
from db import DatabaseConnection
import os

class LogClass:
    def __init__(self, engine, table_name_logs='dimcrtlogsystems'):
        """
        Initializes the log recording class.

        Args:
            engine: Database connection engine for MySQL.
            table_name_logs (str): Name of the table where logs will be saved in the database. Default is 'dimcrtlogsystems'.
        """
        self.engine = engine
        self.table_name_logs = table_name_logs
        print("LogClass initialized!")


    def insert_logs(self, system_code, system_module_message, system_source_message,
                    status, message_type, message, output_format='db'):
        """
        Records log data.

        Args:
            system_code (int): Identification code of the monitored system. Performs the separation of logs 
                               from two different systems into the same log "file".
            system_module_message (str): Class and function where the message is occurring.
            system_source_message (str): File where the message is occurring.
            status (str): Status of the message (e.g., Success, Information, Alert, Error).
            message_type (str): Type of the message (e.g., Success, Alert, Error 0 division, Type Error).
            message (str): The log message to be recorded (e.g., Success, Information, Alert, Error message).
            output_format (str): The output format for the log ('db', 'csv', 'xlsx'). Default is 'db'.
        """
        try:
            register_date = datetime.now()
            data = {
                'System_Code': [system_code], 
                'System_Module_Message': [system_module_message],
                'System_Source_Message': [system_source_message],  
                'Status': [status], 'Message_Type': [message_type],
                'Message': [message], 'Register_Date': [register_date],
            }
            
            dataframe = pd.DataFrame(data)

            if output_format == 'db':
                DatabaseConnection.insert_data_into_table(self.engine, dataframe, self.table_name_logs)
                print("Log successfully saved in database!")
            elif output_format in ['csv', 'xlsx']:
                log_dir = "log"
                if not os.path.exists(log_dir):
                    os.makedirs(log_dir)
                
                file_name = f"{log_dir}/log.{output_format}"

                if output_format == 'csv':
                    if os.path.exists(file_name):
                        dataframe.to_csv(file_name, mode='a', header=False, index=False)
                    else:
                        dataframe.to_csv(file_name, index=False)

                elif output_format == 'xlsx':
                    file_name = f"{log_dir}/log.xlsx"

                    if os.path.exists(file_name):
                        existing_data = pd.read_excel(file_name)
                        new_data = pd.concat([existing_data, dataframe], ignore_index=True)
                        new_data.to_excel(file_name, index=False)

                    else:
                        dataframe.to_excel(file_name, index=False)

                else:
                    print("Select the export option!")
                    print("Use the parameter output_format in the function insert_logs!")

                print(f"Log successfully saved in {file_name}!")

        except Exception as error:
            print(f"Error occurred: {error}")