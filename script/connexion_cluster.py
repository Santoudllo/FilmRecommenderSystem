from cassandra.cluster import Cluster

def retrieve_data_from_cassandra():
    # Connexion à Cassandra
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('movies_keyspace')

    # Exemple de requête pour récupérer toutes les données de la table movies
    query = "SELECT * FROM movies"
    result = session.execute(query)

    # Convertir le résultat en liste de dictionnaires pour une manipulation facile
    data = [row._asdict() for row in result]

    return data

def save_to_csv(data, file_path):
    if data:
        fieldnames = data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Les données ont été sauvegardées sous forme de fichier CSV avec succès.")
    else:
        print("Aucune donnée à sauvegarder.")

# Appel de la fonction pour récupérer les données de Cassandra
data_from_cassandra = retrieve_data_from_cassandra()

# Chemin du fichier CSV de sortie
output_file_path = "/home/santoudllo/Desktop/PROJET_PERSO/FilmRecommenderSystem/data/movies_data.csv"

# Sauvegarde des données dans un fichier CSV
save_to_csv(data_from_cassandra, output_file_path)
