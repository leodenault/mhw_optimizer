class Scorer:
    def __init__(self, config):
        self.config = config

    def score(self, combination):
        deco_slots = combination.total_decoration_slots_by_level
        deco_config = self.config.decoration_config
        return (
            deco_slots[0] * deco_config.lvl1_decoration_weight
            + deco_slots[1] * deco_config.lvl2_decoration_weight
            + deco_slots[2] * deco_config.lvl3_decoration_weight
            + deco_slots[3] * deco_config.lvl4_decoration_weight
            + sum(deco_slots) * deco_config.num_decorations_weight
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
