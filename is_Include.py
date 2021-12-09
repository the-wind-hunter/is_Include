# -*- coding: utf-8 -*-
import os
import argparse
import re

def compare_in(target_file , data_file):
    # 打开文件
    target_R = open(target_file, "r")
    data_R = open(data_file, "r")

    target_list = target_R.read()      #读取所有target文件内容 注意是.read()
    data_list = data_R.readlines()

    with open(result,"w",) as f:
        for line_data in data_list:             #依次读取data文件中的每行
            line_data = line_data.strip()   #去掉每行头尾空白   
            matchObj = re.search( r"\b"+line_data+r"\b", "%s" %  target_list, re.M); #re.M 多行匹配，影响 ^ 和 $,re.I使匹配对大小写不敏感  
            if(matchObj):
                print("[-]" + line_data +" in the target!")
                try:
                    f.writelines("[-]" + line_data +" in the target!"+'\n')
                except:
                    continue
                it = re.finditer(r".*\b"+line_data+r"\b.*", "%s" %  target_list, re.M) 
                for match in it: 
                    print ("   " + match.group() )
                    try:
                        f.writelines("   " + match.group() + '\n')
                    except:
                        continue
            else:
                continue
    f.close() 
                
def compare_diff(target_file , data_file):
    # 打开文件
    target_R = open(target_file, "r")
    data_R = open(data_file, "r")

    target_lines = target_R.read()
    with open(result,"w",) as f:
        for line in data_R.readlines():       #依次读取data文件中的每行  
            line = line.strip()                #去掉每行头尾空白  
            matchObj = re.search( r"\b"+line+r"\b", "%s" %  target_lines, re.M | re.I); #re.M 多行匹配，影响 ^ 和 $,re.I使匹配对大小写不敏感
            #正则匹配开始，使用search可以将全部符合条件的字符集都找出来
            if(matchObj == None):
                print(line +" is not in the target!")
                try:
                    f.writelines(line + '\n')
                except:
                    continue
    f.close()           

    

if __name__ == '__main__':
    print("""
    
 __                  ______                      __                  __           
/  |                /      |                    /  |                /  |          
$$/   _______       $$$$$$/  _______    _______ $$ | __    __   ____$$ |  ______  
/  | /       |        $$ |  /       \  /       |$$ |/  |  /  | /    $$ | /      \ 
$$ |/$$$$$$$/         $$ |  $$$$$$$  |/$$$$$$$/ $$ |$$ |  $$ |/$$$$$$$ |/$$$$$$  |
$$ |$$      \         $$ |  $$ |  $$ |$$ |      $$ |$$ |  $$ |$$ |  $$ |$$    $$ |
$$ | $$$$$$  |       _$$ |_ $$ |  $$ |$$ \_____ $$ |$$ \__$$ |$$ \__$$ |$$$$$$$$/ 
$$ |/     $$/______ / $$   |$$ |  $$ |$$       |$$ |$$    $$/ $$    $$ |$$       |
$$/ $$$$$$$//      |$$$$$$/ $$/   $$/  $$$$$$$/ $$/  $$$$$$/   $$$$$$$/  $$$$$$$/ 
            $$$$$$/                                                               
                                                                                  
    """)
    print("Powered by jax\n")
    print("该工具用于对比A.txt中的每一行是否存在B.txt文件中\n[-m in]将存在于B.txt中的字符串打印并储存\n[-m diff]将不存在于B.txt中的字符串打印并储存\n")
    print("For example:\n >> python3 is_Include.py -t target.txt -d data.txt -r result.txt -m in\n[-] type 'python3 is_Include.py -h' to learn how to use")
    parser = argparse.ArgumentParser(description="== Query whether a line is in another file | Query which line is not in another file ==")
    parser.add_argument('-t', '--target_file', type=str, help="target file path")
    parser.add_argument('-d', '--DB_file', type=str, help="File as database path")
    parser.add_argument('-m', '--mode', type=str, help="Select a mode to query for inclusion or difference",nargs='?', const=1, default='in')
    parser.add_argument('-r', '--result', type=str, help="result")
    args = parser.parse_args()

    mode = args.mode
    if args.target_file == 0 or args.DB_file == 0:
        print("[-]wrong！请输入-f 被比对的文件和-fd 数据源文件！")
    if args.target_file and args.DB_file and args.result:
        result = args.result
        target_file = args.target_file
        data_file = args.DB_file
        if mode == 'in':
            compare_in(target_file , data_file)
        elif mode == 'diff':
            compare_diff(target_file , data_file)
        else:
            print("please input mode: '-m in' or '-m diff'")
    

