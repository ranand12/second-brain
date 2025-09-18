# Terraform Best Practices For Writing Clean, Readable, And Maintainable Code | Build5Nines

Column: https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/
Processed: No
created on: March 7, 2023 8:28 AM
topics: devops, linux, tech-stuff, terraform

![](Terraform%20Best%20Practices%20For%20Writing%20Clean,%20Readab%20726a201f79414cee83c6a3d981603784/Terraform_IAC_Featured_Image_2.jpg)

HashiCorp Terraform has become one of the most popular [infrastructure as code (IaC)](https://build5nines.com/what-is-infrastructure-as-code/) tools. Terraform allows you to define and manage your infrastructure deployments across one or multiple cloud providers through code. This makes it easier to manage, version, and maintain infrastructure deployments. Writing Terraform code can be challenging, especially if you are not familiar with best practices for writing clean, readable, and maintainable code. Writing clean, readable, and maintainable Terraform code is crucial for any [DevOps Engineer](https://build5nines.com/how-to-become-a-devops-engineer/) or [Site Reliability Engineer (SRE)](https://build5nines.com/what-is-a-site-reliability-engineer-sre/) who wants to build scalable infrastructure.

In this article, we will cover the best practices for writing clean, readable, and maintainable Terraform code. We will also explore how some of the principles and practices of “The Pragmatic Programmer” and “Clean Code” books that teach best practices of writing clean, readable, and maintainable source code apply to writing HashiCorp Terraform infrastructure as code projects.

Let’s look at how some of the most popular best practices of writing software can be applied to writing infrastructure as code with HashiCorp Terraform!

- [How the “Clean Code” Principles Apply to Writing Terraform Code](https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/#how_the_clean_code_principles_apply_to_writing_terraform_code)
    - [Single Responsibility Principle (SRP)](https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/#single_responsibility_principle_srp)
    - [Open/Closed Principle (OCP)](https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/#openclosed_principle_ocp)
    - [Dependency Inversion Principle (DIP)](https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/#dependency_inversion_principle_dip)
    - [Code Smells](https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/#code_smells)
- [Conclusion](https://build5nines.com/terraform-best-practices-for-writing-clean-readable-and-maintainable-code/#conclusion)

## Best Practices for Writing Clean, Readable, and Maintainable Terraform Code

### Use a Consistent and Meaningful Naming Convention

Naming conventions play an important role in making your code easy to read and understand. Use a consistent naming convention for all your Terraform resources, modules, inputs, variables, and outputs. Names should be meaningful and descriptive, and should accurately reflect the purpose of the Terraform resource.

### Use Modules to Organize Your Code

[Terraform modules](https://build5nines.com/terraform-modules-create-reusable-infrastructure-as-code/) allow you to organize your code into reusable components. Modules can be used to define a set of resources that can be easily shared and used in other parts of your code. Using modules can help you write clean, maintainable, and reusable code.

### Use Variables and Inputs to Make Your Terraform Code More Flexible

Terraform variables and inputs [allow you to parameterize your Terraform code](https://build5nines.com/use-terraform-input-variables-to-parameterize-infrastructure-deployments/), making it more flexible and easier to maintain. Use variables to define configurable values that can be easily changed. This can help you avoid hardcoding values, and will make your code more easily reusable.

### Use Comments to Document Your Terraform Code

Comments play an important role in making your code easy to understand. Use comments to document your code, explaining what the code does and why it is important. Comments can also be used to provide additional context and explain any complex logic.

### Use Version Control to Manage Your Codebase

Just as with any other codebase, using version control will help you manage your codebase, track changes, and collaborate with other engineers. Using version control system like Git, GitHub, or Azure DevOps will help manage your Terraform code over time. This can help you track changes, collaborate with other engineers, and even roll back changes if necessary.

## How the “Pragmatic Programmer” Concepts Apply to Writing Terraform Code

The “Pragmatic Programmer: From Journeyman to Master” is a very influential book that contains a set of programming and software engineering principles and best practices. The book was written by Andrew Hunt and David Thomas, and published in 1999. Even though the book is over 20 years old at this point, it still provides great insights and best practice ideas on how to write better code.

The following are only a few of the many concepts from “Pragmatic Programmer” that apply to writing HashiCorp Terraform code:

### DRY (Don’t Repeat Yourself)

DRY is a principle that states that you should avoid duplicating code. In Terraform, you can use modules to avoid duplicating code. [Terraform modules](https://build5nines.com/terraform-modules-create-reusable-infrastructure-as-code/) allow you to define a set of resources that can be easily reused across your codebase and help eliminate code duplication. The second time you find your self repeating a block of Terraform code, perhaps it’s the appropriate time to abstract it out as a Terraform module for code reuse.

### KISS (Keep It Simple, Stupid)

KISS is a principle that states that you should keep your code simple and easy to understand. In Terraform, you can use variables to make your code more flexible and easier to understand. You can also use descriptive resource names, as well as comments, to write code that is self explainable as to what it does and what it’s for.

### YAGNI (You Ain’t Gonna Need It)

YAGNI is a principle that states that you should only implement what you need, and avoid adding unnecessary complexity to your code. In Terraform, you should only define resources that are necessary for your infrastructure. Avoid adding unnecessary resources that may increase complexity and confuse other engineers who are working on the codebase.

Also, creating [Terraform modules](https://build5nines.com/terraform-modules-create-reusable-infrastructure-as-code/) only when necessary will help reduce the amount of code to write and maintain. Not everything needs to be written as a Terraform module. The first time you write a block of Terraform code it’s fine to write it in isolation. The second time, perhaps it’s appropriate to abstract it out as a module for reuse.

## How the “Clean Code” Principles Apply to Writing Terraform Code

“Clean Code” is a book by Robert C. Martin (aka “Uncle Bob”) that contains a set of principles and best practices for writing clean, maintainable, and reusable code.

The following are a few of the principles from “Clean Code” that apply to writing HashiCorp Terraform code:

### Single Responsibility Principle (SRP)

SRP is a principle that states that a module or function should have only one responsibility. In HashiCorp Terraform projects, you can use [Terraform modules](https://build5nines.com/terraform-modules-create-reusable-infrastructure-as-code/) to define a set of resources that have a single responsibility. This can help you write clean, maintainable, and reusable code.

### Open/Closed Principle (OCP)

OCP is a principle that states that a module or function should be open for extension but closed for modification. In HashiCorp Terraform projects, you can use [Terraform modules](https://build5nines.com/terraform-modules-create-reusable-infrastructure-as-code/) to define a set of resources that can be easily extended without modifying the existing code. This can help you write maintainable and reusable code.

### Dependency Inversion Principle (DIP)

DIP is a principle that states that high-level modules should not depend on low-level modules. In Terraform projects, you can use Terraform modules to define a set of resources that are independent of other resources. This can help you avoid tight coupling between resources and make your code more maintainable.

### Code Smells

Code smells are indicators of poor code quality. In Terraform projects, code smells can include duplication of code, hardcoding of values, non-descriptive resource and variable names, and the lack of comments or documentation. Writing clean code requires all these best concepts to be followed as best as possible.

## Conclusion

Applying the software development best practices from this article to HashiCorp Terraform code, you can write clean, readable, and maintainable Terraform code that is easy to manage, scale, and extend. Writing clean, readable, and maintainable Terraform code is crucial for any [DevOps Engineer](https://build5nines.com/how-to-become-a-devops-engineer/) or [Site Reliability Engineer (SRE)](https://build5nines.com/what-is-a-site-reliability-engineer-sre/) who wants to build scalable infrastructure. Remember to keep your code simple, modular, and well-documented, and to avoid premature optimization. Keep in mind that writing clean, readable, and maintainable Terraform code is a continuous process, and it requires constant learning, practice, and improvement.

### About the Author