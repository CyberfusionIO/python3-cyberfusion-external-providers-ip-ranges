import ipaddress
import os
from pathlib import Path

from pytest_mock import MockerFixture

from cyberfusion.ExternalProvidersIPRanges import Configuration, main


def test_main(mocker: MockerFixture, ferm_base_path_mock: None):
    spy = mocker.spy(Configuration, "__init__")

    main()

    path = spy.call_args.kwargs["path"]

    with open(path, "r") as f:
        lines = f.read().splitlines()

        assert "@def $BUDDY = (" in lines
        assert "@def $ATLASSIAN = (" in lines
        assert "@def $GOOGLE_CLOUD = (" in lines

        for line in lines:
            if line.startswith("@def") or line == ");":
                continue

            try:
                ipaddress.ip_network(line.strip())
            except ValueError:
                assert False, line.strip()
