from header_handlers.header_handler import HeaderHandler


class DecorationHandler(HeaderHandler):
    def __init__(self, level):
        self.level = level

    def generate_output(self, combination):
        return str(combination.total_decoration_slots_by_level[self.level])

    def name(self):
        return "Lvl {0} Decoration Slot".format(self.level + 1)
