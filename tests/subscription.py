from objson import objson


def test_read_sub(dict_example):
    obj = objson(dict_example)

    assert obj.glossary["GlossDiv"].GlossList["GlossEntry"]["ID"] == "SGML"


def test_write_sub():
    obj = objson({})

    obj["x"] = 8

    assert "x" in obj and obj.x == 8 and obj["x"] == 8
