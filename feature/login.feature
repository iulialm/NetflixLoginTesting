Feature: Check that the login functionality of the Netflix website is working properly

  Background:
    Given I am on the Netflix login page

  Scenario: Attempt to login with invalid username and password
    When I enter invalid username and password and click on login button
    Then I should see an error message stating "Sorry, we can't find an account with this email address. Please try again or create a new account."

  Scenario: Attempt to login with valid username and invalid password
    When I enter valid username and invalid password and click on login button
    Then I should see an error message containing "Incorrect password for iulia.almutairi@gmail.com"
    And I should see an error message containing "You can use a sign-in code, reset your password or try again"

    #avem then si and deoarece mesajul de eroare este pe doua randuri separate

  Scenario: Successful login with valid username and password
    When I enter valid username and password and click on login button
    Then I should be logged in successfully and redirected to the "Choose your profile" page

