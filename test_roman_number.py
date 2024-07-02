from roman_funcs import to_roman

def test_romano_simples():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(500) == "D"
    assert to_roman(1000) == "M"

def test_1_a_9():
    assert to_roman(1) == "I"
    assert to_roman(2) == "II"
    assert to_roman(3) == "III"
    assert to_roman(4) == "IV"
    assert to_roman(5) == "V"
    assert to_roman(6) == "VI"
    assert to_roman(7) == "VII"
    assert to_roman(8) == "VIII"
    assert to_roman(9) == "IX"

def test_11_a_20():
    assert to_roman(11) == "XI"
    assert to_roman(12) == "XII"
    assert to_roman(13) == "XIII"
    assert to_roman(14) == "XIV"
    assert to_roman(15) == "XV"
    assert to_roman(16) == "XVI"
    assert to_roman(17) == "XVII"
    assert to_roman(18) == "XVIII"
    assert to_roman(19) == "XIX"
    assert to_roman(20) == "XX"

def test_21_a_30():
    assert to_roman(21) == "XXI"
    assert to_roman(22) == "XXII"
    assert to_roman(23) == "XXIII"
    assert to_roman(24) == "XXIV"
    assert to_roman(25) == "XXV"
    assert to_roman(26) == "XXVI"
    assert to_roman(27) == "XXVII"
    assert to_roman(28) == "XXVIII"
    assert to_roman(29) == "XXIX"
    assert to_roman(30) == "XXX"

def test_31_a_39():
    assert to_roman(31) == "XXXI"
    assert to_roman(32) == "XXXII"
    assert to_roman(33) == "XXXIII"
    assert to_roman(34) == "XXXIV"
    assert to_roman(35) == "XXXV"
    assert to_roman(36) == "XXXVI"
    assert to_roman(37) == "XXXVII"
    assert to_roman(38) == "XXXVIII"
    assert to_roman(39) == "XXXIX"  

def test_40_a_49():
    assert to_roman(40) == "XL"
    assert to_roman(41) == "XLI"
    assert to_roman(42) == "XLII"
    assert to_roman(43) == "XLIII"
    assert to_roman(44) == "XLIV"
    assert to_roman(45) == "XLV"
    assert to_roman(46) == "XLVI"
    assert to_roman(47) == "XLVII"
    assert to_roman(48) == "XLVIII"
    assert to_roman(49) == "XLIX" 