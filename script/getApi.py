from cassandra.cluster import Cluster
import requests
def load_data_to_cassandra():
    # Connexion à Cassandra
    cluster = Cluster(['127.0.0.1'])  
    session = cluster.connect('movies_keyspace')  

    # Récupération des données de l'API
    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMzAwYTE0ZTg1M2JlMjc3ZDU5ZDM5NWJmYjBlYTg3YyIsInN1YiI6IjY2MjY1MzY5MDdmYWEyMDE2Mzk5NjA2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-jZXRGiZTje2wf8M67ty03IUlpPLHd1G-kcyYiEezSM"
    }
    
    # Nombre total de pages à récupérer
    total_pages = 10  # Modifier le nombre total de pages selon vos besoins

    # Boucle pour récupérer les données de chaque page
    for page in range(1, total_pages + 1):
        params = {'page': page}
        response = requests.get(url, headers=headers, params=params)

        # Vérification de la réponse
        if response.status_code == 200:
            data = response.json()
            movies = data.get("results", [])

            # Insertion des données dans la table Cassandra
            for movie in movies:
                session.execute("""
                    INSERT INTO movies (id, adult, backdrop_path, original_language, original_title,
                    overview, popularity, poster_path, release_date, title, video, vote_average, vote_count, genre_ids)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                    movie.get("id"),
                    movie.get("adult"),
                    movie.get("backdrop_path"),
                    movie.get("original_language"),
                    movie.get("original_title"),
                    movie.get("overview"),
                    movie.get("popularity"),
                    movie.get("poster_path"),
                    movie.get("release_date"),
                    movie.get("title"),
                    movie.get("video"),
                    movie.get("vote_average"),
                    movie.get("vote_count"),
                    movie.get("genre_ids")
                ))
            print(f"Données chargées avec succès pour la page {page}.")
        else:
            print("La requête a échoué avec le code d'état :", response.status_code)

# Appel de la fonction pour charger les données dans Cassandra
load_data_to_cassandra()
