import pytest
from track_duplicates.utils import get_arguments


def test_main_template():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_arguments()
    assert pytest_wrapped_e.type == SystemExit
