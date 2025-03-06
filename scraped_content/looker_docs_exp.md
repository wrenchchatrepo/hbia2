# https://cloud.google.com/looker/docs/exp

Depth: 3

The `exp` function can be used in [custom filters](/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](/looker/docs/table-calculations) to get _e_ raised to the power of a value.

## Syntax

**`exp(value)`**

The `exp` function evaluates a `value` by calculating _e_ raised to the power of that value.

## Examples

The `exp` function can be used to calculate compound interest. For example, the [compound interest](https://en.wikipedia.org/wiki/Compound_interest) formula, _pe rt_, can be written as follows:
    
    
    ${investment.principal) * exp(${investment.rate} * ${investment.term})
    

## Things to know

The number _e_ (2.7182818284590...) is an important mathematical constant, which you can read more about [in this Wikipedia article](https://en.wikipedia.org/wiki/E_\(mathematical_constant\)). It has many applications, including calculating compound interest, performing certain probability calculations, generating normal distributions, and so on.