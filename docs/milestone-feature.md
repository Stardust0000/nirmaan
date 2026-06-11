# Milestones

## Entity:
 - milestone_id
 - project_id [project FK]
 - created_by_upa [user_project_assignment FK] 
 - completed_by_upa [user_project_assignment FK]
 - title
 - description
 - order
 - status
    - Pending
    - In Progress
    - Completed
- start_date [plannned start]
- end_date [estimated completion]
- created_at [record creation timestamp]
- updated_at [record updation timestamp]
- completed_date [actual completion timestamp]


## Actions on milestones:
    - create
    - update
    - delete
    - mark
    - get_project_milestones (get list of all milestones of a project)

## Rules:
    - Supervisor can create, update, and mark a milestone of the assigned project
    - Completed milestons can be edited, this will rollback the status to incompleted
    - Milestones of a project can be reordered any time
    - A milestone can be deleted only by Project manager 

## Permissions:

|       User Role       |                Actions          |
|:---------------------:|:-------------------------------:|
|                       | Create | Update | Delete | Mark |
|:---------------------:|:------:|:------:|:------:|:----:|
| Project Manager       |  Yes   |  Yes   |  Yes   | Yes  |
| Supervisor            |  Yes   |  Yes   |  No    | Yes  |