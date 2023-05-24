Feature: login feature
  @login @ddt
  Scenario Outline: login with valid credentials
    Given in login page
    When entering email say "<email>" and password "<password>" in fields
    And clicking on login button
    Then account page has to open successfully
    Examples:
     | email                   |    password   |
     | bhanuone@gmail.com	   |   12341       |
     | bhanutwo@gmail.com	   |   12342       |
     | bhanuthree@gmail.com	   |   12343       |


  @login
  Scenario Outline: login with invalid credentials
    Given in login page
    When entering unknown email and "<password>" in fields
    And clicking on login button
    Then proper errorr message has to display
    Examples:
            |password|
            |12233|
  @login
  Scenario: login without valid credentials
    Given in login page
    When din't entering email password in fields
    And clicking on login button
    Then  proper errorr message has to display