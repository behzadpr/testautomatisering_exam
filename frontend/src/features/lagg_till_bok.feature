Feature: Lägg till bok - Add New Book
  As a user
  I want to add new books using the "Lägg till bok" view
  So that new books appear in the catalog

  Background:
    Given the main page is open
    And page has all necessary items loaded

  Scenario: Default view shows a clean form
    When I navigate to "Lägg till bok"
    Then I should see a clean form with empty title and author fields

  Scenario Outline: Submit button is disabled with incomplete input
    Given I am on the "Lägg till bok" view
    When <action>
    Then the "Lägg till ny bok" button should be disabled

    Examples:
      | action                         |
      | I have not entered anything    |
      | I enter a title but no author  |
      | I enter an author but no title |

  Scenario: Button becomes enabled when both title and author are entered
    Given I am on the "Lägg till bok" view
    When I enter a title and an author
    Then the "Lägg till ny bok" button should be enabled

  Scenario: Adding a book makes it appear in the catalog
    Given I am on the "Lägg till bok" view
    When I enter a title and an author
    And I click the "Lägg till ny bok" button
    Then the new book should appear in the catalog

  Scenario: Form clears and button disables after successful add
    Given I am on the "Lägg till bok" view
    When I enter a title and an author
    And I click the "Lägg till ny bok" button
    Then the title and author fields should be empty
    And the "Lägg till ny bok" button should be disabled


