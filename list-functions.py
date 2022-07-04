opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


#Sample: create a separate list with data from each column 
column_id = [row[0] for row in apps_data[1:]]
column_track_name = [row[1] for row in apps_data[1:]]
column_size_bytes = [row[2] for row in apps_data[1:]]
column_currency = [row[3] for row in apps_data[1:]]
column_price = [row[4] for row in apps_data[1:]]
column_rating_count_tot = [row[5] for row in apps_data[1:]]
column_rating_count_ver = [row[6] for row in apps_data[1:]]
column_user_rating = [row[7] for row in apps_data[1:]]
column_user_rating_ver = [row[8] for row in apps_data[1:]]
column_ver = [row[9] for row in apps_data[1:]]
column_cont_rating = [row[10] for row in apps_data[1:]]
column_prime_genre = [row[11] for row in apps_data[1:]]
column_sup_devices_num = [row[12] for row in apps_data[1:]]
column_ipadSc_urls_num = [row[13] for row in apps_data[1:]]
column_lang_num = [row[14] for row in apps_data[1:]]
column_vpp_lic = [row[15] for row in apps_data[1:]]


#Manual - without using a function
#Loop any of the columns - Just replace the name of the column in the end of line 30
ratings = {}

for element in column_prime_genre:
    
    if element in ratings:
        ratings[element] += 1
    else:
        ratings[element] = 1

        
#Extract function: it can extract any column from apps_data
def extract (index_column):

    genres = []
        
    for row in apps_data[1:]:
        column = row[index_column]
        genres.append(column)

    print (genres)

    #genres.append(genres)
    
    return genres


#Define genres based on the function above
genres = extract (11)

