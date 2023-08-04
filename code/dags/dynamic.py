"""Example DAG demonstrating the usage of dynamic task mapping."""
from __future__ import annotations
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import  PythonOperator
import random

d={}
op_args=[]
for i in range(5):
    d['filename']=i
    d['tablename']=i+10
    op_args.append(d)


def dum(filename,tablename):
    print(f"hi, the filename is {filename} and tablename is {tablename}")


with DAG(dag_id="example_dynamic_task_mapping", start_date=datetime(2022, 3, 4),catchup=False) as dag:


    
    python_test = PythonOperator.partial(
            task_id="python_test_task",
            python_callable=dum,
        ).expand(op_kwargs=op_args)
##.expand(op_kwargs=XComArg(some_previous_task, key='return_value'))
python_test