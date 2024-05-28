Feature: Adding movie in favorite list

  Scenario:
    Given I am on result search page
    When I click on the movie banner
    And I click "+" button
    And I click "X" button
    And I click on " Lista mea" tab
    Then I should see "Om vs. albină" in my list

