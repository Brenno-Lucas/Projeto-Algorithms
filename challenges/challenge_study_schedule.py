def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    try:
        count = sum(
            1 for start, end in permanence_period
            if start <= target_time <= end
        )
        return count
    except TypeError:
        return None
