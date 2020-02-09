CREATE SCHEMA airbnb_dev;
SET SEARCH_PATH = 'airbnb_dev';

CREATE TABLE places (
    id INTEGER,
    name TEXT,
    host_id INTEGER,
    host_name TEXT,
    neighbourhood_group TEXT,
    neighbourhood  TEXT,
    latitude TEXT,
    longitude TEXT,
    room_type TEXT,
    price TEXT,
    minimum_nights TEXT,
    number_of_reviews TEXT,
    last_review TEXT,
    reviews_per_month TEXT,
    calculated_host_listings_count TEXT,
    availability_365 TEXT
);

\copy places from '/data/AB_NYC_2019.csv' DELIMITER ',' CSV HEADER;
