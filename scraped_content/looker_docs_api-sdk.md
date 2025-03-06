# https://cloud.google.com/looker/docs/api-sdk

Depth: 3

**Note:** As of Looker 22.4, the [Looker API 4.0 is generally available](/looker/docs/api-4-ga). In Looker 23.18, the [Looker API 3.1 has been removed](/looker/docs/api-3x-deprecation).

The [Looker API](/looker/docs/api-getting-started) offers different ways to make use of an SDK. We suggest using one of our SDKs, instead of making manual requests to the API, because the SDKs handle the intricate details of authentication, parameter serialization, response serialization, and other concerns.

## Language SDKs

Looker offers an official Looker API client SDK in several languages:

  * Ruby: You can install the Ruby SDK as a gem from [rubygems.org](https://rubygems.org/gems/looker-sdk). Looker Ruby SDK documentation and source code reside on [GitHub](https://github.com/looker-open-source/looker-sdk-ruby).

  * Python: You can install the Python SDK from [pypi.org](https://pypi.org/project/looker-sdk/). Looker Python SDK documentation and source code reside on [GitHub](https://github.com/looker-open-source/sdk-codegen/tree/master/python).

  * Typescript and JavaScript: You can install the Typescript/JavaScript SDK from [npmjs.com](https://www.npmjs.com/package/@looker/sdk). Looker Typescript/JavaScript SDK documentation and source code reside on [GitHub](https://github.com/looker-open-source/sdk-codegen/tree/master/packages/sdk).

You can find source code and project examples that use SDKs to communicate with the Looker API in Looker's [SDK Example GitHub repository](https://github.com/looker-open-source/sdk-codegen/tree/main/examples).

## Generating client SDKs for the Looker API

If you are not familiar with Ruby, Python, Typescript, or Javascript, or if your company uses a different programming language, you can generate a client SDK in the language of your choice using the "legacy" mode of Looker's SDK codegen project. Instructions for doing so can be found in Looker's [SDK Codegen GitHub repository](https://github.com/looker-open-source/sdk-codegen).