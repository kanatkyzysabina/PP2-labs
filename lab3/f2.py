
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1- - - - - - -
def isAbove(movies):
    i = int(input("Enter number from 0 to 14(to choose movie to check): "))
    if movies[i]["imdb"] > 5.5:
        return True
    return False

if isAbove(movies):
    print("imdb of this movie is above 5.5!")
else:
    print("imdb of this movie is lower than 5.5!")

#2- - - - - -
def SubList(movies):
    sub_movies = []
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            sub_movies.append(movies[i]["name"])
    return sub_movies

print("\n- IMDB of the next movies is above 5.5. \nHere is the Sub List of such movies:")
print(SubList(movies))

#3- - - - - -

def Category(category):
    resMovies = []
    for i in range(len(movies)):
        if movies[i]["category"] == category.capitalize():
            resMovies.append(movies[i]["name"])
        
    print(resMovies)


print("""\n--- Choose the category of a movie: ---
'Thriller', 'Comedy', 'Suspense', 'Crime', 'War',
 'Romance', 'Drama', 'Adventure', 'Action' \nEnter category: """)
category = input()

print(f"\nThe list of {category.capitalize()} movies: ")
Category(category)

#4- - - - - -

def AverageIMDB():
    total = 0
    imdb = []
    for m in movies:
        imdb.append(float(m["imdb"]))
    
    for i in imdb:
        total+=i
    
    average = total/len(imdb)
    return average

print(f"\nAverage imdb of all movies is: {AverageIMDB()}")
    
#5- - - - - - -

def AVG_Category(category):
    resIMDB = []
    for m in movies:
        if m["category"] == category.capitalize():
            resIMDB.append(float(m["imdb"]))
    
    total = 0
    for i in resIMDB:
        total+=i

    avg = total/len(resIMDB)
    return avg



print("""\n--- Choose the category of a movie: ---
'Thriller', 'Comedy', 'Suspense', 'Crime', 'War',
 'Romance', 'Drama', 'Adventure', 'Action' \nEnter category: """)
category = input()

print(f"\nAverage IMDB score of {category.capitalize()} category is: {AVG_Category(category)}")




