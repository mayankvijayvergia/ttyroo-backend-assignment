import pandas as pd
df = pd.read_csv("Tyroo-dummy-data.csv")
print(df)
df['is_free_shipping'] = df['is_free_shipping'].astype(bool)
# df['current_price'] = pd.to_numeric(df['current_price'], errors='coerce')
# df['promotion_price'] = pd.to_numeric(df['promotion_price'], errors='coerce')
numeric_cols = ['price', 'current_price', 'promotion_price', 'discount_percentage',
                'rating_avg_value', 'number_of_reviews', 'product_commission_rate',
                'bonus_commission_rate', 'platform_commission_rate', 'seller_rating']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)
text_cols = ['product_name', 'brand_name', 'description', 'availability', 'seller_name',
             'seller_url', 'business_type', 'business_area', 'venture_category1_name_en',
             'venture_category2_name_en', 'venture_category3_name_en',
             'venture_category_name_local', 'product_url', 'deeplink',
             'product_small_img', 'product_medium_img', 'product_big_img',
             'image_url_2', 'image_url_3', 'image_url_4', 'image_url_5']
df[text_cols] = df[text_cols].fillna("N/A")


import sqlite3

# Connect to (or create) a SQLite database file
conn = sqlite3.connect("products.db")
cursor = conn.cursor()


schema_sql = """
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    platform_commission_rate REAL,
    venture_category3_name_en VARCHAR(255),
    product_small_img VARCHAR(500),
    deeplink VARCHAR(500),
    availability VARCHAR(50),
    image_url_5 VARCHAR(500),
    number_of_reviews INTEGER,
    is_free_shipping BOOLEAN,
    promotion_price REAL,
    venture_category2_name_en VARCHAR(255),
    current_price REAL,
    product_medium_img VARCHAR(500),
    venture_category1_name_en VARCHAR(255),
    brand_name VARCHAR(255),
    image_url_4 VARCHAR(500),
    description TEXT,
    seller_url VARCHAR(500),
    product_commission_rate REAL,
    product_name VARCHAR(255),
    sku_id VARCHAR(100),
    seller_rating INTEGER,
    bonus_commission_rate REAL,
    business_type VARCHAR(100),
    business_area VARCHAR(100),
    image_url_2 VARCHAR(500),
    discount_percentage REAL,
    seller_name VARCHAR(255),
    product_url VARCHAR(500),
    product_id VARCHAR(100),
    venture_category_name_local VARCHAR(255),
    rating_avg_value REAL,
    product_big_img VARCHAR(500),
    image_url_3 VARCHAR(500),
    price REAL
);
"""

cursor.executescript(schema_sql)
conn.commit()

print("Table 'products' created successfully in SQLite.")

df.to_sql("products", conn, if_exists="append", index=False)
print("Data inserted into products.db")