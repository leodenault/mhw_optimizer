import math


class ProgressBar:
    def __init__(self, total, info_text):
        self.total = total
        self.info_text = info_text
        self.current_amount = 0
        self.last_printed_length = 0
        self.current_percentage = -1

    def increment(self):
        self.current_amount += 1
        self._print()

    def _print(self):
        if self.current_amount >= self.total:
            output_text = "{0} Done!".format(self.info_text)
            print(
                output_text.ljust(self.last_printed_length),
                flush=True
            )
            return

        new_percentage = math.floor(100 * self.current_amount / self.total)
        if self.current_percentage == new_percentage:
            return

        self.current_percentage = new_percentage
        output_text = "{0} {1}% of a total of {2:,}".format(
            self.info_text,
            self.current_percentage,
            self.total
        )
        print(
            output_text.ljust(self.last_printed_length),
            end="\r",
            flush=True
        )
        self.last_printed_length = len(output_text)
