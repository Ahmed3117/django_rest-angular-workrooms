# User
- name
- email
- password
- usename
- image

# Room
- title
- description
- room_id (random (8 numbers and characters))
- created_at (auto added)
- is_done (boolean , default = false)
- members  (ManyToMany with User)
- admin (OneToMany with User)

# Todo
- title 
- Room (OneToMany with Room)
- is_done (default = False)
- created_at

# Message
- title
- Room (OneToMany with Room)
- member (OneToMany with User )
- created_at