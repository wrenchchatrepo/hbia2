I think we need to review the plan. This is what I assumed the approach for scraping these websites. 

```markdown
# Scrape all the text from a website url given an objective of Depth=3 constrained by a set of rules, format in .md and .txt
## Depth = 3
## Rules
### 1. Start with a baseline url. This is Rules 1 and Depth 1. 	
+ https://cloud.google.com/looker/docs/
### 2. Set the url that all subsequent urls must match. This is Rule 2.
+ https://cloud.google.com/looker/docs/
### 3. Ignore header and footer. This is Rule 3. 
### 4. Ignore any duplicates with previous urls. This is Rule 4.
### 5. Ignore any urls without the same baseline. This is Rule 5. 
### 6. Grab all the links from the left-hand navigation panel and main page.
### 7. Remainig URLs are Depth 2.
+ https://cloud.google.com/looker/docs/looker-releases
+ https://cloud.google.com/looker/docs/find-and-organize-content
+ https://cloud.google.com/looker/docs/retrieve-and-chart-data
+ ...
+ https://cloud.google.com/looker/docs/looker-core-mobile-app
### 8. Repeat process to acquire Depth 3. 
### 9. Here is an example.
+ Baseline URL: https://cloud.google.com/looker/docs/
	+ Depth 2: https://cloud.google.com/looker/docs/looker-core-create-oauth
		+ Ignore:	https://cloud.google.com/looker/docs/looker-core-create-oauth#required_roles (this a duiplicate--all of data on this page is on the parent page. we know we can ignore this url because this child url contains `#`)
			+ Depth 3: https://cloud.google.com/looker/docs/looker-core-oauth-authentication
				+ Ignore: https://cloud.google.com/iam/docs/creating-custom-roles (we know we can ignore this url because the baseline is different)
### 10. If there are no urls that meet our requiremens on a given page, we can stop that process and move no to the next. Once all processes have stopped, we know we're done.  	
```

First let's map the baseline url (https://cloud.google.com/looker/docs/) to make sure we are on the right path. We can see the urls and the parente/child relaionships. We'll need a progress bar based on the number of pages to scrape. When we map the url it should look something like this:

baselineurl.com
	baselineurl.com/ok1
		baselineurl.com/ok1/still-ok1
		baselineurl.com/ok1/still-ok2
		baselineurl.com/ok1/still-ok3
	baselineurl.com/ok2
		baselineurl.com/ok2/still-ok4
		baselineurl.com/ok1/still-ok3 X Duplicate
		somethingelse.com X Wronge baseline
	baselineurl.com/ok3
		baselineurl.com/ok3/still-ok5
		baselineurl.com/ok3/still-ok5#dupe X dupe reference to /still-ok5

1pg	3pg 5pgs (ignoring 2 dupes, 1 wronge baseline)
so we have 5 pages not 8.

so first we need a map of https://cloud.google.com/looker/docs/, then we need a progress bar, then we need to scrape the map. we'll evaluate the results and hopefull expand the process to the other baseline urls. 

thoughts?	

