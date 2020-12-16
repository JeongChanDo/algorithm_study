def convert_dec_to_any_base_rec(number, base):
    convert_string = "0123456789ABCDEF"
    if number < base:
        return convert_string[number]
    return convert_dec_to_any_base_rec(number // base, base) \
        + convert_string[number % base]



def test_convert_dec_to_any_base_rec():
    number = 9
    base = 2
    assert(convert_dec_to_any_base_rec(number, base) == "1001")
    print("test passed")

if __name__ == "__main__":
    test_convert_dec_to_any_base_rec()