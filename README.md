Table of Contents:
- [PythonExercises](#pythonexercises)
  - [Repository created to track my progress on Python upskilling and using it with many different technologies for DevSecOps approach.](#repository-created-to-track-my-progress-on-python-upskilling-and-using-it-with-many-different-technologies-for-devsecops-approach)
- [codingbat.com](#codingbatcom)
  - [Website that has available Python practice examples with sandbox and unit tests, that each script to practice needs to pass](#website-that-has-available-python-practice-examples-with-sandbox-and-unit-tests-that-each-script-to-practice-needs-to-pass)
- [Google Python Style Guide](#google-python-style-guide)
    - [URL: https://google.github.io/styleguide/pyguide.html](#url-httpsgooglegithubiostyleguidepyguidehtml)
  - [Python Language Rules](#python-language-rules)
    - [Lint](#lint)
    - [Imports](#imports)
    - [Packages](#packages)
    - [Exceptions](#exceptions)
    - [Mutable Global State](#mutable-global-state)
    - [Nested/Local/Inner Classes and Functions](#nestedlocalinner-classes-and-functions)
    - [Comprehensions \& Generator Expressions](#comprehensions--generator-expressions)
    - [Default Iterators and Operators](#default-iterators-and-operators)
    - [Genrators](#genrators)
    - [Lambda Functions](#lambda-functions)
    - [Conditional Expressions](#conditional-expressions)
    - [Default Argument Values](#default-argument-values)
    - [Properties](#properties)
    - [True/False Evaluations](#truefalse-evaluations)
    - [Lexical Scoping](#lexical-scoping)
    - [Function and Method Decorators](#function-and-method-decorators)
    - [Threading](#threading)
    - [Power Features](#power-features)
    - [Modern Python: from \_\_future\_\_ imports](#modern-python-from-__future__-imports)
    - [Type Annotated Code](#type-annotated-code)
  - [Python Style Rules](#python-style-rules)
    - [Semicolons](#semicolons)
    - [Line length](#line-length)
    - [Parentheses](#parentheses)
    - [Indentation](#indentation)
    - [Shebang Line](#shebang-line)
    - [Comments and Docstrings](#comments-and-docstrings)
    - [Strings](#strings)
    - [TODO Comments](#todo-comments)
    - [Imports formatting](#imports-formatting)
    - [Statements](#statements)
    - [Getters and Setters](#getters-and-setters)
    - [Naming](#naming)
    - [Main](#main)
    - [Function length](#function-length)
    - [Type Annotations](#type-annotations)
      - [NoneType](#nonetype)
      - [Type Aliases](#type-aliases)
      - [Tuples vs Lists](#tuples-vs-lists)
      - [String types](#string-types)
---
# PythonExercises

About me:<br/>
Repository created to track my progress on Python upskilling and using it with many different technologies for DevSecOps approach.
---

# codingbat.com
URL: <https://codingbat.com/python>
Website that has available Python practice examples with sandbox and unit tests, that each script to practice needs to pass
---

# Google Python Style Guide

### URL: <https://google.github.io/styleguide/pyguide.html>

Python is the main dynamic language used at Google. This style guide is a list of dos and don’ts for Python programs. Many teams use the Black or Pyink auto-formatter to avoid arguing over formatting.

## Python Language Rules

### Lint

Make sure you run pylint on your code (***pylint ./python_file.py*** or ***pylint ./dir***).<br/>
You can get a list of pylint warnings by doing: ***pylint --list-msgs***<br/>
To get more information on a particular message, use: ***pylint --help-msg=invalid-name*** <br/>

pylint is a tool for finding bugs and style problems in Python source code. It finds problems that are typically caught by a compiler for less dynamic languages like C and C++.<br/>

### Imports

Use import statements for packages and modules only, not for individual classes or functions.
Use import x for importing packages and modules.

* Use from x import y where x is the package prefix and y is the module name with no prefix.
* Use from x import y as z in any of the following circumstances:
  * Two modules named y are to be imported.
  * y conflicts with a top-level name defined in the current module.
  * y conflicts with a common parameter name that is part of the public API (e.g., features).
  * y is an inconveniently long name.
  * y is too generic in the context of your code (e.g., from storage.file_system import options as fs_options).
* Use import y as z only when z is a standard abbreviation (e.g., import numpy as np).

For example the module sound.effects.echo may be imported as follows:

```python
from sound.effects import echo
...
echo.EchoFilter(input, output, delay=0.7, atten=4)
```

### Packages

Import each module using the full pathname location of the module. <br/>
***Pros:***Avoids conflicts in module names or incorrect imports due to the module search path not being what the author expected. Makes it easier to find modules. <br/>
***Cons:*** Makes it harder to deploy code because you have to replicate the package hierarchy. Not really a problem with modern deployment mechanisms. <br/>

### Exceptions

Exceptions are allowed but must be used carefully. Exceptions are a means of breaking out of normal control flow to handle errors or other exceptional conditions.

* Make use of built-in exception classes when it makes sense. For example, raise a ValueError to indicate a programming mistake like a violated precondition (such as if you were passed a negative number but required a positive one).
* Libraries or packages may define their own exceptions. When doing so they must inherit from an existing exception class. Exception names should end in Error and should not introduce repetition (*foo.FooError*).
* Minimize the amount of code in a *try/except* block. The larger the body of the try, the more likely that an exception will be raised by a line of code that you didn’t expect to raise an exception. In those cases, the try/except block hides a real error.
* Use the *finally* clause to execute code whether or not an exception is raised in the try block. This is often useful for cleanup, i.e., closing a file.

### Mutable Global State

Avoid mutable global state.<br/>

In those rare cases where using global state is warranted, mutable global entities should be declared at the module level or as a class attribute and made internal by prepending an _ to the name. If necessary, external access to mutable global state must be done through public functions or class methods. <br/>

Please explain the design reasons why mutable global state is being used in a comment or a doc linked to from a comment. <br/>
**Answer:** Module-level constants are permitted and encouraged. For example: _MAX_HOLY_HANDGRENADE_COUNT = 3 for an internal use constant or SIR_LANCELOTS_FAVORITE_COLOR = "blue" for a public API constant. Constants must be named using all caps with underscores.

### Nested/Local/Inner Classes and Functions

Nested local functions or classes are fine when used to close over a local variable. Inner classes are fine.<br/>
Avoid nested functions or classes except when closing over a local value other than self or cls. Do not nest a function just to hide it from users of a module. Instead, prefix its name with an ```_``` at the module level so that it can still be accessed by tests.

(https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes)
Function and method arguments:
* Always use self for the first argument to instance methods(i.e.: def \_\_init\_\_(self, ...):).
* Always use cls for the first argument to class methods (@classmethod), i.e.: 
```python
@classmethod
def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'load_data_source') and 
            callable(subclass.load_data_source) and 
            hasattr(subclass, 'extract_text') and 
            callable(subclass.extract_text) or 
            NotImplemented)
```

### Comprehensions & Generator Expressions

**Definition:** List, Dict, and Set comprehensions as well as generator expressions provide a concise and efficient way to create container types and iterators without resorting to the use of traditional loops, map(), filter(), or lambda.

Okay to use for simple cases.<br/>Each portion must fit on one line: mapping expression, for clause, filter expression. Multiple for clauses or filter expressions are not permitted. Use loops instead when things get more complicated.<br/>

### Default Iterators and Operators

Use default iterators and operators for types that support them, like lists, dictionaries, and files. <br/>

The default iterators and operators are simple and efficient. They express the operation directly, without extra method calls. A function that uses default operators is generic. It can be used with any type that supports the operation.<br/>
You can’t tell the type of objects by reading the method names (unless the variable has type annotations). This is also an advantage.

### Genrators

**Definition:** A generator function returns an iterator that yields a value each time it executes a yield statement. After it yields a value, the runtime state of the generator function is suspended until the next value is needed. <br/>

Use generators as needed. Use “Yields:” rather than “Returns:” in the docstring for generator functions. If the generator manages an expensive resource, make sure to force the clean up.

(https://prutor.ai/when-to-use-yield-instead-of-return-in-python/)
The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.

### Lambda Functions

**Definition:** Lambdas define anonymous functions in an expression, as opposed to a statement.<br/>
Okay for one-liners. Prefer generator expressions over map() or filter() with a lambda. If the code inside the lambda function is longer than 60-80 chars, it’s probably better to define it as a regular nested function.<br/>
For common operations like multiplication, use the functions from the operator module instead of lambda functions. For example, prefer operator.mul to lambda x, y: x * y.

### Conditional Expressions

**Definition:** Conditional expressions (sometimes called a “ternary operator”) are mechanisms that provide a shorter syntax for if statements. For example: x = 1 if cond else 2. <br/>

Okay to use for simple cases. Each portion must fit on one line: true-expression, if-expression, else-expression. Use a complete if statement when things get more complicated.

### Default Argument Values

**Definition:** You can specify values for variables at the end of a function’s parameter list, e.g., def foo(a, b=0):. If foo is called with only one argument, b is set to 0. If it is called with two arguments, b has the value of the second argument. <br/>

As Python does not support overloaded methods/functions, default arguments are an easy way of “faking” the overloading behavior. **Do not use mutable objects as default values in the function or method definition.**,<br/>
<https://google.github.io/styleguide/pyguide.html#s2.9-generators:~:text=2.12-,Default%20Argument%20Values,-Okay%20in%20most>

### Properties

Properties may be used to control getting or setting attributes that require trivial computations or logic. Property implementations must match the general expectations of regular attribute access: that they are cheap, straightforward, and unsurprising.<br/>

Properties are allowed, but, like operator overloading, should only be used when necessary and match the expectations of typical attribute access.

For example, using a property to simply both get and set an internal attribute isn’t allowed: there is no computation occurring, so the property is unnecessary (make the attribute public instead). In comparison, using a property to control attribute access or to calculate a trivially derived value is allowed: the logic is simple and unsurprising.

Properties should be created with the *@property* decorator. Manually implementing a property descriptor is considered a power feature.

### True/False Evaluations

**Definition:** Python evaluates certain values as False when in a boolean context. A quick “rule of thumb” is that all “empty” values are considered false, so 0, None, [], {}, '' all evaluate as false in a boolean context.

Use the “implicit” false if possible, e.g., if foo: rather than if foo != []:.

```python
if not users:
         print('no users')

     if i % 10 == 0:
         self.handle_multiple_of_ten()

     def f(x=None):
         if x is None:
             x = []
```

### Lexical Scoping

**Definition:**  A nested Python function can refer to variables defined in enclosing functions, but cannot assign to them. Variable bindings are resolved using lexical scoping, that is, based on the static program text. Any assignment to a name in a block will cause Python to treat all references to that name as a local variable, even if the use precedes the assignment. If a global declaration occurs, the name is treated as a global variable.

An example of the use of this feature is:

```python
def get_adder(summand1: float) -> Callable[[float], float]:
    """Returns a function that adds numbers to a given number."""
    def adder(summand2: float) -> float:
        return summand1 + summand2

    return adder
```

### Function and Method Decorators

Use decorators judiciously when there is a clear advantage. Avoid staticmethod and limit use of classmethod. Decorators should follow the same import and naming guidelines as functions. Decorator pydoc should clearly state that the function is a decorator.

* Write unit tests for decorators.
* Never use @staticmethod unless forced to in order to integrate with an API defined in an existing library. Write a module-level function instead.
* Use @classmethod only when writing a named constructor, or a class-specific routine that modifies necessary global state such as a process-wide cache.

### Threading

Do not rely on the atomicity of built-in types.

While Python’s built-in data types such as dictionaries appear to have atomic operations, there are corner cases where they aren’t atomic (e.g. if **hash** or **eq** are implemented as Python methods) and their atomicity should not be relied upon. Neither should you rely on atomic variable assignment (since this in turn depends on dictionaries).

Use the queue module’s Queue data type as the preferred way to communicate data between threads. Otherwise, use the threading module and its locking primitives. Prefer condition variables and threading.Condition instead of using lower-level locks.

### Power Features

**Definition:** Python is an extremely flexible language and gives you many fancy features such as custom metaclasses, access to bytecode, on-the-fly compilation, dynamic inheritance, object reparenting, import hacks, reflection (e.g. some uses of getattr()), modification of system internals, **del** methods implementing customized cleanup, etc.

Avoid these features.

### Modern Python: from \_\_future\_\_ imports

**Definition:** Being able to turn on some of the more modern features via from \_\_future\_\_ import statements allows early use of features from expected future Python versions.

New language version semantic changes may be gated behind a special future import to enable them on a per-file basis within earlier runtimes.<br/>
Use of from \_\_future\_\_ import statements is encouraged. It allows a given source file to start using more modern Python syntax features today. Once you no longer need to run on a version where the features are hidden behind a \_\_future\_\_ import, feel free to remove those lines.

### Type Annotated Code

Type annotations (or “type hints”) are for function or method arguments and return values:

```python
def func(a: int) -> list[int]:
```

---

## Python Style Rules
### Semicolons
Do not terminate your lines with semicolons, and do not use semicolons to put two statements on the same line.

### Line length
Maximum line length is 80 characters. Explicit exceptions to the 80 character limit:
* Long import statements.
* URLs, pathnames, or long flags in comments.
* Long string module-level constants not containing whitespace that would be inconvenient to split across lines such as URLs or pathnames.
  * Pylint disable comments. (e.g.: # pylint: disable=invalid-name)


### Parentheses
Use parentheses sparingly.<br/>
It is fine, though not required, to use parentheses around tuples. Do not use them in return statements or conditional statements unless using parentheses for implied line continuation or to indicate a tuple.

### Indentation
Indent your code blocks with 4 spaces. Never use tabs.

### Shebang Line
Most .py files do not need to start with a #! line. Start the main file of a program with #!/usr/bin/env python3 (to support virtualenvs) or #!/usr/bin/python3 <br/>
This line is used by the kernel to find the Python interpreter, but is ignored by Python when importing modules. It is only necessary on a file intended to be executed directly.

### Comments and Docstrings
Be sure to use the right style for module, function, method docstrings and inline comments.<br/>
Python uses *docstrings* to document code. A docstring is a string that is the first statement in a package, module, class or function. These strings can be extracted automatically through the \_\_doc\_\_ member of the object and are used by pydoc.

### Strings
Use an f-string, the % operator, or the format method for formatting strings, even when the parameters are all strings. Use your best judgment to decide between string formatting options. A single join with + is okay but do not format with +.
```python
items = ['<table>']
for last_name, first_name in employee_list:
    items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
items.append('</table>')
employee_table = ''.join(items)
```

### TODO Comments
Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.

### Imports formatting
Imports should be on separate lines; there are exceptions for typing and collections.abc imports. Imports are always put at the top of the file, just after any module comments and docstrings and before module globals and constants. Imports should be grouped from most generic to least generic.

### Statements
Generally only one statement per line.

However, you may put the result of a test on the same line as the test only if the entire statement fits on one line. In particular, you can never do so with try/except since the try and except can’t both fit on the same line, and you can only do so with an if if there is no else.
```python
# No
if foo: bar(foo)
else:   baz(foo)

try:               bar(foo)
except ValueError: baz(foo)

try:
    bar(foo)
except ValueError: baz(foo)
```

### Getters and Setters
Getter and setter functions (also called accessors and mutators) should be used when they provide a meaningful role or behavior for getting or setting a variable’s value.

In particular, they should be used when getting or setting the variable is complex or the cost is significant, either currently or in a reasonable future.
```python
class SampleClass:
    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a

```
SampleClass has three methods:
* \_\_init\_\_:- It is used to initialize the attributes or properties of a class.
* \_\_a:- It is a private attribute.
* get_a:- It is used to get the values of private attribute a.
* set_a:- It is used to set the value of a using an object of a class.

You are not able to access the private variables directly in Python. That's why you implemented the getter method.


### Naming
* module_name, 
* package_name, 
* ClassName, 
* method_name, 
* ExceptionName, 
* function_name, 
* GLOBAL_CONSTANT_NAME, 
* global_var_name, 
* instance_var_name, 
* function_parameter_name, 
* local_var_name, 
* query_proper_noun_for_thing, 
* send_acronym_via_https.

Always use a .py filename extension. Never use dashes.

### Main
In Python, pydoc as well as unit tests require modules to be importable. If a file is meant to be used as an executable, its main functionality should be in a main() function, and your code should always check if \_\_name\_\_ == '\_\_main\_\_' before executing your main program, so that it is not executed when the module is imported.

### Function length
Prefer small and focused functions.

We recognize that long functions are sometimes appropriate, so no hard limit is placed on function length. If a function exceeds about 40 lines, think about whether it can be broken up without harming the structure of the program.

### Type Annotations
#### NoneType
In the Python type system, NoneType is a “first class” type, and for typing purposes, None is an alias for NoneType. If an argument can be None, it has to be declared! You can use | union type expressions (recommended in new Python 3.10+ code), or the older Optional and Union syntaxes.

Use explicit X | None instead of implicit. Earlier versions of PEP 484 allowed a: str = None to be interpreted as a: str | None = None, but that is no longer the preferred behavior.

```python
# yes
def modern_or_union(a: str | int | None, b: str | None = None) -> str:
  ...
def union_optional(a: Union[str, int, None], b: Optional[str] = None) -> str:
  ...

# no
def nullable_union(a: Union[None, str]) -> str:
  ...
def implicit_optional(a: str = None) -> str:
  ...

```

#### Type Aliases
_Private.

Note that the : TypeAlias annotation is only supported in versions 3.10+.
```python 
from typing import TypeAlias

_LossAndGradient: TypeAlias = tuple[tf.Tensor, tf.Tensor]
ComplexTFMap: TypeAlias = Mapping[str, _LossAndGradient]
```
#### Tuples vs Lists
Typed lists can only contain objects of a single type. Typed tuples can either have a single repeated type or a set number of elements with different types. The latter is commonly used as the return type from a function.
```python
a: list[int] = [1, 2, 3]
b: tuple[int, ...] = (1, 2, 3)
c: tuple[int, str, float] = (1, "2", 3.5)
```

#### String types
Use str for string/text data. For code that deals with binary data, use bytes.
```python
def deals_with_text_data(x: str) -> str:
  ...
def deals_with_binary_data(x: bytes) -> bytes:
  ...
```