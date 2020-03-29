from equipment_piece import ArmourPiece, BodyPart, Charm
from skill import Skill


def import_file(file_location):
    with open(file_location) as csv_file:
        equipment_pieces = []
        try:
            data_lines = csv_file.readlines()[1:]
            for line_num, line in enumerate(data_lines):
                cells = line.split(",")

                if len(cells) != 11:
                    raise IOError("""
                        Expected to find 11 cells per line.
                        The cells should be ordered by:
                        
                        Equipment Piece Name
                        Skill 1 Name
                        Skill 1 Level
                        Skill 2 Name
                        Skill 2 Level
                        Num Lvl 1 Deco Slots
                        Num Lvl 2 Deco Slots
                        Num Lvl 3 Deco Slots
                        Num Lvl 4 Deco Slots
                        Body Part
                        Base Defence
                        
                        Offending line:
                        {0}
                        """.format(line))

                name = cells[0]
                body_part = _parse_body_part(cells[9])
                skills = _parse_skills(
                    skill_1_name=cells[1],
                    skill_1_level=cells[2],
                    skill_2_name=cells[3],
                    skill_2_level=cells[4]
                )
                equipment_pieces.append(
                    _parse_equipment(name, body_part, skills, cells)
                )
            return equipment_pieces
        except ValueError as err:
            print("Error parsing line {0} in CSV file.".format(line_num + 2))
            raise err


def _parse_body_part(name):
    uppercase_name = name.upper()
    for body_part in BodyPart:
        if uppercase_name == body_part.name:
            return body_part

    raise ValueError("'" + name + "' is not a valid body part.")


def _parse_skills(
    skill_1_name,
    skill_1_level,
    skill_2_name,
    skill_2_level
):
    skills = [Skill(skill_1_name, int(skill_1_level))]
    if skill_2_name != "":
        skills.append(Skill(skill_2_name, int(skill_2_level)))
    return skills


def _parse_equipment(name, body_part, skills, cells):
    if body_part == BodyPart.CHARM:
        return Charm(name, skills)
    else:
        defence = int(cells[10])
        decorations = _parse_decorations(
            num_lvl_1_deco_slots=cells[5],
            num_lvl_2_deco_slots=cells[6],
            num_lvl_3_deco_slots=cells[7],
            num_lvl_4_deco_slots=cells[8]
        )
        return ArmourPiece(
            name,
            body_part,
            defence,
            skills,
            decorations
        )


def _parse_decorations(
    num_lvl_1_deco_slots,
    num_lvl_2_deco_slots,
    num_lvl_3_deco_slots,
    num_lvl_4_deco_slots
):
    return {
        1: int(num_lvl_1_deco_slots),
        2: int(num_lvl_2_deco_slots),
        3: int(num_lvl_3_deco_slots),
        4: int(num_lvl_4_deco_slots)
    }
