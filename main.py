'''main app'''

import os
from import_data import create_opere_incompiute_list
from tools import create_dict_obj_for_value_of_attribute, ask_to_save_plot
from tools import ask_bool, ask_position, plot_and_print_clusters
from tools import overwrite_warning, save_and_print_picked_opere_sorted
import matplotlib.pyplot as plt

DATA_URL = "https://s3.us-east-1.amazonaws.com/vrai.univpm/FI/2025/02/opere.json"
REL_PATH_JSON = r"fi_exam/data.json"
REL_PATH_CSV1 = r"fi_exam/clusters.csv"
REL_PATH_CSV2 = r"fi_exam/picked_opere.csv"

def main():
    '''entry point'''
    # import data and create a list of objects OperaInompiuta
    opere_incompiute_list = create_opere_incompiute_list(DATA_URL, REL_PATH_JSON)
    # extract unique values of each attribute
    attributes1 = ['ambito_oggettivo', 'categoria','pubblicata_da',
                  'tipologia_cup', 'tipologia_opera_incompiuta']
    # print the number of objects for each value of every attribute
    # empty-value occurrencies are show as well as NoneType
    create_dict_obj_for_value_of_attribute(
        attributes1, opere_incompiute_list, verbosity=True)


    # do the same as before with a new list of attributes
    attributes2 = ['mancanza_fondi', 'cause_tecniche', 'comunitaria', 'tipologia_cup']
    # create a dict of tables, gathering Opere for attribute values
    objs_for_attribute_dict = create_dict_obj_for_value_of_attribute(
        attributes2, opere_incompiute_list, return_dict=True)
    # plot number of objects for each attribute value
    n_img = 0
    for attribute in attributes2:
        n_img += 1
        table_of_objs = objs_for_attribute_dict[attribute]
        # filter to remove NoneType values
        table_of_objs = [line for line in table_of_objs if line[0] is not None]
        # sort table by number of objs for each attr_value
        sort_filtr_table = sorted(table_of_objs, key=lambda x: x[1])
        unique_attr_values = [line[0] for line in sort_filtr_table]
        num_obj_for_attr_value = [line[1] for line in sort_filtr_table]
        # bar plot of the number of objects
        plt.figure(figsize=(10,8))
        plt.bar(unique_attr_values,num_obj_for_attr_value)
        plt.ylabel('N. Opere Incompiute')
        plt.grid(axis='y')
        plt.title(attribute.upper())
        plt.xticks(rotation=20)
        plt.tight_layout()
        # ask the user whether to save the plot and with which format; then show it
        ask_to_save_plot(n_img)
        plt.show()
    # close previously shown plots
    plt.close(fig='all')


    # create a table of lats and lons
    places = list(map(lambda x:[x.get_lat(),x.get_lon()], opere_incompiute_list))
    # filter and remove NoneType values
    places = list(filter(lambda x: not None in x, places))
    # use KMeans method for n. clustes K from 2 to 7; print places for all clusters and plot them
    clusters_list = plot_and_print_clusters(places)
    # save clusters for all K trials in a CSV file
    if not os.path.exists(REL_PATH_CSV1):
        with open(REL_PATH_CSV1,"w",encoding='utf-8') as csv_file:
            csv_file.write("K;id;nElements;centroidLat;centroidLon\n")
            for item in clusters_list:
                csv_file.write(f"{item['n_cluster']};{item['id_cluster']};{item['n_elements']};"
                                f"{item['centroid_lat']};{item['centroid_lon']}\n")
    # close previous shown plots
    plt.close(fig='all')


    # ask the user to provide his lat and lon; create a Luogo object
    user_position = ask_position()
    # remove from opere_incompiute_list NoneType values of tipologia_cup, lat and lon
    filtered_opere = list(filter(lambda x: (x.get_tipologia_cup() is not None
                                            and x.get_lat() is not None and x.get_lon()
                                            is not None), opere_incompiute_list))
    # get unique values of tipologia_cup
    tipologia_cup_values = list(set(map(lambda x:x.get_tipologia_cup(), filtered_opere)))
    # ask the user to provide a tipologia_cup value among tipologia_cup_values
    while True:
        picked_value = input(
            f"Provide a tipologia_cup value among these: {tipologia_cup_values} --> ")
        if picked_value in tipologia_cup_values:
            break
        print(f"You wrote: {picked_value}, which is a wrong value. Please retry")
    # create a list of OpereIncompiute with only the ones with the tipologia_cup_value provided
    picked_opere = list(filter(
        lambda x:x.get_tipologia_cup() == picked_value, filtered_opere))
    # create a table associating to picked_opera the distance bewtween user and picked_opera
    picked_opere_and_distances_table = []
    for item in picked_opere:
        user_distance_from_opera = item.haversine_distance(user_position)
        picked_opere_and_distances_table.append([item, user_distance_from_opera])
    # ask the user to sort in descending order or not
    descend_order = ask_bool('Do you want to sort selected OpereIncompiute '
                            'with DESCENDING order of distance? (yes or no): ')
    # sort by user_distance_from_opera
    sorted_picked_opere_and_distances_table = sorted(
        picked_opere_and_distances_table,key=lambda x: x[1], reverse=descend_order)
    # Warn the user about the creation of a new file and the risk of overwrite data
    overwrite_warning(REL_PATH_CSV2)
    print(f"\n'OpereIncompiute' with {picked_value} as 'tipologia_cup':")
    # create a CSV file with all the attributes of the picked OpereIncompiute sorted as user's will
    save_and_print_picked_opere_sorted(REL_PATH_CSV2, sorted_picked_opere_and_distances_table)

if __name__=='__main__':
    main()
