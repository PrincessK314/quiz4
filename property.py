
class Movie:
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title:str):
        self._title = title

movie = Movie()
movie.title = "Star Wars"
print(movie.title)