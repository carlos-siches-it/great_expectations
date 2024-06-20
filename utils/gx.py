from great_expectations.data_context.types.base import DataContextConfig, InMemoryStoreBackendDefaults
from utils.cons import CONN_STRING


def get_project_config():
    connection_string = CONN_STRING
    return DataContextConfig(
    config_version="3.00",
    store_backend_defaults=InMemoryStoreBackendDefaults(),
    stores={
            "expectations_store": {
                "class_name": "ExpectationsStore",
                "store_backend": {
                    "class_name": "TupleAzureBlobStoreBackend",
                    "container": "gxs",
                    "prefix": "expectations",
                    "connection_string": connection_string
                },
            },
            "validations_store": {
                "class_name": "ValidationsStore",
                "store_backend": {
                    "class_name": "TupleAzureBlobStoreBackend",
                    "container": "gxs",
                    "prefix": "validations",
                    "connection_string": connection_string
                },
            },
            "evaluation_parameter_store": {
                "class_name": "EvaluationParameterStore"
            },
            "checkpoint_store": {
                "class_name": "CheckpointStore",
                "store_backend": {
                    "class_name": "TupleAzureBlobStoreBackend",
                    "container": "gxs",
                    "prefix": "checkpoints",
                    "connection_string": connection_string
                }
            },
        },
    data_docs_sites={
            "new_site_name": {
                "class_name": "SiteBuilder",
                "store_backend": {
                    "class_name": "TupleAzureBlobStoreBackend",
                    "container": "web",
                    "prefix": "gx_site",
                    "connection_string": connection_string
                },
                "site_index_builder": {
                    "class_name": "DefaultSiteIndexBuilder"
                }
            }
        }
)


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