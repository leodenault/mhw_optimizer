from functools import reduce

from equipment_combination import EquipmentCombination
from equipment_piece import BodyPart
from progress_bar.progress_bar import ProgressBar


class Combiner:
    def __init__(self, equipment):
        self.equipment_by_body_part = {}

        for body_part in BodyPart:
            self.equipment_by_body_part[body_part] = []

        for piece in equipment:
            self.equipment_by_body_part[piece.body_part].append(piece)

        self.progress_bar = ProgressBar(
            reduce(
                lambda x, y: x * len(y),
                self.equipment_by_body_part.values(),
                1
            ),
            "Creating combinations..."
        )

    def generate_combinations(self):
        combinations = []
        self._generate_combinations({}, combinations)
        return combinations

    def _generate_combinations(
        self,
        current_combination,
        all_combinations
    ):
        current_body_part_value = len(current_combination.keys())
        if current_body_part_value < len(BodyPart):
            current_body_part = BodyPart(current_body_part_value)
            for piece in self.equipment_by_body_part[current_body_part]:
                current_combination[current_body_part] = piece
                self._generate_combinations(
                    current_combination,
                    all_combinations)
                del current_combination[current_body_part]
        else:
            all_combinations.append(
                EquipmentCombination(
                    head_piece=current_combination[BodyPart.HEAD],
                    body_piece=current_combination[BodyPart.BODY],
                    arm_piece=current_combination[BodyPart.ARMS],
                    waist_piece=current_combination[BodyPart.WAIST],
                    leg_piece=current_combination[BodyPart.LEGS],
                    charm=current_combination[BodyPart.CHARM]
                )
            )
            self.progress_bar.increment()
