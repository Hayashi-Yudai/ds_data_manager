from pathlib import Path
import subprocess
from typing import Any
from core import config


def exclude_if_exist(target_files: list[str], data_dir: str) -> list[str]:
    res: list[str] = []
    for f in target_files:
        if "/" in f:
            filename = f.rsplit("/", 1)[1]
        else:
            filename = f

        if Path(f"{data_dir}/{filename}").exists():
            print(f"{filename} already exists, skip")
            continue

        res.append(f)

    return res


def _download_resource(
    files: list[str],
    destination_dir: str,
    gcs_base: str,
    skip_if_exist: bool = True,
) -> None:
    Path(destination_dir).mkdir(parents=True, exist_ok=True)
    if skip_if_exist:
        files = exclude_if_exist(files, destination_dir)
        if len(files) == 0:
            print("All files already exist. End")
            return

    targets = " ".join([gcs_base + f for f in files])

    result = subprocess.call(
        [
            f"{config.REPO_ROOT}/scripts/download_data.sh",
            targets,
            destination_dir,
        ]
    )
    if result != 0:
        raise RuntimeError("Script Failed")


def download(project: str, resources: list[dict[str, Any]]):
    for rs in resources:
        gcs_base = f"gs://{rs['bucket']}/{rs['project']}"

        if rs["subproject"] != "":
            gcs_base += f"/{rs['subproject']}/"

        data_dir = f"{config.REPO_ROOT}/data/{project}/{rs['destination']}"
        print(data_dir)

        _download_resource(
            rs["files"],
            data_dir,
            gcs_base,
            skip_if_exist=rs["skip_if_exist"],
        )
