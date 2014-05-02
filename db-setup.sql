CREATE TABLE images (
  image_id    bigserial primary key,
  image_name  varchar(64) NOT NULL,
  image_hash  varchar(64) NOT NULL,
  image_date  timestamp default NULL
);

