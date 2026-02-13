import random

COMMENTS = [
    "Any telegram channel admin interested in growing their channels using cross promotions? kindly reach out",
    "Any fellow admins in here open for a quick cross-promo? Hit me up if you are.",
    "Looking to grow your Telegram channel? Let's connect for cross-promotion opportunities!",
    "Looking for some CP partners to grow with. Any admins down for a swap?",
    "If there are any admins here doing cross-promotions, let’s connect! DMs are open.",
    "If there are any admins in the comments, let's connect for a cross-promo.",
    "Anyone here manage a channel? Looking for some reliable CP partners.",
    "If you're an admin and want to grow together, let's connect for a CP.",
]

def generate_comment(post_text: str, mode="RANDOM"):
    if mode == "RANDOM":
        return random.choice(COMMENTS)

    # placeholder for AI mode
    return f"(AI simulated comment related to: {post_text[:50]}...)"