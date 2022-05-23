import folium

m = folium.Map(location=[42.6249108,25.346004])
output = 'base.map_html'
m.save(output)