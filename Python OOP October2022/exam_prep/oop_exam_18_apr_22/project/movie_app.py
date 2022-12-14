from exam_prep.oop_exam_18_apr_22.project.movie_specification.movie import Movie
from exam_prep.oop_exam_18_apr_22.project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []  # all the movies (objects)
        self.users_collection = []  # all the users (objects)

    def __user_existence(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __movie_existence(self, movie):
        if movie in self.movies_collection:
            return movie

    def register_user(self, username, age):
        if self.__user_existence(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__user_existence(username)

        if self.__movie_existence(movie):
            raise Exception("Movie already added to the collection!")
        elif not user:
            raise Exception("This user does not exist!")
        elif movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if not self.__movie_existence(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, value in kwargs.items():
            setattr(movie, attr, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__user_existence(username)

        if not self.__movie_existence(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__user_existence(username)
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__user_existence(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = []
        [result.append(m.details()) for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]

        return '\n'.join(result)

    def __str__(self):
        result = [f"All users: "
                  f"{', '.join(u.username for u in self.users_collection) if self.users_collection else 'No users.'}\n"
                  f"All movies: "
                  f"{', '.join(m.title for m in self.movies_collection) if self.movies_collection else 'No movies.'}"]
        return '\n'.join(result)
