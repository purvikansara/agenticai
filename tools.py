# tools.py

import openai
from openai import OpenAI
client = OpenAI()

# -------- Simulated Reminder Function --------
def set_reminder(message: str) -> str:
    return f"✅ Reminder set: {message} (simulated)"

# -------- Simulated Appointment Function --------
def book_appointment(time: str) -> str:
    return f"📅 Appointment booked for: {time} (mocked)"

# -------- Static Medical Image Helper --------
def get_static_image_for_term(term: str) -> str:
    term = term.lower()
    if "heart" in term:
        return "https://upload.wikimedia.org/wikipedia/commons/7/7e/Human_Heart_diagram_en.svg"
    if "lungs" in term:
        return "https://upload.wikimedia.org/wikipedia/commons/5/5c/Respiratory_system_complete_en.svg"
    return None

# -------- OpenAI DALL·E Image Generator --------
# def generate_health_image(prompt: str) -> str:
#     response = openai.Image.create(
#         prompt=prompt,
#         n=1,
#         size="256x256"
#     )
#     return response['data'][0]['url']


def generate_health_image(prompt: str) -> str:
    response = openai.images.generate(
        model="dall-e-3",       # or "dall-e-2" if preferred
        prompt=prompt,
        size="256x256",
        n=1
    )
    # Return the image URL
    return response.data[0].url
