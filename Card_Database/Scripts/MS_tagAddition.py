import pandas as pd
import numpy as np
import re

# 1. Read the CSV
df = pd.read_csv("MarvelSnapCardsList_Main.csv")

# 2. Prepare a lookup mapping keyword → Tag
#    (Lowercase both the key and the ability text for matching.)
tags_map = {
    "on reveal": "On Reveal",
    "ongoing": "Ongoing",
    "discard": "Discard",
    "destroy": "Destroy",
    "banish": "Banish",
    "add card to hand": "Add Card to Hand",
    "increase power": "Increase Power",
    "afflict": "Afflict",
    "card draw": "Card Draw",
    "duplicate": "Duplicate Card",
    "decrease cost": "Decrease Cost",
    "activate": "Activate",
    "add card to location": "Add Card to Location",
    "game start": "Game Start",
    "return to hand": "Return to Hand",
    "end of turn": "End of Turn",
    "increase cost": "Increase Cost",
    "move": "Move",
    "add card at location": "Add Card At Location",
    "set cost": "Set Cost",
    "skill": "Skill",
    "transform": "Transform",
    "add card to deck": "Add Card to Deck",
    "add card": "Add Card",
    "change location": "Change Location",
    "copy text": "Copy Text",
    "game end": "Game End",
    "merge": "Merge",
    "double power": "Double Power",
    "max energy": "Max Energy",
    "remove text": "Remove Text",
    "play at location restriction": "Play at Location Restriction",
    "set power": "Set Power",
    "start in hand": "Start in Hand",
    "steal power": "Steal Power",
    "switch sides": "Switch Sides",
    "trigger": "Trigger"
}

def get_tags_for_ability(ability_text):
    # Handle NaN/empty string/explicit "no ability"
    if pd.isna(ability_text) or ability_text.strip().lower() in ["", "no ability"]:
        return "No Ability"
    
    lower_ability = str(ability_text).strip().lower()
    
    matched_tags = set()
    
    for keyword, tag in tags_map.items():
        # Use word boundaries to prevent partial matches:
        # e.g., "move" won't match "remove".
        # Also use `re.escape` to ensure special chars in `keyword` are handled safely.
        pattern = re.escape(keyword)
        if re.search(pattern, lower_ability):
            matched_tags.add(tag)

    # Remove duplicates, then join as a comma-separated string
    #matched_tags = list(set(matched_tags))

    if len(matched_tags) == 0:
        # If no known keywords matched, you might decide to mark as "No Ability",
        return "No Ability"    
        
    return ", ".join(sorted(matched_tags)) if matched_tags else ""

# 3. Assign Tags only for rows where Series != "Unreleased".
# Skip "Unreleased" completely, leaving those tags blank:    
df["Tags"] = df["Tags"].astype("string")
mask_released = df["Series"] != "Unreleased"
df.loc[mask_released, "Tags"] = df.loc[mask_released, "Card Ability"].apply(get_tags_for_ability)

# 4. Write the updated DataFrame out to a new CSV
df.to_csv("MarvelSnapCardsList_Main.csv", index=False)