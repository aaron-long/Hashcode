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


def find_perfect_v_pairs(v_photos, slideshow):
    filtered_v_photos = []
    for i, photo in enumerate(v_photos, 0):
        if i > len(v_photos) - 2:
            break
        slide1 = Slide(photo)
        slide2 = Slide(v_photos[i + 1])

        min_interest_factor = min(get_interest_factors(slide1, slide2))

        if min_interest_factor == 1:
            slideshow.append(slide1)
            slideshow.append(slide2)
            filtered_v_photos.append(photo)
            filtered_v_photos.append(v_photos[i + 1])
            v_photos.remove(photo)
            v_photos.remove(v_photos[i + 1])

    return


def find_perfect_scores(h_photos, v_photos, slideshow):
    max_itr = 100
    filtered_v_photos = []

    for photo in h_photos:
        for _ in range(max_itr):
            # Sample two unique vertical photos
            sample = random.sample(v_photos, 2)
            slide1 = Slide(photo)
            slide2 = Slide(sample[0], sample[1])

            min_interest_factor = min(get_interest_factors(slide1, slide2))

            if min_interest_factor == 1:
                slideshow.append(slide1)
                h_photos.remove(photo)
                slideshow.append(slide2)
                v_photos.remove(sample[0])
                v_photos.remove(sample[1])
                filtered_v_photos.extend(sample)
                break

    return


def find_perfect_h_pairs(h_photos, slideshow):
    filtered_h_photos = []

    for i, photo in enumerate(h_photos, 0):
        if i > len(h_photos) - 2:
            break
        slide1 = Slide(photo)
        slide2 = Slide(h_photos[i + 1])

        min_interest_factor = min(get_interest_factors(slide1, slide2))

        if min_interest_factor == 1:
            slideshow.append(slide1)
            slideshow.append(slide2)
            filtered_h_photos.append(photo)
            filtered_h_photos.append(h_photos[i + 1])
            h_photos.remove(photo)
            h_photos.remove(h_photos[i + 1])

    return


def h_pairs(h_photos, slideshow, max_itr=100):
    for _ in range(max_itr):
        sample = random.sample(h_photos, 2)

        slide1 = Slide(slideshow[-1])
        slide2 = Slide(sample[1])

        min_interest_factor = min(get_interest_factors(slide1, slide2))

        if min_interest_factor == 1:
            slideshow.append(slide2)


def match_next_h_slide(h_photos, slideshow):

    current_slide = slideshow[-1]

    for photo in h_photos:
        new_slide = Slide(photo)

        interest_factor = min(get_interest_factors(current_slide, new_slide))

        if interest_factor != 0:
            print('Interest factor: {0}'.format(interest_factor))
        if interest_factor == 1:
            slideshow.append(new_slide)
            h_photos.remove(photo)
            break

    return


def find_h_pairs(h_photos, slideshow):
    max_iter = 100
    previous_best = None

    for photo in h_photos:
        itr = 0
        current_slide = slideshow[-1]
        trial_slide = Slide(photo)

        interest_factor = min(get_interest_factors(current_slide, trial_slide))

        if interest_factor == 1:
            slideshow.append(trial_slide)
            h_photos.remove(photo)
            continue
        elif interest_factor > 1:
            if itr > max_iter:
                slideshow.append(previous_best[1])
                h_photos.remove(previous_best[0])
            previous_best = [photo, trial_slide]
            continue

    return

