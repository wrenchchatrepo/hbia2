# https://cloud.google.com/looker/docs/extension-overview

Depth: 3

> These extensions are different from [LookML extends/extensions](/looker/docs/reusing-code-with-extends), the code organization syntax used when modeling data in LookML.

Looker extensions allow you to provide highly customized and integrated experiences to your Looker instance's users.

A dedicated Looker page becomes your canvas, with a wide array of tools at your disposal, including the ability to:

  * Run JavaScript code 
  * Access the Looker APIs through a pre-authenticated client
  * Leverage [Looker components](/looker/docs/components) for seamless UI
  * Make HTTP calls from the client or through a convenient server proxy
  * Authenticate with third-party services via OAuth
  * Use additional [extension framework features](/looker/docs/intro-to-extension-framework#extension_framework_features)

Simultaneously, detailed sandboxing controls and built-in user permissioning allow your instance's administrators to be confident about what data is accessible to application developers and end users.

## Using extensions

The first step to using a Looker extension is authoring a JavaScript-based client-side application that uses the APIs that are exposed by Looker's extension framework.

The quickest way to get up and running with such an application is with our [`create-looker-extension`](https://www.npmjs.com/package/create-looker-extension) command line tool, which will set you up with a boilerplate codebase, including the necessary build tooling to bundle your application code via webpack. The tool lets you choose between either JavaScript or TypeScript, and lets you select whether to use React.

Once your codebase is ready to go, you can load it into your Looker instance in one of three ways:

  * During development, you can use a [URL](/looker/docs/reference/param-manifest-application#url) to reference a locally hosted web server for quick and convenient development.
  * You can build a JS bundle and [load the file through your LookML project](/looker/docs/reference/param-manifest-application#file).
  * You can deploy the JS file to a remote server or content delivery network (CDN) and then [reference it by URL](/looker/docs/reference/param-manifest-application#url). This option is often the most convenient when used together with continuous deployment automation from your extension's codebase.

## Try it out

Want to see Looker extensions in action before writing any code? Several [Looker-published extensions](https://marketplace.looker.com/marketplace/directory?Type=applications) can be [installed with one click](/looker/docs/marketplace) into your Looker instance from the Looker Marketplace.