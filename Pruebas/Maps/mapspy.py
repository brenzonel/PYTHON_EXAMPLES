# import folium package
import folium
import geocoder

g = geocoder.ip('me')
print(g.latlng)
print(g.latlng[0])

g1 = 'https://www.google.com.mx/maps/search/'+ str(g.latlng[0]) + ',' + str(g.latlng[1])

print(g1)

my_map3 = folium.Map(location = [g.latlng[0], g.latlng[1]],
                                        zoom_start = 15)
 
# Pass a string in popup parameter
folium.Marker([g.latlng[0], g.latlng[1]],
               popup = ' Geeksforgeeks.org ').add_to(my_map3)
 
 
my_map3.save(" my_map3.html ")