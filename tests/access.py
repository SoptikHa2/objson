from objson import objson


def test_access_simple():
    obj = objson({"a": "foo", "b": 4, "c": [1, 2, 3]})

    assert obj.a == "foo"
    assert obj.b == 4
    assert obj.c == [1, 2, 3]


def test_access_nested(dict_example):
    obj = objson(dict_example)

    assert obj.glossary.title == "example glossary"
    assert obj.glossary.GlossDiv.title == "S"
    assert obj.glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso == [
        "GML",
        "XML",
    ]
    assert obj.glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso[0] == "GML"
