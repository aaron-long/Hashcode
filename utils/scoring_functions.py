from slide_objects import Slide


def get_interest_factors(slide1=Slide(), slide2=Slide()):
    """
    Get the interest factor between two slides

    Args:
        slide1 (Slide): First slide to be compared
        slide2 (Slide): Second slide to be compared

    Returns:
        interest_factors (list): The interest factor between slides

    """
    interest_factors = [0, 0, 0]

    # Get the set of tags for each slide
    set1 = set(slide1.tags)
    set2 = set(slide2.tags)

    # Get the common tags between s1 & s2
    interest_factors[0] = len(set1.intersection(set2))

    # Get the number of tags in s1 but not in s2
    interest_factors[1] = len(set1.difference(set2))

    # Get the number of tags in s2 but not s1
    interest_factors[2] = len(set2.difference(set1))

    return interest_factors


def get_slides_score(slides):
    """
    Get the total score of a slideshow.

    Args:
        slides (list[Slide]): A list of slides to be scored

    Returns:
        score (int): The total score of the slideshow
    """
    score = 0

    for i in range(len(slides)-1):
        score += min(get_interest_factors(slides[i], slides[i+1]))

    return score
