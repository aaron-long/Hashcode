import itertools
import random

from slide_objects import Slide
from utils.scoring_functions import get_interest_factors


def create_optimal_slideshow(photos):
    """
    Sort a collection of photos to create an optimal slideshow.

    Args:
        photos (list[slide_objects.Photo]): List of photos to be sorted

    Returns:
        slideshow (list[Slide]): A list of slides forming a slideshow
    """
    # Currently sparse but would like to allow for different algorithm selections
    slideshow = combine_photos(photos)

    return slideshow


def combine_photos(photos):
    """

    Args:
        photos (list[Photo]): List of photo objects

    Returns:

    """
    slideshow = []

    v_photos = list(filter(lambda x: x.orientation == 'V', photos))
    h_photos = list(filter(lambda x: x.orientation == 'H', photos))

    collection_type = get_collection_type(v_photos, h_photos)
    print('Collection type: {0}'.format(collection_type))

    seed_photo = random.choice(h_photos)
    slideshow.append(Slide(seed_photo))

    for _ in range(1000):
        if _ % 100 == 0:
            print('At iter: {0}'.format(_))

        current_slide = slideshow[-1]

        if current_slide.orientation == 'H':
            # First try to match a V combination
            for photo1, photo2 in itertools.combinations(v_photos, 2):
                trial_slide = Slide(photo1, photo2)
                interest_factor = min(get_interest_factors(current_slide, trial_slide))

                if interest_factor == 1:
                    slideshow.append(trial_slide)
                    v_photos.remove(photo1)
                    v_photos.remove(photo2)
                    current_slide = slideshow[-1]
                    break

            # If we exhausted all V combinations try an H match
            for photo in h_photos:
                trial_slide = Slide(photo)
                interest_factor = min(get_interest_factors(current_slide, trial_slide))

                if interest_factor == 1:
                    slideshow.append(trial_slide)
                    h_photos.remove(photo)
                    current_slide = slideshow[-1]
                    break

        if current_slide.orientation == 'V':
            # First try and match a H slide
            for photo in h_photos:
                trial_slide = Slide(photo)
                interest_factor = min(get_interest_factors(current_slide, trial_slide))

                if interest_factor == 1:
                    slideshow.append(trial_slide)
                    h_photos.remove(photo)
                    current_slide = slideshow[-1]
                    break

            # If we exhausted all H slides then try a V combo
            for photo1, photo2 in itertools.combinations(v_photos, 2):
                trial_slide = Slide(photo1, photo2)
                interest_factor = min(get_interest_factors(current_slide, trial_slide))

                if interest_factor == 1:
                    slideshow.append(trial_slide)
                    v_photos.remove(photo1)
                    v_photos.remove(photo2)
                    current_slide = slideshow[-1]
                    break

    print('V: {0}'.format(len(v_photos)))
    print('H: {0}'.format(len(h_photos)))
    print('Slideshow: {0}'.format(slideshow))

    return slideshow


def get_collection_type(v_photos, h_photos):
    """
    Get the photo collection type (Vertical, Horizontal or, Mixed)

    Args:
        v_photos (list[Photo]): List of vertical photos
        h_photos (list[Photo]): List of horizontal photos

    Returns:
        collection_type (str): The string describing the collection type

    """
    collection_type = 'unknown'

    if len(v_photos) and len(h_photos) == 0:
        exit('Warning failed to find any photos in collection')
    elif len(v_photos) != 0 and len(h_photos) == 0:
        collection_type = 'vertical'
    elif len(v_photos) == 0 and len(h_photos) != 0:
        collection_type = 'horizontal'
    else:
        collection_type = 'mixed'

    return collection_type
