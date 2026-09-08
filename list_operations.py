participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements
if len(participants) != len(scores):
    print("Error: The participants and scores lists must have the same length.")
    raise SystemExit


# First, display all the current participants with their scores. Use zip()
print("Current participants and their scores:")
for participant, score in zip(participants, scores):
    print(f"- {participant}: {score}")


# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
print("\n--- Register a new participant ---")
new_name = input("Enter the participant's name: ").strip()

if new_name in participants:
    print(f"{new_name} is already registered. Participant was not added.")
elif new_name == "":
    print("Name cannot be empty. Participant was not added.")
else:
    score_input = input(f"Enter the score for {new_name}: ")

    try:
        new_score = float(score_input)
    except ValueError:
        print("Score must be a number. Participant was not added.")
    else:
        if new_score.is_integer():
            new_score = int(new_score)
        if new_score < 0 or new_score > 100:
            print("Score must be between 0 and 100. Participant was not added.")
        else:
            participants.append(new_name)
            scores.append(new_score)
            print(f"{new_name} has been successfully registered with a score of {new_score}.")

                                   

# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
print("\n--- Search for a participant ---")
search_name = input("Enter the participant's name to search: ").strip()

def qualification_status(score):
    if score > distinction_score:
        return "DISTINCTION"
    elif score >= qualification_score:
        return "QUALIFIED"
    else:
        return "NOT QUALIFIED"
    
if search_name in participants:
    index = participants.index(search_name)
    score = scores[index]
    print(f"Name: {search_name}")
    print(f"Score: {score}")
    print(f"Status: {qualification_status(score)}")
else:
    print(f"{search_name} was not found.")



# Display every participant's name, score, and whether they are qualified or not. 
print("\nAll participants and their qualification status:")
for participant, score in zip(participants, scores):
    print(f"- {participant}: {score} ({qualification_status(score)})")






# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
has_distinction = any(score > distinction_score for score in scores)
all_passed = all(score >= 50 for score in scores)

print("\nAny participant with a DISTINCTION?", has_distinction)
print("All participants passed (50 or above)?", all_passed)


# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.
print("\n--- Update a participant's score ---")
update_name = input("Enter the participant's name whose score you want to update: ").strip()

if update_name not in participants:
    print(f"{update_name} was not found. Score was not updated.")
else:
    new_score_input = input(f"Enter the new score for {update_name}: ")

    try:
        updated_score = float(new_score_input)
    except ValueError:
        print("New score must be a number. Score was not updated.")
    else:
        if updated_score.is_integer():
            updated_score = int(updated_score)
        if updated_score < 0 or updated_score > 100:
            print("New score must be between 0 and 100. Score was not updated.")
        else:
            index = participants.index(update_name)
            scores[index] = updated_score
            print(f"{update_name}'s score has been updated to {updated_score}.")



# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
print("\n--- Withdraw a participant ---")
remove_name = input("Enter the participant's name to withdraw: ").strip()

if remove_name not in participants:
    print(f"{remove_name} was not found.")
else:
    index = participants.index(remove_name)
    removed_participant = participants.pop(index)
    removed_score = scores.pop(index)
    print(f"{removed_participant} (score {removed_score}) has been withdrawn.")



# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
scoreboard = sorted(zip(scores, participants), reverse=True)

print("\nScoreboard (highest score first):")
for rank, (score, participant) in enumerate(scoreboard, start=1):
    print(f"#{rank}: {participant} - {score}")




# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)

highest_count = scores.count(highest_score)
lowest_count = scores.count(lowest_score)

statuses = [qualification_status(score) for score in scores]
distinction_count = statuses.count("DISTINCTION")
qualified_count = statuses.count("QUALIFIED")
not_qualified_count = statuses.count("NOT QUALIFIED")



# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above
report = sorted(zip(scores, participants), reverse=True)

print("\n=== FINAL REPORT ===")
for rank, (score, participant) in enumerate(report, start=1):
    print(f"#{rank}: {participant} | Score: {score} | {qualification_status(score)}")

print("\n--- Statistics ---")
print(f"Highest score: {highest_score} (achieved by {highest_count} participant(s))")
print(f"Lowest score: {lowest_score} (achieved by {lowest_count} participant(s))")
print(f"Average score: {average_score:.2f}")
print(f"Participants with DISTINCTION: {distinction_count}")
print(f"Participants QUALIFIED: {qualified_count}")
print(f"Participants NOT QUALIFIED: {not_qualified_count}")
