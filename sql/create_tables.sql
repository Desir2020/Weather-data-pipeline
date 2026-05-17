CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(150) NOT NULL,
    country VARCHAR(10),

    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    recorded_at TIMESTAMP NOT NULL,

    weather_main VARCHAR(50),
    weather_description TEXT,

    temperature DOUBLE PRECISION NOT NULL,
    feels_like DOUBLE PRECISION,
    temp_min DOUBLE PRECISION,
    temp_max DOUBLE PRECISION,

    humidity INT,
    pressure INT,
    wind_speed DOUBLE PRECISION,

    inserted_at TIMESTAMP DEFAULT NOW()
);