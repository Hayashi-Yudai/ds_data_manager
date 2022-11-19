from core import download


def test_judge_exist_files():
    target_files = ["test_download.py", "test_test.py"]
    data_dir = "./tests"

    non_exist_files = download.exclude_if_exist(target_files, data_dir)

    assert len(non_exist_files) == 1
    assert non_exist_files[0] == "test_test.py"
