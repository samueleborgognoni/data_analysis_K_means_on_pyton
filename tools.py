'''Useful functions'''

import os
from datetime import datetime,date
from luogo import Luogo
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from custom_exs import LatValueError,LonValueError

def str_to_date(date_string:str) -> date|None:
    '''Converts a string to a date object.
    "##..." values in the dataset are deleted'''
    if (date_string == '') or (date_string is None) or ("##" in date_string):
        return None
    if not isinstance(date_string,str):
        raise TypeError(f"Wrong type for str_to_datetime arg: {type(date_string)} provided")
    form = "%d/%m/%Y"
    datatime_obj = datetime.strptime(date_string, form).date()
    return datatime_obj

def str_to_num(string:str,decimal_split:str=",",
               k_split:str="",perc:bool=False, integ:bool=False) -> float|None:
    '''Converts a string to a float or int number.
    k_split = source separator of thousand; none by default,
    decimal_split = source decimal separator; comma by default,
    perc = if True remove % symbol as the last character,
    integ = if True returns a int.
    '''
    if string in ("", None):
        return None
    if not isinstance(string,str):
        raise TypeError(f"Wrong type for str_to_float arg: {type(string)} provided")
    if perc is True:
        string = string.replace("%","")
    if k_split != "":
        string = string.replace(k_split,"")
    if decimal_split != "":
        string = string.replace(decimal_split,'.')
    if integ is True:
        return int(string)
    return float(string)

def clear_str(string:str) -> str|None:
    '''clear a str'''
    if string in ("", None):
        return None
    if not isinstance(string,str):
        raise TypeError(f"Wrong type for clear_str arg: {type(string)} provided")
    return string.lower().strip().replace(';',',').replace('.','')

def shorten_str(my_str:str,chars_each_word:int=5, char_limit:int=20) -> str:
    '''create a short string from a long compound str'''
    if my_str is None:
        return my_str
    word_list = (my_str).split(" ")
    clean_str = ''
    for i in range(len(word_list)):
        if i < len(word_list)-1:
            clean_str += f"{word_list[i][:chars_each_word]}_"
        else:
            clean_str += f"{word_list[i][:chars_each_word]}"
    return clean_str[:char_limit]

def count_iterations(value, iterable:list, return_idxs:bool=False) -> int|tuple:
    '''returns number of iterations of a given value in a list;
    when return_idxs is True, returns a tuple with also the indexes.
    It also supports numpy.array type as iterable'''
    iterations = 0
    idxs = []
    for i in range(len(iterable)):
        if iterable[i] == value:
            iterations += 1
            idxs.append(i)
    if return_idxs is True:
        return iterations, idxs
    return iterations

def create_dict_obj_for_value_of_attribute(attributes:list, list_of_objects:list,
                                     verbosity:bool=False, return_dict:bool=False):
    '''counts the number of OpereIncompiute for every value of each attribute;
    if verbosity is True, prints the the count; returns a dict of tables if return_dict True'''
    unique_attributes_values_dict = {}
    for attribute in attributes:
        # create a list of values for attribute
        try:
            attribute_values = [getattr(item,f"get_{attribute}")()
                                for item in list_of_objects]
        except AttributeError as ex:
            print(f"error: {ex}")
        # create a list of unique attr_values
        unique_attribute_values_list = list(set(attribute_values))
        # creating 1 key of the dict and init 1 list as its value
        unique_attributes_values_dict[attribute] = []
        # print the number of objects for the attribute_values
        if verbosity is True:
            print(f"\nATTR: {attribute.upper()}\n")
        for value in unique_attribute_values_list:
            number_attribute_values = count_iterations(value, attribute_values)
            if return_dict is True:
                unique_attributes_values_dict[attribute].append([value,
                                                number_attribute_values])
            if verbosity is True:
                print(f"{value}: {number_attribute_values} ")
        if verbosity is True:
            print('\n' + "-" * 50)
    if return_dict is True:
        return unique_attributes_values_dict

def ask_bool(question:str) -> bool:
    '''ask the user a bool question, validates the
    yes or no answer and retuns a BOOL'''
    while True:
        will_save = input(f"{question}: ")
        will_save = will_save.lower()
        if 'y' in will_save:
            return True
        if 'n' in will_save:
            return False
        print("Wrong answer value; retry")

def ask_image_format() -> str:
    '''asks the user to input a image format'''
    while True:
        formats_available = ['jpeg','png','svg']
        frmt = input("Pick a format between [jpeg,png,svg]: ")
        if frmt in formats_available:
            return frmt
        print('Wrong format provided. Please retry')

def ask_to_save_plot(n_img:int):
    '''asks the user to save the following plot;
    the user can choose the image format;
    it lets the user change the name of other possible images with the same name'''
    while True:
        # ask the user to save the plots as images
        will_to_save = ask_bool(
            "\nDo you prefer to save the following plot? ('yes' or 'no')")
        if will_to_save is False:
            break
        format_img = ask_image_format()
        if not os.path.exists(f"plot_{n_img}.{format_img}"):
            plt.savefig(f"plot_{n_img}.{format_img}", format=format_img)
            print(f"\nImage saved as plot_{n_img}.{format_img}\n")
            break
        print(f"\nA file named plot_{n_img}.{format_img} already exists. "
            f"Change its name or do not save it again")

def plot_and_print_clusters(places:list) -> list:
    '''uses KMeans methodfor n. clustes K from 2 to 7;
    prints places for all clusters and plot them;
    returns a list of dicts, each of them representing a cluster'''
    # create a list of Luogo objects
    places_obj = [Luogo(lat=place[0],lon=place[1]) for place in places]
    # create a numpy 2D array useful for KMeans
    places_array = np.array(places)
    # initialize a list containing clusters as dicts
    clusters_list = []
    # apply KMeans method for n_cluster from 2 to 7
    for n_clusters in range(2,8):
        kmeans = KMeans(n_clusters=n_clusters, random_state=25, n_init="auto").fit(places_array)
        labels_arr = kmeans.labels_
        centroids_arr = kmeans.cluster_centers_
        centroids = centroids_arr.tolist()
        centroids_obj = [Luogo(lat=centroid[0],lon=centroid[1]) for centroid in centroids]
        print(f"\nNUMBER OF CLUSTERS: {n_clusters}\n")
        for id_cluster in range(n_clusters):
            centroid_lat = centroids_obj[id_cluster].get_lat()
            centroid_lon = centroids_obj[id_cluster].get_lon()
            num_places_cluster, idxs_places_cluster = count_iterations(
                                                    id_cluster, labels_arr, return_idxs=True)
            cluster_dict = {'n_cluster': n_clusters,
                            'id_cluster':id_cluster + 1,
                            'n_elements':num_places_cluster,
                            'centroid_lat':centroid_lat,
                            'centroid_lon':centroid_lon}
            clusters_list.append(cluster_dict)
            # create 2 lists with lats and lons of places belonging to the cluster
            latitudes_in_cluster = [places_obj[idx].get_lat() for idx in idxs_places_cluster]
            longitudes_in_cluster = [places_obj[idx].get_lon() for idx in idxs_places_cluster]
            # add to final plot: places belonging to the cluster
            plt.scatter(longitudes_in_cluster,latitudes_in_cluster)
            # add to final plot: centroid and a label with its id_number
            plt.scatter(centroid_lon,centroid_lat,s=250)
            plt.text((centroid_lon - 0.1),
                     (centroid_lat - 0.15), s=f"{id_cluster + 1}", fontweight='bold')
            print(f"cluster {id_cluster + 1} -> {num_places_cluster} places")
        print("\n" + ("." * 35))
        # plot places in all K clusters
        plt.grid(True)
        plt.xlabel('LON [°]')
        plt.ylabel('LAT [°]')
        plt.title(f"PLACES FOR K={n_clusters}, DIVIDED BY CLUSTERS")
        plt.show()
    return clusters_list

def ask_position() -> Luogo:
    '''asks the user for latitude and longitude separately; returns a Luogo object'''
    while True:
        try:
            lat = float(input("Provide your LATITUDE: "))
            # test of ValueError for lat
            _p = Luogo(lat=lat,lon=0.0)
            break
        except LatValueError as ex:
            print(f"error: {ex}. Please retry")
        except ValueError as ex:
            print(f"error: {ex}. Please retry")
    while True:
        try:
            lon = float(input("Provide your LONGITUDE: "))
            place = Luogo(lat=lat,lon=lon)
            break
        except LonValueError as ex:
            print(f"error: {ex}. Please retry")
        except ValueError as ex:
            print(f"error: {ex}. Please retry")
    print(f"Position provided: {place}")
    return place

def overwrite_warning(relative_path):
    '''Warn the user about the creation of a new file'''
    print("\nA new CSV file is being created ...")
    if os.path.exists(relative_path):
        input(f"\nA file at {relative_path} already exists. "
                f"Change name to the existing file not to overwrite data. "
                f"Type any character to continue: ")

def save_and_print_picked_opere_sorted(relative_path:str, picked_opere_table:list):
    '''create a CSV file with all the attributes of
    the picked OpereIncompiute sorted as user's will'''
    with open(relative_path,"w",encoding='utf-8') as csv_file2:
        # create a list of all the attributes of OperaIncompiuta
        attr_list = ['pubblicata_da','anno_rif','tipologia_opera_incompiuta',
                    'perc_avanzamento','mancanza_fondi','cause_tecniche',
                    'importo_complessivo','natura_opera','tipologia_cup',
                    'ambito_oggettivo','categoria','comunitaria',
                    'data_assegnazione_cup','lat','lon','indirizzo']
        for att in attr_list:
            csv_file2.write(f"{att};")
        csv_file2.write('distance_from_you\n')
        for item in picked_opere_table:
            opera_obj = item[0]
            distance = item[1]
            print(f"{opera_obj}\n")
            try:
                print(f"--> YOUR DISTANCE FROM THIS OPERA: {round(distance,2)} km\n")
            except TypeError as ex:
                print(f"error: {ex}\n")
            print('<>'*30)
            for att in attr_list:
                csv_file2.write(str(getattr(opera_obj,f"get_{att}")()))
                csv_file2.write(';')
            csv_file2.write(f'{distance}\n')
