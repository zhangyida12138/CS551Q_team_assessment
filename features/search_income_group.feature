Feature: Income Group Country List

  Scenario: User selects an income group and submits the form
    Given the user is on the home page
    When the user selects an "Low income" group from the dropdown
    When the user clicks the submit button
    Then the countries for the "Low income" group should be displayed
