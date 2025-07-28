from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig  # 🔁 Required import

class ConfigurationManager:  # Define a class to manage configuration settings
    def __init__(  # Constructor to initialize configuration manager
        self,
        config_filepath = CONFIG_FILE_PATH,  # Default path for config.yaml file
        params_filepath = PARAMS_FILE_PATH   # Default path for params.yaml file
    ):
        self.config = read_yaml(config_filepath)  # Read and load the configuration YAML file
        self.params = read_yaml(params_filepath)  # Read and load the parameters YAML file

        create_directories([self.config.artifacts_root])  # Create root directory for storing artifacts if it doesn't exist

    def get_data_ingestion_config(self) -> DataIngestionConfig:  # Method to return data ingestion configuration
        config = self.config.data_ingestion  # Access the 'data_ingestion' section from the config

        create_directories([config.root_dir])  # Create the root directory for data ingestion step

        data_ingestion_config = DataIngestionConfig(  # Create an instance of DataIngestionConfig using values from the config
            root_dir=config.root_dir,  # Directory where data ingestion outputs will be stored
            source_URL=config.source_URL,  # URL to download the dataset from
            local_data_file=config.local_data_file,  # Path to save the downloaded file locally
            unzip_dir=config.unzip_dir   # Directory to unzip the downloaded data
        )

        return data_ingestion_config  # Return the data ingestion configuration object