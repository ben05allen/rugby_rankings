from decimal import Decimal, getcontext

getcontext().prec = 8


def calculate_points(
    a_rank: str | float | int,
    b_rank: str | float | int,
    a_score: int,
    b_score: int,
    is_a_home: bool,
    is_b_home: bool,
    is_rwc_finals: bool,
) -> (Decimal, Decimal):
    if not isinstance(a_rank, str):
        a_rank = str(a_rank)

    if not isinstance(b_rank, str):
        b_rank = str(b_rank)

    a_rank = Decimal(a_rank)
    b_rank = Decimal(b_rank)

    if abs(a_score - b_score) > 15:
        multiplier = Decimal("1.5")
    else:
        multiplier = Decimal("1.0")

    if is_rwc_finals:
        multiplier *= Decimal("2.0")

    if is_a_home:
        a_rank += 3

    if is_b_home:
        b_rank += 3

    rating_gap = min(Decimal("10"), max(Decimal("-10"), b_rank - a_rank))
    a_points = rating_gap / 10

    if a_score > b_score:
        a_points += 1
    elif a_score < b_score:
        a_points -= 1

    points_to_return = float(round(multiplier * a_points, 2))

    return points_to_return, -points_to_return


if __name__ == "__main__":
    print(calculate_points(78.66, 88.97, 16, 52, True, False, False))

    print(calculate_points(81.53, 78.70, 22, 30, False, False, False))
