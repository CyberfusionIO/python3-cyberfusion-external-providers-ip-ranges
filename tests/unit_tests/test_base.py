from cyberfusion.ExternalProvidersIPRanges import get_ferm_base_path


def test_get_ferm_base_path() -> None:
    assert get_ferm_base_path() == "/etc/ferm/vars.d"
