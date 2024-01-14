import my_patches as mp


def test_password_strange():
    assert mp.password_strange('') == 'Too Weak'
    assert mp.password_strange('1234567') == 'Too Weak'
    assert mp.password_strange('qwertyu') == 'Too Weak'
    assert mp.password_strange('QWERTYU') == 'Too Weak'
    assert mp.password_strange('QWErt12') == 'Too Weak'
    assert mp.password_strange('12345678') == 'Weak'
    assert mp.password_strange('12345678901112') == 'Weak'
    assert mp.password_strange('QWERTYUI') == 'Weak'
    assert mp.password_strange('QWERTYUIOPAS') == 'Weak'
    assert mp.password_strange('qwertyui') == 'Weak'
    assert mp.password_strange('qwertyuiopas') == 'Weak'
    assert mp.password_strange('1234qwer') == 'Good'
    assert mp.password_strange('1234qwerty') == 'Good'
    assert mp.password_strange('1234QWER') == 'Good'
    assert mp.password_strange('1234QWERTY') == 'Good'
    assert mp.password_strange('qwerQWER') == 'Good'
    assert mp.password_strange('qwertyQWER') == 'Good'
    assert mp.password_strange('@#$%^QWER') == 'Good'
    assert mp.password_strange('@#$%^qwer') == 'Good'
    assert mp.password_strange('@#$%12345') == 'Good'
    assert mp.password_strange('123qwerQWER') == 'Very Good'
    assert mp.password_strange('123435qQ') == 'Very Good'
    assert mp.password_strange('qwertyuiQ1') == 'Very Good'
    assert mp.password_strange('QWERTYUIq1') == 'Very Good'
    assert mp.password_strange('QWERTYUIq#$') == 'Very Good'
    assert mp.password_strange('QWERTYUI23#$') == 'Very Good'
    assert mp.password_strange('qwertyui23#$') == 'Very Good'
    assert mp.password_strange('QWERTYUI1q&') == 'Super Very Good'
    assert mp.password_strange('qwertyui1Q&') == 'Super Very Good'
    print('+ test_password_strange - Complete')


def test_coalesce():
    assert mp.coalesce(' ') == ' '
    assert mp.coalesce('') is None
    assert mp.coalesce(None) is None
    assert mp.coalesce(None, '2ndArgs') == '2ndArgs'
    assert mp.coalesce('', '2ndArgs') == '2ndArgs'
    print('+ test_coalesce - Complete')


if __name__ == '__main__':
    test_password_strange()
    test_coalesce()
