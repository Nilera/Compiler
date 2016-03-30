# x86 Сompiler

## Features
* supported types: `int` and `boolean`
* functions
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

## Requirements
* `python3`
* `antlr4`
* `yasm`
* `gcc` for Linux, `VC` for Windows

## Run
### Linux (tested on Ubuntu 15.10 32bit)
`python3 Compiler.py -f elf32 -o <output file>`

`./<output file>`

### Windows (tested on Windows 10)
`python3 Compiler.py -f win32 -o <output file>`

Unfortunately generated `*.asm` file only (no `*.exe`), so to run resulted `*.asm` file use combination of MS VS2010 and yasm1.2.0 (http://yasm.tortall.net/Download.html)
