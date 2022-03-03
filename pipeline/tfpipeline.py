import proto
from  tfx.components.example_gen import utils
import tfx.v1.proto as proto
from tfx.v1.components import CsvExampleGen, StatisticsGen, ExampleValidator, SchemaGen
from tfx.proto import range_config_pb2
import os
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext
from tfx import v1 as tfx
from tfx.orchestration import metadata

pipeline_name = "test_pipeline"
pipeline_root = os.path.join(os.environ["AIRFLOW_HOME"], "tfxartifacts", pipeline_name)
metadata_path = os.path.join(pipeline_root, "metadata.sqlite")


def init_components(span=1, input_dir='input'):

    #span = utils.date_to_span_number(2022, 1, 31)
    range = proto.RangeConfig(static_range=range_config_pb2.StaticRange(start_span_number=span, end_span_number=span))
    input = proto.Input(splits=[proto.Input.Split(name='train', pattern='datadir-{SPAN:2}/ver-{VERSION}/train/*')])
    output = proto.Output(split_config=proto.SplitConfig(splits=[proto.SplitConfig.Split(name='train', hash_buckets=3),
    proto.SplitConfig.Split(name='val', hash_buckets=1)]
    ))
    example_gen = CsvExampleGen(input_base=input_dir, input_config=input, output_config=output, range_config=range)

    statistics_gen = StatisticsGen(examples=example_gen.outputs['examples'])
    schema_gen = SchemaGen(statistics=statistics_gen.outputs['statistics'], infer_feature_shape=True)
    validator = ExampleValidator(statistics=statistics_gen.outputs['statistics'],schema=schema_gen.outputs['schema'])
    components = [example_gen, statistics_gen, schema_gen, validator]
    return tfx.dsl.Pipeline(pipeline_name=pipeline_name, pipeline_root=pipeline_root,
            metadata_connection_config=metadata.sqlite_metadata_connection_config(metadata_path),
            components=components
            )