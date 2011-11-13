Feature: Browse images

Scenario: Browse Image Index
  When I visit the url "/images/"
  Then I should see "Art by Date"
