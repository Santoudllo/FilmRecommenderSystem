from cassandra.cluster import Cluster

def retrieve_data_from_cassandra():
    # Connexion à Cassandra
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('movies_keyspace')

    #  requête pour récupérer toutes les données de la table movies
    query = "SELECT * FROM movies"
    result = session.execute(query)

    # Convertir le résultat en liste de dictionnaires pour une manipulation facile
    data = []
    for row in result:
        data.append(row)

    return data

# Appel de la fonction pour récupérer les données de Cassandra
data_from_cassandra = retrieve_data_from_cassandra()

# Afficher le total des lignes récupérées
total_rows = len(data_from_cassandra)
print("Total des lignes récupérées :", total_rows)

# Afficher le nombre de colonnes récupérées dans la première ligne
if total_rows > 0:
    num_columns = len(data_from_cassandra[0])
    print("Nombre de colonnes récupérées :", num_columns)
else:
    print("Aucune donnée récupérée.")
