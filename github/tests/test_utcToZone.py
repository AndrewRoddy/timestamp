from github import utcToZone

def test_utcToZone_empty():
    # checks for empty time zone (should default to EST)
    assert utcToZone(date="2026-03-06T04:10:12Z") == "2026-03-05 23:10:12"
    assert utcToZone("America/New_York", "2026-03-06T04:10:12Z") == "2026-03-05 23:10:12"
    
def test_utcToZone_daylight_savings():
    # checks for daylight savings time
    assert utcToZone("America/New_York", "2026-03-07T04:10:12Z") == "2026-03-06 23:10:12"
    assert utcToZone("America/New_York", "2026-03-08T04:10:12Z") == "2026-03-07 23:10:12"
    
    # it would switch here
    assert utcToZone("America/New_York", "2026-03-09T03:10:12Z") == "2026-03-08 23:10:12"
    assert utcToZone("America/New_York", "2026-03-10T03:10:12Z") == "2026-03-09 23:10:12"
