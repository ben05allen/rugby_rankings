from points import calculate_points
from static import Country, Ground

FULL_TABLE = True

table = {
    Country.SOUTH_AFRICA: 92.48,
    Country.NEW_ZEALAND: 90.91,
    Country.IRELAND: 90.57,
    Country.FRANCE: 87.81,
    Country.ENGLAND: 84.03,
    Country.SCOTLAND: 83.43,
    Country.ARGENTIA: 83.07,
    Country.WALES: 80.65,
    Country.AUSTRALIA: 77.48,
    Country.FIJI: 76.38,
    Country.ITALY: 75.93,
    Country.JAPAN: 74.27,
    Country.PORTUGAL: 72.78,
    Country.GEORGIA: 72.68,
    Country.SAMOA: 72.23,
    Country.TONGA: 71.57,
    Country.URUGUAY: 67.39,
    Country.USA: 66.22,
    Country.SPAIN: 64.05,
    Country.ROMANIA: 63.28,
    Country.NAMIBIA: 60.56,
    Country.CHILE: 60.49,
}


results = [
    ((Country.ARGENTIA, 6, Ground.AWAY), (Country.NEW_ZEALAND, 44, Ground.AWAY)),
    ((Country.ENGLAND, 15, Ground.AWAY), (Country.SOUTH_AFRICA, 16, Ground.AWAY)),
]

old_ranking = {
    k: i + 1
    for i, (k, _) in enumerate(
        reversed(sorted([(k.name, v) for k, v in table.items()], key=lambda x: x[1]))
    )
}


def position_change(old_position: int, new_position: int) -> str:
    if old_position == new_position:
        return "-"
    elif new_position > old_position:
        return f"-{new_position - old_position}"
    return f"+{old_position - new_position}"


for fixture in results:
    (a, a_score, a_home), (b, b_score, b_home) = fixture
    a_pts, b_pts = calculate_points(
        table[a],
        table[b],
        a_score,
        b_score,
        a_home.value,
        b_home.value,
        is_rwc_finals=True,
    )
    print(f"{a.name} - {a_score} ({a_pts}), {b.name} - {b_score} ({b_pts})")

    table[a] = round(table[a] + a_pts, 2)
    table[b] = round(table[b] + b_pts, 2)

if FULL_TABLE:
    for i, (k, v) in enumerate(reversed(sorted(table.items(), key=lambda x: x[1]))):
        print(
            f"{i + 1:3}. {k.value:15}{v:.2f}   "
            f"({position_change(old_ranking[k.name], i+1):>2})"
        )
else:
    for k, v in reversed(sorted(table.items(), key=lambda x: x[1])):
        print(f"Country.{k.name}: {v:.2f},")
