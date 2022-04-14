https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/

C#支持结构化的注释，结构化注释可以产生XML文件，供其它文档生成工具进一步生成美观的文档。  

```csharp
/// <summary>
///  This class performs an important function.
/// </summary>
public class MyClass {}
```

指明参数和返回值
```csharp
/// <summary>
/// Enter description for operator.
/// ID string generated is "M:MyNamespace.MyClass.op_Explicit(MyNamespace.X)~System.Int32".
/// </summary>
/// <param name="myParameter">Describe parameter.</param>
/// <returns>Describe return value.</returns>
```
在注释中使用列表
```plain

<list type="bullet" | "number" | "table">
    <listheader>
        <term>term</term>
        <description>description</description>
    </listheader>
    <item>
        <term>term</term>
        <description>description</description>
    </item>
    ...
    <item>
        <term>term</term>
        <description>description</description>
    </item>
</list>
```

```plain
public class MyClass
{
    /// <summary>Here is an example of a bulleted list:
    /// <list type="bullet">
    /// <item>
    /// <description>Item 1.</description>
    /// </item>
    /// <item>
    /// <description>Item 2.</description>
    /// </item>
    /// </list>
    /// </summary>
    public static void Main()
    {
        // ...
    }
}
```

给泛型进行注释
```plain
/// <summary>A generic list class.</summary>
/// <typeparam name="T">The type stored by the list.</typeparam>
public class MyList<T>
{
   ...
}
```
# XML 注释的格式
支持两种格式：
* 行内注释：`///`
* 多行注释：`/** */`

The following tools create output from XML comments:
- [DocFX](https://dotnet.github.io/docfx/): DocFX is an API documentation generator for .NET, which currently supports C#, Visual Basic, and F#. It also allows you to customize the generated reference documentation. DocFX builds a static HTML website from your source code and Markdown files. Also, DocFX provides you the flexibility to customize the layout and style of your website through templates. You can also create custom templates.
- [Sandcastle](https://github.com/EWSoftware/SHFB): The Sandcastle tools create help files for managed class libraries containing both conceptual and API reference pages. The Sandcastle tools are command-line based and have no GUI front-end, project management features, or automated build process. The Sandcastle Help File Builder provides standalone GUI and command-line based tools to build a help file in an automated fashion. A Visual Studio integration package is also available for it so that help projects can be created and managed entirely from within Visual Studio.
- [Doxygen](https://github.com/doxygen/doxygen): Doxygen generates an on-line documentation browser (in HTML) or an off-line reference manual (in LaTeX) from a set of documented source files. There's also support for generating output in RTF (MS Word), PostScript, hyperlinked PDF, compressed HTML, DocBook, and Unix man pages. You can configure Doxygen to extract the code structure from undocumented source files.

# XML注释规范
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/documentation-comments