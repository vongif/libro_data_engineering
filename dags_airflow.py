import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

def CSVToJson():
    df = pd.read_csv('data.CSV')
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON', orient='records')

default_args = {
    'owner': 'cristian',
    'start_date': dt.datetime(2023, 5, 6),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         # '0 * * * *',
         ) as dag:
    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "I am reading the CSV now....."')
    CSVJson = PythonOperator(task_id='convertCSVtoJson',
                             python_callable=CSVToJson)

print_starting.set_downstream(CSVJson)
CSVJson.set_upstream(print_starting)
print_starting >> CSVJson
CSVJson << print_starting
