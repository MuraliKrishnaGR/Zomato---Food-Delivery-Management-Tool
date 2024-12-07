import pandas as pd
import plotly.express as px
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from oop_database.database_manager import DatabaseManager
from . import queries


class DataInsights:
    def __init__(self, db_path):
        self.db_manager = DatabaseManager(db_path)

    def fetch_data(self, query, columns):
        """Fetch data dynamically based on query and column names."""
        try:
            result = self.db_manager.fetch_all(query)
            return pd.DataFrame(result, columns=columns)
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def visualize_data(self, data, chart_type, x, y, title=None, color=None):
        """Generate a visualization using Plotly."""
        if data.empty:
            print("No data to visualize.")
            return None

        if chart_type == "bar":
            fig = px.bar(data, x=x, y=y, title=title, color=color)
        elif chart_type == "line":
            fig = px.line(data, x=x, y=y, title=title, color=color)
        elif chart_type == "scatter":
            fig = px.scatter(data, x=x, y=y, title=title, color=color)
        elif chart_type == "pie":
            fig = px.pie(data, names=x, values=y, title=title)
        else:
            print(f"Unsupported chart type: {chart_type}")
            return None

        return fig

    def fetch_and_visualize_peak_ordering_times(self):
        query = queries.get_peak_ordering_times()
        columns = ["Hour", "Total Orders"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Hour", y="Total Orders", title="Peak Ordering Times")

    def fetch_and_visualize_top_customers(self):
        query = queries.get_top_customers()
        columns = ["Customer Name", "Order Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Customer Name", y="Order Count", title="Top Customers")

    def fetch_and_visualize_top_restaurants(self):
        query = queries.get_top_restaurants()
        columns = ["Restaurant Name", "Total Orders"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Total Orders", title="Top Restaurants")

    def fetch_and_visualize_popular_cuisines(self):
        query = queries.get_popular_cuisines()
        columns = ["Cuisine Type", "Popularity"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "pie", x="Cuisine Type", y="Popularity", title="Popular Cuisines")

    def fetch_and_visualize_average_delivery_times(self):
        query = queries.get_avg_delivery_times()
        columns = ["Restaurant Name", "Avg Delivery Time (mins)"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Avg Delivery Time (mins)",
                                         title="Average Delivery Times")

    def fetch_and_visualize_feedback_summary(self, top=True):
        order = "DESC" if top else "ASC"
        query = queries.get_feedback_summary(order)
        columns = ["Feedback Rating", "Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Feedback Rating", y="Count",
                                         title="Customer Feedback Summary")

    def fetch_and_visualize_orders_by_day(self):
        query = queries.get_orders_by_day()
        columns = ["Order Date", "Total Orders"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "line", x="Order Date", y="Total Orders", title="Orders by Day")

    def fetch_and_visualize_orders_by_month(self):
        query = queries.get_orders_by_month()
        columns = ["Month", "Total Orders"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Month", y="Total Orders", title="Orders by Month")

    def fetch_and_visualize_avg_order_value(self):
        query = queries.get_avg_order_value()
        columns = ["Avg Order Value"]
        data = self.fetch_data(query, columns)
        return data, None  # No visualization needed for single value

    def fetch_and_visualize_top_rated_restaurants(self):
        query = queries.get_top_rated_restaurants()
        columns = ["Restaurant Name", "Avg Rating"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Avg Rating",
                                         title="Top Rated Restaurants")

    def fetch_and_visualize_highest_rated_customers(self):
        query = queries.get_highest_rated_customers()
        columns = ["Customer Name", "Avg Rating"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Customer Name", y="Avg Rating",
                                         title="Highest Rated Customers")

    def fetch_and_visualize_most_ordered_items(self):
        query = queries.get_most_ordered_items() 
        columns = ["Item Name", "Order Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Item Name", y="Order Count",
                                         title="Most Ordered Items")

    def fetch_and_visualize_order_value_by_restaurant(self):
        query = queries.get_order_value_by_restaurant()
        columns = ["Restaurant Name", "Total Revenue"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Total Revenue",
                                         title="Order Value by Restaurant")

    def fetch_and_visualize_avg_feedback_by_restaurant(self):
        query = queries.get_avg_feedback_by_restaurant()
        columns = ["Restaurant Name", "Avg Feedback"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Avg Feedback",
                                         title="Average Feedback by Restaurant")

    def fetch_and_visualize_order_distribution_by_feedback(self):
        query = queries.get_order_distribution_by_feedback()
        columns = ["Rating", "Order Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Rating", y="Order Count",
                                         title="Order Distribution by Feedback")

    def fetch_and_visualize_most_active_delivery_persons(self):
        query = queries.get_most_active_delivery_persons()
        columns = ["Delivery Person Name", "Delivery Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Delivery Person Name", y="Delivery Count",
                                         title="Most Active Delivery Persons")

    def fetch_and_visualize_avg_order_value_by_restaurant(self):
        query = queries.get_avg_order_value_by_restaurant()
        columns = ["Restaurant Name", "Avg Order Value"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Avg Order Value",
                                         title="Average Order Value by Restaurant")

    def fetch_and_visualize_peak_ordering_days(self):
        query = queries.get_peak_ordering_days()
        columns = ["Weekday", "Total Orders"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Weekday", y="Total Orders", title="Peak Ordering Days")

    def fetch_and_visualize_top_restaurants_by_rating(self):
        """
        Fetch and visualize the top 5 restaurants by rating.
        """
        query = queries.get_top_restaurants_by_rating()
        columns = ["Restaurant Name", "Cuisine", "Location", "Average Rating"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Restaurant Name", y="Average Rating", 
                                        title="Top Restaurants by Rating")


    def fetch_and_visualize_most_ordered_cuisine_by_customer(self):
        query = queries.get_most_ordered_cuisine_by_customer()
        columns = ["Customer Name", "Cuisine", "Order Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "scatter", x="Customer Name", y="Order Count",
                                         title="Most Ordered Cuisine by Customer")

    def fetch_and_visualize_order_count_by_hour(self):
        query = queries.get_order_count_by_hour()
        columns = ["Hour", "Order Count"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Hour", y="Order Count", title="Order Count by Hour")

    def fetch_and_visualize_top_customer_locations(self):
        """
        Fetch and visualize the top 5 customer locations by the number of orders.
        """
        query = queries.get_top_customer_locations()
        columns = ["Customer Location", "Total Orders"]
        data = self.fetch_data(query, columns)
        return data, self.visualize_data(data, "bar", x="Customer Location", y="Total Orders", 
                                        title="Top Customer Locations")
