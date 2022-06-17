
from services.mpesa import authenticate

def test_authenticate() -> None:
    access_token = authenticate()
    assert type(access_token) == str
    assert len(access_token) == 28