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
    

        