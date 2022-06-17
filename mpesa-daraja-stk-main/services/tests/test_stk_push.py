from services.mpesa import stk_push
from pytest import MonkeyPatch

def test_stk_push(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv('BUSINESS_CODE', '174379')
    monkeypatch.setenv('PASSKEY', 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919')
    monkeypatch.setenv('PHONE_NUMBER', '254708374149')
    assert stk_push() == 'Success. Request accepted for processing'