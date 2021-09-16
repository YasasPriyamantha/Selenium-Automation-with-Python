Feature: Complete a simple order
  Scenario: Go to website and buy two kilos of carrot
    Given launch chrome browser
    When open the Green Kart website
    Then type the vegetable name (carrot) in the searchbar
    Then click one time on the plus icon
    Then click Add to cart icon
    Then click bag icon to purchase order
    Then check out button
    Then click place order
    Then tick terms and condition button
    Then click proceed to complete order
    And Close browser