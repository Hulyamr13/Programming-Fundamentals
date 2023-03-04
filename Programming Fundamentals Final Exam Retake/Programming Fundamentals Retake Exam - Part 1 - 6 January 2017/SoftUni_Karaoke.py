participants = input().split(", ")
songs = input().split(", ")

participants_dict = {p: set() for p in participants}
songs_dict = {s: set() for s in songs}

while True:
    performance = input()
    if performance == "dawn":
        break
    participant, song, award = performance.split(", ")
    if participant in participants and song in songs:
        participants_dict[participant].add(award)
        songs_dict[song].add(award)

participants_awards = [(p, len(participants_dict[p]), sorted(participants_dict[p]))
                       for p in participants if participants_dict[p]]
participants_awards.sort(key=lambda x: (-x[1], x[0]))

if participants_awards:
    for p, count, awards in participants_awards:
        print(f"{p}: {count} awards")
        for award in awards:
            print(f"--{award}")
else:
    print("No awards")
