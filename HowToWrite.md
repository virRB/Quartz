# Writing your first program in Quartz!
- In quartz, you are given 5 slots. these are your slots to store values in.
- all commands in quartz must be seperated by "|"
- for example
```Quartz
+|-|etc...
```
- There are multiple different operators you can use with these slots
- Slots go in order 0 - 5
- You start at slot 0
## Operators
"+" will increase the value of the current slot by 1
"-" will decrease the value of the current slot by 1
"%" can be used to repeat operations in one command. for example
```Quartz
%+++--++
```
"^x" can be used to change the value of the current slot, 1 -> x. example:
```Quartz
^7
```
## Movement
`~+` can be used to move one slot forward
`~-` can be used to move one slot backward
`~>` is used to loop through every slot and run a command on them until it reaches a given number
Example:
```Quartz
~>5:+
```
- That adds 1 to ever slot it loops through until it finds a slot of value 5
## Memory
"#x" can be used to set the value of the current slot
example:
```Quartz
#5
```
## Input and Output
To take input from the user (only integers) you can use:
"&*" to take input and ovveride the slot
"&*+" to add the inputted value to the value of the slot
"&*-" to subtract the inputted value to the value of the slot
to print the value of the current slot you can do:
```Quartz
,,,
```
to print the value of any slot, 0 - 4 you can do:
```Quartz
,,,4,,,
```
and to print the sum of any 2 slots
```Quartz
,,,3:4,,,,
```
## Time
You can pause for an x amount of seconds using:
```Quartz
...x...
```
Example:
```Quartz
...3...
```
## Conditionals
For conditionals, you can use "?"
This detects if the current slot is equal to a given value, if so it runs a command
Example:
```Quartz
?5:%++
```
## Functions
Quartz has the ability to create functions, which are basically reusable chunks of code
To create a function, you can use the keyword "@"
```Quartz
@functionName:command
```
for example:
```Quartz
@addThree:%+++
```
To add multiple commands to one function, you can seperate them using "/"
Example:
```Quartz
@addTwoToNext:~+/%++
```
To call a function, you can use "$"
Example:
```Quartz
$addThree
```
## Comments
Comments can be used to organise and make your code cleaner - or, as clean as this language can get.
The comment syntax is simple, "!"
Example:
```Quartz
! This is a comment
```

Example program (this takes input from the user, and shows its descendant and ascendant):
```Quartz
@addThree:%+++ #5|~+|^3|~+| ?2:$addThree|,,,
```
