from powerdnsadmin.compat import flask_compat

def test_json_roundtrip():
    payload = {"a": 1}
    dumped = flask_compat.dumps(payload)
    assert flask_compat.loads(dumped) == payload
