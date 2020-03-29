from functools import reduce

from header_handlers.header_handler import HeaderHandler


def generate_from(equipment_pieces):
    return list(
        map(
            lambda skill_name: SkillHandler(skill_name),
            sorted(
                set(
                    map(
                        lambda skill: skill.name,
                        reduce(
                            list.__add__,
                            map(
                                lambda piece: piece.skills,
                                equipment_pieces
                            )
                        )
                    )
                )
            )
        )
    )


class SkillHandler(HeaderHandler):
    def __init__(self, skill_name):
        self.skill_name = skill_name

    def generate_output(self, combination):
        skill_level = (
            str(combination.total_skill_levels[self.skill_name])
            if self.skill_name in combination.total_skill_levels
            else "0"
        )
        return skill_level

    def name(self):
        return self.skill_name
