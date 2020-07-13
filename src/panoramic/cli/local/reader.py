from panoramic.cli.local.file_utils import (
    FileExtension,
    FilePackage,
    get_work_dir_abs_filepath,
    read_yaml,
)
from panoramic.cli.pano_model import PanoDataSource, PanoModel


class FileReader:
    def read(self, package: FilePackage):
        directory = get_work_dir_abs_filepath() / package
        data_source_path = directory / 'data_source.yaml'
        data_source = PanoDataSource.from_dict(read_yaml(data_source_path))
        models = [
            PanoModel.from_dict(read_yaml(model_path))
            for model_path in directory.glob(f'*{FileExtension.MODEL_YAML.value}')
        ]
        return data_source, models
