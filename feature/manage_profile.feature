Feature: Manage Netflix Profiles

  Background:
    Given I am logged in to Netflix

  Scenario: Add a new profile
    When I click on the "Adauga un profil" icon
    And I enter "abc" into the profile name input field
    And I click the "Continuare" button
    Then a profile named "abc" should be created