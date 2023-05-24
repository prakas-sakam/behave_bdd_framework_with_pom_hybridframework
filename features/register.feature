Feature: register feature
  @register @retest
  Scenario: registering with valid details
    Given i am at register page
    When entering all below details for to register
          |f_name |l_name |phone|password|confirm_pass|
          |bhanu  |reddy  |1234 |1111    |1111        |

    And clicking on register button
    Then registration has to be succesfully

  @register @retest
  Scenario: registering with invalid details
    Given i am at register page
    When entering all below same email details for to register
           |f_name |l_name |email      |phone|password|confirm_pass|
          |bhanu  |reddy  |brooo@gmail.com |1234 |1111    |1111        |
    And clicking on register button
    Then proper er message has to display

@register @retest
  Scenario: registering without valid details
    Given i am at register page
    When entering nodetails register
    And clicking on register button
    Then proper eerror message has to display