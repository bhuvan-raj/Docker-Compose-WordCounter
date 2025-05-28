-- Initialize the results table
CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    text TEXT,
    word_count INT
);
