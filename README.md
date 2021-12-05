## :wrench: is_Include 批量提取重复行和非重复行

​	该工具用于对比A.txt中的每一行是否存在B.txt文件中。

## :speaker: 工具说明

该工具有两个模式，使用参数`-m`区分。`-m in` 将存在于B.txt中的A的字符串打印并储存，`-m diff` 将不存在于B.txt中的A的字符串打印并储存。

## :gun:使用教程

**安装依赖：**

```
pip install -r requirements.txt
```

**使用：**

```
usage: is_Include.py [-h] [-t TARGET_FILE] [-d DB_FILE] [-m [MODE]] [-r RESULT]

== Query whether a line is in another file | Query which line is not in another file ==

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET_FILE, --target_file TARGET_FILE
                        target file path
  -d DB_FILE, --DB_file DB_FILE
                        File as database path
  -m [MODE], --mode [MODE]
                        Select a mode to query for inclusion or difference
  -r RESULT, --result RESULT
                        result
```

**（1）查询存在data.txt中target.txt的字符串**

​	**target.txt**

```
123
456
abc
def
rfv
```

​	**data.txt**

```
474
7565123
45623
45313
12346
```

执行命令：`python3 is_Include.py -t target.txt -d data.txt -r result.txt -m in`

**输出结果result.txt**	

```
123
456
```



**（2）查询不存在data.txt中target.txt的字符串**

​	**target.txt**

```
123
456
abc
def
rfv
```

​	**data.txt**

```
474
7565123
45623
45313
12346
```

执行命令：`python3 is_Include.py -t target.txt -d data.txt -r result.txt -m in`

**输出结果result.txt**	

```
abc
def
rfv
```