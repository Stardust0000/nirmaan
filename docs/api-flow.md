## Admin 

Admin adds a project -> System validates admin role -> System validates required fields -> System checks if project does not already exist -> System creats a new project -> Stores project in database -> returns success response

## Supervisor 

Supervisor marks attendance -> System validates supervisor role -> System checks if worker exists and is active -> System checks if attendance is not aleady marked for the today -> Stores attendance -> Returns success response

## Accountant 

Accountant enters purchase -> System validates accountant role -> System validates material exists -> System creates purchase entry -> Updates material stock -> Stores updates stock -> Returns updated stock response

## Signup

User enters signup details -> System validates required fields ->System validates email format and password rules -> System checks if user aleady exists -> if user exists, return error response -> System hashes password -> System creates new user -> stores user in database -> System generates auth token -> Returns success response and token -> Frontend redirects user to login page.

## Login

User enters email and password -> System finds user by email -> System verifies password hash -> System generates access token/session -> System fetches user role -> Returns user details and access token -> Frontend opens respective dashboard

User selects "remember me" -> User enters email and password -> System finds user by email -> System verifies password hash-> System generates long-lived refresh token -> System generates access token/session -> Returns tokens and user role -> Frontend securely stores refresh token -> Frontend opens respective dashboard

