# https://cloud.google.com/looker/docs/rand

Depth: 3

The `rand` function can be used in [custom filters](/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](/looker/docs/table-calculations) to return a random number between 0 and 1.

## Syntax

**`rand()`**

The `rand` function returns a random number between 0 and 1.

## Examples

The `rand` function is often used to generate random integers, sometimes to select a random sampling of data. For example, to generate an integer between 1 and 100 (inclusive) you could use:
    
    
    (floor(rand()*100)+1)
    

This expression works as follows:

  1. Uses the `rand()` function to generate a random number between 0 and 1.
  2. Multiplies by 100 to turn it into a random number between 1 and 100.
  3. Uses the [`floor`](/looker/docs/functions-and-operators#function-floor) function to round down the random number to the nearest integer, producing a random number between 0 and 99 (inclusive).
  4. Adds 1 to bring the random integer up to 1 to 100 (inclusive).

You could then filter your query to only include data below a certain random number.

## Things to know

The `rand` function produces a number with 16 decimal places, such as 0.04277424614631747.