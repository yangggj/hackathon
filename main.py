
import sys
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


FILE = './data/Confidentiel_d2-25.csv'
N_VOL = 2



if len(sys.argv) > 1:
	FILE = sys.argv[1]

data = pd.read_csv(FILE, delimiter=';')
data = data[data["Vol"] == N_VOL]

def get_temp_name(mini, maxi):
	return [f"T{i:0>2}" for i in range(mini, maxi+1)]

def correct_temp(temp):
	mean_diff = 100*abs(temp.diff().mean())
	tmp = temp.copy()
	tmp[abs(tmp.diff()) >= mean_diff] = np.nan
	return tmp.interpolate()


name_equip_sab = get_temp_name(1, 7)
name_amb_sab = get_temp_name(8, 15)
name_living = get_temp_name(16, 26)
name_equip_cockpit = get_temp_name(27, 28)
name_carb = get_temp_name(29, 31)
name_equip_intern = get_temp_name(32, 38)
name_karman = get_temp_name(39, 43)
name_nose_cone = get_temp_name(44, 46)
name_planche = get_temp_name(47, 51)
name_soute = get_temp_name(52, 59)
name_surf = get_temp_name(60, 62)
name_sous_plancher = get_temp_name(63, 65)
name_ecs = ["T66"]

names = [name_equip_sab, name_amb_sab, name_living, name_equip_cockpit,
		 name_carb, name_equip_intern, name_karman, name_nose_cone,
		 name_planche, name_soute, name_surf, name_sous_plancher, name_ecs]
names_str = ["Equipment SaB", "Ambiance SaB", "Living", "Equipment cockpit",
		 	 "Carbu", "Equipment intern", "Karman", "Nose Cone",
		 	 "Planche de bord", "Soute", "Surf", "Sous Plancher", "ECS"]

temps = pd.DataFrame()
for col in get_temp_name(1, 66):
	if col not in name_carb:
		temps[col] = correct_temp(data.pop(col))
	else:
		temps[col] = data.pop(col)


for i, category in enumerate(names):
	plt.figure()
	plt.title(names_str[i])
	for temp in category:
		temps[temp].plot(legend=temp)

plt.show()
