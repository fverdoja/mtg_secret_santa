import random
from typing import Sequence

import yaml


def secret_santa(
    color_combinations: Sequence[str],
    deck_archetypes: Sequence[str],
    participants: Sequence[str],
) -> None:
    num_participants = len(participants)
    participants_sorted = random.sample(participants, num_participants)
    selected_color_combos = random.sample(color_combinations, num_participants * 2)
    selected_deck_archetypes = random.sample(deck_archetypes, num_participants * 2)

    for i, participant in enumerate(participants_sorted):
        giftee = participants_sorted[(i + 1) % num_participants]
        first_color_combo = selected_color_combos[(i * 2)]
        second_color_combo = selected_color_combos[(i * 2 + 1)]
        first_deck_archetype = selected_deck_archetypes[(i * 2)]
        second_deck_archetype = selected_deck_archetypes[(i * 2 + 1)]
        # Output the result
        print(
            f"{participant}: your Giftee is **{giftee}**!\nYou need to build a "
            "deck under 25€ choosing one from these two color combinations: **"
            f"{first_color_combo}** or **{second_color_combo}** "
            f"and one from these two deck archetypes: **{first_deck_archetype}** "
            f"or **{second_deck_archetype}**."
        )


# Run the script multiple times to get different combinations
if __name__ == "__main__":
    with open("data.yaml", "r") as stream:
        out = yaml.load(stream, Loader=yaml.Loader)
    color_combinations = out["color_combinations"]
    deck_archetypes = out["deck_archetypes"]
    participants = out["participants"]
    secret_santa(color_combinations, deck_archetypes, participants)
