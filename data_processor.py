def calculate_average_wind_speed(velocities):
    if not velocities:
        raise ValueError("Velocity data cannot be empty.")

    return sum(velocities) / len(velocities)
