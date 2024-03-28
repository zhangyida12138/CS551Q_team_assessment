Feature: check detail page

  Scenario: user click the detail page and then load detail page
    Given the user is on the home page(detail)
    When the user clicks the "Aruba" detail button
    Then the details of "Aruba" should be shown
