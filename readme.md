# 角斗场

## 准备

生成jar包放到./jars下，源文件不要使用 import javafx

## 启动

./run.sh 可以执行从生成到测试的全部流程

./run_without_gen.sh 只测试不生成用例

## 其他说明

gen.py 生成测试用例，存在./tests中

test.py 多线程测试，所有./jars路径下的测试文件都会被测试，结果存放在./results中

compare.py 进行结果比较，比较结果在./res.txt中

