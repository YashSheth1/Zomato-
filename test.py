from zomato import Zomato
z = Zomato("6833acc57f2a5d311450865c59d3b7f2")
# A call to categories endpoint from zomato API.
#z.parse("categories","")
# A call to restaurants endppoint from zomato 
# API with required parameters res_id
#z.parse("restaurant","res_id=16774318")
#cities={"Mumbai":{"lat":19.0176,"log":72.856}}
z.parse("search","lat=19.0176,lon=72.856")
z.parse("search","lat=17.366,lon=78.476")
z.parse("search","lat=28.625789,lon=77.210276")
z.parse("search","lat=13.083889,lon=80.27")

