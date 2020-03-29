from enum import Enum


class BodyPart(Enum):
    HEAD = 0
    BODY = 1
    ARMS = 2
    WAIST = 3
    LEGS = 4
    CHARM = 5


class EquipmentPiece:
    def __init__(self, name, body_part, skills):
        self.name = name
        self.body_part = body_part
        self.skills = skills


class ArmourPiece(EquipmentPiece):
    def __init__(self, name, body_part, defence, skills, decoration_slots):
        EquipmentPiece.__init__(self, name, body_part, skills)
        self.defence = defence
        self.decoration_slots = decoration_slots


class Charm(EquipmentPiece):
    def __init__(self, name, skills):
        EquipmentPiece.__init__(self, name, BodyPart.CHARM, skills)
