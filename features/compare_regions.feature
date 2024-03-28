Feature: Comparison of Countries in Region

  Scenario: user input a region code then click compare then load the chart 
    Given the user is on the Comparison of Countries in Region page
    When the user input "1" in the search bar
    When the user clicks the compare button1
    Then the countries for the "Latin America & Caribbean" group should be displayed1