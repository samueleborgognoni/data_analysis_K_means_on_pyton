# data_analysis_K_means_on_pyton

The Python project, related to the course "Fundamentals of Informatics" taught by Prof. Adriano Mancini at Università Politecnica delle Marche (UNIVPM), aims at analyzing a JSON dataset concerning unfinished public works in Italy (dataset source: https://dati.mit.gov.it/catalog/dataset/opere-incompiute). Custom classes, exceptions, functions, and the K-means algorithm have been used, without relying on the pandas and csv libraries, as required by the exam instructions.


**Here below, the detailed track of the exam**:

Develop Python code that implements the following functionalities:

- Create one or more classes—possibly using inheritance—to model a single data element (in this case, an individual "Opera Incompiuta", i.e., unfinished public work).

- Load the dataset and convert it into a list of objects that conform to the class defined above. The list must contain N elements, each being an instance of the class. Pay attention to numerical values that are stored as strings in the JSON file. Perform appropriate conversions from strings to numbers, taking care to handle decimal and thousand separators. It is not necessary to model every attribute from the JSON—only those considered useful.

- Print the number of unfinished public works grouped by:
"ambito_oggettivo", "categoria", "pubblicata_da", "tipologia_cup", and "tipologia_opera_incompiuta".

- Create bar charts showing the number of unfinished works grouped by:
"mancanza_fondi", "cause_tecniche", "comunitaria", and "tipologia_cup".
The user must be able to save these charts. Input provided by the user should be validated.

- For k ranging from 2 to 7 (inclusive):

- Apply the K-means algorithm to latitude and longitude data and:

- Compute the number of elements in each cluster.

- Visualize the clusters using matplotlib, using different colors (also display the centroids).

- Generate a CSV text file where each row contains: the current value of k, the cluster ID, the number of elements in the cluster, and the centroid. Example format:

K, id, nElements, centroidLat, centroidLon  
3, 1, 10, 43.2, 13.4  
3, 2, 3, 43.21, 13.45  
...

- Ask the user to input their position in terms of latitude and longitude. Handle cases where the user provides invalid values for lat/lon. Also prompt the user to provide a "tipologia_cup" using the input() function, choosing from the available ones.

- Print the unfinished public works that match the user's criteria and calculate the distance from the user's location using the Haversine formula. Allow the user to sort the results in ascending or descending order based on distance. Save the results to a CSV file using any encoding of your choice, ensuring easy import into Excel.

- Implement at least 4 unit tests using the unittest module (including at least one assertRaises).

--------
- The code must be well commented and organized in a modular way, including the implementation of a main() function.
- The code must handle any exceptions that may occur during execution.
- User input must be validated (e.g., file format, data types, etc.).
- Where applicable, it is recommended to use lambda functions, map, filter, etc.
