import itertools
import random

from slide_objects import Slide
from utils.scoring_functions import get_interest_factors, get_slides_score


def create_optimal_slideshow(photos, iter, tol):
    """
    Sort a collection of photos to create an optimal slideshow.

    Args:
        photos (list[slide_objects.Photo]): List of photos to be sorted
        iter (int): Search iterations

    Returns:
        slideshow (list[Slide]): A list of slides forming a slideshow
    """
    # Currently sparse but would like to allow for different algorithm selections
    slideshow = combine_photos(photos, iter, tol)

    return slideshow


def combine_photos(photos, max_iter=100, delta_zero_tolerance=1):
    """
    Brute force.

    Priority on matching vertical combos against horizontal slides, and horizontal slides to vertical ones.

    Args:
        photos (list[Photo]): List of photo objects
        max_iter (int): Maximum number of iterations for main loop
        delta_zero_tolerance (int): If score remains unchanged for n iterations then stop

    Returns:
        slideshow (list[Slide]): List of slides
    """
    slideshow = []

    v_photos = list(filter(lambda x: x.orientation == 'V', photos))
    h_photos = list(filter(lambda x: x.orientation == 'H', photos))

    collection_type = get_collection_type(v_photos, h_photos)
    print('Collection type: {0}'.format(collection_type))

    if collection_type == 'vertical':
        seed_photo = random.choice(v_photos)
    else:
        seed_photo = random.choice(h_photos)
    slideshow.append(Slide(seed_photo))
    score = 0
    converged = False
    conv_count = 0

    for _ in range(max_iter):

        if _ % 100 == 0:
            old_score = score
            score = get_slides_score(slideshow)
            score_delta = score - old_score
            if score_delta == 0:
                conv_count += 1
                if conv_count > delta_zero_tolerance:
                    converged = True
            print('Iteration, Score, Score_delta: {0}, {1}, {2}'.format(_, score, score_delta))
            if _ > 1 and converged:
                break

        find_next_slide(h_photos, slideshow, v_photos)



    print('V: {0}'.format(len(v_photos)))
    print('H: {0}'.format(len(h_photos)))



    return slideshow


def find_next_slide(h_photos, slideshow, v_photos):
    current_slide = slideshow[-1]
    if current_slide.orientation == 'H':

        current_slide = match_v_combo(current_slide, slideshow, v_photos)
        current_slide = match_h(current_slide, h_photos, slideshow)

    if current_slide.orientation == 'V':

        current_slide = match_h(current_slide, h_photos, slideshow)
        current_slide = match_v_combo(current_slide, slideshow, v_photos)

    return


def match_h(current_slide, h_photos, slideshow):
    for photo in h_photos:
        trial_slide = Slide(photo)
        interest_factor = min(get_interest_factors(current_slide, trial_slide))

        if interest_factor == 1:
            slideshow.append(trial_slide)
            h_photos.remove(photo)
            current_slide = slideshow[-1]
            break
        elif interest_factor > 1:
            slideshow.append(trial_slide)
            h_photos.remove(photo)
            current_slide = slideshow[-1]
            break
    return current_slide


def match_v_combo(current_slide, slideshow, v_photos):
    for photo1, photo2 in itertools.combinations(v_photos, 2):
        trial_slide = Slide(photo1, photo2)
        interest_factor = min(get_interest_factors(current_slide, trial_slide))

        if interest_factor == 1:
            slideshow.append(trial_slide)
            v_photos.remove(photo1)
            v_photos.remove(photo2)
            current_slide = slideshow[-1]
            break
        elif interest_factor > 1:
            slideshow.append(trial_slide)
            v_photos.remove(photo1)
            v_photos.remove(photo2)
            current_slide = slideshow[-1]
            break
    return current_slide


def get_collection_type(v_photos, h_photos):
    """
    Get the photo collection type (Vertical, Horizontal or, Mixed)

    Args:
        v_photos (list[Photo]): List of vertical photos
        h_photos (list[Photo]): List of horizontal photos

    Returns:
        collection_type (str): The string describing the collection type

    """
    collection_type = None

    if len(v_photos) > 0 and len(h_photos) == 0:
        collection_type = 'vertical'
    elif len(v_photos) == 0 and len(h_photos) > 0:
        collection_type = 'horizontal'
    elif len(v_photos) and len(h_photos) > 0:
        collection_type = 'mixed'
    else:
        exit('ERROR: failed to find any photos in collection')

    return collection_type
