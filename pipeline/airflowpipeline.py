import os
import datetime

#from typing import Text

#from tfx.orchestration import metadata
from tfx.orchestration.airflow.airflow_dag_runner import AirflowDagRunner
from tfx.orchestration.airflow.airflow_dag_runner import AirflowPipelineConfig
from tfpipeline import init_components
from tfx import v1 as tfx

airflow_dir = os.environ["AIRFLOW_HOME"]
data_dir = os.path.join(airflow_dir, "input")
airflow_config = {
    "schedule_interval": None,
    "start_date": datetime.datetime(2020, 4, 17),
}


pipeline = init_components(span=1, input_dir=data_dir)
DAG = AirflowDagRunner(AirflowPipelineConfig(airflow_config)).run(pipeline)