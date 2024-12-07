def get_peak_ordering_times():
    return """
        SELECT strftime('%H', order_date) AS Hour, COUNT(*) AS Total_Orders
        FROM Orders
        GROUP BY Hour
        ORDER BY Total_Orders DESC
        LIMIT 5;
    """

def get_top_customers():
    return """
        SELECT Customers.name AS Customer_Name, COUNT(Orders.order_id) AS Order_Count
        FROM Customers
        JOIN Orders ON Customers.customer_id = Orders.customer_id
        GROUP BY Customers.name
        ORDER BY Order_Count DESC
        LIMIT 5;
    """

def get_top_restaurants():
    return """
        SELECT Restaurants.name AS Restaurant_Name, COUNT(Orders.order_id) AS Total_Orders
        FROM Restaurants
        JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id
        GROUP BY Restaurants.name
        ORDER BY Total_Orders DESC
        LIMIT 5;
    """

def get_popular_cuisines():
    return """
        SELECT cuisine_type AS Cuisine, COUNT(*) AS Popularity
        FROM Restaurants
        GROUP BY cuisine_type
        ORDER BY Popularity DESC
        LIMIT 5;
    """

def get_avg_delivery_times():
    return """
        SELECT Restaurants.name AS Restaurant_Name, AVG(Orders.delivery_time) AS Avg_Delivery_Time
        FROM Restaurants
        JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id
        GROUP BY Restaurants.name
        ORDER BY Avg_Delivery_Time ASC
        LIMIT 5;
    """

def get_feedback_summary(order):
    return f"""
        SELECT feedback_rating AS Rating, COUNT(*) AS Count
        FROM Orders
        GROUP BY feedback_rating
        ORDER BY feedback_rating {order}
        LIMIT 5;
    """


def get_orders_by_day():
    return """
        SELECT strftime('%Y-%m-%d', order_date) AS Order_Date, COUNT(*) AS Total_Orders
        FROM Orders
        GROUP BY Order_Date
        ORDER BY Total_Orders DESC
        LIMIT 5;
    """

def get_orders_by_month():
    return """
        SELECT strftime('%Y-%m', order_date) AS Month, COUNT(*) AS Total_Orders
        FROM Orders
        GROUP BY Month
        ORDER BY Total_Orders DESC
        LIMIT 5;
    """

def get_avg_order_value():
    return """
        SELECT AVG(order_value) AS Avg_Order_Value
        FROM Orders
        LIMIT 5;
    """

def get_top_rated_restaurants():
    return """
        SELECT Restaurants.name AS Restaurant_Name, AVG(Orders.feedback_rating) AS Avg_Rating
        FROM Restaurants
        JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id
        GROUP BY Restaurants.name
        ORDER BY Avg_Rating DESC
        LIMIT 5;
    """

def get_highest_rated_customers():
    return """
        SELECT Customers.name AS Customer_Name, AVG(Orders.feedback_rating) AS Avg_Rating
        FROM Customers
        JOIN Orders ON Customers.customer_id = Orders.customer_id
        GROUP BY Customers.name
        ORDER BY Avg_Rating DESC
        LIMIT 5;
    """

def get_most_ordered_items():
    return """
        SELECT Orders.order_id, COUNT(*) AS Order_Count
        FROM Orders
        GROUP BY Orders.order_id
        ORDER BY Order_Count DESC
        LIMIT 5;
    """


def get_order_value_by_restaurant():
    return """
        SELECT Restaurants.name AS Restaurant_Name, SUM(Orders.total_amount) AS Total_Revenue
        FROM Restaurants
        JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id
        GROUP BY Restaurants.name
        ORDER BY Total_Revenue DESC
        LIMIT 5;
    """

def get_avg_feedback_by_restaurant():
    return """
        SELECT Restaurants.name AS Restaurant_Name, AVG(Orders.feedback_rating) AS Avg_Feedback
        FROM Restaurants
        JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id
        GROUP BY Restaurants.name
        ORDER BY Avg_Feedback DESC
        LIMIT 5;
    """

def get_order_distribution_by_feedback():
    return """
        SELECT feedback_rating AS Rating, COUNT(*) AS Order_Count
        FROM Orders
        GROUP BY feedback_rating
        ORDER BY Rating DESC
        LIMIT 5;
    """

def get_most_active_delivery_persons():
    return """
        SELECT DeliveryPersonnel.name AS Delivery_Person_Name, COUNT(Orders.order_id) AS Delivery_Count
        FROM DeliveryPersonnel
        JOIN Orders ON DeliveryPersonnel.delivery_person_id = Orders.delivery_person_id
        GROUP BY DeliveryPersonnel.name
        ORDER BY Delivery_Count DESC
        LIMIT 5;
    """

def get_avg_order_value_by_restaurant():
    return """
        SELECT Restaurants.name AS Restaurant_Name, AVG(Orders.order_value) AS Avg_Order_Value
        FROM Restaurants
        JOIN Orders ON Restaurants.restaurant_id = Orders.restaurant_id
        GROUP BY Restaurants.name
        ORDER BY Avg_Order_Value DESC
        LIMIT 5;
    """

def get_peak_ordering_days():
    return """
        SELECT strftime('%A', order_date) AS Weekday, COUNT(*) AS Total_Orders
        FROM Orders
        GROUP BY Weekday
        ORDER BY Total_Orders DESC
        LIMIT 5;
    """

def get_top_restaurants_by_rating():
    return """
        SELECT name AS Restaurant_Name, 
               cuisine_type AS Cuisine, 
               location AS Location, 
               rating AS Average_Rating
        FROM Restaurants
        WHERE is_active = 1
        ORDER BY rating DESC
        LIMIT 5;
    """


def get_most_ordered_cuisine_by_customer():
    return """
        SELECT Customers.name AS Customer_Name, Restaurants.cuisine_type AS Cuisine, COUNT(*) AS Order_Count
        FROM Customers
        JOIN Orders ON Customers.customer_id = Orders.customer_id
        JOIN Restaurants ON Orders.restaurant_id = Restaurants.restaurant_id
        GROUP BY Customers.name, Restaurants.cuisine_type
        ORDER BY Order_Count DESC
        LIMIT 5;
    """

def get_order_count_by_hour():
    return """
        SELECT strftime('%H', order_date) AS Hour, COUNT(*) AS Order_Count
        FROM Orders
        GROUP BY Hour
        ORDER BY Order_Count DESC
        LIMIT 5;
    """

def get_top_customer_locations():
    return """
        SELECT c.location AS Customer_Location, 
               COUNT(o.order_id) AS Total_Orders
        FROM Customers c
        INNER JOIN Orders o ON c.customer_id = o.customer_id
        GROUP BY c.location
        ORDER BY Total_Orders DESC
        LIMIT 5;
    """


def get_orders_by_customer():
    return """
        SELECT Customers.name AS Customer_Name, COUNT(Orders.order_id) AS Order_Count
        FROM Customers
        JOIN Orders ON Customers.customer_id = Orders.customer_id
        GROUP BY Customers.name
        ORDER BY Order_Count DESC
        LIMIT 5;
    """
