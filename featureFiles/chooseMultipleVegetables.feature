Feature: Choose multiple vegetables
  Scenario: Go to website choose multiple vegetables and check out
    Given launch chrome browser
    When open the Green Kart website
    Then select six kilos of carrots
    Then remove three kilos from carrots
    Then add to cart carrots
    Then select two kilo of pears
    Then add to cart pears
    Then search for walnuts
    Then select one kilo of walnuts
    Then add to cart walnuts
    Then click bag button
    Then remove kilo of pears from cart
    Then check out button
    Then click place order
    Then tick terms and condition button
    Then click proceed to complete order
    And Close the browser
