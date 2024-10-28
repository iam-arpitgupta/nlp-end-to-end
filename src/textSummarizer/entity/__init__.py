from dataclass import dataclass 
from Pathlib import Path 

@dataclass 
class DataIngestionConfig:
    toor_dir : Path
    souce_URL :Path
    local_data_file :Path
    unzip_dir : Path

