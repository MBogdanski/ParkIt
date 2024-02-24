from src.spot.spot import Spot


class TestSpot:

    def test_create_spot_object(self):
        spot_number = 1
        level = 1
        is_available = True
        spot = Spot(spot_number, level, is_available)

        assert spot.id
        assert spot.number == spot_number
        assert spot.level == level
        assert spot.is_available == is_available
