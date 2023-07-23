-- name: get-user-by-username
SELECT id, 
    username, salt, 
    hashed_password, 
    created_at, 
    updated_at
FROM users
WHERE username = :username
LIMIT 1;

-- name: create-new-user<!
INSERT INTO users(
    username,
    salt, 
    hashed_password
) VALUES (
    :username,
    :salt, 
    :hashed_password
)
RETURNING id, created_at, updated_at;

-- name: update-user-by-username
UPDATE users
SET username = :new_username,
    salt = :new_salt,
    hashed_password = :new_hashed_password
WHERE username = :username
RETURNING updated_at;