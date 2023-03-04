def calculate_time_needed(efficiency_1, efficiency_2, efficiency_3, student_count):
    total_efficiency = efficiency_1 + efficiency_2 + efficiency_3
    time_needed = 0
    while student_count > 0:
        time_needed += 1
        if time_needed % 4 != 0:
            student_count -= total_efficiency
    return f"Time needed: {time_needed}h."

# Example usage:
efficiency_1 = int(input())
efficiency_2 = int(input())
efficiency_3 = int(input())
student_count = int(input())

print(calculate_time_needed(efficiency_1, efficiency_2, efficiency_3, student_count))