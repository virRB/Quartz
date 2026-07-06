# Writing Your First Program in Quartz

Quartz is an esoteric programming language built around **50 memory slots**. Each slot can store either an **integer** or a **string**, and your program moves between these slots to perform operations.

Commands are separated using the `|` character.

Example:

```Quartz
+|-|^7|,,,
```

---

# Memory Slots

* Quartz has **50 slots**, numbered **0–49**.
* Your program starts on **slot 0**.
* Most commands affect the **current slot**.

---

# Data Types

Quartz supports two data types.

## Integers

Integers are written normally.

Example:

```Quartz
42
```

## Strings

Strings begin with `s` instead of using quotation marks.

Example:

```Quartz
sHello
sQuartz
sHello, World!
```

---

# Operators

### `+`

Increase the current slot by **1**.

```Quartz
+
```

### `-`

Decrease the current slot by **1**.

```Quartz
-
```

### `%`

Repeat several operations in a single command.

Example:

```Quartz
%+++--++
```

This is equivalent to:

```Quartz
+++--++
```

### `^x`

Replace the current slot with a **random integer** between **1** and `x` (inclusive).

Example:

```Quartz
^10
```

This sets the current slot to a random number from **1** to **10**.

### `++`

Concatenate strings.

If the current slot contains a string, `++` lets you add text before or after it.

Append text to the end:

```Quartz
++sVir
```

If the current slot contains `Hello`, it becomes:

```text
HelloVir
```

Prepend text to the beginning:

```Quartz
sBye++
```

If the current slot contains `Hello`, it becomes:

```text
ByeHello
```

---

# Movement

### `~+`

Move to the next slot.

```Quartz
~+
```

### `~-`

Move to the previous slot.

```Quartz
~-
```

### `~>x:command`

Loop through slots, running a command on each one until a slot containing `x` is found.

`x` may be either an integer or a string.

Examples:

```Quartz
~>5:+
```

```Quartz
~>sHello:%++--
```

---

# Memory

### `#x`

Store `x` in the current slot.

`x` may be either an integer or a string.

Examples:

```Quartz
#5
```

```Quartz
#sHello
```

---

# Input & Output

## Input

Read an integer from the user and replace the current slot.

```Quartz
&*
```

Add the user's input to the current slot.

```Quartz
&*+
```

Subtract the user's input from the current slot.

```Quartz
&*-
```

Read a string from the user and replace the current slot.

```Quartz
s&*
```

> **Note:** `s&*+` and `s&*-` are currently **not supported**.

## Output

Print the current slot.

```Quartz
,,,
```

---

# Time

Pause the program for a number of seconds.

Syntax:

```Quartz
...x...
```

Example:

```Quartz
...3...
```

Pauses for 3 seconds.

---

# Conditionals

Use `?` to check whether the current slot equals a value.

`value` may be either an integer or a string.

Syntax:

```Quartz
?value:command
```

Examples:

```Quartz
?5:%++
```

```Quartz
?sHello:,,,
```

---

# Functions

Functions let you reuse code.

## Creating a function

Use `@`.

```Quartz
@functionName:command
```

Example:

```Quartz
@addThree:%+++
```

## Multiple commands

Separate commands with `/`.

```Quartz
@addTwoToNext:~+/%++
```

## Calling a function

Use `$`.

```Quartz
$addThree
```

---

# Comments

Comments begin with `!`.

Example:

```Quartz
! This is a comment.
```

---

# Imports

Import another `.qrtz` file using `QPort`.

Syntax:

```Quartz
QPort<stuff.qrtz>
```

Call imported functions using the module name followed by a dot.

Example:

```Quartz
$stuff.sayHi
```

Complete example:

```Quartz
QPort<stuff.qrtz>
$stuff.sayHi
```

---

# Example Program

```Quartz
#sHello
++s, World!
?sHello, World!:,,,
```

This program stores the string `Hello`, appends `, World!` to it, checks if the resulting string matches `Hello, World!`, and prints it.
