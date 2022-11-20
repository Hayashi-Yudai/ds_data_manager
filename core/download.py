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


def _build_source_and_destination(
    project: str, resource: dict[str, Any]
) -> tuple[str, str]:
    source = f"gs://{resource['bucket']}/{resource['blob']}"
    if resource["subblob"] != "":
        source += f"/{resource['subblob']}/"

    destination = f"{config.REPO_ROOT}/data/{project}/{resource['destination']}"

    return source, destination


def download(project: str, resources: list[dict[str, Any]]):
    for rs in resources:
        source, destination = _build_source_and_destination(project, rs)

        _download_resource(
            rs["files"],
            destination,
            source,
            skip_if_exist=rs["skip_if_exist"],
        )
