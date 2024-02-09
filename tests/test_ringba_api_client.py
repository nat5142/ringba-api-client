"""Tests for `ringba_api_client` module."""
from typing import Generator

import pytest

import ringba_api_client


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield ringba_api_client.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.0.1"
