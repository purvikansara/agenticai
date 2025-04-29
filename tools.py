# tools.py

# tools.py

import openai

def generate_health_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return response['data'][0]['url']

def set_reminder(message):
    return f"Reminder set: {message} (simulated)"

def book_appointment(time):
    return f"Appointment booked for: {time} (mocked)"
