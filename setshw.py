# Question 1 

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Destinations both fly to
ambos = our_routes.intersection(competitor_routes)
print(ambos)

#Destinations unique to your airline
para_mi = our_routes.difference(competitor_routes)
print(para_mi)

#Whether there are any destinations that neither airline shares
different = our_routes.union(competitor_routes)
aeropuerto = input("Airport: ")
nunca = different.discard(aeropuerto)
print(nunca)


# Question 2

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
x = set(customer_ids)
print(x)