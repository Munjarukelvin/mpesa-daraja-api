from services.mpesa import encoder

def test_encoder() -> None:
    base64_encoded_string = encoder()
    assert type(base64_encoded_string) == str
    assert len(base64_encoded_string) == 112