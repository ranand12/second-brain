# PowerShell to C# and back - Classes | Ridicurious.com

Column: https://ridicurious.com/2020/06/29/powershell-to-csharp-and-back-classes/
Processed: No
created on: May 24, 2021 10:00 PM
topics: powershell, tech-stuff

![](PowerShell%20to%20C#%20and%20back%20-%20Classes%20Ridicurious%20co%20b473254ed19e4ae7bb6f5e004ccc1ea8/PowerShell-to-C-and-Back-11.png)

# Introduction to C# and C# Classes

The purpose of this blog post is to bridge the learning and concept gap between PowerShell and C# classses, to jump start you from scripting to development. This is not deep diving in C# concepts, we will cover this in later sessions of this series.

## *Table of Contents*

- *Introduction to C# Class*
    - *Prerequisites*
    - *Overview of C# Language*
    - *Compilers, Runtime, and .NET Framework*
    - *C# Hello world using `dotnet` CLI*
    - *Interactive C# – Bridging the gap between scripting and development*
    - *C# Namespaces*
    - *C# Classes*
    - *Using C# in PowerShell*

## Prerequisites

## *[Announcement] PowerShell to C# and back Book*

*This book **bridges concept and knowledge the gap** between a scripting language like **PowerShell and modern programming language like C#**, which is a natural language of choice for People who know PowerShell.*

*Increase in adoption of software development inside Infrastructure teams, makes this the **perfect time to get started with a programming language and C# is a natural choice for people using PowerShell today.** As it fits best with the basket of **matching skillsets like Azure, Azure DevOps which will add value in your career**.*

*Download the **FREE Book Sample** from the book web page which covers all basics of C# within 50 pages – [https://leanpub.com/powershell-to-csharp](https://leanpub.com/powershell-to-csharp)*

## Video Tutorial

- *Prerequisites*
- *Overview of C# Language*
- *Compilers, Runtime, and .NET Framework*
- *C# Hello world using ‘dotnet’ CLI*
- *Interactive C# – Bridging the gap between scripting and development*
- *Using C# in PowerShell*

*[[1:12:50](https://www.youtube.com/watch?v=6aIIDF0KQqU&t=4370s)] Announcement – “PowerShell to C# and back” Book*

## Overview of C# language

C# is a powerful, flexible, and very popular modern programming language, which is simple and easy to learn and at the same time elegant as a programming language of few words.

1. **Modern** – Automatic garbage collection, lambda expressions, advanced debugging, exception handling, and most importantly security.
2. **Open source** and **Cross-platform** – .NET Core and the C# compiler are both open source and developers can build .NET applications that can run on Windows, Linux, and macOS.
3. **Object-Oriented** – Concepts like `encapsulation`, `inheritance`, and `polymorphism` are all supported, which makes development and maintenance of code easier as the project grows compared to a Procedure-oriented programming language.
4. **Type safety** – C# enforces type safety by limiting ways of interaction of objects by the object type. Only operations are permitted by type definition are applied to the object, which means type casting objects to an incompatible data type is restricted.
5. **Modular** – C# supports modular software development, that means applications can be written in chunks or pieces of code as in `functions`, `classes` etc that are reusable, easy to modify, and extensible.
6. **Secure** – Enable developers to secure their code with pre-built cryptographic algorithms like Advanced Encryption Standard (`AES`) and Data protection API (`DAPI`).
7. **Robust, Versatile** and **Evolving** – Fastest evolving programming language, from Windows client applications to pretty much anything like cross-platform client applications, Web services, distributed components, cloud applications, database applications, Internet of Things (`IoT`) and now `AI` and Machine learning ( [ML.NET](https://dotnet.microsoft.com/apps/machinelearning-ai/ml-dotnet) ).

## Compilers, Runtime, and .NET Framework

1. C# programs\source code is saved as: `FirstProgram.cs` file which is a High-level language.
2. A compiler which is a program that converts the source code into an intermediate language (`MSIL`) and saves that into a files `FirstProgram.exe` or `FirstProgram.dll`.
3. The computer processor still doesn’t understand the intermediate language and can only work on native\machine codes. So we need another program called ‘Common Language Runtime’ (`CLR`) that uses a ‘Just-In-Time’ (`JIT`) compiler to transform this intermediate language into machine code in runtime.
    
    ***NOTE:*** `.NET` is a blanket term to cover both the .NET Framework, which is an application framework library and the Common Language Runtime (`CLR`) which is the runtime in which .NET assemblies are run.
    
4. The machine code can be understood by the computers as a set of instructions to perform which low-level instructions.

![](PowerShell%20to%20C#%20and%20back%20-%20Classes%20Ridicurious%20co%20b473254ed19e4ae7bb6f5e004ccc1ea8/fig1.png)

C# source code to Machine level instructions

On a high-level these steps can also be categorized into two parts:

1. `Compile Time` – Transformation of source code to an intermediate language.
2. `Run time` – Conversion of intermediate language to machine code and executing machine code instructions.

## C# Hello world using `dotnet` CLI

1. Initialize the project, by navigating to the folder in which you like to create a project and run the following command:
    
    ```
    dotnet new console --output MyApp
    
    ```
    
    This will scaffold a folder for a basic C# console application, which will have a `program.cs` file with a `Main()` method that is the entry point of the program, from where it starts executing.
    
2. Open the `program.cs` file and modify it.
    
    ```
    using System;
    
    namespace MyApp
    {
        public class Program
        {
            public static void Main()
            {
                var name = "Prateek";
                Console.WriteLine("Hello World! from "+name);
            }
        }
    }
    
    ```
    
3. Navigate to project folder: `MyApp` and run the following commands to build and run the project for you.
    
    ```
    Set-Location .\MyApp\
    
    # build and run the project
    dotnet run -v m
    
    # load the assembly in PowerShell
    [Reflection.Assembly]::LoadFrom((Resolve-Path .\bin\Debug\netcoreapp3.1\MyApp.dll).path)
    
    # use the class and methods
    [MyApp.Program]::Main()
    
    ```
    

## Interactive C# – Bridging the gap between scripting and development

1. C# Interactive Window in Visual Studio
    
    C# Interactive Window is a simple, `REPL` (`read-eval-print-loop`) interactive programming environment that takes one user input at a time in form of commands and expressions to let you play with APIs, learn new language features and experiment by enabling us to evaluate them directly with immediate feedback as results to the user.
    
    You must have latest version of Visual Studio installed to access the Interactive Window.
    
    `Visual Studio > Menu Bar > View > Other Windows > C# Interactive`
    
2. C# interactive from command line ( `CSI.exe` )
    
    This command-line script execution engine (CSI) is also available outside Visual Studio and can be accessed from Developer Command Prompt or PowerShell for Visual Studio 2019, just by running the command: `csi` , here `csi` stands for C Sharp Interactive.
    
3. `dotnet-script` extension for .Net Core CLI
    
    A list of tool extensions for .NET Core Command-Line, also known as ‘.NET Core global tools’ can be downloaded using the dotnet CLI, but we are specifically looking for a tool called `dotnet-scripts`. This extension allows you to run C# scripts (`.csx` files) from the .NET CLI, define NuGet packages inline, edit and debug them in VS Code. More than that you get an interactive C# console to run your snippets directly from Visual Studio Code Terminal or any console like PowerShell or even Command prompt (CMD).
    
    To install the `dotnet script` extension run the following command, simply using nothing but the .NET CLI:
    
    ```
    dotnet tool install -g dotnet-script
    
    ```
    
    Once the installation is complete you can also list them and verify all the tool extension using the .NET CLI again as demonstrated in the following example and enter in an interactive REPL console by running `dotnet script`:
    
    ```
    dotnet tool list -g
    dotnet script
    
    ```
    
    Above image illustrates, that we can define variables interactively and access methods on them one line at a time. Moreover, you can combine such commands into a file and save it as `.csx` extension, which is a CSharp script file and execute the script using the syntax:
    
    ```
    dotnet script <path to .csx script file>
    
    ```
    

## C# Namespaces

- `namespace` keyword to define namespaces
- `using` directive to use the types\classes in your program
- C# namespaces are used to neatly organize classes
- Logical separation of your code and avoid any `class` naming conflicts.

Example:

```
using System;

namespace Demo
{
    class Class1
    {
        // body of Class1
    }

    class Class2
    {
        // body of Class2
    }
}

```

In the above example, `System` is a namespace defined in .Net Framework that contains the fundamental and base classes like `Console`, which has a method called `WriteLine()` that can write the specified data to the standard output stream. At the top of the program, in our example, we used `using` directive followed by the name of namespace , which allows the use of types in the namespace, without fully qualified name like `Console.WriteLine()` instead of `System.Console.WriteLine()`.

## C# Classes

- A class is a blueprint or prototype that is used to define an object.
- A Class is a `cohesive unit` of logically similar members (properties\methods)
- Classes enforce design patterns and help to organize the project as it grows.
- Object-oriented programming – Inheritance, Polymorphism, Function overloading.

### Declaring a Class

Classes are declared by using `class` keyword.

Syntax:

```
<Access Modifier> class <Name of Class>
{
    // Fields, Methods, Events, etc.
}

```

Let’s take an example, that we want to define a Car in C#, first thing we have do is create a class declaration for that using the following code snippet:

```
using System;
public class Car
{
    public string color = "red"; // Field
    public int maxSpeedMPH = 200; // Field

    public void start() // method
    {
        Console.WriteLine("Car started");
    }

    public void stop() // method
    {
        Console.WriteLine("Car stopped");
    }
}

```

Here, first thing you notice is `public` which is an access modifier, followed by the keyword `class` and the name of the class. then the body of class is enclosed in open and close brackets `{ }`.

### Members of class

Class is a programmatical representation of a real-world object that has characteristics or properties such as color, height, width and can perform functionalities such as start, stop, move, jump, etc.

All the constants, properties and methods defined inside body of a `class` are known as members of that class. Generally speaking members can be:

1. FIELD – Fields are attributes or characteristics of the class, which by default are `private` but, if they are `public` they can be accessed using class objects to change the characteristics of the Object. Like for `Car` Class, `color`, `maxSpeedMPH` are properties that can have some default value like `color = "red"`, but these can be accessed and changed on each instance of this class called object.
2. METHOD – Methods are functions defined in a class, which have access to all the members of a class. The purpose is to perform functions for the object of the class, for example `Car` Class has methods like: `start()` and `stop()`.

C# language doesn’t support any global variables or methods, that means all the entry point of the program, which the `Main()` method is also defined inside a class. More than that class is just a blueprint and we have to instantiate the class or in other words create objects of the class to access the members.

### Creating an Object of Class

Syntax:

```
<NameOfClass> NameOfObject = new <NameOfClass>();

```

Example:

```
Car tesla = new Car();

// accessing the members
tesla.color
tesla.maxSpeedMPH
tesla.start()
tesla.stop()

```

So, to create a `tesla` object from `Car` class, we will use the `new` keyword as demonstrated in the above example, and then access the members of this object using the `(.)` Dot operator in C#.

## C# in PowerShell

C# can be used in PowerShell to extend the functionalities of features of PowerShell

```
$CSharpCode = @"
using System;
namespace HelloWorld
{
    public class Program
    {
        public static void Main(){
            Console.WriteLine("Hello world!");
        }
    }
}
"@

Add-Type -TypeDefinition $CSharpCode -Language CSharp

# creating objects of the class
# throws error because we didn't mention the namespace before class
[Program]::Main()

 New-Object -TypeName HelloWorld.Program # alternatively

```

Let’s take another example and make a simple calculator in C# and use that in PowerShell

```
$CalcCode = @"
public class Calc{
    public int Add(int x,int y){
        return x+y;
    }
    public int Sub(int x,int y){
        return x-y;
    }
    public int Mul(int x,int y){
        return x*y;
    }
    // this method can be accessed without creating the object
    public static float Div(int x,int y){
        return x/y;
    }
}
"@

Add-Type -TypeDefinition $CalcCode -Language CSharp

# calling static method in Powershell
[Calc]::Div(10,2)
[Calc]::Add(1,2) # throws an exception

# calling instance method
# instantiate the class to access the non-static methods
$c = New-Object Calc
$c.Add(1,2)
$c.Mul(3,3)
$c.Div(16,4) # throws error

```

![](PowerShell%20to%20C#%20and%20back%20-%20Classes%20Ridicurious%20co%20b473254ed19e4ae7bb6f5e004ccc1ea8/sign.png)

*Author of “[PowerShell Guide to Python](https://leanpub.com/PowerShell-to-Python)“, “[Windows Subsystem for Linux (WSL)](https://leanpub.com/wsl)” and currently writing the most awaited book: “[PowerShell to C# and Back](https://leanpub.com/powershell-to-csharp)” !*

## Subscribe to our mailing list