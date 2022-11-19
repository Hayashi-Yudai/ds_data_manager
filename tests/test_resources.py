import pytest

from core.resource_classes import Resource, GCSResource


def test_gcs_resource():
    res = GCSResource(
        bucket="bucket",
        project="project",
        subproject="",
        files=["file1"],
        destination="destination",
        skip_if_exist=True,
        description="",
    )

    assert isinstance(res, GCSResource)
    assert isinstance(res, Resource)


def test_gcs_resource_with_invalid_values():
    bucket = "bucket"
    project = "project"
    subproject = ""
    files = ["file"]
    destination = "destination"
    skip_if_exist = True
    description = ""

    with pytest.raises(ValueError) as e:
        GCSResource(
            "", project, subproject, files, destination, skip_if_exist, description
        )

    assert str(e.value) == "Bucket name is necessary"

    with pytest.raises(ValueError) as e:
        GCSResource(
            bucket, "", subproject, files, destination, skip_if_exist, description
        )

    assert str(e.value) == "Project name is necessary"

    with pytest.raises(ValueError) as e:
        GCSResource(
            bucket, project, subproject, [], destination, skip_if_exist, description
        )

    assert str(e.value) == "Download files list is empty"

    with pytest.raises(ValueError) as e:
        GCSResource(bucket, project, subproject, files, "", skip_if_exist, description)

    assert str(e.value) == "Destination of download files is necessary"


def test_skip_param_is_arbitrarily_in_gcs_resource():
    try:
        _ = GCSResource(
            "bucket", "project", "subproject", ["file"], "destination", description=""
        )
    except Exception:
        pytest.fail("skip_if_exist is not arbitrarily argument")


def test_description_is_arbitrarily_in_gcs_resource():
    try:
        _ = GCSResource(
            "bucket",
            "project",
            "subproject",
            ["file"],
            "destination",
            skip_if_exist=False,
        )
    except Exception:
        pytest.fail("description is not arbitrarily argument")
