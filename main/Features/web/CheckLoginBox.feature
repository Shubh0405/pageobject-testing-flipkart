Feature: Check Login Box

    Scenario: Login text in home page
        Given launch chrome browser
        When Flipkart home page opens
        Then Verify Login Text is Present
        And Close Browser

    Scenario: Verify username field in home page
        Given launch chrome browser
        When Flipkart home page opens
        Then Verify username field is present
        And Close Browser

    Scenario: Verify password field in home page
        Given launch chrome browser
        When Flipkart home page opens
        Then Verify password field is present
        And Close Browser