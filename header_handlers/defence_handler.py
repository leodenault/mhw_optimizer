from header_handlers.header_handler import HeaderHandler


class DefenceHandler(HeaderHandler):

    def generate_output(self, combination):
        return str(combination.total_defence)

    def name(self):
        return "Defence"
