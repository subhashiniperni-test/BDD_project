Feature: Verifying registration functionality

    @smoke
    Scenario: Registration with Valid data
    Given   User is on registration page
    When    User enters "username"
    And     User enter password
    And     User enters email
    And     User clicks on Signup button
    Then    User should get registered


    @sanity
    Scenario: Registration with inValid or duplicate username data
    Given   User is on registration page
    When    User enters username
    And     User enter password
    And     User enters email
    And     User clicks on Signup button
    Then    User should not get registered