from points import calculate_points
from static import Country, Ground

table = {
    Country.IRELAND: 91.82,
    Country.NEW_ZEALAND: 90.77,
    Country.SOUTH_AFRICA: 89.37,
    Country.FRANCE: 89.22,
    Country.SCOTLAND: 84.01,
    Country.ENGLAND: 81.53,
    Country.ARGENTIA: 80.86,
    Country.AUSTRALIA: 79.87,
    Country.FIJI: 78.70,
    Country.WALES: 78.26,
    Country.GEORGIA: 76.23,
    Country.SAMOA: 76.19,
    Country.ITALY: 74.63,
    Country.JAPAN: 74.29,
    Country.TONGA: 70.29,
    Country.PORTUGAL: 68.61,
    Country.URUGUAY: 66.63,
    Country.USA: 66.22,
    Country.ROMANIA: 64.56,
    Country.SPAIN: 64.05,
    Country.NAMIBIA: 61.61,
    Country.CHILE: 60.49,
}


results = [
    ((Country.NEW_ZEALAND, 7, Ground.AWAY), (Country.SOUTH_AFRICA, 35, Ground.AWAY)),
    ((Country.SPAIN, 3, Ground.HOME), (Country.ARGENTIA, 62, Ground.AWAY)),
    ((Country.IRELAND, 17, Ground.AWAY), (Country.SAMOA, 13, Ground.AWAY)),
    ((Country.ITALY, 42, Ground.HOME), (Country.JAPAN, 21, Ground.HOME)),
    ((Country.SCOTLAND, 33, Ground.HOME), (Country.GEORGIA, 6, Ground.AWAY)),
    ((Country.ENGLAND, 22, Ground.HOME), (Country.FIJI, 30, Ground.AWAY)),
    ((Country.FRANCE, 41, Ground.HOME), (Country.AUSTRALIA, 17, Ground.AWAY)),
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
        is_rwc_final=False,
    )
    print(f"{a.name} - {a_score} ({a_pts}), {b.name} - {b_score} ({b_pts})")

    table[a] = round(table[a] + a_pts, 2)
    table[b] = round(table[b] + b_pts, 2)

for i, (k, v) in enumerate(reversed(sorted(table.items(), key=lambda x: x[1]))):
    print(
        f"{i + 1:3}. {k.value:15}{v:.2f}   "
        f"({position_change(old_ranking[k.name], i+1):>2})"
    )
