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

# Your core instruction for the AI model
SYSTEM_INSTRUCTION = (
    "You are a sophisticated and smart business strategist and digital marketing expert. "
    "Your response must be a single, short, one-liner statement. "
    "Comment with the insight of a professional who 'knows his onions'. "
    "When contextually relevant, you may drop a classic, simple business quote or mantra, but keep it brief. "
    "Do not use any emojis, adhere strictly to simple English, and avoid complex grammar or punctuation (use only periods). "
    "The comment must be valuable and directly related to the provided post text, and must not exceed 100 characters."
)

# ----------------------------------------------------
#  REMOVED: FALLBACK_COMMENTS list has been deleted.
# ----------------------------------------------------


def generate_comment(post_text: str, mode="RANDOM"):
    if mode == "RANDOM":
        # Keep the existing static comment logic for RANDOM mode
        # NOTE: This assumes cfg.COMMENTS is defined in config.py
        try:
            return random.choice(cfg.COMMENTS)
        except AttributeError:
            # Handle case where cfg.COMMENTS doesn't exist (good practice)
            print("ERROR: cfg.COMMENTS not found for RANDOM mode.")
            return None 
    
    if mode == "AI" and client:
        # Construct the user prompt, giving the AI the post to comment on
        user_prompt = f"The channel post text is: \"{post_text}\""
        
        try:
            # Call the Gemini API
            response = client.models.generate_content(
                model='gemini-2.5-flash', # A fast and capable model for this task
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    # Setting temperature low encourages more focused, less random output
                    temperature=0.5, 
                )
            )
            
            # The AI might return extra text or formatting; we'll strip it down
            ai_comment = response.text.strip()
            
            if ai_comment:
                print(f"AI-Generated Comment: '{ai_comment}'")
                return ai_comment
            
            # -----------------------------------------------------------------------
            #  CHANGE 1 & 2: If AI returns empty, we log it and return None (skip).
            # -----------------------------------------------------------------------
            print("AI returned an empty comment. Skipping comment.")
            return None
            
        except Exception as e:
            #  CHANGE 3: If API call fails, we log it and return None (skip).
            print(f"Error calling Gemini API: {e}. Skipping comment entirely.")
            return None

    # If the client couldn't be initialized or mode is neither, return None
    print("AI client not available or mode not 'AI'. Skipping comment.")
    return None