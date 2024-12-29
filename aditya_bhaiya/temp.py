import requests

def solve():
  api_url = "https://635a7b406f97ae73a62de4cd.mockapi.io/certa/challenges/backend/jVhKP/scores"
  
  res = requests.get(api_url)
  new_res = res.json()
  main_dict = {}
  for elem in new_res:
    key_name = elem["city"]
    products = [(product["name"], float(product["price"])) for product in elem["products"]]
    products = sorted(products, key=lambda x: x[1], reverse=True)
    final = products[:3]

    main_dict[key_name] = products[:3]
  
  print(main_dict)
  return main_dict

  # Add code here to extract API response and return top 3 expensive products per city

  return top_3_products_per_city





solve()


{
    "Castle Rock": [
        ("Modern Fresh Ball", "836.00"),
        ("Small Fresh Bacon", "711.00"),
        ("Ergonomic Granite Salad", "590.00")
    ],
    "Palatine": [
        ("Handmade Rubber Pizza", "633.00"),
        ("Awesome Granite Shoes", "585.00"),
        ("Handmade Wooden Shirt", "498.00")
    ]
}