from donnes_des_sous.banque import donnes_des_sous


def test_donne_des_sous():
    result = donnes_des_sous(12, 11)
    assert result == 23


def test_donne_beaucoup_des_sous():
    result = donnes_des_sous(212, 11)
    assert result == 243