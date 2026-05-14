Feature: Statistik - Catalog Statistics
  As a user
  I want to view statistics about the catalog and favorites
  So that I can see how many books are available and how many have been favorited

  Background:
    Given the main page is open
    And page has all necessary items loaded

  Scenario: Statistik view shows total number of books
    When I navigate to "Statistik"
    Then I should see the total number of books in the catalog

  Scenario: Statistik view shows heart-marked count as zero when no favorites
    Given I have no favorite books
    When I navigate to "Statistik"
    Then I should see that 0 books have been heart-marked

  Scenario: Heart-marked count increases when a book is favorited
    Given I have no favorite books
    And I navigate to "Statistik"
    And I store the current heart-marked count
    When I favorite a book in Katalog
    And I navigate to "Statistik"
    Then the heart-marked count should have increased by 1

  Scenario: Total book count increments when a new book is added
    Given I navigate to "Statistik"
    And I note the current total book count
    When I add a new book in "Lägg till bok"
    And I navigate to "Statistik"
    Then the total book count should have incremented by 1


