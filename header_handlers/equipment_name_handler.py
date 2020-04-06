from header_handlers.header_handler import HeaderHandler


class EquipmentNameHandler(HeaderHandler):
    def __init__(self, body_part_name, equipment_name_fetcher):
        self.body_part_name = body_part_name
        self.fetch_equipment_name = equipment_name_fetcher

    def generate_output(self, combination):
        return self.fetch_equipment_name(combination)

    def name(self):
        return self.body_part_name
