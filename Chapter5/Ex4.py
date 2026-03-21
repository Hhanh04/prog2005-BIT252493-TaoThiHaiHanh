import matplotlib.pyplot as plt
cities = ["Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno",
          "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim"]

areas = [1302, 964, 469, 600, 298, 259, 170, 202, 388, 131]
sorted_data = sorted(zip(areas, cities), reverse=True)
areas_sorted, cities_sorted = zip(*sorted_data)
plt.barh(cities_sorted, areas_sorted)
plt.title("Top 10 thành phố lớn nhất California (theo diện tích)")
plt.xlabel("Diện tích (km²)")
plt.ylabel("Thành phố")
plt.gca().invert_yaxis()
plt.show()