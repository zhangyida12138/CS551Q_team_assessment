Feature: Comparison of Countries

  Scenario: user chooses two countries to compare and the chart will show it. 
    Given the user is on the Compare Countries Rural Population page
    When the user selects "Aruba(ABW)" from the dropdown1
    When the user selects "Africa Eastern and Southern(AFE)" from the dropdown2
    When the user clicks the compare button
    Then the comparison for "Aruba(ABW)" and "Africa Eastern and Southern(AFE)" should be displayed
