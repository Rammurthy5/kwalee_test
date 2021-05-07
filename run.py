# standard imports
from pathlib import Path

# local imports
from src.file_handler import process_player_data


if __name__ == "__main__":
    input_file = Path.joinpath(Path(__file__).parents[0], "Tools Programmer Test (Analytics) sorted_exam_data.csv")
    print("Please refer the files {0} present in {1}".format(process_player_data(input_file), Path(__file__).parents[0]))
