Feature: search feature
  @search1
  Scenario: searching for valid product
    Given i am in home page
    When entering valid product say "HP" in search box field
    And clicking on search icon
    Then valid product has to display
  @search
  Scenario: searching for invalid product
    Given i am in home page
    When entering invalid product say "hp" in search box field
    And clicking on search icon
    Then proper error message has to display
  @search
  Scenario: searching for nothing
    Given i am in home page
    When no product in search box field
    And clicking on search icon
    Then proper error message has to display
