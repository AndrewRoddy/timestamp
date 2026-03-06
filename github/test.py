from . import func

def test_func():
    env = getEnv()
    assert func(1) == 2
    utcToZone(env, "2026-03-05T23:14:15Z")