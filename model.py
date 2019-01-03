

class Movie:
    
    def __init__(self, name, year, duration, likes):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def like(self):
        self.like += 1

class Serie:

    def __init__(self, name, year, seasons, likes):
        self.name = name.title()
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def like(self):
        self.like += 1

avengers = Movie('avengers - infinite war', 2018, 160, 5)
print(avengers.name)
print(f'Name {avengers.name} | Year {avengers.year} | Duration {avengers.duration}'
        f' | Like {avengers.likes}')

jobs = Serie('jobs', 2013, 5, 3)
print(jobs.name)
print(f'Name {jobs.name} | Year {jobs.year} | Seasons {jobs.seasons}'
        f' | Like {jobs.likes}')