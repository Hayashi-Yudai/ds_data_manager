from dataclasses import dataclass


# Experimental
@dataclass(frozen=True)
class Resource:
    """
    Interface for resources
    """

    def download(self):
        raise NotImplementedError


@dataclass(frozen=True)
class GCSResource(Resource):
    bucket: str
    project: str
    subproject: str
    files: list[str]
    destination: str
    skip_if_exist: bool = True
    description: str = ""

    def __post_init__(self):
        if self.bucket == "":
            raise ValueError("Bucket name is necessary")
        if self.project == "":
            raise ValueError("Project name is necessary")
        if len(self.files) == 0:
            raise ValueError("Download files list is empty")
        # TODO: give default value $REPO_ROOT/outputs/$PROJECT/
        if self.destination == "":
            raise ValueError("Destination of download files is necessary")


class BQResource(Resource):
    dataset: str
    table: str
    query: str
    destination: str
    skip_if_exist: bool = True
    description: str = ""


# Example: downloads the following files to the destination directory
# gs://my-bucket/project-1/latest/parent1/file1
# gs://my-bucket/project-1/latest/parent1/file2
# gs://my-bucket/project-1/latest/file3
resources_exp: list[Resource] = [
    GCSResource(
        bucket="my-bucket",
        project="project-1",
        subproject="latest",
        files=["parent1/file1", "parent1/file2", "file3"],
        destination="path to save",
        skip_if_exist=True,
        description="Sample GCS resource",
    )
]
