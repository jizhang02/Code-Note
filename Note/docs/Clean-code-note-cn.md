# Clean Code Notes（中文版）

## 前言

这份中文版由 Codex 基于原始英文内容翻译和整理，方便中文读者阅读与查阅。

原始内容来自 GitHub 仓库：[JuanCrg90/Clean-Code-Notes](https://github.com/JuanCrg90/Clean-Code-Notes)。

## 目录

- [第 1 章 - 干净代码](#chapter1)
- [第 2 章 - 有意义的命名](#chapter2)
- [第 3 章 - 函数](#chapter3)
- [第 4 章 - 注释](#chapter4)
- [第 5 章 - 格式](#chapter5)
- [第 6 章 - 对象与数据结构](#chapter6)
- [第 7 章 - 错误处理](#chapter7)
- [第 8 章 - 边界](#chapter8)
- [第 9 章 - 单元测试](#chapter9)
- [第 10 章 - 类](#chapter10)
- [第 11 章 - 系统](#chapter11)
- [第 12 章 - 自然演化](#chapter12)
- [第 13 章 - 并发](#chapter13)

<a name="chapter1">
<h1>第 1 章 - 干净代码</h1>
</a>
这是一本关于良好编程的书。它讲的是如何写出好代码，以及如何把坏代码改造成好代码。

代码代表了需求的细节，而这些细节不能被忽略或抽象掉。我们可以创造出更贴近需求的语言；我们可以创造工具帮助我们把需求解析并组装成正式结构。但我们永远不能消除必要的精确性。

### 为什么会写出糟糕代码？

- 你赶时间吗？
- 你想要“快”吗？
- 你没有时间把事情做好吗？
- 你是否已经厌倦了在同一个程序/模块里工作？
- 你的老板是否催你早点完成？

这些理由可能会让你陷入一片毫无意义的代码沼泽。

如果你说“我以后会回来修复它”，你可能会陷入 [LeBlanc 定律](https://en.wikipedia.org/wiki/Talk%3AList_of_eponymous_laws#Proposal_to_add_LeBlanc.27s_law) 所描述的“以后等于永远”。

你是专业人士，代码是你的责任。我们来分析这个故事：

> 如果你是一名医生，而有一个病人要求你在手术前停止那些看起来浪费时间的洗手流程，你会怎么办？显然病人是“老板”；但医生绝对不能照做。为什么？因为医生比病人更了解疾病和感染的风险。顺从病人的要求不仅不专业，而且可能违法。

程序员面对不理解制造混乱风险的管理者时，同样不应妥协。

也许你有时会觉得为了赶上截止日必须快。真正的快速方式，是始终把代码保持得尽可能干净。

### 什么是干净代码？

每个有经验的程序员对干净代码都有自己的定义，但有一点很明确：干净代码是容易阅读的代码。干净代码是已经被精心维护过的代码。

在《Uncle Bob》的书里，他说：

> 把这本书看作是 Object Mentor 干净代码学派的描述。书中的技术和教导，是我们实践这门艺术的方式。我们敢说，如果你遵循这些教导，你会享受我们所享受的好处，并学会写出干净且专业的代码。但不要犯下绝对化的错误，认为我们在任何意义上都是“完全正确”的。还有其他学派和其他大师，同样具备专业性。你也应该向他们学习。

### 童子军规则

仅仅写好代码还不够。代码需要随着时间保持干净。我们都见过代码随着时间腐烂和退化，所以我们必须积极防止这种退化。

遵循 [童子军规则](http://programmer.97things.oreilly.com/wiki/index.php/The_Boy_Scout_Rule) 是一个好习惯。

> 总是让营地比你发现它时更干净。

<a name="chapter2">
<h1>第 2 章 - 有意义的命名</h1>
</a>

命名在软件中无处不在：文件、目录、变量、函数等。既然我们要做这么多命名，就更要把它做好。

### 使用意图明确的名字

我们常说名字应该揭示意图。选择好名字需要时间，但它节省的比耗费的更多。所以要认真对待命名，并在找到更好名字时及时替换。

变量、函数或类的名字应该回答所有关键问题：它为什么存在，做什么，用在哪里。**如果一个名字需要注释来解释，那说明这个名字没有揭示它的意图。**

| 不揭示意图 | 揭示意图 |
| --- | --- |
| `d = 5  # 以天为单位的时间` | `elapsed_time_in_days = 5` |

选择揭示意图的名字可以让代码更容易理解和修改。举个例子：

```python
def get_them(the_list):
    list1 = []
    for x in the_list:
        if x[0] == 4:
            list1.append(x)
    return list1
```

这段代码很简单，但会带来许多问题：

1. `the_list` 的内容是什么？
2. 列表中 `x[0]` 的含义是什么？
3. 为什么要把 `x[0]` 与 `4` 比较？
4. 返回的列表如何使用？

这些问题在代码示例中并没有得到回答，但本可以回答。假设我们在写一个扫雷游戏。我们可以改写为：

```python
def get_flagged_cells(game_board):
    flagged_cells = []
    for cell in game_board:
        if cell[STATUS_VALUE] == FLAGGED:
            flagged_cells.append(cell)
    return flagged_cells
```

现在我们能够明白：

1. `the_list` 表示游戏棋盘 `game_board`。
2. `x[0]` 表示单元格的状态值，`4` 表示被标记的单元格。
3. 返回的列表表示所有被标记的单元格。

注意，代码的简洁性并没有改变。操作数和常量的数量一样多，嵌套层级也一样。但代码变得更明确。

我们还可以继续改进：用一个简单的 `Cell` 类代替数组，并添加一个揭示意图的函数 `is_flagged` 来隐藏魔法数字。

```python
class Cell:
    def is_flagged(self):
        return self.status == FLAGGED


def get_flagged_cells(game_board):
    flagged_cells = []
    for cell in game_board:
        if cell.is_flagged():
            flagged_cells.append(cell)
    return flagged_cells
```

现在 `cell.is_flagged()` 直接表达了这个判断的意图。

### 避免误导性命名

程序员必须避免留下会混淆含义的假线索。

如果一个账户组不是 `list` 类型，就不要把它叫成 `account_list`。`List` 对程序员来说有特定含义。如果容器不是实际的列表，`account_group`、`bunch_of_accounts` 或直接 `accounts` 会更合适。

别使用意义差异很小的名字。想象一下在一个模块里有 `XYZControllerForEfficientHandlingOfStrings`，另一个地方又有 `XYZControllerForEfficientStorageOfStrings`，这两个名字的区别非常难察觉。

### 产生有意义的区别

当你为满足编译器或解释器而写代码时，往往会制造问题。例如因为同一作用域不能用相同名字，你可能被迫随意改一个名字。有时这会导致拼写错误，结果改正拼写后代码又编译不了。

下面这个函数，参数名 `a1` 和 `a2` 毫无信息量：

```python
def copy_chars(a1, a2):
    for i in range(len(a1)):
        a2[i] = a1[i]
```

我们可以改成更明确的参数名：

```python
def copy_chars(source, destination):
    for i in range(len(source)):
        destination[i] = source[i]
```

噪音词也是另一种无意义的区分。假设你有一个 `Product` 类，如果你再有一个 `ProductInfo` 或 `ProductData`，你只是让名字不同而已，并没有增加含义。`Info` 和 `Data` 类似于 `a`、`an`、`the`，是冗余的噪音词。

噪音词是多余的。变量名里不应包含 `variable`，表名里不该包含 `table`。

### 使用可发音的名字

想象你有一个变量 `genymdhms`（生成日期：年、月、日、小时、分钟、秒）并且你需要念出它的名字，那会是“gen why emm dee aitch emm ess”。你可以把这样的类：

```python
from datetime import datetime

class DtaRcrd102:
    def __init__(self):
        self.genymdhms: datetime | None = None
        self.modymdhms: datetime | None = None
        self.pszqint = "102"
```

换成：

```python
from datetime import datetime

class Customer:
    def __init__(self, generation_timestamp: datetime, modification_timestamp: datetime, record_id: str = "102"):
        self.generation_timestamp = generation_timestamp
        self.modification_timestamp = modification_timestamp
        self.record_id = record_id
```

更好的名字更容易交流。

### 使用可搜索的名字

单字符名字和数字常量很难在文本中定位。

### 避免编码信息

我们已经有足够多的编码方式了，不要再把类型或作用域信息编码进名字。编码名字会增加额外的解读负担，通常也不利于发音和输入。

例如，不要使用 [Hungarian Notation](https://en.wikipedia.org/wiki/Hungarian_notation)，也不要用成员前缀。

#### 接口与实现

这有时是编码的特殊情况。比如你要构建一个抽象工厂来创建形状。这个工厂可能是一个接口，由具体类实现。你应该如何命名？`IShapeFactory` 和 `ShapeFactory`？更好的做法是让接口名保持简洁。我不想让使用者知道我给他们的东西是一个接口，我只希望他们知道它是一个 `ShapeFactory`。所以如果必须对接口或实现做编码，我会选择编码实现。命名它为 `ShapeFactoryImpl`，甚至令人厌恶地叫 `CShapeFactory`，都比编码接口要好。

### 避免心理映射

读者不应该需要把你的名字在脑中翻译成他们已经知道的其他名称。

聪明程序员和专业程序员之间的区别之一就是，专业程序员明白清晰性至上。专业程序员用他们的能力做正确的事情，写别人能理解的代码。

### 类名

类和对象应该使用名词或名词短语命名，比如 `Customer`、`WikiPage`、`Account`、`AddressParser`。避免在类名中使用 `Manager`、`Processor`、`Data`、`Info` 等词。类名不应该是动词。

### 方法名

方法应该使用动词或动词短语命名，比如 `post_payment`、`delete_page`、`save`。访问器、修改器、谓词应根据标准命名为 `get_`、`set_`、`is_`。

当构造函数被重载时，使用描述参数的静态工厂方法：

```python
class Complex:
    def __init__(self, real):
        self.real = real

    @classmethod
    def from_real_number(cls, real):
        return cls(real)

fulcrum_point = Complex.from_real_number(23.0)
```

这通常比直接写：

```python
fulcrum_point = Complex(23.0)
```

要更好。你还可以通过把对应构造器设为私有来强制使用这种方式。

### 不要取可爱的名字

| 可爱名称 | 干净名称 |
| --- | --- |
| `holy_hand_grenade` | `delete_items` |
| `whack` | `kill` |
| `eat_my_shorts` | `abort` |

### 每个概念选一个词

为同一个抽象概念选一个词并坚持使用。例如，不要在不同类中把 `fetch`、`retrieve` 和 `get` 当成等价方法。

### 不要玩文字游戏

避免为两个不同用途使用相同的词。同一个术语在两个不同含义上的使用本质上就是双关。

例如，一个类中用 `add` 表示通过相加或连接两个值创建新值，而另一个类中用 `add` 表示把参数放入集合，那更好的做法是使用 `insert` 或 `append`。

### 使用解法领域的名字

记住你的代码读者是程序员。所以尽管使用计算机科学术语、算法名、设计模式名、数学术语等。

### 使用问题领域的名字

当没有“程序员行话”能描述你要做的事情时，就使用问题领域中的名称。至少维护你代码的程序员可以去问领域专家它的含义。

### 添加有意义的上下文

少数名字本身就足够有意义，但大多数不是。你需要通过把它们放在良命名的类、函数或命名空间中，为读者提供上下文。

比如变量 `first_name`、`last_name`、`street`、`city`、`state`。放在一起时很明显它们构成地址，但如果你在一个方法中单独看到 `state`，你就不清楚它的含义。你可以通过前缀 `addr_state` 来添加上下文，但更好的方法是创建一个叫 `Address` 的类，这样即便编译器也知道这些变量属于更大的概念。

### 不要添加无谓的上下文

在一个虚构的“Gas Station Deluxe”应用里，把每个类都加上 `GSD` 前缀是个坏主意。例如：`GSDAccountAddress`。

只要清晰，短名字通常优于长名字。不要为名字添加超过必要的上下文。

<a name="chapter3">
<h1>第 3 章 - 函数</h1>
</a>

函数是任何主题中的第一层组织结构。

### 小！

函数的第一条规则是它们应该很小。第二条规则是它们应该比这更小。

#### 块与缩进

这意味着 `if`、`else`、`while` 等语句内部的块应该只有一行。那一行很可能应该是函数调用。这样不仅能保持外层函数小巧，还增加了文档价值，因为块内调用的函数可以有一个含义清晰的名字。

这也意味着函数不应大到包含嵌套结构。函数的缩进层级应不超过一到两层。这当然让函数更容易读取和理解。

### 做一件事

**函数应该只做一件事。它们应该把这件事做好，只做这件事。**

#### 函数内部的区块

如果你的函数被划分为“声明”、“初始化”等多个部分，这明显说明函数做了多件事。只做一件事的函数不应被合理地划分成多个区块。

### 每个函数一个抽象层级

为了确保我们的函数只做“一件事”，我们需要确保函数内部的语句都处于相同的抽象层级。

#### 自上而下阅读代码：下降规则

我们希望代码像自上而下的叙述一样阅读。每个函数之后都应跟着下一个抽象层级的函数，这样我们就可以在阅读函数列表时逐层下降。

换句话说，我们希望把程序读作一组“要做什么”的段落，每个段落描述当前抽象层级，并引用接下来更低一层的段落。

```
- 为了包含 setup 和 teardown，我们先包含 setup，然后包含测试页面内容，最后包含 teardown。
- 为了包含 setup，如果这是一个测试套件，我们包含套件 setup，然后包含常规 setup。
- 为了包含套件 setup，我们搜索父层次结构中的 “SuiteSetUp” 页面，并添加带有该页面路径的 include 语句。
- 为了搜索父层次结构……
```

程序员学习遵守这条规则并编写保持单一抽象层级的函数确实很难。但掌握这个技巧也非常重要。它是保持函数简短并确保它们只做一件事的关键。让代码像一组自上而下的段落一样读起来，是保持抽象层级一致的有效方法。

### switch 语句

很难让 switch 语句保持简短。即便只有两个分支，switch 语句也比我希望的单个块或函数要大。要让 switch 语句只做一件事也很难。按其性质，switch 语句总是做 N 件事。不幸的是，我们不能总是避免 switch 语句，但我们可以确保每个 switch 语句都被藏在低层类中并且绝不重复。我们当然可以通过多态来实现这一点。

### 使用描述性名字

> 当每个例程都基本符合你的预期时，你知道自己正在编写干净代码。

实现这个原则的一半战斗就是为执行一件事的小函数选择好名字。函数越小越专注，越容易起出描述性名字。

不要害怕让名字变长。一个长而描述性的名字，比一个短而晦涩的名字要好。一个长而描述性的名字，也比一个长而注释性的名字要好。使用一个允许多个单词在函数名中轻松阅读的命名约定，然后利用这些多个词来让函数名说明它的作用。

选择描述性名字会澄清模块的设计，并帮助你改进它。通常在寻找好名字的过程中，你会顺便做出对代码有利的重构。

### 函数参数

函数的理想参数数量是零（无参）。其次是一（单参），紧接着是二（双参）。三参数应尽量避免。超过三个（多参）需要特别理由，而且一般也不应该使用。

参数从测试角度看更难处理。想象一下要为所有参数组合写测试用例的难度。如果没有参数，这很简单；如果只有一个参数，也不是太难；两个参数时问题变得更具挑战性；超过两个参数时，要测试每种合理值组合可能会非常艰巨。

输出参数比输入参数更难理解。当我们阅读一个函数时，习惯了信息通过参数进入函数，再通过返回值出来。我们不习惯信息通过参数从函数中输出。因此输出参数常常让我们愣一下。

#### 常见的单参形式

传入一个参数到函数一般有两种常见原因。你可能是在询问该参数的某个属性，比如 `file_exists("myfile")`。或者你可能在对该参数进行操作，把它转换成其它东西并返回，比如 `open_file("myfile")`。这两种用法是读者看到函数时所期望的。你应该选择能够清楚表达区别的命名，并在上下文中始终保持这两种形式的一致性。

#### 标志参数

标志参数很丑。把一个布尔值当成参数传入函数是一种非常糟糕的做法。它会立即让方法签名变得复杂，明确地表明这个函数做了不止一件事。如果标志为 `True` 就做一件事，而为 `False` 就做另一件事！

#### 双参数函数

带两个参数的函数比单参函数更难理解。例如，`write_field(name)` 比 `write_field(output_stream, name)` 更容易理解。

当然，有时两个参数是合适的。例如，`Point(0, 0)` 是完全合理的。笛卡尔点自然需要两个参数。

即便是显而易见的双参数函数，例如 `assert_equals(expected, actual)` 也有问题。你多少次把 actual 放到了 expected 的位置？这两个参数没有自然的顺序。`expected, actual` 只是一个需要练习才能掌握的约定。

双参数不是邪恶，你肯定会写它们。但你应该意识到它们有成本，并利用可用机制把它们转换为单参。例如，你可以把 `write_field` 方法做成 `output_stream` 的成员，这样写成 `output_stream.write_field(name)`；或者把 `output_stream` 设为当前类的成员变量，这样就不用传它；或者抽取一个新类 `FieldWriter`，在构造时接收 `output_stream`，并提供一个 `write` 方法。

#### 三参数函数

接受三个参数的函数比双参数函数更难理解。参数顺序、暂停和忽略问题的难度不止翻倍。我建议在创建三参数函数前务必认真思考。

#### 参数对象

比较：

```python
# 不太好
def make_circle(x, y, radius):
    return Circle(Point(x, y), radius)
```

vs

```python
# 更好
def make_circle(center, radius):
    return Circle(center, radius)
```

#### 动词与关键词

为函数选择好名字，可以大大解释函数的意图和参数顺序。对于单参数函数，函数名和参数应该形成一个很好的动词/名词对。例如，`write(name)` 非常有表现力。无论这个“name”是什么，它正在被“写”。一个更好的名字可能是 `write_field(name)`，它告诉我们这个“name”实际上是一个“字段”。

这最后一个例子展示了函数名的关键词形式。使用这种形式，我们把参数名编码进函数名。例如，`assert_equals` 可能更好地写成 `assert_expected_equals_actual(expected, actual)`。这能强烈减轻记住参数顺序的问题。

### 输出参数

一般应避免输出参数。如果你的函数必须改变某个状态，让它改变所属对象的状态。

### 命令查询分离原则

函数要么做某件事，要么返回某些信息，而不应两者兼顾。两者兼顾往往会导致混淆。

### 更倾向于抛出异常而不是返回错误码

从命令函数返回错误码是对命令查询分离原则的微妙违反。

### 不要重复自己

重复可能是软件领域的一切罪恶根源。许多原则和实践都为了控制或消除重复而产生。

### 结构化编程

有些程序员遵循 Edsger Dijkstra 的结构化编程规则。他说每个函数和函数内的每个块都应只有一个入口和一个出口。遵循这些规则意味着函数中只应有一个 `return` 语句，循环中不应有 `break` 或 `continue`，绝不使用 `goto`。

虽然我们理解结构化编程的目标和纪律，但当函数非常小时，这些规则收益有限。只有在更大的函数中，这些规则才显得更加有价值。

### 如果函数足够小，多重返回、break、continue 也无妨

如果你的函数保持得很小，那么偶尔出现多个 `return`、`break` 或 `continue` 并不会造成伤害，有时甚至比单入口、单出口规则更清晰。另一方面，`goto` 只有在大型函数里才可能有意义，因此应该避免。

<a name="chapter4">
<h1>第 4 章 - 注释</h1>
</a>

没有什么比恰到好处的注释更有帮助。也没有什么比轻浮、教条式的注释更会污染模块。也没有什么比过时注释传播谎言更有害。

如果我们的编程语言足够表达意图，或者我们有能力巧妙地运用这些语言表达意图，我们就不需要太多注释——甚至根本不需要。

### 注释不能弥补糟糕代码

清晰且富有表达力的代码，哪怕注释少，也远比充斥注释的混乱代码好得多。与其花时间写注释来解释你造的烂摊子，不如把时间用来清理那堆烂摊子。

### 用代码解释自己

```python
# 检查员工是否符合完整福利资格
if (employee.flags & HOURLY_FLAG) and (employee.age > 65):
```

vs

```python
if employee.is_eligible_for_full_benefits():
```

### 好注释

有些注释是必要或有益的。然而，唯一真正好的注释就是你设法不写的那条注释。

#### 法律注释

有时我们的公司编码规范会强制我们出于法律原因写某些注释。例如，版权和作者声明是合理且必要的，通常放在每个源文件的开头。

#### 信息性注释

有时用注释提供基本信息是有用的。例如，下面这条注释说明了一个抽象方法的返回值：

```python
# 返回正在测试的 Responder 实例。
@abc.abstractmethod
def responder_instance(self) -> Responder:
    pass
```

这样的注释有时有用，但更好的做法是用函数名来传达这条信息。例如在这个例子里，将函数重命名为 `responder_being_tested` 可以让注释变得多余。

#### 意图说明

有时注释超越了对实现的描述，提供了决策背后的意图。例如：

```python
def compare_to(self, other):
    if isinstance(other, WikiPagePath):
        compressed_name = "".join(self.names)
        compressed_argument_name = "".join(other.names)
        return (compressed_name > compressed_argument_name) - (compressed_name < compressed_argument_name)
    return 1  # 我们更大，因为我们是正确类型。
```

#### 澄清

有时把某个晦涩参数或返回值翻译成可读形式是有帮助的。通常更好的办法是让这个参数或返回值本身就足够清晰；但当它属于标准库或你无法修改的代码时，一条有帮助的澄清性注释是有价值的。

#### 警告后果

有时警告其他程序员某些后果是有用的。

```python
# 只有在你有足够时间消磨时才运行。
def _test_with_really_big_file():
    write_lines_to_file(10000000)
    response.body = test_file
    response.ready_to_send(self)
    response_string = output.getvalue()
    assert "Content-Length: 1000000000" in response_string
    assert bytes_sent > 1000000000
```

#### TODO 注释

有时以 `# TODO` 形式留下“待办”说明是合理的。在下例中，TODO 注释解释了该函数为何现在使用退化实现，以及它将来的演进方向。

```python
# TODO: 这些不再需要。
# 预计当我们完成结账模型时，这些会被移除。
def make_version(self):
    return None
```

TODO 是程序员认为应该做但暂时做不了的工作。它可能是删除废弃功能的提醒，或者是请求别人关注某个问题。它也可能是请人想一个更好的名字，或提醒需要在某个计划事件后进行修改。不管 TODO 是什么，都不应该成为把坏代码留在系统里的借口。

#### 放大说明

注释可以用来强调本来似乎微不足道的事情的重要性。

```python
list_item_content = match.group(3).strip()
# 这里的 strip 非常重要。它删除了开头的空格，
# 这些空格可能导致该项被识别为另一条列表。
new_list_item = ListItemWidget(self, list_item_content, self.level + 1)
return build_list(text[match.end():])
```

#### 公共 API 的文档字符串

没有什么比描述良好的公共 API 更有帮助。标准库中的文档字符串就是一个典型例子。缺少它们的编程语言会让编写程序变得更加困难。

### 坏注释

大多数注释都属于这一类。它们通常是为糟糕代码提供的拐杖或借口，或者是对不充分决策的辩解，本质上只是程序员自言自语。

#### 含糊的注释

随便写一条注释只是因为你觉得应该写，或者因为流程要求，这是一种敷衍。如果你决定写注释，就应该花必要的时间确保它是最好的注释。例子：

```python
def load_properties():
    try:
        properties_path = f"{properties_location}/{PROPERTIES_FILE}"
        with open(properties_path, "rb") as properties_stream:
            loaded_properties.load(properties_stream)
    except IOError as e:
        # 没有配置文件时会加载所有默认值
        pass
```

这个 `except` 中的注释是什么意思？它显然对作者有意义，但并没有很好地传达出来。显然，如果出现 `IOError`，意味着没有配置文件；在这种情况下，默认值会被加载。但谁来加载这些默认值？

#### 冗余注释

```python
# 当 self.closed 为 True 时返回。如果超时则抛出异常。
def wait_for_close(self, timeout_millis):
    if not self.closed:
        self.wait(timeout_millis)
        if not self.closed:
            raise Exception("MockResponseSender could not be closed")
```

这条注释有何意义？它并没有比代码更有信息量。它既不解释代码，也不提供意图或理由。它不比代码更容易读，反而不够精确，让读者误以为注释可以替代对代码的理解。

#### 误导性注释

有时，即使出发点良好，注释也可能不够精确而产生误导。再看上一节中的例子。该方法并不是在 `self.closed` 变为 `True` 时返回；它是在 `self.closed` 已经为 `True` 时返回，否则等待超时，并在 `self.closed` 仍然为 `False` 时抛出异常。

#### 强制注释

规定每个函数都必须有文档字符串，或者每个变量都必须有注释，这种规则纯属荒谬。这样的注释只会使代码混乱、传播错误信息、增加困惑。

```python
"""

:param title: CD 的标题
:param author: CD 的作者
:param tracks: CD 的曲目数
:param duration_in_minutes: CD 的时长（分钟）
"""
def add_cd(title, author, tracks, duration_in_minutes):
    cd = CD()
    cd.title = title
    cd.author = author
    cd.tracks = tracks
    cd.duration = duration_in_minutes
    cd_list.append(cd)
```

#### 编辑日志注释

有些人每次编辑模块时都会在开头写修改日志。例如：

```
# Changes (from 11-Oct-2001)
# --------------------------
# 11-Oct-2001 : reorganized the class and moved it to new package ...
```

现在我们有源代码版本控制系统，不需要这种日志。

#### 噪音注释

下面的注释并没有提供新信息。

```python
# 默认构造函数。
def __init__(self):
    pass
```

```python
# 这个字段表示月份中的某一天。
self.day_of_month = 1
```

文档字符串有时也会变成这种冗余噪音注释。许多时候它们只是出于错误的文档欲望而写出来的。

#### 如果可以用函数或变量替代，就不要用注释

```python
# 判断全局列表中的模块 <mod> 是否依赖于我们所在的子系统？
if submodule.get_dependent_subsystems().contains(subsys_mod.get_subsystem()):
```

vs

```python
module_dependees = submodule.get_dependent_subsystems()
our_subsystem = subsys_mod.get_subsystem()
if our_subsystem in module_dependees:
```

#### 位置标记注释

这种注释会制造噪音。

```python
# Actions //////////////////////////////////
```

#### 结束大括号注释

这种注释在 Python 中通常不是问题，因为缩进已经表示结构。原版中的 Java 反例如下：

```java
public class wc {
  public static void main(String[] args) {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line;
    int lineCount = 0;
    int charCount = 0;
    int wordCount = 0;
    try {
      while ((line = in.readLine()) != null) {
        lineCount++;
        charCount += line.length();
        String words[] = line.split("\\W");
        wordCount += words.length;

      } //while
      System.out.println("wordCount = " + wordCount);
      System.out.println("lineCount = " + lineCount);
      System.out.println("charCount = " + charCount);

    } // try
    catch (IOException e) {
      System.err.println("Error:" + e.getMessage());

    } //catch

  } //main
}
```

如果你需要这种注释，这通常意味着可以把代码拆成更小的函数。

#### 署名和作者说明

例如：`# Added by Rick`

版本控制系统可以管理这些信息，不应该写进代码。

#### 注释掉的代码

```python
response = InputStreamResponse()
response.set_body(formatter.get_result_stream(), formatter.get_byte_count())
# results_stream = formatter.get_result_stream()
# reader = StreamReader(results_stream)
# response.set_content(reader.read(formatter.get_byte_count()))
```

如果你不再需要它，就删除它。如果以后需要，可以从版本控制中恢复。

#### HTML 注释

源码注释里出现 HTML 是一种反模式。

```java
/**
* Task to run fit tests.
* This task runs fitnesse tests and publishes the results.
* <p/>
* <pre>
* Usage:
* &lt;taskdef name=&quot;execute-fitnesse-tests&quot;
* classname=&quot;fitnesse.ant.ExecuteFitnesseTestsTask&quot;
* classpathref=&quot;classpath&quot; /&gt;
* OR
* &lt;taskdef classpathref=&quot;classpath&quot;
* resource=&quot;tasks.properties&quot; /&gt;
* <p/>
* &lt;execute-fitnesse-tests
* suitepage=&quot;FitNesse.SuiteAcceptanceTests&quot;
* fitnesseport=&quot;8082&quot;
* resultsdir=&quot;${results.dir}&quot;
* resultshtmlpage=&quot;fit-results.html&quot;
* classpathref=&quot;classpath&quot; /&gt;
* </pre>
*/
```

#### 非本地信息

如果必须写注释，确保它描述的是它所在代码附近的内容。不要在本地注释里提供系统范围的信息。

#### 信息过多

不要把历史讨论或无关细节写到注释里。

#### 关联不明显

注释与它描述的代码之间的联系应该明显。如果你要费心写注释，读者至少应该看得出注释对应的是哪段代码。

#### 函数头注释

短函数不需要太多描述。一个精心选择的名字对于只做一件事的小函数，通常比注释头更好。

#### 非公开代码中的文档字符串

文档字符串适用于公共 API，在非公开代码中可能更多是干扰而不是帮助。

<a name="chapter5">
<h1>第 5 章 - 格式</h1>
</a>

代码格式很重要。它既太重要到不能忽视，也太重要到不能教条化。代码格式关乎沟通，而沟通是专业开发者的第一要务。

### 垂直格式

#### 概念之间的垂直空白

这个概念说明了你如何在代码中分隔不同的概念。下面的例子说明了这一点。

```python
class BoldWidget(ParentWidget):
    REGEXP = r"'''(.+?)'''"
    pattern = re.compile(REGEXP, re.MULTILINE | re.DOTALL)

    def __init__(self, parent, text):
        super().__init__(parent)
        match = self.pattern.search(text)
        match.find()
        self.add_child_widgets(match.group(1))

    def render(self):
        html = ["<b>"]
        html.append(self.child_html()).append("</b>")
        return "".join(html)
```

```python
class BoldWidget(ParentWidget):
    REGEXP = r"'''(.+?)'''"
    pattern = re.compile(REGEXP, re.MULTILINE | re.DOTALL)
    def __init__(self, parent, text):
        super().__init__(parent)
        match = self.pattern.search(text); match.find(); self.add_child_widgets(match.group(1))
    def render(self): return "<b>" + self.child_html() + "</b>"
```

你可以看到，第一个例子的可读性远高于第二个。

#### 垂直密度

垂直密度表示紧密关联。因此紧密相关的代码行应该垂直靠近。

```python
class ReporterConfig:

    # reporter listener 的类名
    m_class_name = None

    # reporter listener 的属性
    m_properties = []

    def add_property(self, property):
        self.m_properties.append(property)
```

```python
class ReporterConfig:
    def __init__(self):
        self.m_class_name = None
        self.m_properties = []

    def add_property(self, property):
        self.m_properties.append(property)
```

第二个版本更容易阅读。它能够一次“眼神扫过”看到完整逻辑。

#### 垂直距离

变量声明应该尽可能靠近它们的使用位置。因为我们的函数很短，局部变量通常出现在函数顶部。

实例变量则应声明在类的顶部。在一个设计良好的类中，实例变量会被该类的多数方法使用，所以它们应当在一个大家都熟悉的位置声明。

#### 依赖函数

如果一个函数调用另一个，它们应当垂直靠近，并尽量让调用者在被调用者之上。这给程序带来自然的流程。如果这一约定可靠遵循，读者就可以信赖函数定义会在使用后不久出现。

#### 概念关联

某些代码片段希望靠近其他片段。它们有某种概念关联。关联越强，它们之间的垂直距离就越短。

#### 垂直顺序

一般来说，我们希望函数调用依赖沿着向下的方向指向。也就是说，被调用的函数应该位于调用它的函数之下。这样会在源代码模块中形成从高层到低层的自然流动。

### 水平格式

#### 水平空白与密度

我们使用水平空白来关联紧密相关的事物，并分离关系较弱的事物。例如：

```python
def measure_line(line):
    line_count += 1
    line_size = len(line)
    total_chars += line_size
    line_width_histogram.add_line(line_size, line_count)
    record_widest_line(line_size)
```

赋值语句有两个主要部分：左边和右边。空格让这种分离更明显。

#### 水平对齐

```python
class Example(Base):
    def __init__(self, socket, input_stream):
        self.socket       = socket
        self.input_stream = input_stream
        self.request      = None
```

在现代语言中，这种对齐通常无益。它似乎强调了错误的东西，并把视线从真实意图上带走。

```python
class Example(Base):
    def __init__(self, socket, input_stream):
        self.socket = socket
        self.input_stream = input_stream
```

这通常比刻意对齐更好。

### 缩进

缩进很重要，因为它帮助我们看到可见的层次结构和明确的代码块。

### 团队规则

每个程序员都有自己喜欢的格式规则，但如果他在团队里工作，就应该采用团队规则。

开发团队应当就一种格式风格达成一致，并让每个成员都遵守它。我们希望软件具有一致的风格，不希望它看起来像一群意见不合的人写的。

<a name="chapter6">
<h1>第 6 章 - 对象与数据结构</h1>
</a>

### 数据抽象

隐藏实现不仅仅是在变量和函数之间加一层封装。隐藏实现是关于抽象！一个类不应该只是通过 getter 和 setter 将其变量暴露出去。它应该暴露抽象接口，让使用者操作数据的本质，而无需了解其具体实现。

### 数据/对象反对称性

下面两个例子展示了对象和数据结构之间的区别。对象将数据隐藏在抽象后面，并公开作用于这些数据的函数。数据结构公开数据，而没有有意义的函数。

**过程式形状**

```python
class Square:
    def __init__(self, top_left, side):
        self.top_left = top_left
        self.side = side

class Rectangle:
    def __init__(self, top_left, height, width):
        self.top_left = top_left
        self.height = height
        self.width = width

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Geometry:
    PI = 3.141592653589793

    def area(self, shape):
        if isinstance(shape, Square):
            return shape.side * shape.side
        elif isinstance(shape, Rectangle):
            return shape.height * shape.width
        elif isinstance(shape, Circle):
            return self.PI * shape.radius * shape.radius
        raise ValueError("Unknown shape")
```

**多态形状**

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, top_left, side):
        self.top_left = top_left
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, top_left, height, width):
        self.top_left = top_left
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Circle(Shape):
    PI = 3.141592653589793

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius
```

我们再次看到这两个定义的互补性质；它们几乎是完全相反的！这揭示了对象和数据结构之间的根本二分法：

> 过程式代码（使用数据结构的代码）让新增函数变得容易，而无需修改现有数据结构。另一方面，面向对象代码使新增类变得容易，而无需修改现有函数。

反过来也一样：

> 过程式代码让新增数据结构变得困难，因为所有函数都必须更改。面向对象代码让新增函数变得困难，因为所有类都必须更改。

成熟的程序员知道“万物皆对象”是一个神话。有时你确实需要简单的数据结构和在其上操作的过程。

### [Demeter 法则](https://en.wikipedia.org/wiki/Law_of_Demeter)

有一个著名的启发式原则叫 Demeter 法则，它说一个模块不应该了解它操作对象的内部细节。

更准确地说，Demeter 法则要求类 `C` 的方法 `f` 只调用以下对象的方法：

- `C` 本身
- 由 `f` 创建的对象
- 作为参数传入 `f` 的对象
- `C` 的实例变量中保存的对象

该方法不应调用由上述允许对象返回的对象的方法。换句话说，要和朋友交谈，而不是陌生人。

### 数据传输对象

数据结构的典型形式是一个公开变量但没有方法的类。这有时称为数据传输对象（DTO）。DTO 在与数据库通信或解析来自套接字的消息时非常有用。它们通常是把数据库原始数据转换为应用程序对象的一系列翻译阶段中的第一步。

<a name="chapter7">
<h1>第 7 章 - 错误处理</h1>
</a>

许多代码库完全被错误处理主导。当我说主导时，并不是说它们只处理错误，而是说因为散落的错误处理，几乎看不清代码本身在做什么。错误处理很重要，但如果它遮蔽了逻辑，那就是错误的。

### 使用异常而不是返回错误码

远在很久以前，有许多语言没有异常。在那些语言中，处理和报告错误的技术有限。你要么设置一个错误标志，要么返回一个调用者可以检查的错误码。

### 先写 try/except/finally 语句

从某种意义上说，try 代码块像事务。你的 except 必须无论 try 中发生什么都让程序保持一致状态。因此，当你编写可能抛出异常的代码时，先写好 try/except/finally 语句是一个好习惯。这有助于定义该代码的使用者在出现错误时应该期待什么。

### 用异常提供上下文

每个抛出的异常都应提供足够的上下文以判断错误来源和位置。

创建有信息量的错误消息，并随异常一起传递它们。说明失败的操作和失败的类型。如果你的应用程序会记录日志，那么在 except 中传递足够的信息以便记录错误。

### 不要返回 None

如果你想从方法返回 `None`，考虑抛出异常或返回特殊情况对象。若你调用的第三方 API 返回 `None`，可以考虑用一个方法封装它，使其要么抛出异常，要么返回特殊情况对象。

### 不要传递 None

从方法返回 `None` 是糟糕的，但把 `None` 传给方法更糟。除非你在处理一个确实期待 `None` 的 API，否则应尽量避免在代码中传递 `None`。

<a name="chapter8">
<h1>第 8 章 - 边界</h1>
</a>

我们很少控制系统中的所有软件。有时我们会购买第三方包或使用开源。其他时候我们依赖公司内部团队提供组件或子系统。我们必须想办法把这些外部代码干净地集成到我们自己的代码中。

### 使用第三方代码

接口提供者和接口使用者之间存在自然张力。第三方包和框架的提供者倾向于追求广泛适用性，以便在更多环境中工作、吸引更大受众。而使用者则希望接口专注于自己的特定需求。这种张力会在系统边界产生问题。

例子：

```python
sensors = {}
s = sensors.get(sensor_id)
```

vs

```python
class Sensors:
    def __init__(self):
        self._sensors = {}

    def get_by_id(self, id):
        return self._sensors.get(id)
```

第一种写法把类型转换暴露在 `dict` 之外，而第二种写法则能以很小的代价演化。转换和类型管理保留在 `Sensors` 类内部。

接口也被定制和约束以满足应用需求。这样得到的代码更易理解，也更难被误用。`Sensors` 类可以强制实现设计和业务规则。

### 探索和学习边界

第三方代码可以帮助我们更快地交付更多功能。当我们想使用一个第三方包时，应该从哪里入手？测试第三方代码并不是我们的职责，但为我们使用的第三方代码编写测试往往是最明智的做法。

为学习和理解第三方代码编写测试是一个好主意。Newkirk 称这种测试为学习测试。

### 学习测试比免费更好

学习测试最终不是白花钱。我们本来就需要学习 API，而写这些测试是一个简单而隔离的方式来获取知识。学习测试是精确的实验，有助于提高理解。

学习测试不仅是免费的，它还有正向投资回报。当第三方包有新版本时，我们运行学习测试以查看是否存在行为差异。

### 使用尚不存在的代码

有时需要在某个模块中工作，该模块将与另一个正在开发的模块连接，但我们尚不知道如何传递信息，因为 API 尚未设计。在这种情况下，建议创建一个接口来封装与待开发模块的通信。这样我们可以保持对自己模块的控制，并且即使第二个模块尚不可用也能进行测试。

### 干净的边界

边界会产生有趣的事情。变化就是其中之一。好的软件设计能够在不投入巨大精力和返工的情况下适应变化。当我们使用不受我们控制的代码时，必须格外小心保护我们的投入，确保未来变化不会过于昂贵。

<a name="chapter9">
<h1>第 9 章 - 单元测试</h1>
</a>

**测试驱动开发**

### TDD 的三条法则

- **第一法则** 在编写失败的单元测试之前，不允许写生产代码。
- **第二法则** 你不能写多于使测试失败所必需的测试；不编译也算失败。
- **第三法则** 你不能写多于使当前失败测试通过所必需的生产代码。

### 干净的测试

如果你不保持测试干净，你就会失去它们。

可读性对于保持测试干净非常重要。

### 每个测试一个断言

建议每个测试只包含一个断言，因为这有助于让每个测试易于理解和维护。

### 单个概念的测试

这个规则有助于你保持函数短小。

- **为你需要验证的每个概念编写一个测试**

### F.I.R.S.T

- **快速** 测试应当迅速执行。
- **独立** 测试不应相互依赖。
- **可重复** 测试应该在任何环境中可重复运行。
- **自验证** 测试应该有布尔输出：要么通过，要么失败。
- **及时** 单元测试应在使其通过的生产代码之前编写。如果你在生产代码之后编写测试，可能会发现生产代码很难测试。

<a name="chapter10">
<h1>第 10 章 - 类</h1>
</a>

## 类组织

### 封装

我们喜欢把变量和辅助函数保持小巧，但我们不对此狂热。有时我们需要把一个变量或辅助函数设为受保护，以便测试可以访问它。

## 类应该小

- 第一条规则：类应该小。
- 第二条规则：类应该比第一条规则更小。

### 单一职责原则

**类应该只有一个职责——一个改变的理由**

SRP 是面向对象设计中最重要的概念之一。它也是最容易理解和遵循的简单概念之一。

### 内聚性

类应该拥有少量实例变量。类的每个方法都应该操作其中一个或多个变量。一般来说，一个方法操作的变量越少，它与该类的内聚性越高。一个类中每个变量都被每个方法使用时，达到了最大内聚性。

### 保持内聚性会导致许多小类

仅仅将大函数拆成小函数，就会导致类数量增加。

## 为变化组织

对于大多数系统，变化是持续的。每一次变化都使我们面临系统其余部分不再按预期工作的风险。在干净系统中，我们组织类以降低变化风险。

### 隔离变化

需求会变化，因此代码会变化。我们在面向对象 101 课上学到，有具体类，它们包含实现细节（代码）；还有抽象类，它们只表示概念。客户端类依赖具体实现细节时，当这些细节变化就会有风险。我们可以引入接口和抽象类来帮助隔离这些细节的影响。

<a name="chapter11">
<h1>第 11 章 - 系统</h1>
</a>

## 将构建系统与使用系统分离

**软件系统应该把启动过程（创建应用对象并将依赖关系连接起来）与启动后接管的运行时逻辑分离开来。**

### 与 main 的分离

一种将构建与使用分离的方法是把所有构建方面都移到 `main` 或由 `main` 调用的模块中，并把系统其余部分设计成假设所有对象已经创建并正确连接好了。

抽象工厂模式是这种方法的一种选择。

### 依赖注入

一个强有力的将构建与使用分离的机制是依赖注入（DI），它是控制反转（IoC）在依赖管理上的应用。控制反转把次要责任从对象转移到专门承担该职责的其他对象，从而支持单一职责原则。在依赖管理的上下文中，对象不应自己负责实例化依赖项。相反，它应将此责任传递给另一个“权威”机制，从而实现控制反转。由于设置是一个全局关注点，这个权威机制通常是 `main` 例程或一个专用的容器。

<a name="chapter12">
<h1>第 12 章 - 自然演化</h1>
</a>

根据 Kent Beck 的说法，设计是“简单的”，如果它遵循这些规则：

- 运行所有测试
- 不包含重复
- 表达程序员的意图
- 最小化类和方法的数量

<a name="chapter13">
<h1>第 13 章 - 并发</h1>
</a>

并发是一种解耦策略。它帮助我们将“做什么”和“什么时候做”解耦。在单线程应用中，“做什么”和“什么时候”通常耦合得如此紧密，以至于整个应用程序的状态往往可以通过查看调用栈来确定。调试这样的系统时，程序员可以设置一个断点或一系列断点，并通过命中哪些断点来了解系统状态。

将“做什么”与“什么时候”解耦，可以显著改善应用的吞吐量和结构。从结构上看，应用变成了许多协作的小计算机，而不是一个大的主循环。这可以让系统更易理解，并提供一些强大的关注点分离方式。

## 神话与误解

- 并发总是提高性能。
  并发有时可以提高性能，但只有当存在大量可由多个线程或处理器共享的等待时间时。两种情形都不简单。
- 写并发程序时设计不会改变。
  事实上，并发算法的设计可能与单线程系统的设计大不相同。将“做什么”与“什么时候”解耦，通常会对系统结构产生巨大影响。
- 在使用 Web 或 EJB 容器时，不需要理解并发问题。
  事实上，你最好了解你的容器在做什么，以及如何防范后面本章所述的并发更新和死锁问题。

还有一些更平衡的说法：
- 并发会带来一些开销，既有性能上的，也有额外代码编写上的。
- 正确的并发很复杂，即使对于简单问题也是如此。
- 并发错误通常不具可重复性，因此它们常被忽略为一次性问题，而不是被当作真正缺陷。
- 并发通常需要根本性的设计策略改变。

