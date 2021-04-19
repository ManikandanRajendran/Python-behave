Feature: Testing website

#  Background: setup environment
#    Given setup the driver and base url

  Scenario Outline: Verify the logo in the webpage
    Given user opens the homepage
    When user enters <username> and <password>
    And user clicks login button
    Then user should see the dashboard page

    Examples:
    | username | password |
    | admin    | admin123 |
    | test     | test     |