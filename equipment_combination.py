class EquipmentCombination:
    __slots__ = [
        "head_piece",
        "body_piece",
        "arm_piece",
        "waist_piece",
        "leg_piece",
        "charm",
        "total_defence",
        "total_decoration_slots_by_level",
        "total_skill_levels",
    ]

    def __init__(
        self,
        head_piece,
        body_piece,
        arm_piece,
        waist_piece,
        leg_piece,
        charm
    ):
        self.head_piece = head_piece
        self.body_piece = body_piece
        self.arm_piece = arm_piece
        self.waist_piece = waist_piece
        self.leg_piece = leg_piece
        self.charm = charm
        self.total_defence = (
            self.head_piece.defence
            + self.body_piece.defence
            + self.arm_piece.defence
            + self.waist_piece.defence
            + self.leg_piece.defence
        )
        self.total_decoration_slots_by_level = [
            self.head_piece.decoration_slots[i]
            + self.body_piece.decoration_slots[i]
            + self.arm_piece.decoration_slots[i]
            + self.waist_piece.decoration_slots[i]
            + self.leg_piece.decoration_slots[i]
            for i in range(1, 5)
        ]
        all_skills = (
            self.head_piece.skills
            + self.body_piece.skills
            + self.arm_piece.skills
            + self.waist_piece.skills
            + self.leg_piece.skills
            + self.charm.skills
        )
        self.total_skill_levels = {
            skillName: 0 for skillName in set(
                map(
                    lambda skill: skill.name, all_skills
                )
            )
        }
        for skill in all_skills:
            self.total_skill_levels[skill.name] = (
                self.total_skill_levels[skill.name] + skill.level
            )

    def __lt__(self, other):
        # Return true by default so that sort operations resulting in a tie
        # simply choose one of the two equipment pieces.
        return True
