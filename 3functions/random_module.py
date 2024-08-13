import random

#random_number= random.uniform(1,10) : float numbers
#print(random_number)

for i in range(5):
    print(random.randint(1,10))

movie_list = ["Inception","The Shawshank Redemption","The Dark Knight","Titanic","The Saw"]
random_movie = random.choice(movie_list)
print(random_movie)

random.shuffle(movie_list)
print(movie_list)

print(random.sample(movie_list,2))