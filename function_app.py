import azure.functions as func
import logging
import os

from great_expectations import get_context
from great_expectations.core.yaml_handler import YAMLHandler
from great_expectations.data_context.types.base import DataContextConfig
from great_expectations.data_context.data_context.ephemeral_data_context import EphemeralDataContext
import pathlib

from great_expectations.data_context import EphemeralDataContext
from utils.gx import get_project_config
from utils.cons import CONN_STRING

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_validate_data")
def http_validate_data(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    context = get_context(context_root_dir="./gx")

    checkpoint = context.get_checkpoint(name="my_checkpoint")
    checkpoint.run()

    return func.HttpResponse(f"This HTTP triggered function executed successfully.")



@app.route(route="http_validate_data_with_ephemeral_data_context")
def http_validate_data_with_ephemeral_data_context(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')



    connection_string = CONN_STRING
    project_config = get_project_config()

    context = EphemeralDataContext(
        project_config=project_config
    )

    datasource_name = "my_pandas_dataframe"
    azure_options = {
        "conn_str": connection_string
    }

    datasource = context.sources.add_pandas_abs(
        name=datasource_name, azure_options=azure_options
    )

    asset_name = "my_data_asset"
    abs_container = "data"
    batching_regex = r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2})\.csv"


    data_asset = datasource.add_csv_asset(
        name=asset_name,
        abs_container=abs_container,
        batching_regex=batching_regex
    )

    checkpoint = context.get_checkpoint(name="my_checkpoint")
    checkpoint.run()



    return func.HttpResponse(f"This HTTP triggered function executed successfully.")


# @app.route(route="http_validate_data_with_ephemeral_data_context")
# def http_validate_data_with_ephemeral_data_context(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     yaml = YAMLHandler()
#     my_file_str = pathlib.Path("./gx/great_expectations.yml").read_text()
#     config_file = yaml.load(my_file_str)


#     config = DataContextConfig(
#         config_version=config_file["config_version"],
#         fluent_datasources=config_file["fluent_datasources"],
#         expectations_store_name=config_file["expectations_store_name"],
#         validations_store_name=config_file["validations_store_name"],
#         evaluation_parameter_store_name=config_file["evaluation_parameter_store_name"],
#         checkpoint_store_name=config_file["checkpoint_store_name"],
#         data_docs_sites=config_file["data_docs_sites"],
#         config_variables_file_path=config_file["config_variables_file_path"],
#         stores=config_file["stores"]
#     )

#     context = EphemeralDataContext(
#         project_config=config
#     )

#     checkpoint = context.get_checkpoint(name="my_checkpoint")
#     checkpoint.run()

#     return func.HttpResponse(f"This HTTP triggered function executed successfully.")









