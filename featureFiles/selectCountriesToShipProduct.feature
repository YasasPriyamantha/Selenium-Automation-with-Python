Feature: Select a country to ship the goods
  Scenario: After buying products select a country to ship the products
    Given launch chrome browser
    When open the Green Kart website
    Then type the vegetable name (carrot) in the searchbar
    Then click one time on the plus icon
    Then click Add to cart icon
    Then click bag icon to purchase order
    Then check out button
    Then click place order
    Then choose a country
    Then tick terms and condition button
    Then click proceed to complete order
    And Close browser