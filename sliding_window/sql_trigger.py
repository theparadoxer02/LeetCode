# # Write a query to find the second highest salary without using limit


# # select emp.name (
# #     select count(*) as total_count from Empolyee(
# #         select emp.name from Empolyee order by salary asc 
# #     ) offset total_count - 2 order by desc
# # )  offset 2

# # 1000 - 998


# # 999 1000
# # 1000 999 -> offset 1 - > 998th elem


# # query to find the department with highth total salry

# # select department, sum(salary) as total_salary from Empolyee
# #     group by 'department'
# #     order by total_salary desc limit 1

# # dense rank

# # CollectionTable

# CollectionID - 
# creation_date = (today, yesterday, 4 days back)


# Select * from Collection
#     collection.amt,
#     *
#     ROW NUMBER() OVER
#         PARTITAION BY creation_date  order by desc
#     ) as ranked_partiion
# )


# #  total sales for each product in the collection of order

# # Order.get_all({
    
# # })

# age > 30

# Customer.get_all(age30)


# customer_name started_with "ab"

# # .search_all({
# #     "": ,
# #     match: "ab*" 
# # })