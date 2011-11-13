Feature: Browse images

Scenario: Browse Image Index
  Given the image "Hello World" exists
  When I visit the url "/images/"
  Then I should see the heading "Art by Date"
  And I should see the image title "Hello World"

  When I follow "Hello World"
  Then I should see the heading "Hello World"
  And I should see the image "hello_world.png"
  And I should see the image description "Hello World description"
