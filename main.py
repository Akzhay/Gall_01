from n_faker import Gen_N
from exec_01 import execute_sql_file
from logger_config import log_message
from database import connect_to_database, create_table




    

if __name__ == "__main__":
    # Gen_N(5000)
    execute_sql_file('example.db', 'commands.sql', 'Output\output.xlsx')