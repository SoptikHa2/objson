from objson import objson


def test_del_via_attr(dict_example):
    obj = objson(dict_example)

    assert "title" in obj.glossary
    assert "GlossDiv" in obj.glossary

    del obj.glossary.title

    assert "title" not in obj.glossary
    assert "GlossDiv" in obj.glossary


def test_del_via_item(dict_example):
    obj = objson(dict_example)

    assert "title" in obj.glossary
    assert "GlossDiv" in obj.glossary

    del obj.glossary["title"]

    assert "title" not in obj.glossary
    assert "GlossDiv" in obj.glossary
