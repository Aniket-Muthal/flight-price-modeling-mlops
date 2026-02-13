"""
data_acquisition.py

This script mimics basic data engineering workflow where datasets are:
- Retrieved from Google drive using File ID.
- Downloaded as a ZIP file to a configured local directory.
- Validated for successfull download.
- Extracted into a specified data folder.
"""

## ------------------------------------------------------------------------------------------------------------------------------------ ##
## Imports
## ------------------------------------------------------------------------------------------------------------------------------------ ##
import yaml
import gdown
import zipfile
from pathlib import Path
from box import ConfigBox
from dataclasses import dataclass


## ------------------------------------------------------------------------------------------------------------------------------------ ##
## Load Data Source config
## ------------------------------------------------------------------------------------------------------------------------------------ ##
CONFIG_FILE_PATH = Path("configs/data-source.yaml")

with open(CONFIG_FILE_PATH, "rb") as f:
    content = yaml.safe_load(f)

config_content = ConfigBox(content)

## ------------------------------------------------------------------------------------------------------------------------------------ ##
## Immutable Configuration Dataclass
## ------------------------------------------------------------------------------------------------------------------------------------ ##
@dataclass(frozen=True)
class DataAcquisitionConfig:
    """
    Configuration for data acquisition.

    Attributes
    ----------
    file_id: str
        Google Drive file ID.
    download_file_path: Path
        Local path to store to store downloaded ZIP file.
    extract_dir: Path
        Directory to extract ZIP contents.
    """
    file_id: str = config_content.gdrive.file_id
    download_file_path: Path = Path(config_content.gdrive.download_file_path)
    extract_dir: Path = Path(config_content.gdrive.extract_dir)

## ------------------------------------------------------------------------------------------------------------------------------------ ##
## Data Acquisition class
## ------------------------------------------------------------------------------------------------------------------------------------ ##
class DataAcquisition:
    """
    Handles downloading and extracting dataset files from external sources.

    Attributes
    ----------
    config: DataAcquisitionConfig
        Data acquisition config
    
    Methods
    -------
    download_zip
        Responsible for downloading dataset files in ZIP format
    
    extract_all
        Responsible for extracting ZIP content to data folder   
    """
    def __init__(self, config: DataAcquisitionConfig):
        self.config = config

    def download_zip(self):
        """
        Downloads the dataset ZIP file from Google Drive.
        Skips download if file already exists and is non-empty.

        Returns
        -------
        None

        Raises
        ------
        RuntimeError: If download fails or results in an empty file.
        """
        try:
            file_id = self.config.file_id
            download_file_path = self.config.download_file_path
            url = f"https://drive.google.com/uc?id={file_id}"

            download_file_path.parent.mkdir(parents=True, exist_ok=True)

            if download_file_path.exists() and download_file_path.stat().st_size > 0:
                print(
                    f"Zip file already exists with size ({download_file_path.stat().st_size / (1024**2):.2f} MB).Skipping download"
                )
                return

            gdown.download(url=url, output=str(download_file_path), quiet=False)

            if not download_file_path.exists() and download_file_path.stat().st_size == 0:
                raise RuntimeError("Download failed or produced an empty file")

        except Exception as e:
            raise 
    
    def extract_all(self):
        """
        Extracts the downloaded ZIP file to the configured directory.

        Returns
        -------
        None

        Raises
        ------
        FileNotFoundError: If the ZIP file is missing or empty.
        """
        try:
            zip_file_path = self.config.download_file_path
            extract_dir = self.config.extract_dir
            
            extract_dir.mkdir(parents=True, exist_ok=True)

            if not zip_file_path.exists() and zip_file_path.stat().st_size == 0:
                raise FileNotFoundError("Zip file is missing or empty. Cannot extract.")
            
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(extract_dir)
        
        except Exception as e:
            raise


## ------------------------------------------------------------------------------------------------------------------------------------ ##
## Entry point
## ------------------------------------------------------------------------------------------------------------------------------------ ##
if __name__ == "__main__":
    data_acquisition_config = DataAcquisitionConfig()
    data_acquisition = DataAcquisition(config=data_acquisition_config)
    data_acquisition.download_zip()
    data_acquisition.extract_all()

## ------------------------------------------------------------------------------------------------------------------------------------ ##