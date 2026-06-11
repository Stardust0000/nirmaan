## Project
    - project_id
    - project_name
    - location
    - start_date
    - status

## Worker
    - worker_id
    - worker_name
    - worker_phone
    - wage_type 
    - wage_amount
```
wage_type
    - Daily
    - Hourly
    - Fixed
```

## WorkerProjectAssignment
    - worker_id
    - project_id
    - joined_date
    - left_date
    - is_active
    
## Attendance
    - worker_id
    - project_id
    - date
    - status
    - marked_by 
```
marked_by is a FK to User
```
## Milestone
    - id
    - project_id
    - title
    - description
    - order
    - status
        - Pending
        - In Progress
        - Completed
    - created_by
    - completed_by
    - start_date
    - end_date
    - created_at
    - updated_at
    - completed_date

## UserProjectAssignment
    - user_id
    - project_id
    - project_role
    - is_active

## Materials
    - material_id
    - material_name
    - unit

## MaterialPurchase
    - material_id
    - quantity
    - price
    - supplier
    - puchase_date
    - project_id

## MaterialStock
    - material_id
    - project_id
    - quantity_in_stock

## WorkerPayment
    - worker_id
    - project_id
    - amount
    - payment_type
    - payment_date
```
payment_type:
    - Advance
    - Salary
```

## User
    - user_id
    - name
    - email
    - phone
    - password
    - company_role
```
role
    - project manager
    - supervisor
    - accountant
```