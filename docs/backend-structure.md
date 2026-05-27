
## backend/
    |- apps/
        |- mvp-feature/
            | - models
            | - serializers
            | - services
            | - repositories
            | - dtos
            | - views
    |- core/
        | - exceptions.py
        | - permissions.py

### models - define database structure
### serialzer - validate incoming API data
### services - business logic
### repositories - database access/queries
### dtos - control outgoing response shape
### views - receives requests, calls service, returns response