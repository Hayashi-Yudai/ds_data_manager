## DS Data Manager

![workflow](https://github.com/Hayashi-Yudai/ds_data_manager/actions/workflows/python_app.yml/badge.svg)

### Quick start

Run

```bash
poetry install
./scripts/setup.sh $PROJECT_NAME
```

`$PROJECT_NAME` directory is generated in `src` directory. Next, edit `resources.py` in the generated directory based on the example below and write the files to be downloaded from GCS

```python
resources: list[dict[str, Union[str, list[str], bool]]] = [
    {
        "bucket": "",
        "project": "",
        "subproject": "",  # Optional: ex. date
        "files": ["parent_dir/file1", "file2"],
        "destination": "path/to/save",
        "skil_if_exist": True,
        "description": "Sample resource",  # Optional
    }
]
```

then, run

```bash
poetry run python src/$PROJECT_NAME/resources.py
```

You can find files in `data/$PROJECT_DIR`.
