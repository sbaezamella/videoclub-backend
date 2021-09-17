-- upgrade --
CREATE TABLE IF NOT EXISTS "movie" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(170) NOT NULL,
    "year" SMALLINT NOT NULL,
    "stock" INT NOT NULL,
    "duration" INT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
);;
CREATE TABLE "movie_genre" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "genre_id" INT NOT NULL REFERENCES "genre" ("id") ON DELETE CASCADE,
    "movie_id" INT NOT NULL REFERENCES "movie" ("id") ON DELETE CASCADE);

INSERT INTO "genre" (name, created_at, updated_at) VALUES
    ('Action', now(), now()),
    ('Adventure', now(), now()),
    ('Comedy', now(), now()),
    ('Crime', now(), now()),
    ('Drama', now(), now()),
    ('Epic', now(), now()),
    ('Fantasy', now(), now()),
    ('Historical Film', now(), now()),
    ('Horror', now(), now()),
    ('Musical', now(), now()),
    ('Mystery', now(), now()),
    ('Romance', now(), now()),
    ('Satire', now(), now()),
    ('Science Fiction', now(), now()),
    ('Spy Film', now(), now()),
    ('Thriller', now(), now()),
    ('War', now(), now()),
    ('Western', now(), now());

-- downgrade --
DROP TABLE IF EXISTS "movie_genre";
DROP TABLE IF EXISTS "movie";

DELETE FROM "genre";
