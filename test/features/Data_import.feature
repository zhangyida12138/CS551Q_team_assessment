Feature: Data Import
  As a developer
  I want to import initial data successfully
  So that the application has data to display

  Scenario: Importing data using the parse_data script
    Given I have the initial data file ready
    When I run the parse_data.py script
    Then the data should be imported into the database without errors