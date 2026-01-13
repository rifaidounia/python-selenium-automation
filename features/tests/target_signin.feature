Feature: Signin page

  Scenario: User can access signin page from Account button
    Given Open Target main page
    When Click on Account button
    When Click on Sign in button
    Then sign in button is displayed