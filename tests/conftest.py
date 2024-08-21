import os
import shutil
import uuid
from typing import Generator

import pytest
from pytest_mock import MockerFixture


@pytest.fixture(autouse=True)
def ferm_configuration_is_valid_mock(mocker: MockerFixture) -> None:
    mocker.patch(
        "cyberfusion.FermSupport.configuration.Configuration.is_valid",
        new=mocker.PropertyMock(return_value=True),
    )


@pytest.fixture(autouse=True)
def systemd_restart_mock(mocker: MockerFixture) -> None:
    mocker.patch(
        "cyberfusion.SystemdSupport.units.Unit.restart", return_value=None
    )


@pytest.fixture
def ferm_base_path_mock(mocker: MockerFixture) -> Generator[None, None, None]:
    directory = os.path.join(os.path.sep, "tmp", str(uuid.uuid4()))

    os.mkdir(directory)

    mocker.patch(
        "cyberfusion.ExternalProvidersIPRanges.get_ferm_base_path",
        return_value=directory,
    )

    yield

    shutil.rmtree(directory)
