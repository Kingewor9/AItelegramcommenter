import random
import config as cfg
from google import genai
from google.genai import types
import sys # <--for clean exits if needed


# Initialize the Gemini Client globally
# It will automatically use the GEMINI_API_KEY from config.py
try:
    client = genai.Client(api_key=cfg.GEMINI_API_KEY)
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    client = None

# Core instruction for extracting GIF search keywords
SYSTEM_INSTRUCTION = (
    "You are an assistant that extracts keywords for a GIF search from sports-related Telegram posts. "
    "Identify the most prominent football player, coach, manager, or event mentioned in the post. "
    "Return ONLY their name or a concise action (e.g., 'Bruno Fernandes celebration', 'Bukayo Saka', 'Erik ten Hag'). "
    "Do not include any other text, punctuation, or conversational filler. "
    "If no relevant person, team, or clear visually-representable event can be identified, return an empty string."
)

def generate_comment(post_text: str, mode="RANDOM"):
    if mode == "RANDOM":
        # Keep the existing static comment logic for RANDOM mode
        # NOTE: This assumes cfg.COMMENTS is defined in config.py
        try:
            return random.choice(cfg.COMMENTS)
        except AttributeError:
            print("ERROR: cfg.COMMENTS not found for RANDOM mode.")
            return None 
    
    if mode == "AI" and client:
        # Construct the user prompt
        user_prompt = f"The channel post text is: \"{post_text}\""
        
        try:
            # Call the Gemini API
            response = client.models.generate_content(
                model='gemini-2.5-flash', # A fast and capable model for this task
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    # Setting temperature low encourages more focused, less random output
                    temperature=0.3, 
                )
            )
            
            # Extract the raw keyword
            keyword = response.text.strip()
            
            if keyword:
                print(f"AI-Extracted GIF Keyword: '{keyword}'")
                return keyword
            
            print("AI returned an empty extracted keyword. Skipping GIF.")
            return None
            
        except Exception as e:
            print(f"Error calling Gemini API: {e}. Skipping entirely.")
            return None

    # If the client couldn't be initialized or mode is neither, return None
    print("AI client not available or mode not 'AI'. Skipping comment.")
    return None