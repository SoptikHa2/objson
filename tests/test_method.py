from objson import objson


def test_call_keys_on_dict(dict_example):
    obj = objson(dict_example)

    assert list(obj.glossary.keys()) == ["title", "GlossDiv"]
