import glob

from utils.file_handler import read_photo_collection
from utils.create_slideshow import create_optimal_slideshow
from utils.scoring_functions import get_slides_score

input_path = 'input_files'
output_path = 'output_files'
files = sorted(glob.glob(input_path + '/*.txt'))
problems = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


def main():
    # Create the slideshow
    photos = read_photo_collection(files[problems.get('e')])

    # Sort photos
    slideshow = create_optimal_slideshow(photos, 1000000, 2)

    score = get_slides_score(slideshow)
    print('Final score = {0}'.format(score))

    # Write the slideshow to file
    # write_output(file, slides)


if __name__ == '__main__':
    main()

