from progress_bar.progress_bar import ProgressBar


class Filter:
    def __init__(self, config, combinations):
        self.config = config
        self.combinations = combinations
        self.progress_bar = ProgressBar(
            len(combinations),
            "Scoring and filtering combinations..."
        )

    def filter(self):
        return list(
            map(
                lambda scored_combination: scored_combination[0],
                sorted(
                    map(
                        lambda combination: (
                            combination,
                            self._generate_score(combination)
                        ),
                        self.combinations
                    ),
                    key=lambda scored_combination: scored_combination[1],
                    reverse=True
                )[:self.config.result_limit]
            )
        )

    def _generate_score(self, combination):
        deco_slots = combination.total_decoration_slots_by_level
        deco_config = self.config.decoration_config
        self.progress_bar.increment()
        return (
            deco_slots[1] * deco_config.lvl1_decoration_weight
            + deco_slots[2] * deco_config.lvl2_decoration_weight
            + deco_slots[3] * deco_config.lvl3_decoration_weight
            + deco_slots[4] * deco_config.lvl4_decoration_weight
            + sum(deco_slots.values()) * deco_config.num_decorations_weight
            + self._generate_skills_score(combination)
            + combination.total_defence * self.config.defence_weight
        )

    def _generate_skills_score(self, combination):
        skill_levels = combination.total_skill_levels
        skill_config = self.config.skill_config
        return sum(
            map(
                lambda kv: kv[1] * skill_config.skill_weight(kv[0], kv[1]),
                skill_levels.items()
            )
        )
