from objson import objson


def test_construction_empty():
    obj = objson({})
    assert "xxx" not in obj


def test_contains(dict_example):
    obj = objson(dict_example)

    assert "title" in obj.glossary
    assert "GlossDiv" in obj.glossary
    assert not "twilight" in obj.glossary
