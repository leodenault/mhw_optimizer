import sys

from combiner import Combiner
from config.config_importer import ConfigImporter
from scorer import Scorer
import csv_exporter
import csv_importer

args = sys.argv

if len(args) != 4:
    print("""
    Usage:
        python main.py <input_file.csv> <output_file.csv> <config_file.json>
    """)
    exit()

equipment_pieces = csv_importer.import_file(args[1])
config = ConfigImporter(args[3]).load()
combinations = Combiner(equipment_pieces, Scorer(config)).generate_combinations(
    config.result_limit
)

csv_exporter.export_combinations(combinations, args[2])
