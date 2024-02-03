import matplotlib.pyplot as plt
import pandas as pd
from db.models import Property
from db.database import SessionLocal
from sqlalchemy import func

def generate_price_distribution():
    db = SessionLocal()
    try:
        # Example query - adjust according to your actual data model and requirements
        query = db.query(
            Property.category_main_cb, 
            func.count().label('count'), 
            func.avg(Property.price).label('avg_price')
        ).group_by(Property.category_main_cb)

        df = pd.read_sql(query.statement, db.bind)
        df['count'] = pd.to_numeric(df['count'], errors='coerce')
        df['avg_price'] = pd.to_numeric(df['avg_price'], errors='coerce')
        df['count'] = pd.to_numeric(df['count'], errors='coerce')
        df['avg_price'] = pd.to_numeric(df['avg_price'], errors='coerce')
 
        print(df.columns)  # Correctly prints the DataFrame columns
        print(df.dtypes)  # Correct usage to print the data types of the DataFrame columns

        # Convert 'avg_price' to numeric type just in case it's not already recognized as such
        df['avg_price'] = pd.to_numeric(df['avg_price'], errors='coerce')

        # Plotting
        if 'category_main_cb' in df.columns and 'avg_price' in df.columns:
            df.plot(kind='bar', x='category_main_cb', y='avg_price')
            plt.title('Average Price Distribution by Property Type')
            plt.xlabel('Property Type')
            plt.ylabel('Average Price')
            plt.savefig('price_distribution.png')
            plt.show()
        else:
            print("Required columns not found in DataFrame")
        if not df.empty:
            df.plot(kind='bar', x='category_main_cb', y='avg_price')
    # Additional plotting configuration...
        else:
            print("DataFrame is empty. No data to plot.")

    finally:
        db.close()

if __name__ == "__main__":
    generate_price_distribution()

