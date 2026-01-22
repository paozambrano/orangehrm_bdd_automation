Feature: Admin User Management
    As an Admin user
    I want to manage system users
    So that I can keep the employee ddirectory updated

    Background: Login to the system
        Given I navigate to the OrangeHRM login page
        When I login with username "Admin" and password "admin123"
        Then I should be on the Dashboard page

    @smoke @admin 
    Scenario Outline: Add and verify a new system user
        Given I navigate to the Admin User Management page
        When I click on the Add button
        And I fill the user form with "<user_role>", "<employee_name>", "<username>" and "<password>"
        And I click on Save
        Then I should be able to find "<username>" in the user table

        Examples:
            |user_role  |   employee_name  | username      | password      |
            |Admin      |   John A Doe     | PaoTester_01  | Admin123!     |
            |ESS        |   John A Doe     | PaoTester_04  | Admin123!     |