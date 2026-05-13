Feature: Mina böcker - My Favorite Books
  As a user
  I want to manage and review my favorite books in the "Mina böcker" view
  So that I can find and review my selected favorites in one place

  Background:
    Given the main page is open
    And page has all necessary items loaded

  Scenario: Default message shown when no favorites are selected
    Given I have no favorite books
    When I navigate to "Mina böcker"
    Then I should see a default message indicating no favorites have been added

  Scenario: Favorite books are listed in "Mina böcker"
    Given I have marked several books as favorites in Katalog
    When I navigate to "Mina böcker"
    Then I should see all my favorited books listed

  Scenario: Deselecting a heart in "Katalog" removes book from "Mina böcker"
    Given I have marked a book as a favorite
    And I can see the book in "Mina böcker"
    When I navigate to Katalog
    And I click the heart icon on that book to deselect it
    Then the book should no longer appear in "Mina böcker"

