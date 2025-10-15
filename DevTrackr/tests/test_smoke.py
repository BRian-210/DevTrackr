def test_import():
    import devtrackr
    assert hasattr(devtrackr, '__version__')
