import os
import pandas as pd
from datetime import datetime
from database import get_db_connection

def handle_history(download=False, user_id="default_user"):
    conn = get_db_connection()
    query = 'SELECT query, response, timestamp FROM user_history WHERE user_id = ?'
    df = pd.read_sql(query, conn, params=(user_id,))

    if download:
        file_path = f'chat_history_{user_id}_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
        df.to_csv(file_path, sep='\t', index=False)
        return file_path
    else:
        return df

def log_query(user_id, query, response):
    conn = get_db_connection()
    with conn:
        conn.execute('''
            INSERT INTO user_history (user_id, query, response)
            VALUES (?, ?, ?)
        ''', (user_id, query, response))