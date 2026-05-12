Feature: Katalog - Book Catalog Management
  As a user
  I want to browse and manage my favorite books in the Katalog view
  So that I can see available books and mark my favorites

  Background:
    Given the main page is open
    And page has all necessary items loaded

  Scenario: Default view shows "Katalog" on application start
    Then I should see the Katalog view by default
    And the list of available books should be displayed

  Scenario: Low-opacity heart icon appears on hover
    Given I see a list of books
    When I hover over a book item
    Then a low-opacity heart icon should appear to the left of the book

  Scenario: Toggle book as favorite by clicking heart
    Given I see a book in the catalog
    When I click the heart icon
    Then the heart icon should appear in filled state

  Scenario: Deselect favorite by clicking heart again
    Given I have marked a book as a favorite
    When I click the heart icon
    Then the heart icon should return to unfilled state

  Scenario: Favorites persist during navigation
    Given I have marked several books as favorites in Katalog
    When I navigate to another page
    And then I return to Katalog
    Then my favorite selections should still be marked

  Scenario: Favorite in "Katalog" updates "Mina böcker" list
    Given I see a book in the catalog
    When I click the heart icon
    Then the book should appear in my "Mina böcker" list

