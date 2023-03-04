# Read input
leave_time = input()
steps = int(input())
step_time = int(input())

# Convert leave_time to seconds
leave_seconds = sum([int(x)*60**(2-i) for i,x in enumerate(leave_time.split(':'))])

# Calculate arrival time in seconds
total_time = steps * step_time
arrival_seconds = (leave_seconds + total_time) % (24*60*60)

# Convert arrival time to HH:mm:ss format
hours = arrival_seconds // 3600
minutes = (arrival_seconds % 3600) // 60
seconds = arrival_seconds % 60
arrival_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Print result
print(f"Time Arrival: {arrival_time}")
