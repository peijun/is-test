from modules.calc import plus


class TestPlusTest:
    def test__can_plus(self):
        value = plus(-1, -1)
        assert value == -2
