'''1. Movie Recommendation Assistant
Concept:
 Load a JSON file containing movie data (titles, genres, ratings, runtime, release year).
 Tasks:
Parse the JSON file to find the top-rated films by genre or year.


Implement search and filter functionality (e.g. “Find all sci-fi movies released after 2010 with IMDb > 8”).


Allow users to add or remove movies and update the JSON file.


Add “personal watchlist” saving in another JSON file.


Extension (A*): Implement similarity scoring — recommend new films based on user preferences using cosine similarity or Jaccard index between genre sets.
'''

import json
from pathlib import Path
def get_best_by_year(file):
    file_path = Path(file)
    print(file_path.exists(), file_path)
    

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    best_by_year = {}
    

    for item in data:
        year = item.get("Year")
        rating = item.get("imdbRating")
        title = item.get("Title")


        if not year or rating in [None, "N/A"]:
            continue

        try:
            rating = float(rating)
        except ValueError:
            continue
        

 
        if year not in best_by_year or rating > best_by_year[year][1]:
            best_by_year[year] = (title, rating)
            
    for year in sorted(best_by_year):
        title, rating = best_by_year[year]
        print(f"{year}: {title} ({rating})")




def filterfunctionality(file):
    file_path = Path(file)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
        
        print("what genre would you like, leave empty if you dont mind")
        usergenre = input()
        print("what rating would you like, leave empty if you dont mind")
        userrating = input()
        print("what year would you like?, leave empty if you dont mind")
        useryear = input()
        if userrating:
            try:
                userrating = float(userrating)
            except ValueError:
                print("invalid rating")
                
                
                
        filtered = {}
        for item in data:
            title = item.get("Title")
            genre = item.get("Genre")
            rating = item.get("imdbRating")
            year = item.get("Year")
            try:
                if rating in ['N/A',None]:
                    rating = None
                else:
                    rating = float(rating)
            except ValueError:
                print("invalid rating")
            
            if not usergenre == '':
                
                if genre and genre.lower() != usergenre.lower():
                    continue
                
            if not useryear == '':
                
                if str(year) != str(useryear):
                    continue
                
            if not userrating == '':
                
                if rating not in[None, 'N/A']:
                    
                    if rating != userrating:
              
                        continue
                else:
                    continue
            

            filtered[title] = (rating, genre, year)
                
            
        for choice in sorted(filtered):
            title,genre,rating,year = filtered[choice]
            print(f'Title:{title} , genre{genre}, rating{rating}, year{year}')
        
            
def menu():
    print("hellooo, would you like to get the highest rated results for every year(HRY)\n Get a specialised list of movies for you(S)")
    choice = input()

    if choice == 'HRY':
        
        results = get_best_by_year('/Users/haydenfletcher/Documents/programming/githubrepositiories/School-code/inschool/films.json')

    if choice == "S":
        results = filterfunctionality('/Users/haydenfletcher/Documents/programming/githubrepositiories/School-code/inschool/films.json')
        

menu()