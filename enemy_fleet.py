import kobayashi as kob

def generate(arena):
    kob.generate.generate_fleet(arena, size=10, team=1, center=(0, 0, 0))
    kob.generate.generate_fleet(arena, size=10, team=2, center=(0, 0, 100))
    kob.generate.generate_fleet(arena, size=10, team=3, center=(100, 0, 0))
