Feature: Search bar

  Background:
    Given I am logged in to Netflix


  Scenario:
    When I enter in "Utilizator Testare" profile
    And I click on search icon
    And I type "Film inexistent"
    Then An error message contains "Căutarea pentru „Film inexistent” nu a returnat rezultate." should be displayed on the screen


  Scenario:
    When I click on search box
    And Delete the written content
    And I type "Om vs. albină"
    Then I should be able to see the result on the screen