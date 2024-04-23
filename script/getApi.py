from datetime import datetime, timedelta
import time
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
    
    # Temps de début de l'exécution
    start_time = datetime.now()

    # Durée minimale de l'exécution (30 minutes)
    min_execution_time = timedelta(minutes=30)

    # Nombre total de pages à récupérer
    total_pages = 100  # Modifier le nombre total de pages selon vos besoins
    page = 1  # Initialisation de la page

    # Boucle pour récupérer les données jusqu'à ce que le temps minimum soit écoulé
    while datetime.now() - start_time < min_execution_time:
        params = {'page': page}
        response = requests.get(url, headers=headers, params=params)

        # Vérification de la réponse
        if response.status_code == 200:
            data = response.json()
            movies = data.get("results", [])

            # Insertion des données dans la table
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
            page += 1  # Passer à la page suivante
        else:
            print("La requête a échoué avec le code d'état :", response.status_code)
            break  # Sortir de la boucle en cas d'échec de la requête

        time.sleep(1)  # Attente d'une seconde entre les requêtes pour éviter de surcharger l'API

# Appel de la fonction pour charger les données dans Cassandra
load_data_to_cassandra()
