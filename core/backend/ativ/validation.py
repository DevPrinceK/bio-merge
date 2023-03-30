
class Validator():
    '''Class for validating data'''

    def __init__(self):
        # self.dataframe = dataframe
        pass

    def validate_column_data_type(self, dataframe, column):
        # check of column contains the expected data type
        expected_data_types = {
            "gene_id": "object",
            "uniprot_id": "object",
            "protein_name": "object",
        }

        if column in expected_data_types:
            expected_data_type = expected_data_types[column]
            return df[column].dtype == expected_data_type
        else:
            return True


    def validate(self, dataframe):
        # Check for missing values
        if dataframe.isnull().values.any():
            print("Missing values detected:")
            print(dataframe.isnull().sum())

        # Check data types
        for column in dataframe.columns:
            if not self.validate_column_data_type(dataframe, column):
                print(f"Invalid data type in column '{column}'")

    
