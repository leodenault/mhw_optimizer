from equipment_piece import BodyPart
from header_handlers.equipment_name_handler import EquipmentNameHandler
from header_handlers.decoration_handler import DecorationHandler
from header_handlers.defence_handler import DefenceHandler
from header_handlers import skill_handler
from progress_bar.progress_bar import ProgressBar

_generate_header_handlers = (
    lambda equipment_pieces:
    ([
         EquipmentNameHandler(BodyPart.HEAD),
         EquipmentNameHandler(BodyPart.BODY),
         EquipmentNameHandler(BodyPart.ARMS),
         EquipmentNameHandler(BodyPart.WAIST),
         EquipmentNameHandler(BodyPart.LEGS),
         EquipmentNameHandler(BodyPart.CHARM)
     ]
     + skill_handler.generate_from(equipment_pieces)
     + [
         DecorationHandler(level=1),
         DecorationHandler(level=2),
         DecorationHandler(level=3),
         DecorationHandler(level=4),
         DefenceHandler(),
     ])
)


def export_combinations(equipment_pieces, combinations, file_name):
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
