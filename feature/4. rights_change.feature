Feature: Rights Changing

  Background:
    Given I am logged in to Netflix

  Scenario:
    When I click on "Gestionarea profilurilor" button
    And I click on "Utilizator Testare" profile icon
    And I press on "Editare" button
    And I enter the password "qweasdzxc"
    And I press "Continuare" button
    And I activate "Profil pentru copii"
    And I scroll down
    And I press "Salvare"
    And I click "Inapoi la Netflix"
    Then "Utilizator Testare" should be a kids profile
