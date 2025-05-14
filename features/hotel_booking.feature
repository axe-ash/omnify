Feature: Hotel Booking Automation

  Scenario: Apply coupon and verify discount on hotel booking
    Given I open the hotel booking application
    When I search for hotels in "New York" from "2025-04-10" to "2025-04-15"
    And I select the first hotel from the search results
    And I apply the coupon code "SUMMER25"
    Then I should see the discount applied correctly
    And I proceed to checkout without completing payment
