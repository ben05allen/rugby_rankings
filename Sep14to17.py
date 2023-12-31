from points import calculate_points
from static import Country, Ground

FULL_TABLE = True

table = {
    Country.IRELAND: 91.82,
    Country.SOUTH_AFRICA: 91.67,
    Country.FRANCE: 90.59,
    Country.NEW_ZEALAND: 87.69,
    Country.SCOTLAND: 83.42,
    Country.ENGLAND: 83.22,
    Country.AUSTRALIA: 81.78,
    Country.WALES: 80.66,
    Country.FIJI: 77.88,
    Country.ARGENTIA: 77.59,
    Country.SAMOA: 76.19,
    Country.ITALY: 75.63,
    Country.GEORGIA: 74.32,
    Country.JAPAN: 73.29,
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
    ((Country.URUGUAY, 12, Ground.AWAY), (Country.FRANCE, 27, Ground.HOME)),
    ((Country.NEW_ZEALAND, 71, Ground.AWAY), (Country.NAMIBIA, 3, Ground.AWAY)),
    ((Country.SAMOA, 43, Ground.AWAY), (Country.CHILE, 10, Ground.AWAY)),
    ((Country.WALES, 28, Ground.AWAY), (Country.PORTUGAL, 8, Ground.AWAY)),
    ((Country.IRELAND, 59, Ground.AWAY), (Country.TONGA, 16, Ground.AWAY)),
    ((Country.SOUTH_AFRICA, 76, Ground.AWAY), (Country.ROMANIA, 0, Ground.AWAY)),
    ((Country.AUSTRALIA, 15, Ground.AWAY), (Country.FIJI, 22, Ground.AWAY)),
    ((Country.ENGLAND, 34, Ground.AWAY), (Country.JAPAN, 12, Ground.AWAY)),
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
