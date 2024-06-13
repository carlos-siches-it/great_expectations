import great_expectations as gx

context = gx.get_context()

# datasource = context.sources.add_or_update_pandas(name="my_pandas_dataframe")

# dataasset = datasource.add_csv_asset(name="my_data_asset",
#                                      filepath_or_buffer="data\yellow_tripdata_sample_2019-01.csv"
#                                      )


# batch_request = dataasset.build_batch_request()


# print (datasource)

data_asset = context.get_datasource("my_pandas_dataframe").get_asset("my_data_asset")

batch_request = data_asset.build_batch_request()

context.add_or_update_expectation_suite("my_expectation_suite")
# context.add_or_update_checkpoint("my_checkpoint")

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="my_expectation_suite"
)

result = validator.expect_column_values_to_not_be_null(column="vendor_id")

validator.save_expectation_suite(discard_failed_expectations=False)

print (result)


