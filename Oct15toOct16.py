from points import calculate_points
from static import Country, Ground

FULL_TABLE = True

table = {
    Country.IRELAND: 93.79,
    Country.FRANCE: 90.59,
    Country.SOUTH_AFRICA: 89.70,
    Country.NEW_ZEALAND: 87.69,
    Country.SCOTLAND: 83.43,
    Country.ENGLAND: 83.24,
    Country.WALES: 83.17,
    Country.ARGENTIA: 80.55,
    Country.AUSTRALIA: 77.48,
    Country.FIJI: 77.16,
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
    ((Country.WALES, 17, Ground.AWAY), (Country.ARGENTIA, 29, Ground.AWAY)),
    ((Country.IRELAND, 24, Ground.AWAY), (Country.NEW_ZEALAND, 28, Ground.AWAY)),
    ((Country.ENGLAND, 30, Ground.AWAY), (Country.FIJI, 24, Ground.AWAY)),
    ((Country.FRANCE, 28, Ground.HOME), (Country.SOUTH_AFRICA, 29, Ground.AWAY)),
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
