import os
import pytest
from typing import Any, Generator


@pytest.fixture(scope="function")
def change_test_dir(tmpdir: str, request: Any) -> Generator[Any, Any, Any]:
    os.chdir(tmpdir)
    yield (tmpdir)
    os.chdir(request.config.invocation_dir)
