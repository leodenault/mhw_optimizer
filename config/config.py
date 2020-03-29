class DecorationConfig:
    def __init__(
        self,
        lvl1_decoration_weight,
        lvl2_decoration_weight,
        lvl3_decoration_weight,
        lvl4_decoration_weight,
        num_decorations_weight
    ):
        self.lvl1_decoration_weight = lvl1_decoration_weight
        self.lvl2_decoration_weight = lvl2_decoration_weight
        self.lvl3_decoration_weight = lvl3_decoration_weight
        self.lvl4_decoration_weight = lvl4_decoration_weight
        self.num_decorations_weight = num_decorations_weight


class SkillData:
    def __init__(self, max, weight, penalty):
        self.max = max
        self.weight = weight
        self.penalty = penalty


class SkillConfig:
    def __init__(self, skill_mappings):
        self._skill_mappings = skill_mappings

    def skill_weight(self, skill, skill_level):
        if skill not in self._skill_mappings:
            return 1.0

        skill_data = self._skill_mappings[skill]
        if skill_data.max < skill_level:
            return skill_data.penalty
        else:
            return skill_data.weight


class Config:
    def __init__(
        self,
        decoration_config,
        skill_config,
        defence_weight,
        result_limit
    ):
        self.decoration_config = decoration_config
        self.skill_config = skill_config
        self.defence_weight = defence_weight
        self.result_limit = result_limit
