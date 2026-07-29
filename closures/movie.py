# Write a function movie(movie_name).
#
# -   The outer function stores the movie name.
# -   The inner function receives the person’s name.
# -   Print that the person booked a ticket for the movie.
# -   Return the inner function.
def movie(movie_name):
    def name(person_name):
        return f"{person_name} booked a ticket for the {movie_name} movie"
    return name
m1=movie("Jersey")
print(m1("Nikhil"))