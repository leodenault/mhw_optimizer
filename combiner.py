import heapq
from abc import ABCMeta
from abc import abstractmethod
from functools import reduce

from equipment_combination import EquipmentCombination
from equipment_piece import BodyPart
from progress_bar.progress_bar import ProgressBar


class Combiner:
    def __init__(self, equipment, scorer):
        self.equipment_by_body_part = {body_part: [] for body_part in BodyPart}
        self.scorer = scorer

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

    def generate_combinations(self, max_combinations):
        combinations = _MaxSizeHeap(max_combinations)
        self._generate_combinations({}, combinations)
        return list(
            map(
                lambda combination: combination[1],
                sorted(
                    combinations.heap,
                    key=lambda combination: combination[0],
                    reverse=True
                )
            )
        )

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
            combination = EquipmentCombination(
                head_piece=current_combination[BodyPart.HEAD],
                body_piece=current_combination[BodyPart.BODY],
                arm_piece=current_combination[BodyPart.ARMS],
                waist_piece=current_combination[BodyPart.WAIST],
                leg_piece=current_combination[BodyPart.LEGS],
                charm=current_combination[BodyPart.CHARM])
            score = self.scorer.score(combination)
            all_combinations.push((score, combination))
            self.progress_bar.increment()


class _MaxSizeHeap:
    def __init__(self, max_size):
        self.heap = []
        self.push_strategy = _NotYetAtMaxStrategy(max_size, self, self.heap)

    def push(self, combination):
        self.push_strategy.push(combination)


class _HeapPushStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, combination):
        pass


class _NotYetAtMaxStrategy(_HeapPushStrategy):
    def __init__(self, max_size, max_size_heap, heap):
        self.max_size_heap = max_size_heap
        self.max_size = max_size
        self.heap = heap

    def push(self, combination):
        if len(self.heap) < self.max_size:
            heapq.heappush(self.heap, combination)
            return

        new_strategy = _FixedSizeHeap(self.heap)
        self.max_size_heap.push_strategy = new_strategy
        new_strategy.push(combination)


class _FixedSizeHeap(_HeapPushStrategy):
    def __init__(self, heap):
        self.heap = heap

    def push(self, combination):
        heapq.heappushpop(self.heap, combination)
