# BinaryNinja NodeJS NAPI Types Importer
Author: **Cesaryuan**

A plugin that imports NodeJS N-API Types.

## Description:

The embedded `Import Header File` seems can't handle the `NAPI` types because they are [/DELAYLOAD (Delay Load Import) | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/build/reference/delayload-delay-load-import?view=msvc-170).

So I wrote this plugin to import the `NAPI` types.

Also see: [DLL 延迟加载与资源释放 - nice_0e3 - 博客园](https://www.cnblogs.com/nice0e3/p/15178232.html)

## Minimum Version

This plugin requires the following minimum version of Binary Ninja:

 * 3000

## License

This plugin is released under an [MIT license](./license).

## Metadata Version

2
