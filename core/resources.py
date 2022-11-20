from typing import Union

from core.download import download

PROJECT = "fawef230rfaw"

resources: list[dict[str, Union[str, list[str], bool]]] = [
    {
        "bucket": "",
        "blob": "",
        "subblob": "",  # Optional: ex. date
        "files": ["parent_dir/file1", "file2"],
        "destination": "path/to/save",
        "skil_if_exist": True,
        "description": "Sample resource",  # Optional
    }
]

if __name__ == "__main__":
    download(PROJECT, resources)
