Note: to create, update, and delete items you need to provide the admin token.
So you must create a superuser to make these operations.

API paths that you can want to test on insomnia:
-> GET MenuList: http://127.0.0.1:8000/restaurant/menu-items/
-> GET UserList: http://127.0.0.1:8000/auth/users/
-> GET Your own User details: http://127.0.0.1:8000/auth/users/me/
-> POST - Create new User: http://127.0.0.1:8000/auth/users/
-> POST - Obtain the User Token: http://127.0.0.1:8000/restaurant/api-token-auth/
-> POST - Create Token for the User: http://127.0.0.1:8000/auth/token/login/
-> GET Booking Tables: http://127.0.0.1:8000/restaurant/booking/tables
-> POST - Create menuItems: http://127.0.0.1:8000/restaurant/menu-items/
-> Put - Update menu-items: http://127.0.0.1:8000/restaurant/menu-items/5
-> Delete items: http://127.0.0.1:8000/restaurant/menu-items/4