from src.data_processor import calculate_average_wind_speed


def test_calculate_average_wind_speed():
    velocities = [10.0, 12.0, 14.0]

    result = calculate_average_wind_speed(velocities)

    assert result == 12.0
