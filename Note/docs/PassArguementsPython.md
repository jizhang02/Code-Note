# Pass arguements methods in Python

### 🟢 Pass arguements to a function
* Pass single varible to a function

```{python}
def pass_arg_func(a,b):
    result = a+b
    return result
```
👉 in command line: `print(pass_arg_func(39,100))`

* Pass an array to a function

```
def pass_arr_func(list):
    sum = 0
    for n in list:
        sum += n
    return sum
```
👉 in command line: `print(pass_arr_func([10,20,30]))`

### 🟢 Pass arguments to a script
* Using `sys` library

```
import sys

def pass_arg_scri():
    print("arguements length：", len(sys.argv))
    print("type:", type(sys.argv))
    print("function name:", sys.argv[0])
    print("the first arg is:", sys.argv[1])
    print("the second arg is:", sys.argv[2])
```
👉 in command line: `python pass_arg_scri.py 30 jing`

* Using `argparse` library    
in function `add_argument()`:    
🔹`--xx`  full argument input    
🔹`-x`    simple argument input    
🔹`type`  the type of input argument    
🔹`default` default value    
🔹`help`   introduction of arguements    
🔹`nargs`  the number of arguements, "+" means All command-line arguments present are gathered into a list    
🔹`required`  if it is required arguement     


```
import argparse

def pass_arg_scri2():
    parser = argparse.ArgumentParser(description='argparse testing')
    parser.add_argument('--name','-n',type=str, default = "jing",required=True,help="a programmer's name")
    parser.add_argument('--age','-a',type=int, default=35,help='age of the programmer')
    parser.add_argument('--sex','-s',type=str, default='male')
    parser.add_argument('--favorite','-f',type=str, nargs="+",required=False,help="favorite of the programmer")
    args = parser.parse_args()
    print(args.name, args.age, args.sex, args.favorite)
```

👉 in command line: `python pass_arg_scri2.py -n jing -a 30 -s female ` or `python pass_arg_scri2.py --name jing --age 30 --sex female`

### 🟢 Pass arguments to a script from shell

* Run python code with shell    

📜in python script (arg_pass.py):

```
def pass_shell():
    return "function without arguements"
```

🐚 in shell:
```
#!/bin/bash
python arg_pass.py
```
or
```
#!/bin/bash
python -c 'import arg_pass; print(arg_pass.pass_shell())'
```

👉 in command line: `bash shell_function.sh` or `sh shell_function.sh`

* Pass arguments to python script with shell

📜in python script (arg_pass.py):

```
def pass_arg_shell(x):
    return f"function with arguements, and the arguement is{x}"
```

🐚 in shell:
```
#!/bin/bash
python -c "import arg_pass; print(arg_pass.pass_arg_shell('$1'))"
```

👉 in command line: `bash shell_function.sh jing`

### Reference
* [使用python脚本传递参数](https://www.cnblogs.com/mrwhite2020/p/16812198.html)
* [Shell 基本运算符](https://www.runoob.com/linux/linux-shell-basic-operators.html)
