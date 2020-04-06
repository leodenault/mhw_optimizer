from equipment_piece import BodyPart
from header_handlers import skill_handler
from header_handlers.decoration_handler import DecorationHandler
from header_handlers.defence_handler import DefenceHandler
from header_handlers.equipment_name_handler import EquipmentNameHandler
from progress_bar.progress_bar import ProgressBar

_generate_header_handlers = (
    lambda equipment_pieces:
    ([
         EquipmentNameHandler(
             BodyPart.HEAD.name,
             lambda combination: combination.head_piece.name
         ),
         EquipmentNameHandler(
             BodyPart.BODY.name,
             lambda combination: combination.body_piece.name
         ),
         EquipmentNameHandler(
             BodyPart.ARMS.name,
             lambda combination: combination.arm_piece.name
         ),
         EquipmentNameHandler(
             BodyPart.WAIST.name,
             lambda combination: combination.waist_piece.name
         ),
         EquipmentNameHandler(
             BodyPart.LEGS.name,
             lambda combination: combination.leg_piece.name
         ),
         EquipmentNameHandler(
             BodyPart.CHARM.name,
             lambda combination: combination.charm.name
         )
     ]
     + skill_handler.generate_from(equipment_pieces)
     + [
         DecorationHandler(level=0),
         DecorationHandler(level=1),
         DecorationHandler(level=2),
         DecorationHandler(level=3),
         DefenceHandler(),
     ])
)


def export_combinations(combinations, file_name):
    equipment_pieces = set()
    for combination in combinations:
        equipment_pieces.add(combination.head_piece)
        equipment_pieces.add(combination.body_piece)
        equipment_pieces.add(combination.arm_piece)
        equipment_pieces.add(combination.waist_piece)
        equipment_pieces.add(combination.leg_piece)
        equipment_pieces.add(combination.charm)
    header_handlers = _generate_header_handlers(equipment_pieces)
    headers = [_capitalize_words(x.name()) for x in header_handlers]

    file_contents = [",".join(headers) + "\n"]
    progress_bar = ProgressBar(len(combinations), "Exporting combinations...")
    for index, combination in enumerate(combinations, start=1):
        line_contents = []
        for handler in header_handlers:
            line_contents.append(handler.generate_output(combination))
        file_contents.append(",".join(line_contents) + "\n")
        progress_bar.increment()

    with open(file_name, "w") as output_file:
        output_file.writelines(file_contents)
    print("\nDone!")


def _capitalize_words(chars):
    return " ".join(map(lambda word: word.capitalize(), chars.split(" ")))
