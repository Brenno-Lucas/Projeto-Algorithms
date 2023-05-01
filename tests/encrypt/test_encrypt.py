from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(23, "ABCBA")
    assert encrypt_message("ABCBA", 23) == "ABCBA"
    assert encrypt_message("ABCBA", 2) == "ABC_BA"
    assert encrypt_message("ABCA", 3) == "CBA_A"
