# x86 Сompiler [![Build Status](https://travis-ci.org/Nilera/Compiler.svg?branch=master)](https://travis-ci.org/Nilera/Compiler)

For more information visit wiki: https://github.com/Nilera/Compiler/wiki

## Features
* supported types: `int`, `boolean`, `char`
* functions
* arrays
* strings
* global and local variables
* arithmetic expressions: 
  * `+`, `-`, `*`, `/`, `%`
  * `<`, `<=`, `>`, `>=`, `==`, `!=`
  * `&&`, `||`
* control flow statements: `if`, `if/else`, `while`
* I/O statements: `read(a)` and `write(a)`


## Example
```java
int n;
int k;

int power(int k, int n) {
    int r = 1;
    while (k > 0) {
        if (k % 2 == 1) {
            r = r * n;
        }
        n = n * n;
        k = k / 2;
    }
    return r;
}

void main() {
    read(k);
    read(n);

    int r = power(k, n);

    write(r);
}
```
