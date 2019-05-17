# 角斗场

## 准备

生成jar包放到./jars下，源文件不要使用 import javafx

测试脚本run_without_gen.sh的最后一行调用了not.sh这个脚本是发邮件用的，但是not.sh调用的python程序和发邮件脚本因为包含帐密敏感信息所以并未上传，所以not.sh不能使用，删掉run_without_gen的最后一行即可

## 启动

./run.sh 可以执行从生成到测试的全部流程

./run_without_gen.sh 只测试不生成用例

## 其他说明

gen.py 生成测试用例，存在./tests中

test.py 多线程测试，所有./jars路径下的测试文件都会被测试，结果存放在./results中

compare.py 进行结果比较，比较结果在./res.txt中

