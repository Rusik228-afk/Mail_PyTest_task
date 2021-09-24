import pytest


class TestTuple:
    def test_equality(self):
        t1 = (-1000, 'string', False)
        t2 = (False, 'string', -1000)
        assert t1 != t2

    @pytest.mark.parametrize(
        'tuple_contents, expected',
        [
            ([True, ['l', 'i', 's', 't'], 2.71], (True, ['l', 'i', 's', 't'], 2.71)),
            ([False, True, False], (0, 1, 0))
        ]
    )
    def test_creation(self, tuple_contents, expected):
        assert tuple(tuple_contents) == expected

    def test_assignment(self):
        t = tuple([100, 200, 300])
        try:
            t[1] = [True, True, True]
        except TypeError:
            assert t[1] == 200 # assignment was not 
    

class TestDict:
    def test_equality(self):
        d1 = {
            'a': 100500,
            True: [.2, .75, .99]
        }
        d2 = {
            True: [.2, .75, .99],
            'a': 100500
        }
        assert d1 == d2

    @pytest.mark.parametrize(
        'dict_contents, expected',
        [
            (zip(['key1', 'key2', 'key3'], range(3)), {'key1': 0, 'key2': 1, 'key3': 2}),
            ([('galaktionov', 'english'*2), ('gladyshev', 'oscilloscope')], {'gladyshev': 'oscilloscope', 'galaktionov': 'englishenglish'})
        ]
    )
    def test_creation(self, dict_contents, expected):
        assert dict(dict_contents) == expected

    def test_comparison(self):
        d = {
            'key': ['v', 'a', 'l', 'u', 'e']
        }
        try:
            assert d < {'key': ['v', 'a', 'l', 'u', 'e']}
        except TypeError:
            pass        