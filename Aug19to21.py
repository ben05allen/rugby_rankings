from points import calculate_points
from static import Country, Ground


table = {
    Country.IRELAND: 91.82,
    Country.NEW_ZEALAND: 90.77,
    Country.FRANCE: 89.22,
    Country.SOUTH_AFRICA: 88.97,
    Country.SCOTLAND: 84.01,
    Country.ENGLAND: 81.53,
    Country.ARGENTIA: 80.86,
    Country.AUSTRALIA: 79.87,
    Country.FIJI: 78.70,
    Country.WALES: 78.66,
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
    ((Country.WALES, 16, Ground.HOME),(Country.SOUTH_AFRICA, 52, Ground.AWAY)),
    ((Country.IRELAND, 29, Ground.HOME),(Country.ENGLAND, 10, Ground.AWAY)),
    ((Country.ITALY, 57, Ground.HOME),(Country.ROMANIA, 21, Ground.HOME)),
    ((Country.FRANCE, 34, Ground.HOME),(Country.FIJI, 17, Ground.AWAY)),
]

for fixture in results:
    (a, a_score, a_home), (b, b_score, b_home) = fixture
    a_pts, b_pts = calculate_points(table[a], table[b], a_score, b_score, a_home.value, b_home.value, is_rwc_final=False)
    print(f'{a.name} {a_pts} {round(table[a] + a_pts, 2)}, {b.name} {b_pts} {round(table[b] + b_pts, 2)}')

    table[a] = round(table[a] + a_pts, 2)
    table[b] = round(table[b] + b_pts, 2)

for i, (k,v) in enumerate(reversed(sorted(table.items(), key=lambda x: x[1]))):
    print(f'{i + 1}. {k.name} - {v}')
