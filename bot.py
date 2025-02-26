import berserk
import os

# Connect to Lichess API
session = berserk.TokenSession(os.getenv("LICHESS_API_TOKEN"))
client = berserk.Client(session)

# Listen for events
for event in client.bots.stream_incoming_events():
    print(event)  # Debugging - shows events in logs
    if event.get("type") == "challenge":
        challenge_id = event["challenge"]["id"]
        client.bots.accept_challenge(challenge_id)
