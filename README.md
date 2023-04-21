## BinaryNinja NodeJS NAPI Types Importer

### Why

The embedded `Import Header File` seems can't handle the `NAPI` types because they are [/DELAYLOAD (Delay Load Import) | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/build/reference/delayload-delay-load-import?view=msvc-170).

So I wrote this plugin to import the `NAPI` types.