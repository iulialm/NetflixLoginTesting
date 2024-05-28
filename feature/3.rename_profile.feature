Feature: Rename Netflix Profile

  Background:
    Given I am logged in to Netflix

  Scenario: Rename the profile from "abc" to "Utilizator Testare"
    When I click on "Gestionarea profilurilor" button
    And I click on "abc" profile icon
    And I rename the user profile to "Utilizator Testare"
    And I scroll down
    And I click on "Salvare" button
    And I click on "Gata" button
    Then I should see a profile named "Utilizator Testare" on the browse page
