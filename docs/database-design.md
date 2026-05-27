## Project
    - project_id
    - project_name
    - location
    - start_date
    - status
    - supervisor_id

## Worker
    - worker_id
    - worker_name
    - worker_phone
    - project_id
    - wage_type 
    - wage_amount

 wage_type:
    - Daily
    - Hourly
    - Fixed

## Attendance
    - worker_id
    - project_id
    - date
    - status
    - marked_by

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
    - amount
    - payment_type
    - payment_date

 payment_type:
    - Advance
    - Salary

## User
    - user_id
    - name
    - email
    - phone
    - password
    - role

 role:
    - admin
    - supervisor
    - accountant