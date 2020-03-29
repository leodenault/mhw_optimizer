from header_handlers.header_handler import HeaderHandler


class EquipmentNameHandler(HeaderHandler):
    def __init__(self, body_part):
        self.body_part = body_part

    def generate_output(self, combination):
        return combination.equipment[self.body_part].name

    def name(self):
        return self.body_part.name
