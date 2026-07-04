# Writing Your First Program in Quartz

Quartz is an esoteric programming language built around **50 memory slots**. Each slot can store a value, and your program moves between these slots to perform operations.

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

Set the current slot's value to `x`.

Example:

```Quartz
^7
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

Loop through slots, running a command on each one until a slot with the value `x` is found.

Example:

```Quartz
~>5:+
```

This adds 1 to every slot visited until a slot containing `5` is reached.

---

# Memory

### `#x`

Store the current slot's value into memory variable `x`.

Example:

```Quartz
#5
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

## Output

Print the current slot.

```Quartz
,,,
```

Print any slot.

```Quartz
,,,4,,,
```

Print the sum of two slots.

```Quartz
,,,3:4,,,,
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

Syntax:

```Quartz
?value:command
```

Example:

```Quartz
?5:%++
```

If the current slot contains `5`, it increases it by `2`.

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

* Import another `.qrtz` file using `QPort`.

Syntax:

```Quartz
QPort<stuff.qrtz>
```

* Call imported functions using the module name followed by a dot.

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
@addThree:%+++
#5|~+|^3|~+|?2:$addThree|,,,
```

This program creates a function, moves between slots, performs a conditional check, and prints the final value.

