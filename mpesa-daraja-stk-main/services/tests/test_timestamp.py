from services.mpesa import time_stamp

def test_time_stamp() -> None:
    timestamp = time_stamp()
    assert type(timestamp) == str
    assert len(timestamp) == 14
    