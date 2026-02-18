import streamlit as st
import time
from google import genai

def generate_story(prompt):
    if prompt:
        st.toast("Imagining a peaceful setting...")
        time.sleep(2)

        st.toast("Weaving a gentle story...")
        time.sleep(2)

        st.toast("Your story is ready!", icon="📖")
        time.sleep(1)

        st.write(f"### Story Prompt: {prompt}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Write a short, warm, descriptive story inspired by Ruskin Bond's storytelling style.
            Theme: {prompt}
            Use simple language, vivid nature imagery, gentle emotions, and a calm nostalgic tone.
            """
        )
        

        st.write(response.text)


if __name__ == "__main__":
    API_KEY = "AIzaSyAfzGpwJbbZkAmw3PNyrrOXAcQcNvawGnw"   # Replace with your real API key

    # Initialize client
    client = genai.Client(api_key=API_KEY)

    # Title
    st.title("🌿 Storyteller Bot")

    st.write("Enter a theme and enjoy a calm, heartwarming short story.")

    # Input
    prompt = st.chat_input("Enter your story theme...")

    # Generate story
    generate_story(prompt)
