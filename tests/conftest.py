from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    # Arrange: capture a deep snapshot of in-memory state before each test.
    original_activities = deepcopy(activities)

    try:
        yield TestClient(app)
    finally:
        # Assert isolation: restore global state so tests do not affect each other.
        activities.clear()
        activities.update(deepcopy(original_activities))
