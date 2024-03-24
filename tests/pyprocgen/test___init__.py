import pytest

import pyprocgen


@pytest.mark.parametrize("module_name", pyprocgen.__all__)
def test_imports(module_name: str) -> None:
    """It exposes the pyqueuesimu modules."""
    assert hasattr(pyprocgen, module_name)
