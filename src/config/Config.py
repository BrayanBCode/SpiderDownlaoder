from dataclasses import dataclass


@dataclass
class DataConfig:
    download_path: str = "Descargas"


config = DataConfig()


