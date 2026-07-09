# ai_assistant.py

import openai
from config import OPENAI_API_KEY, DIFFICULTY

openai.api_key = OPENAI_API_KEY

def get_clue_openai(correct_solution, eliminated=[]):
    suspect, location, weapon = correct_solution

    base_prompt = f"""
    You are Clarence, an extremely condescending, annoyingly verbose AI assistant helping a human solve a murder.
    The murder took place in Hollywood. You know the correct answer: the killer is {suspect}, the location is {location}, and the weapon is {weapon}.

    The player is desperately trying to solve it. Based on the difficulty '{DIFFICULTY}', generate one clue that:
    - Provides partial information (e.g., rules out one suspect, location, or weapon, or links two together).
    - Is phrased in a long-winded, smug, overly intellectual, slightly rude way.
    - Should *still be helpful*, even if buried under sarcasm.

    Previous eliminated guesses (for reference): {eliminated if eliminated else 'None'}.

    Return ONLY the AI’s obnoxious clue text.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use 'gpt-3.5-turbo' if preferred
        messages=[{"role": "user", "content": base_prompt}],
        temperature=1.0,
        max_tokens=150
    )

    return response['choices'][0]['message']['content'].strip()
