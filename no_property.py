
class Movie:
    def get_title(self):
        return self._title
    
    def set_title(self, title:str):
        self._title = title

movie = Movie()
movie.set_title("Star Wars")
print(movie.get_title())