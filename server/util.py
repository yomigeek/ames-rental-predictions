import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def predict_sale_price(Neighborhood, Overall_Qual, Gr_Liv_Area, Year_Built, Garage_Area):
    try:
        loc_index = __data_columns.index(Neighborhood.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Overall_Qual
    x[1] = Gr_Liv_Area
    x[2] = Year_Built
    x[3] = Garage_Area
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open('./artifacts/Ames_house_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(predict_sale_price('Neighborhood_StoneBr', 6, 1656, 1960, 528))
