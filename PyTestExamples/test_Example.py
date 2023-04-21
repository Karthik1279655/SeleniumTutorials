import pytest

class Test:

    @pytest.fixture()
    def comedy_series(self):
        return [
            ("The Office", 2005, 8.8),
            ("Scrubs", 2001, 8.4),
            ("IT Crowd", 2006, 8.5),
            ("Parks and Recreation", 2009, 8.6),
            ("Seinfeld", 1989, 8.9),
        ]

    def test_highly_rated(self, comedy_series):
        assert comedy_series[1] == 'Seinfeld'
