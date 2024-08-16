import json
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture(scope="session")
def dict_example() -> dict[str, Any]:
    return json.loads((Path(__file__).parent / "data/example.json").read_text())
