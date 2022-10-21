Feature: Cart Page as an unauthorized user

    Scenario: If user is logged in, login button should be displayed
        Given launch chrome browser
        When Flipkart home page opens
        And cart page opens
        Then login button and message should be displayed
        And Close Browser